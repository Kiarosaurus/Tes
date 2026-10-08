"""P1-MAISI — ida y vuelta con el VAE 3D de MAISI, con la regla preinscrita del Objetivo 1.

POR QUE
-------
Decision 2026-09-19 (`01-decisiones.md`): tras el No-Go de P1 (#91), MAISI se mide **como extension
del Objetivo 1**, con los mismos 34 pacientes de test y la misma regla (media por paciente del MAE en
hueso < 25 HU). Subordinado a la opcion A; su resultado **no cambia** el diseno del Objetivo 3.
La ficha `guo2025maisi.md` dejo dos cosas claras (#93): el paper **no publica** como normaliza los HU
(remite a un suplementario que no incluye) y **no da error en HU**. Por eso este script tiene dos
subcomandos y el primero no es opcional.

SUBCOMANDO `inspeccionar` (PASO 0, sin GPU)
-------------------------------------------
Lee la configuracion del bundle de MAISI y **imprime la normalizacion de intensidad que encuentre**
(claves tipo `ScaleIntensityRange`, `a_min`, `a_max`, `b_min`, `b_max`, `clip`), el tamano de entrada
y los pesos disponibles. **Si el recorte deja fuera el hueso denso (p. ej. a_max = 1000 HU), MAISI se
descarta por diseno y no se corre nada**, que es exactamente la salida barata de #93.

SUBCOMANDO `evaluar` (GPU)
--------------------------
Ida y vuelta `HU -> normalizacion de MAISI -> VAE 3D -> HU` sobre los pacientes de test, con los ROI
y el estimador de P1: hueso HU > 150, metal HU > 2500 y `bdelta` (banda de 12 mm alrededor del metal),
submuestreo por paso fijo, MAE y RMSE. **La normalizacion NO tiene valor por defecto**: se pasa con
`--hu-min/--hu-max`, tomados del paso 0. Si no se pasan, el script aborta: inventarlos seria falsear
la comparacion.

DIFERENCIAS CON P1, QUE HAY QUE DECLARAR AL COMPARAR
-----------------------------------------------------
- MAISI es **3D y de un canal**: no hay multi-ventana ni decodificadores `oraculo`/`regla`. La
  columna que se compara con P1 es la de HU reconstruidos directamente.
- El volumen se procesa en **bloques con solape** (`--bloque`, `--solape`) porque un volumen entero no
  cabe; los bordes se promedian. Es una eleccion de este script, no de MAISI.
- No se afina nada: es el VAE preentrenado tal cual.

SALIDA (`--out`)
----------------
`p1_maisi.csv` (una fila por volumen), `p1_maisi_errores.csv` y `p1_maisi.md` con el veredicto contra
el mismo umbral de 25 HU. Reanudable: salta los casos ya escritos.
"""
from __future__ import annotations

import argparse
import csv
import json
import time
import traceback
from pathlib import Path

import nibabel as nib
import numpy as np

from p1_decodificador_sd15 import ROIS, indices_bdelta, leer_particion, rutas
from e6b_vae_sd15 import UMBRAL_GO, abrir, eje_axial, indices_roi, mae_rmse
from e6c_techo_lw import BONE_HU, METAL_HU, submuestrea

CSV_RES, CSV_ERR = 'p1_maisi.csv', 'p1_maisi_errores.csv'
CLAVES_NORMA = ('a_min', 'a_max', 'b_min', 'b_max', 'clip', 'ScaleIntensityRange',
                'NormalizeIntensity', 'intensity', 'spacing', 'roi_size', 'latent_channels')


def campos() -> list[str]:
    """Columnas de la tabla por volumen."""
    return (['Caso', 'Dataset', 'Grupo paciente', 'Metal', 'particion', 'forma', 'spacing',
             'hu_min_norma', 'hu_max_norma', 'bloque', 'solape', 'segundos']
            + [f'maisi {r}{s}' for r in ROIS for s in ('', ' rmse')]
            + [f'n {r}' for r in ROIS])


def inspeccionar(bundle: Path) -> None:
    """PASO 0: imprime la normalizacion de intensidad y la forma de entrada que declare el bundle."""
    bundle = bundle.expanduser()
    if not bundle.exists():
        raise SystemExit(f'ERROR: no existe {bundle}')
    jsons = sorted(bundle.rglob('*.json')) + sorted(bundle.rglob('*.yaml'))
    pesos = sorted(bundle.rglob('*.pt')) + sorted(bundle.rglob('*.pth')) + sorted(bundle.rglob('*.safetensors'))
    print(f'bundle: {bundle}\narchivos de configuracion: {len(jsons)}; pesos: {len(pesos)}', flush=True)
    for p in pesos:
        print(f'  pesos: {p.relative_to(bundle)}  ({p.stat().st_size / 2**20:.0f} MB)', flush=True)
    for p in jsons:
        texto = p.read_text(encoding='utf-8', errors='replace')
        golpes = [k for k in CLAVES_NORMA if k in texto]
        if not golpes:
            continue
        print(f'\n--- {p.relative_to(bundle)} (claves: {", ".join(golpes)})', flush=True)
        try:
            datos = json.loads(texto)
        except Exception:
            for linea in texto.splitlines():
                if any(k in linea for k in CLAVES_NORMA):
                    print('   ', linea.strip()[:160], flush=True)
            continue

        def recorre(obj, ruta=''):
            if isinstance(obj, dict):
                if any(k in obj for k in ('a_min', 'a_max', 'b_min', 'b_max', 'clip')) or \
                        any(k in str(obj.get('_target_', '')) for k in ('Intensity', 'Normalize', 'Scale')):
                    print(f'    {ruta}: {json.dumps(obj)[:400]}', flush=True)
                for k, v in obj.items():
                    if any(c in k.lower() for c in ('a_min', 'a_max', 'b_min', 'b_max', 'clip', 'intensity', 'range')):
                        print(f'    {ruta}.{k} = {json.dumps(v)[:200]}', flush=True)
                    recorre(v, f'{ruta}.{k}' if ruta else k)
            elif isinstance(obj, list):
                for i, v in enumerate(obj):
                    recorre(v, f'{ruta}[{i}]')
        recorre(datos)
    for p in sorted(bundle.rglob('*.py')):
        lineas = p.read_text(encoding='utf-8', errors='replace').splitlines()
        golpes = [(i, l.strip()[:150]) for i, l in enumerate(lineas, 1)
                  if any(k in l for k in ('a_min', 'a_max', 'ScaleIntensity', 'NormalizeIntensity', 'clip('))]
        if golpes:
            print(f'\n--- {p.relative_to(bundle)} (codigo)', flush=True)
            for i, l in golpes[:12]:
                print(f'    {i}: {l}', flush=True)
    print('\nLECTURA: si el recorte de intensidad deja fuera el hueso denso (a_max cerca de 1000 HU), '
          'MAISI se descarta por diseno (#93) y no se corre la evaluacion. Si no aparece ningun rango, '
          'la normalizacion no esta en el bundle y hay que buscarla en el repositorio del modelo.', flush=True)


def cargar_vae_maisi(bundle: Path, pesos: Path | None, dispositivo: str):
    """Instancia el autoencoder de MAISI desde el bundle de MONAI y carga sus pesos."""
    import torch
    from monai.bundle import ConfigParser

    bundle = bundle.expanduser()
    cfgs = [p for p in sorted(bundle.rglob('*.json')) if 'autoencoder' in p.read_text(
        encoding='utf-8', errors='replace')]
    if not cfgs:
        raise SystemExit(f'ERROR: ningun json de {bundle} define el autoencoder. Corre primero `inspeccionar`.')
    parser = ConfigParser()
    parser.read_config(str(cfgs[0]))
    clave = next((k for k in ('autoencoder_def', 'autoencoder', 'network_def') if k in parser.config), None)
    if clave is None:
        raise SystemExit(f'ERROR: {cfgs[0].name} no trae `autoencoder_def`. Revisa el paso 0.')
    modelo = parser.get_parsed_content(clave, instantiate=True)
    ruta = pesos.expanduser() if pesos else next(iter(sorted(bundle.rglob('*autoencoder*.pt'))), None)
    if ruta is None or not Path(ruta).exists():
        raise SystemExit('ERROR: no se encontraron los pesos del autoencoder (--pesos).')
    estado = torch.load(ruta, map_location='cpu', weights_only=False)
    estado = estado.get('state_dict', estado) if isinstance(estado, dict) else estado
    faltan = modelo.load_state_dict(estado, strict=False)
    print(f'pesos {ruta}; claves no cargadas: {len(getattr(faltan, "missing_keys", []))}', flush=True)
    return modelo.to(dispositivo).eval()


def ida_vuelta_3d(modelo, dispositivo: str, hu_min: float, hu_max: float,
                  bloque: int, solape: int):
    """f(volumen HU) -> volumen HU reconstruido, por bloques con solape y promediado en los bordes."""
    import torch

    def f(vol: np.ndarray) -> np.ndarray:
        u = (np.clip(vol, hu_min, hu_max) - hu_min) / (hu_max - hu_min)  # [0, 1]
        salida = np.zeros_like(u, dtype=np.float32)
        peso = np.zeros_like(u, dtype=np.float32)
        paso = max(1, bloque - solape)
        with torch.no_grad():
            for z0 in range(0, max(1, u.shape[0] - solape), paso):
                z1 = min(z0 + bloque, u.shape[0])
                z0 = max(0, z1 - bloque)
                x = torch.from_numpy(u[z0:z1][None, None]).to(dispositivo) * 2.0 - 1.0
                if hasattr(modelo, 'reconstruct'):
                    y = modelo.reconstruct(x)
                else:
                    z = modelo.encode(x)
                    z = z[0] if isinstance(z, (tuple, list)) else z
                    y = modelo.decode(z)
                    y = y[0] if isinstance(y, (tuple, list)) else y
                y = ((y.float() + 1.0) / 2.0).clamp(0.0, 1.0).cpu().numpy()[0, 0]
                salida[z0:z1] += y
                peso[z0:z1] += 1.0
                if z1 >= u.shape[0]:
                    break
        u_rec = salida / np.maximum(peso, 1e-6)
        return u_rec * (hu_max - hu_min) + hu_min
    return f


def analizar(path: Path, meta: dict, f, args) -> dict:
    """Una fila por volumen: MAE y RMSE en hueso, metal y bdelta."""
    t0 = time.time()
    img = nib.load(path)
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
    fila = {k: meta[k] for k in ('Caso', 'Dataset', 'Grupo paciente', 'Metal', 'particion')}
    fila.update({'forma': ' '.join(map(str, arr.shape)), 'spacing': ' '.join(f'{z:.4f}' for z in zooms),
                 'hu_min_norma': args.hu_min, 'hu_max_norma': args.hu_max,
                 'bloque': args.bloque, 'solape': args.solape})
    idx = {'hueso': indices_roi(arr, BONE_HU), 'metal': indices_roi(arr, METAL_HU)}
    idx['bdelta'], _ = indices_bdelta(arr, zooms, args.bdelta_mm)
    plano = arr.ravel()
    vals = {r: plano[i] for r, i in idx.items()}
    for r, umbral in (('hueso', BONE_HU), ('metal', METAL_HU)):
        if not np.array_equal(submuestrea(arr[arr > umbral]), vals[r]):
            raise RuntimeError(f'los indices del ROI de {r} no dan los voxeles de E6c')
    del plano
    for r in ROIS:
        fila[f'n {r}'] = int(vals[r].size)
    rec = np.moveaxis(f(np.moveaxis(arr, eje, 0)), 0, eje).ravel()
    for r in ROIS:
        if vals[r].size:
            m, q = mae_rmse(np.abs(rec[idx[r]] - vals[r]))
            fila[f'maisi {r}'], fila[f'maisi {r} rmse'] = round(m, 4), round(q, 4)
    fila['segundos'] = round(time.time() - t0, 1)
    return fila


def resumen(out: Path, n_test: int) -> None:
    """Informe con la misma regla que P1: media por paciente del MAE en hueso < 25 HU."""
    import pandas as pd

    d = pd.read_csv(out / CSV_RES)
    err = out / CSV_ERR
    n_err = len(pd.read_csv(err)) if err.exists() and err.stat().st_size > 0 else 0
    L = ['# P1-MAISI — ida y vuelta con el VAE 3D de MAISI (extension del Objetivo 1)', '',
         f'Volumenes: {len(d)}; con error: {n_err}. Normalizacion: '
         f'[{d["hu_min_norma"].iloc[0] if len(d) else "?"}, {d["hu_max_norma"].iloc[0] if len(d) else "?"}] HU '
         '(tomada del paso 0, no del paper: `guo2025maisi` no la publica, #93).', '',
         '**Regla, la misma de P1 (#76):** pasa si la media por paciente del MAE en hueso es < 25 HU sobre TODOS '
         'los pacientes de test. **No hay `oraculo` ni `regla`: MAISI es de un canal.** Su resultado NO cambia el '
         'diseno del Objetivo 3 (decision 2026-09-19).', '']
    if len(d):
        v = d[d['particion'] == 'test']['maisi hueso'].dropna().to_numpy()
        L += ['| ROI | media | mediana | p10 | p90 |', '|---|---|---|---|---|']
        for r in ROIS:
            s = d[f'maisi {r}'].dropna()
            if len(s):
                L.append(f'| {r} | {s.mean():.2f} | {s.median():.2f} | {s.quantile(0.1):.2f} | {s.quantile(0.9):.2f} |')
        L.append('')
        if len(v) == n_test:
            L.append(f'**Media por paciente en hueso: {v.mean():.2f} HU** sobre {len(v)} pacientes de test -> '
                     f'**{"PASA" if v.mean() < UMBRAL_GO else "NO PASA"}** el umbral de {UMBRAL_GO:.0f} HU. '
                     f'Pacientes >= {UMBRAL_GO:.0f} HU: {int((v >= UMBRAL_GO).sum())}/{len(v)}.')
        else:
            L.append(f'**Sin veredicto:** {len(v)} de {n_test} pacientes de test evaluados.')
        L += ['', f'Tiempo por volumen: mediana {d["segundos"].median():.0f} s.', '']
    (out / 'p1_maisi.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'Escrito {out / "p1_maisi.md"}', flush=True)
    for x in L:
        if x.startswith('**Media por paciente') or x.startswith('**Sin veredicto'):
            print(x, flush=True)


def cota(args: argparse.Namespace) -> None:
    """Cota INFERIOR del error solo por el recorte de intensidad: sin modelo, sin GPU.

    Si la tuberia mapea su salida a [hu_min, hu_max], todo voxel fuera de ese rango ya esta perdido
    antes de que el autoencoder haga nada. Recortar y comparar da el suelo de error que ningun peso
    puede bajar. Es el mismo razonamiento de la columna `identidad` de E6c/P1.
    """
    metas = [m for m in leer_particion(args.particion) if m['particion'] in args.particiones]
    if args.casos:
        metas = [m for m in metas if m['Caso'] in set(args.casos)]
    ubic = rutas(metas, args.data)
    filas = []
    for i, meta in enumerate(metas, 1):
        caso = meta['Caso']
        if caso not in ubic:
            continue
        arr = nib.load(ubic[caso]).get_fdata(dtype=np.float32)
        fila = {'Caso': caso, 'Metal': meta['Metal']}
        for roi, umbral in (('hueso', BONE_HU), ('metal', METAL_HU)):
            v = submuestrea(arr[arr > umbral])
            if v.size:
                err = np.abs(np.clip(v, args.hu_min, args.hu_max) - v)
                m, q = mae_rmse(err)
                fila[f'{roi} mae'], fila[f'{roi} rmse'] = round(m, 2), round(q, 2)
                fila[f'{roi} frac_recortada'] = round(float((v > args.hu_max).mean()), 4)
                fila[f'n {roi}'] = int(v.size)
        filas.append(fila)
        print(f'{i}/{len(metas)} {caso}: hueso MAE {fila.get("hueso mae")} HU '
              f'(recortado {fila.get("hueso frac_recortada")}) | metal MAE {fila.get("metal mae", "-")}', flush=True)
    if not filas:
        raise SystemExit('Sin volumenes: nada que medir.')
    h = np.array([f['hueso mae'] for f in filas if 'hueso mae' in f])
    print(f'\nCOTA por recorte a [{args.hu_min:.0f}, {args.hu_max:.0f}] HU sobre {len(h)} pacientes '
          f'({", ".join(args.particiones)}):', flush=True)
    print(f'  MAE en hueso: media {h.mean():.2f} HU, mediana {np.median(h):.2f}, '
          f'min {h.min():.2f}, max {h.max():.2f}', flush=True)
    print(f'  Pacientes por encima del umbral de {UMBRAL_GO:.0f} HU: {int((h >= UMBRAL_GO).sum())}/{len(h)}', flush=True)
    print('  Es una COTA INFERIOR: ningun peso del modelo puede bajar de aqui mientras la salida '
          'se mapee a ese rango.', flush=True)
    if args.out:
        out = args.out.expanduser()
        out.mkdir(parents=True, exist_ok=True)
        campos = ['Caso', 'Metal'] + [f'{r} {s}' for r in ('hueso', 'metal')
                                      for s in ('mae', 'rmse', 'frac_recortada')] + ['n hueso', 'n metal']
        with (out / 'p1_maisi_cota.csv').open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=campos, extrasaction='ignore')
            w.writeheader()
            w.writerows(filas)
        print(f'Escrito {out / "p1_maisi_cota.csv"}', flush=True)


def evaluar(args: argparse.Namespace) -> None:
    """Recorre los volumenes de la particion pedida; reanudable por caso."""
    if args.hu_min is None or args.hu_max is None:
        raise SystemExit('ERROR: --hu-min y --hu-max son obligatorios y salen del paso 0 '
                         '(`inspeccionar`). No se asume ninguna normalizacion.')
    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    metas = [m for m in leer_particion(args.particion) if m['particion'] in args.particiones]
    if args.casos:
        metas = [m for m in metas if m['Caso'] in set(args.casos)]
    ubic = rutas(metas, args.data)
    hechos: set[str] = set()
    for nombre in (CSV_RES, CSV_ERR):
        ruta = out / nombre
        if ruta.exists() and ruta.stat().st_size > 0:
            with ruta.open(encoding='utf-8') as h:
                hechos |= {r['Caso'] for r in csv.DictReader(h)}

    import torch
    if args.dispositivo.startswith('cuda') and not torch.cuda.is_available():
        raise SystemExit('ERROR: se pidio cuda y torch no ve ninguna GPU.')
    print(f'torch {torch.__version__}; dispositivo {args.dispositivo}', flush=True)
    modelo = cargar_vae_maisi(args.bundle, args.pesos, args.dispositivo)
    f = ida_vuelta_3d(modelo, args.dispositivo, args.hu_min, args.hu_max, args.bloque, args.solape)
    print(f'{len(metas)} volumenes; {len(hechos)} ya hechos; normalizacion '
          f'[{args.hu_min}, {args.hu_max}] HU; bloques de {args.bloque} con solape {args.solape}', flush=True)

    s_res, s_err = abrir(out / CSV_RES, campos()), abrir(out / CSV_ERR, ['Caso', 'Error'])
    n = 0
    try:
        for meta in metas:
            caso = meta['Caso']
            if caso in hechos or caso not in ubic:
                continue
            if args.max is not None and n >= args.max:
                break
            n += 1
            try:
                fila = analizar(ubic[caso], meta, f, args)
            except Exception as exc:  # un volumen roto no detiene la cohorte
                s_err[1].writerow({'Caso': caso, 'Error': f'{type(exc).__name__}: {exc}'})
                s_err[0].flush()
                print(f'{caso}: ERROR {exc}', flush=True)
                traceback.print_exc()
                continue
            s_res[1].writerow(fila)
            s_res[0].flush()
            print(f'{caso}: ok {fila["segundos"]} s | hueso {fila.get("maisi hueso")} | '
                  f'metal {fila.get("maisi metal", "-")} | bdelta {fila.get("maisi bdelta", "-")}', flush=True)
    finally:
        for h, _ in (s_res, s_err):
            h.close()
    resumen(out, sum(m['particion'] == 'test' for m in leer_particion(args.particion)))


def main() -> None:
    """Subcomandos `inspeccionar` (paso 0, sin GPU) y `evaluar` (GPU)."""
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('inspeccionar')
    a.add_argument('--bundle', type=Path, required=True, help='carpeta del bundle de MAISI')

    c = sub.add_parser('cota', help='cota inferior del error por el recorte de intensidad, sin modelo ni GPU')
    c.add_argument('--particion', type=Path, default=aqui / 'p1_particion.csv')
    c.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    c.add_argument('--out', type=Path, default=None)
    c.add_argument('--particiones', nargs='+', default=['test'])
    c.add_argument('--hu-min', type=float, required=True)
    c.add_argument('--hu-max', type=float, required=True)
    c.add_argument('--casos', nargs='*', default=None)

    e = sub.add_parser('evaluar')
    e.add_argument('--bundle', type=Path, required=True)
    e.add_argument('--pesos', type=Path, default=None)
    e.add_argument('--particion', type=Path, default=aqui / 'p1_particion.csv')
    e.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'])
    e.add_argument('--out', type=Path, required=True)
    e.add_argument('--particiones', nargs='+', default=['test'])
    e.add_argument('--hu-min', type=float, default=None, help='del paso 0; sin valor por defecto')
    e.add_argument('--hu-max', type=float, default=None, help='del paso 0; sin valor por defecto')
    e.add_argument('--bloque', type=int, default=128, help='cortes por bloque en z')
    e.add_argument('--solape', type=int, default=32)
    e.add_argument('--bdelta-mm', type=float, default=12.0)
    e.add_argument('--dispositivo', default='cuda')
    e.add_argument('--casos', nargs='*', default=None)
    e.add_argument('--max', type=int, default=None)
    args = p.parse_args()

    if args.cmd == 'inspeccionar':
        inspeccionar(args.bundle)
    elif args.cmd == 'cota':
        cota(args)
    else:
        evaluar(args)


if __name__ == '__main__':
    main()
