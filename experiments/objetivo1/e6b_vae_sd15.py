"""E6b / implicancias #36 y #39 — ida y vuelta `HU -> ventanas -> VAE de SD 1.5 -> HU`.

POR QUE
-------
El Go/No-Go del Objetivo 1 (`tesis/main.tex`) exige MAE < 25 HU en hueso para el viaje
`HU -> multi-ventana -> VAE -> HU`. E6a y E6c midieron solo la ventana y la cuantizacion, sin VAE
(cota inferior). #36 y #39 deben decidirse juntas: la mejor salida de E6c (`pub+MTW`) tiene 4 canales
y el VAE que sugiere `main.tex` ("Stable Diffusion 1.5 backbone") recibe 3. Este script mide ese VAE,
preentrenado y SIN reentrenar, con las configuraciones de 3 canales que entran sin tocarlo. No decide.

CONFIGURACIONES
---------------
`pub`, `LW20000` y `pub+asinh`, importadas tal cual de `e6c_techo_lw.py`. `pub+MTW` no se mide: sus 4
canales no entran en el VAE de SD 1.5 sin modificar la primera capa del encoder.

DISENO DE LA MEDICION (elecciones de este script, declaradas; no son decisiones de la tesis)
-------------------------------------------------------------------------------------------
- VAE: `AutoencoderKL` de `stable-diffusion-v1-5/stable-diffusion-v1-5`, subcarpeta `vae`, float32.
  Que ese sea "el VAE de SD 1.5" es la lectura de #36/#39, no una decision escrita.
- Cortes 2D sobre el eje axial del archivo (el de codigo S/I en el affine), a tamano nativo. Si un lado
  no es multiplo de 8 se rellena repitiendo el borde y se recorta al volver.
- Canal k de la configuracion -> canal k de la imagen; u en [0, 1] -> 2u - 1. Latente = media de la
  posterior (determinista, sin muestreo). Salida -> (x + 1) / 2 recortada a [0, 1].
- ROI y submuestreo identicos a E6c: hueso HU > 150, metal HU > 2500, paso fijo hasta 1 000 000.
- Cuatro decodificadores de HU por voxel:
  * `identidad oraculo`: sin VAE, mejor canal por voxel. Es la columna `float` de E6c.
  * `identidad regla`: sin VAE, canal elegido por la regla de abajo.
  * `vae oraculo`: con VAE, mejor canal por voxel (usa el HU verdadero; comparable con E6c).
  * `vae regla`: con VAE y sin verdad: el canal mas estrecho (SW, luego MW, luego LW) cuyo valor
    decodificado no esta saturado (EPS <= u <= 1 - EPS); si todos saturan, LW. Es lo que podria hacer
    un pipeline real.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- `identidad oraculo` debe coincidir con `e6c_techo_lw.csv` (`--e6c`) a 0.01 HU en cada volumen,
  configuracion y ROI. Si no coincide, las columnas de VAE no valen.
- Los indices del ROI deben dar los mismos voxeles que `e6c_techo_lw.submuestrea`; si no, el caso aborta.
- `--vae eco` pasa los canales por la misma tuberia de torch sin modelo: sus columnas `vae` deben
  igualar a las de `identidad` (prueba del script, no resultado).

METRICAS (anadido 2026-09-15, decision 2026-09-15 (2))
------------------------------------------------------
Cada combinacion de configuracion, decodificador y ROI se reporta con DOS metricas sobre el mismo
vector de errores absolutos por voxel:
- **MAE**, que es el criterio del Go/No-Go (`main.tex`, Objetivo 1): columna `{cfg} {dec} {roi}`.
- **RMSE**, que es lo que publica el campo (`peters2025hybrid` 2.5 p. 5 y `haneda2025aapm` Sec. 2.3
  p. 6 definen *CT number accuracy* como RMSE): columna `{cfg} {dec} {roi} rmse`.
La columna de MAE se deja SIN sufijo a proposito: asi no se rompe el control contra `e6c_techo_lw.csv`
ni la lectura de las corridas anteriores.
El oraculo elige canal por **menor error absoluto por voxel**, igual que antes, y las dos metricas se
calculan despues sobre ese mismo vector. El oraculo NO se re-optimiza para RMSE; si se re-optimizara,
su RMSE seria menor. Queda declarado, no corregido.

SALIDA (`--out`)
----------------
`e6b_vae_sd15.csv` (una fila por volumen), `e6b_vae_sd15_errores.csv`, `e6b_vae_sd15_control.csv` y
`e6b_vae_sd15.md`. Reanudable: salta los volumenes ya escritos. `--solo-resumen` rehace control e informe.
"""
from __future__ import annotations

import argparse
import csv
import math
import time
import traceback
from pathlib import Path
from typing import Callable

import nibabel as nib
import numpy as np

from e6c_techo_lw import BONE_HU, MAX_VOX, METAL_HU, configuraciones, submuestrea

CONFIGS = ('pub', 'LW20000', 'pub+asinh')
EPS = 0.01
UMBRAL_GO = 25.0
TOLERANCIA_CONTROL = 0.01
DECODIFICADORES = ('identidad oraculo', 'identidad regla', 'vae oraculo', 'vae regla')
ROIS = ('hueso', 'metal')
SUF_RMSE = ' rmse'
REPO_VAE = 'stable-diffusion-v1-5/stable-diffusion-v1-5'
CSV_RES, CSV_ERR = 'e6b_vae_sd15.csv', 'e6b_vae_sd15_errores.csv'

IdaVuelta = Callable[[np.ndarray], np.ndarray]


def campos() -> list[str]:
    """Columnas de la tabla por volumen."""
    base = ['Caso', 'Dataset', 'forma', 'eje_axial', 'n hueso', 'n metal', 'vae', 'segundos']
    return base + [f'{c} {d} {r}{suf}' for c in CONFIGS for d in DECODIFICADORES
                   for r in ROIS for suf in ('', SUF_RMSE)]


def eje_axial(img: nib.Nifti1Image) -> int:
    """Eje del array cuyo codigo de orientacion es S o I."""
    codigos = nib.aff2axcodes(img.affine)
    ejes = [i for i, c in enumerate(codigos) if c in ('S', 'I')]
    if len(ejes) != 1:
        raise ValueError(f'orientacion sin eje axial unico: {codigos}')
    return ejes[0]


def indices_roi(arr: np.ndarray, umbral: float) -> np.ndarray:
    """Indices planos (orden C) del ROI con el mismo paso fijo que `e6c_techo_lw.submuestrea`."""
    idx = np.flatnonzero(arr > umbral)
    if idx.size > MAX_VOX:
        idx = idx[::int(np.ceil(idx.size / MAX_VOX))]
    return idx


def regla(us: dict[str, np.ndarray], canales: dict) -> np.ndarray:
    """HU por voxel sin verdad: canal mas estrecho no saturado; si todos saturan, LW."""
    hu = np.asarray(canales['LW'][1](us['LW']), dtype=np.float64)
    for nombre in ('MW', 'SW'):
        u = us[nombre]
        ok = (u >= EPS) & (u <= 1.0 - EPS)
        hu[ok] = canales[nombre][1](u[ok])
    return hu


def mae_rmse(err: np.ndarray | None) -> tuple[float, float]:
    """Las dos metricas sobre un mismo vector de errores absolutos por voxel."""
    if err is None or err.size == 0:
        return math.nan, math.nan
    return float(err.mean()), float(np.sqrt(np.mean(np.square(err, dtype=np.float64))))


def err_oraculo(vals: np.ndarray, us: dict[str, np.ndarray], canales: dict) -> np.ndarray | None:
    """Error absoluto por voxel del oraculo: el menor entre los canales. Codigos `us` ya del ROI."""
    err = None
    for nombre, (_, vuelta) in canales.items():
        e = np.abs(vuelta(us[nombre]) - vals)
        err = e if err is None else np.minimum(err, e)
    return err


def errores(vals: np.ndarray, us: dict[str, np.ndarray],
            canales: dict) -> tuple[np.ndarray | None, np.ndarray | None]:
    """Errores absolutos por voxel del oraculo y de la regla."""
    if vals.size == 0:
        return None, None
    return err_oraculo(vals, us, canales), np.abs(regla(us, canales) - vals)


def ida_vuelta_torch(modelo, dispositivo: str) -> IdaVuelta:
    """f(u) para lotes (B, C, H, W) en [0, 1]. Con `modelo=None` es la prueba de tuberia (`eco`)."""
    import torch

    def f(u: np.ndarray) -> np.ndarray:
        _, _, h, w = u.shape
        ph, pw = (-h) % 8, (-w) % 8
        if ph or pw:
            u = np.pad(u, ((0, 0), (0, 0), (0, ph), (0, pw)), mode='edge')
        with torch.no_grad():
            x = torch.from_numpy(np.ascontiguousarray(u, dtype=np.float32)).to(dispositivo) * 2.0 - 1.0
            if modelo is not None:
                x = modelo.decode(modelo.encode(x).latent_dist.mean).sample
            y = ((x.float() + 1.0) / 2.0).clamp(0.0, 1.0).cpu().numpy()
        return y[:, :, :h, :w]
    return f


def cargar_vae(ruta: Path, dispositivo: str):
    """AutoencoderKL de SD 1.5 desde la copia local de los pesos (sin internet)."""
    import torch
    from diffusers import AutoencoderKL
    modelo = AutoencoderKL.from_pretrained(str(ruta), subfolder='vae', torch_dtype=torch.float32)
    return modelo.to(dispositivo).eval()


def analizar(path: Path, cfgs: dict, f: IdaVuelta | None, lote: int, etiqueta: str) -> dict:
    """Una fila por volumen: MAE de cada configuracion, decodificador y ROI."""
    t0 = time.time()
    img = nib.load(path)
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    caso = path.name.split('.nii')[0]
    fila: dict[str, object] = {'Caso': caso, 'Dataset': caso.split('_')[0],
                               'forma': ' '.join(map(str, arr.shape)), 'eje_axial': eje, 'vae': etiqueta}
    idx = {'hueso': indices_roi(arr, BONE_HU), 'metal': indices_roi(arr, METAL_HU)}
    plano = arr.ravel()
    vals = {r: plano[i] for r, i in idx.items()}
    for r, umbral in (('hueso', BONE_HU), ('metal', METAL_HU)):
        if not np.array_equal(submuestrea(arr[arr > umbral]), vals[r]):
            raise RuntimeError(f'los indices del ROI de {r} no dan los voxeles de E6c')
    del plano
    fila['n hueso'], fila['n metal'] = int(vals['hueso'].size), int(vals['metal'].size)
    movido = np.moveaxis(arr, eje, 0)

    for cfg in CONFIGS:
        canales = cfgs[cfg]
        for r in ROIS:
            if vals[r].size:
                us = {n: ida(vals[r]) for n, (ida, _) in canales.items()}
                e_o, e_g = errores(vals[r], us, canales)
                for dec, e in (('identidad oraculo', e_o), ('identidad regla', e_g)):
                    m, q = mae_rmse(e)
                    fila[f'{cfg} {dec} {r}'] = round(m, 4)
                    fila[f'{cfg} {dec} {r}{SUF_RMSE}'] = round(q, 4)
        if f is None:
            continue
        nombres = list(canales)
        dec = np.empty((len(nombres),) + movido.shape, dtype=np.float32)
        for k0 in range(0, movido.shape[0], lote):
            bloque = movido[k0:k0 + lote]
            u = np.stack([canales[n][0](bloque) for n in nombres], axis=1)
            dec[:, k0:k0 + bloque.shape[0]] = f(u).transpose(1, 0, 2, 3)
        us_roi: dict[str, dict[str, np.ndarray]] = {r: {} for r in ROIS}
        for c, n in enumerate(nombres):
            plano_c = np.moveaxis(dec[c], 0, eje).ravel()
            for r in ROIS:
                us_roi[r][n] = plano_c[idx[r]]
            del plano_c
        del dec
        for r in ROIS:
            if vals[r].size:
                e_o, e_g = errores(vals[r], us_roi[r], canales)
                for dec, e in (('vae oraculo', e_o), ('vae regla', e_g)):
                    m, q = mae_rmse(e)
                    fila[f'{cfg} {dec} {r}'] = round(m, 4)
                    fila[f'{cfg} {dec} {r}{SUF_RMSE}'] = round(q, 4)
    fila['segundos'] = round(time.time() - t0, 1)
    return fila


def abrir(ruta: Path, columnas: list[str]):
    """CSV en modo anexar; si es nuevo o esta vacio, escribe la cabecera y la vuelca ya."""
    nuevo = not ruta.exists() or ruta.stat().st_size == 0
    h = ruta.open('a', encoding='utf-8', newline='')
    w = csv.DictWriter(h, fieldnames=columnas, extrasaction='ignore')
    if nuevo:
        w.writeheader()
        h.flush()
    return h, w


def control(out: Path, e6c: Path | None) -> None:
    """Identidad frente a E6c y, si la corrida es `eco`, columnas vae frente a identidad."""
    import pandas as pd

    d = pd.read_csv(out / CSV_RES)
    filas = []
    if e6c is not None:
        ref = pd.read_csv(e6c)[['Caso'] + [f'{c} float {r}' for c in CONFIGS for r in ROIS]]
        m = d.merge(ref, on='Caso', how='inner')
        for cfg in CONFIGS:
            for r in ROIS:
                a, b = m[f'{cfg} identidad oraculo {r}'], m[f'{cfg} float {r}']
                for caso, x, y in zip(m['Caso'], a, b):
                    if pd.isna(x) and pd.isna(y):
                        continue
                    filas.append({'control': 'identidad frente a E6c float', 'Caso': caso, 'columna': f'{cfg} {r}',
                                  'valor': x, 'referencia': y,
                                  'coincide': bool(pd.notna(x) and pd.notna(y) and abs(x - y) <= TOLERANCIA_CONTROL)})
    for dec in ('oraculo', 'regla'):
        e = d[d['vae'] == 'eco']
        for cfg in CONFIGS:
            for r in ROIS:
                for caso, x, y in zip(e['Caso'], e[f'{cfg} vae {dec} {r}'], e[f'{cfg} identidad {dec} {r}']):
                    if pd.isna(x) and pd.isna(y):
                        continue
                    filas.append({'control': 'eco frente a identidad', 'Caso': caso, 'columna': f'{cfg} {dec} {r}',
                                  'valor': x, 'referencia': y,
                                  'coincide': bool(pd.notna(x) and pd.notna(y) and abs(x - y) <= TOLERANCIA_CONTROL)})
    if not filas:
        print('CONTROL NO EJECUTADO: ningun valor en comun con E6c ni corrida eco. El resultado no esta validado.',
              flush=True)
        return
    c = pd.DataFrame(filas)
    c.to_csv(out / 'e6b_vae_sd15_control.csv', index=False)
    for nombre, g in c.groupby('control'):
        print(f'CONTROL {nombre}: {int(g["coincide"].sum())} de {len(g)} valores coinciden '
              f'(tolerancia {TOLERANCIA_CONTROL} HU)', flush=True)
        if not g['coincide'].all():
            print(g.loc[~g['coincide'], ['Caso', 'columna', 'valor', 'referencia']].to_string(index=False), flush=True)


def resumen(out: Path, e6c: Path | None) -> None:
    """Informe en Markdown: medianas, Go/No-Go y comparacion con E6c sobre los mismos volumenes."""
    import pandas as pd

    d = pd.read_csv(out / CSV_RES)
    err = out / CSV_ERR
    n_err = len(pd.read_csv(err)) if err.exists() and err.stat().st_size > 0 else 0
    ref = pd.read_csv(e6c).set_index('Caso').reindex(d['Caso']) if e6c is not None else None
    L = ['# E6b — ida y vuelta HU -> ventanas -> VAE de SD 1.5 -> HU (#36, #39)', '',
         f'Volumenes: {len(d)}; con error: {n_err}. VAE: {", ".join(sorted(d["vae"].astype(str).unique()))}.',
         f'ROI y submuestreo de E6c (hueso HU > {BONE_HU:.0f}, metal HU > {METAL_HU:.0f}). `oraculo` usa el HU '
         'verdadero para elegir canal (cota); `regla` no lo usa (pipeline real).',
         '`pub+MTW` no se mide: 4 canales no entran en el VAE de SD 1.5 sin modificarlo. Generado por '
         '`e6b_vae_sd15.py`; no decide nada.',
         'Se reportan **MAE** (criterio del Go/No-Go) y **RMSE** (metrica de `peters2025hybrid` y '
         '`haneda2025aapm`) sobre el mismo vector de errores. El oraculo elige canal por error absoluto '
         'en los dos casos.', '']
    hay_rmse = all(f'{c} {dec} {r}{SUF_RMSE}' in d.columns
                   for c in CONFIGS for dec in DECODIFICADORES for r in ROIS)
    if not hay_rmse:
        L += ['> Corrida anterior al 2026-09-15: solo trae MAE. Las columnas `rmse` faltan y sus tablas se omiten.', '']
    metricas = [('MAE', ''), ('RMSE', SUF_RMSE)] if hay_rmse else [('MAE', '')]
    for nombre, suf in metricas:
        # E6c solo tiene MAE: la comparacion lateral solo se imprime en la tabla de MAE
        lado = ref is not None and suf == ''
        for r in ROIS:
            cab = '| Configuracion | ' + ' | '.join(DECODIFICADORES) + (' | E6c float | E6c 8b |' if lado else ' |')
            L += [f'## {nombre} en ROI de {r}: mediana sobre los volumenes (HU)', '', cab,
                  '|---|' + '---|' * (len(DECODIFICADORES) + (2 if lado else 0))]
            for cfg in CONFIGS:
                celdas = [f'{d[f"{cfg} {dec} {r}{suf}"].median():.2f}'
                          if d[f'{cfg} {dec} {r}{suf}'].notna().any() else '-'
                          for dec in DECODIFICADORES]
                if lado:
                    celdas += [f'{ref[f"{cfg} {b} {r}"].median():.2f}' for b in ('float', '8b')]
                L.append(f'| `{cfg}` | ' + ' | '.join(celdas) + ' |')
            L.append('')
    L += [f'## Go/No-Go del Objetivo 1: volumenes que FALLAN (MAE >= {UMBRAL_GO:.0f} HU en hueso)', '',
          'El criterio de la tesis es **MAE**. La fila de RMSE es contraste con la metrica que publica el '
          'campo, NO el Go/No-Go.', '',
          '| Configuracion | Metrica | ' + ' | '.join(DECODIFICADORES) + ' |',
          '|---|---|' + '---|' * len(DECODIFICADORES)]
    for cfg in CONFIGS:
        for nombre, suf in metricas:
            celdas = []
            for dec in DECODIFICADORES:
                v = d[f'{cfg} {dec} hueso{suf}'].dropna()
                celdas.append(f'{int((v >= UMBRAL_GO).sum())}/{len(v)}' if len(v) else '-')
            L.append(f'| `{cfg}` | {nombre} | ' + ' | '.join(celdas) + ' |')
    L += ['', '## Hueso por dataset: mediana con VAE (oraculo / regla), HU', '',
          '| Configuracion | Dataset | n | vae oraculo | vae regla |', '|---|---|---|---|---|']
    for cfg in CONFIGS:
        for ds, g in d.groupby('Dataset'):
            o, gr = g[f'{cfg} vae oraculo hueso'], g[f'{cfg} vae regla hueso']
            L.append(f'| `{cfg}` | {ds} | {len(g)} | '
                     f'{o.median():.2f} | {gr.median():.2f} |' if o.notna().any() else f'| `{cfg}` | {ds} | {len(g)} | - | - |')
    L += ['', f'Tiempo por volumen: mediana {d["segundos"].median():.0f} s; total {d["segundos"].sum() / 3600:.2f} h.', '']
    (out / 'e6b_vae_sd15.md').write_text('\n'.join(L), encoding='utf-8')
    print(f'Escrito {out / "e6b_vae_sd15.md"}', flush=True)


def main() -> None:
    """Recorre los CT; reanudable (`--max`, `--casos`)."""
    raiz = Path(__file__).resolve().parents[2]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--data', type=Path, default=raiz / 'data')
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--modelo', type=Path, default=None, help='carpeta local con vae/config.json y los pesos')
    p.add_argument('--vae', choices=('sd15', 'identidad', 'eco'), default='sd15')
    p.add_argument('--dispositivo', default='cuda')
    p.add_argument('--lote', type=int, default=4, help='cortes por lote en el VAE')
    p.add_argument('--e6c', type=Path, default=None, help='e6c_techo_lw.csv para el control')
    p.add_argument('--casos', nargs='*', default=None)
    p.add_argument('--max', type=int, default=None)
    p.add_argument('--solo-resumen', action='store_true')
    args = p.parse_args()

    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    e6c = args.e6c.expanduser() if args.e6c else None
    if not args.solo_resumen:
        paths = sorted(args.data.expanduser().rglob('*_data.nii*'))
        if args.casos:
            paths = [q for q in paths if q.name.split('.nii')[0] in set(args.casos)]
        if not paths:
            raise SystemExit('No se encontraron CT *_data.nii[.gz]. No se escribio nada.')
        hechos: set[str] = set()
        for nombre in (CSV_RES, CSV_ERR):
            ruta = out / nombre
            if ruta.exists() and ruta.stat().st_size > 0:
                with ruta.open(encoding='utf-8') as h:
                    hechos |= {r['Caso'] for r in csv.DictReader(h)}

        f, etiqueta = None, 'identidad'
        if args.vae in ('sd15', 'eco'):
            import torch
            if args.dispositivo.startswith('cuda') and not torch.cuda.is_available():
                raise SystemExit('ERROR: se pidio cuda y torch no ve ninguna GPU.')
            print(f'torch {torch.__version__}; dispositivo {args.dispositivo}'
                  + (f' ({torch.cuda.get_device_name(0)})' if args.dispositivo.startswith('cuda') else ''), flush=True)
            if args.vae == 'sd15':
                import diffusers
                if args.modelo is None:
                    raise SystemExit('ERROR: --vae sd15 necesita --modelo.')
                print(f'diffusers {diffusers.__version__}; pesos {args.modelo}', flush=True)
                f, etiqueta = ida_vuelta_torch(cargar_vae(args.modelo.expanduser(), args.dispositivo), args.dispositivo), 'sd15'
            else:
                f, etiqueta = ida_vuelta_torch(None, args.dispositivo), 'eco'
        print(f'{len(paths)} volumenes en {args.data}; {len(hechos)} ya procesados; vae = {etiqueta}', flush=True)

        cfgs = configuraciones()
        s_res, s_err = abrir(out / CSV_RES, campos()), abrir(out / CSV_ERR, ['Caso', 'Error'])
        nuevos = 0
        try:
            for path in paths:
                caso = path.name.split('.nii')[0]
                if caso in hechos:
                    continue
                if args.max is not None and nuevos >= args.max:
                    break
                nuevos += 1
                try:
                    fila = analizar(path, cfgs, f, args.lote, etiqueta)
                except Exception as exc:  # un volumen roto no detiene la cohorte
                    s_err[1].writerow({'Caso': caso, 'Error': f'{type(exc).__name__}: {exc}'})
                    s_err[0].flush()
                    print(f'{caso}: ERROR {exc}', flush=True)
                    traceback.print_exc()
                    continue
                s_res[1].writerow(fila)
                s_res[0].flush()
                print(f'{caso}: ok {fila["segundos"]} s | pub hueso MAE identidad '
                      f'{fila.get("pub identidad oraculo hueso")} vae oraculo '
                      f'{fila.get("pub vae oraculo hueso", "-")} regla {fila.get("pub vae regla hueso", "-")} '
                      f'| RMSE regla {fila.get("pub vae regla hueso" + SUF_RMSE, "-")}',
                      flush=True)
        finally:
            for h, _ in (s_res, s_err):
                h.close()
    control(out, e6c)
    resumen(out, e6c)


if __name__ == '__main__':
    main()
