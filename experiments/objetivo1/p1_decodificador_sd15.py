"""P1 — compuerta del Objetivo 1: VAE de SD 1.5 preentrenado frente a decodificador afinado (encoder congelado).

POR QUE
-------
Decision 2026-09-17 (`docs/01-decisiones.md`, B.3 y D.1) y regla preinscrita en `tesis/main.tex` (Objetivo 1):
el Go/No-Go (MAE en hueso < 25 HU, `HU -> multi-ventana -> VAE -> HU`) se evalua en pacientes separados para
(i) el autoencoder preentrenado y (ii) una variante con decodificador adaptado y encoder congelado. Si ninguno
pasa, no hay Objetivo 3 y el No-Go es el resultado. E6b ya midio (i) sobre los 178 CT sin particion; este script
no modifica E6b: reutiliza su codificacion, su seleccion de ROI, sus decodificadores de HU y su control de identidad.

REGLA DEL GO/NO-GO (fijada por la autora el 2026-09-17, ANTES de correr)
-----------------------------------------------------------------------
- Combinaciones: modelo {`sd15` preentrenado, `afinado`} x configuracion {`pub`, `LW20000`, `pub+asinh`}.
  Se afina un decodificador por configuracion. **Hay Go si ALGUNA combinacion pasa** (comparacion multiple
  declarada, no corregida).
- Lectura de HU: `vae regla` (canal mas estrecho no saturado, sin usar el HU verdadero). `vae oraculo` es cota.
- Estadistico: MAE en hueso por volumen (un volumen por paciente); **media sobre los pacientes de test < 25 HU**.
  IC95 bootstrap por paciente, mediana, pacientes que fallan y subgrupos se reportan y NO deciden.
- #76 (decidida como asesor, 2026-09-17, escrita en `main.tex`): un pase con limite superior del IC95 >= 25 HU se
  etiqueta MARGINAL (no cambia el veredicto). Si pasan varias, la que sigue al Objetivo 3 sale de un ORDEN A PRIORI,
  no del error: `pub+asinh`, `LW20000`, `pub`; dentro de cada una, `sd15` antes que `afinado` (`ORDEN_OBJ3`).
- Poblacion: todo el test (estratificado). Si falta algun paciente de test, la combinacion queda INCOMPLETA y sin
  veredicto.

DISENO (elecciones del asistente como asesor, 2026-09-17; no cambian el criterio)
--------------------------------------------------------------------------------
- Particion por paciente (`Grupo paciente` de `revision.csv`), sin ningun caso de `exclusiones.csv`; los dos
  `fusionado` entran como su union de `data/derivados/`. Estratos Dataset x Metal, restos mayores; semilla fija.
- "Decodificador" = `post_quant_conv` + `decoder`. `encoder` y `quant_conv` congelados: el latente no cambia.
- Entrenamiento: cortes axiales completos de pacientes `train`, codificados como en E6b (canal k -> canal k,
  u -> 2u - 1), latente = media de la posterior; perdida L1 entre salida y entrada en [-1, 1]; AdamW
  (weight_decay 0), warmup lineal y lr constante, recorte de gradiente 1.0, float32. Se usa el ultimo paso;
  `val` solo registra la curva y no elige checkpoint.
- ROI: hueso HU > 150 y metal HU > 2500 (identicos a E6b/E6c); `bdelta` = voxeles a distancia euclidea 3D
  <= 12 mm del metal (spacing del header), sin el metal. Mismo submuestreo por paso fijo hasta 1 000 000.
  `bdelta` es descriptivo (`main.tex`); los voxeles < -1000 HU del borde del FOV salen recortados por la ventana
  y su error ya aparece en `identidad`.

CONTROLES QUE PUEDEN FALLAR
---------------------------
- `identidad oraculo` frente a `e6c_techo_lw.csv` (hueso y metal), tolerancia 0.01 HU (el de E6b).
- `--vaes eco`: columnas `vae` iguales a `identidad` en los tres ROI.
- `sd15` en test frente a la cohorte MAE de E6b (`--e6b`): mismas cifras de `vae oraculo/regla` en hueso y metal.
- Hash del `encoder` + `quant_conv` al evaluar el afinado igual al registrado al entrenar (encoder congelado de
  verdad), y hash del decodificador afinado DISTINTO del preentrenado (el afinado cambio algo).
- Particion: ningun `Grupo paciente` en dos particiones.

SUBCOMANDOS
-----------
`particion` (CPU, local) -> `p1_particion.csv`. `entrenar --config C` (GPU, reanudable) -> `pesos/`.
`evaluar` (GPU, reanudable) -> `p1_eval.csv`, control y `p1_compuerta.md`. `resumen` rehace control e informe.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import math
import time
import traceback
from pathlib import Path
from typing import Callable

import nibabel as nib
import numpy as np

from e6b_vae_sd15 import (CONFIGS, DECODIFICADORES, SUF_RMSE, TOLERANCIA_CONTROL, UMBRAL_GO, abrir,
                          cargar_vae, eje_axial, errores, ida_vuelta_torch, indices_roi, mae_rmse, regla)
from e6c_techo_lw import BONE_HU, METAL_HU, configuraciones, submuestrea

ROIS = ('hueso', 'metal', 'bdelta')
BDELTA_MM = 12.0
SEMILLA_PARTICION = 20260917
N_TEST, N_VAL = 34, 8
TOLERANCIA_E6B = 0.05
N_BOOTSTRAP = 10_000
MODELOS = ('identidad', 'eco', 'sd15', 'afinado')
ORDEN_OBJ3 = tuple((m, c) for c in ('pub+asinh', 'LW20000', 'pub') for m in ('sd15', 'afinado'))  # #76, a priori
CSV_PART, CSV_EVAL, CSV_ERR, CSV_CTRL = 'p1_particion.csv', 'p1_eval.csv', 'p1_eval_errores.csv', 'p1_control.csv'

IdaVuelta = Callable[[np.ndarray], np.ndarray]
Fabrica = Callable[[str], IdaVuelta]


# ----------------------------------------------------------------------------------------------- particion
def particion(revision: Path, exclusiones: Path, out: Path, semilla: int, n_test: int, n_val: int) -> None:
    """Asigna train/val/test por paciente, estratificando por Dataset x Metal (restos mayores)."""
    import pandas as pd

    r = pd.read_csv(revision, encoding='utf-8-sig')
    e = pd.read_csv(exclusiones, encoding='utf-8-sig')
    metal = r.set_index('Caso')['Metal'].map(lambda v: 'si' if str(v).strip().lower().startswith('s') else 'no')
    k = r[~r['Caso'].isin(e['Caso'])][['Caso', 'Archivo', 'Dataset', 'Grupo paciente']].copy()
    k['Metal'] = k['Caso'].map(metal)
    uniones = [{'Caso': Path(destino).name.split('.nii')[0], 'Archivo': Path(destino).relative_to('data').as_posix(),
                'Dataset': g['Dataset'].iloc[0], 'Grupo paciente': g['Grupo paciente'].iloc[0],
                'Metal': 'si' if (metal[g['Caso']] == 'si').any() else 'no'}
               for destino, g in e[e['Estado'] == 'fusionado'].groupby('Sustituido por')]
    k = pd.concat([k, pd.DataFrame(uniones)], ignore_index=True)
    grupos = k.groupby('Grupo paciente').agg(Dataset=('Dataset', 'first'), Metal=('Metal', 'max')).reset_index()
    grupos['estrato'] = grupos['Dataset'] + ' ' + grupos['Metal']
    n = len(grupos)

    def cuotas(total: int) -> dict[str, int]:
        tam = grupos['estrato'].value_counts().sort_index()
        exacta = tam * total / n
        base = np.floor(exacta).astype(int)
        for est in (exacta - base).sort_values(ascending=False, kind='stable').index[:total - int(base.sum())]:
            base[est] += 1
        return base.to_dict()

    rng = np.random.default_rng(semilla)
    q_test, q_val = cuotas(n_test), cuotas(n_val)
    asignado: dict[str, str] = {}
    for est, g in grupos.groupby('estrato', sort=True):
        orden = sorted(g['Grupo paciente'])
        rng.shuffle(orden)
        for i, gp in enumerate(orden):
            asignado[gp] = 'test' if i < q_test[est] else 'val' if i < q_test[est] + q_val[est] else 'train'
    k['particion'] = k['Grupo paciente'].map(asignado)
    k = k.sort_values('Caso')
    k.to_csv(out, index=False, encoding='utf-8')
    print(f'Escrito {out}: {len(k)} casos, {n} pacientes, semilla {semilla}', flush=True)
    print(pd.crosstab(k['Dataset'] + ' ' + k['Metal'], k['particion'], margins=True).to_string(), flush=True)


def leer_particion(ruta: Path) -> list[dict[str, str]]:
    """Filas de la particion; aborta si un paciente cae en dos particiones."""
    with ruta.open(encoding='utf-8') as h:
        filas = list(csv.DictReader(h))
    por_grupo: dict[str, set[str]] = {}
    for f in filas:
        por_grupo.setdefault(f['Grupo paciente'], set()).add(f['particion'])
    mezclados = [g for g, s in por_grupo.items() if len(s) > 1]
    if mezclados:
        raise SystemExit(f'CONTROL particion FALLA: pacientes en dos particiones: {mezclados}')
    return filas


def rutas(filas: list[dict[str, str]], datas: list[Path]) -> dict[str, Path]:
    """Caso -> archivo, buscando por nombre bajo las raices dadas (la estructura difiere entre PC y Khipu)."""
    buscados = {f['Caso'] for f in filas}
    encontrados: dict[str, Path] = {}
    for d in datas:
        for q in d.expanduser().rglob('*.nii*'):
            caso = q.name.split('.nii')[0]
            if caso in buscados:
                encontrados.setdefault(caso, q)
    return encontrados


# ------------------------------------------------------------------------------------------------- pesos
def hash_estado(*modulos) -> str:
    """SHA256 de los tensores de uno o varios modulos, en orden de nombre."""
    h = hashlib.sha256()
    for m in modulos:
        for nombre, t in sorted(m.state_dict().items()):
            h.update(nombre.encode())
            h.update(t.detach().cpu().contiguous().numpy().tobytes())
    return h.hexdigest()


def nombre_pesos(cfg: str) -> str:
    """Archivo final del decodificador afinado de una configuracion."""
    return f'decoder_{cfg}.pt'


# ----------------------------------------------------------------------------------------- entrenamiento
def codifica(bloque: np.ndarray, canales: dict) -> np.ndarray:
    """(B, H, W) en HU -> (B, C, H, W) en [0, 1], canal k de la configuracion en el canal k (como E6b)."""
    return np.stack([canales[n][0](bloque) for n in canales], axis=1).astype(np.float32)


def cortes_train(paths: list[Path], rng: np.random.Generator, buffer: int):
    """Cortes axiales en HU, mezclados entre volumenes con un buffer; recorre todos los volumenes por epoca."""
    reserva: list[np.ndarray] = []
    epoca = 0
    while True:
        orden = list(paths)
        rng.shuffle(orden)
        for p in orden:
            img = nib.load(p)
            vol = np.moveaxis(img.get_fdata(dtype=np.float32), eje_axial(img), 0)
            reserva.extend(np.array(c) for c in vol)
            del vol
            while len(reserva) >= buffer:
                i = int(rng.integers(len(reserva)))
                reserva[i], reserva[-1] = reserva[-1], reserva[i]
                yield reserva.pop(), epoca
        epoca += 1


def cortes_val(paths: list[Path], por_volumen: int) -> np.ndarray:
    """Cortes fijos y equiespaciados de los volumenes `val` (deterministas)."""
    sel = []
    for p in paths:
        img = nib.load(p)
        vol = np.moveaxis(img.get_fdata(dtype=np.float32), eje_axial(img), 0)
        for i in np.linspace(0, vol.shape[0] - 1, por_volumen + 2)[1:-1].round().astype(int):
            sel.append(np.array(vol[i]))
    return np.stack(sel)


def mide_val(modelo, val: np.ndarray, canales: dict, dispositivo: str, lote: int) -> tuple[float, float, float]:
    """L1 en [-1, 1] (salida recortada, como al evaluar) y MAE/RMSE de `regla` en hueso sobre los cortes de val."""
    f = ida_vuelta_torch(modelo, dispositivo)
    l1, n, err = 0.0, 0, []
    for k in range(0, len(val), lote):
        hu = val[k:k + lote]
        u = codifica(hu, canales)
        y = f(u)
        l1 += float(np.abs((y - u) * 2.0).sum())
        n += y.size
        hueso = hu > BONE_HU
        if hueso.any():
            us = {nm: y[:, c][hueso] for c, nm in enumerate(canales)}
            err.append(np.abs(regla(us, canales) - hu[hueso]))
    m, q = mae_rmse(np.concatenate(err) if err else None)
    return l1 / n, m, q


def entrenar(args: argparse.Namespace) -> None:
    """Afina `post_quant_conv` + `decoder` para una configuracion; reanudable desde `ckpt_<cfg>.pt`."""
    import torch

    cfg = args.config
    canales = configuraciones()[cfg]
    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    final, ckpt = out / nombre_pesos(cfg), out / f'ckpt_{cfg}.pt'
    if final.exists():
        print(f'{final} ya existe: entrenamiento de {cfg} terminado. No se hace nada.', flush=True)
        return
    filas = leer_particion(args.particion)
    ubic = rutas(filas, args.data)
    faltan = [f['Caso'] for f in filas if f['particion'] in ('train', 'val') and f['Caso'] not in ubic]
    if faltan:
        raise SystemExit(f'ERROR: faltan {len(faltan)} volumenes train/val: {faltan[:5]}')
    tr = [ubic[f['Caso']] for f in filas if f['particion'] == 'train']
    va = [ubic[f['Caso']] for f in filas if f['particion'] == 'val']
    if args.max_vol:
        tr, va = tr[:args.max_vol], va[:max(1, args.max_vol // 4)]
    if args.dispositivo.startswith('cuda') and not torch.cuda.is_available():
        raise SystemExit('ERROR: se pidio cuda y torch no ve ninguna GPU.')
    torch.manual_seed(args.semilla)
    modelo = cargar_vae(args.modelo.expanduser(), args.dispositivo)
    for p in modelo.parameters():
        p.requires_grad_(False)
    entrenables = list(modelo.post_quant_conv.parameters()) + list(modelo.decoder.parameters())
    for p in entrenables:
        p.requires_grad_(True)
    h_enc = hash_estado(modelo.encoder, modelo.quant_conv)
    h_dec_pre = hash_estado(modelo.post_quant_conv, modelo.decoder)
    opt = torch.optim.AdamW(entrenables, lr=args.lr, weight_decay=0.0)
    paso = 0
    if ckpt.exists():
        est = torch.load(ckpt, map_location=args.dispositivo, weights_only=False)
        if est['hash_encoder'] != h_enc or est['config'] != cfg:
            raise SystemExit('ERROR: el checkpoint no corresponde a este VAE base o a esta configuracion.')
        modelo.post_quant_conv.load_state_dict(est['post_quant_conv'])
        modelo.decoder.load_state_dict(est['decoder'])
        opt.load_state_dict(est['opt'])
        paso = est['paso']
        print(f'Reanuda {cfg} desde el paso {paso}', flush=True)
    n_train = sum(p.numel() for p in entrenables)
    print(f'{cfg}: {len(tr)} volumenes train, {len(va)} val; {n_train} parametros entrenables; '
          f'hash encoder {h_enc[:16]}; decoder preentrenado {h_dec_pre[:16]}', flush=True)

    val = cortes_val(va, args.val_por_volumen)
    curva = out / f'curva_{cfg}.csv'
    s_curva = abrir(curva, ['paso', 'epoca', 'l1 train', 'l1 val', 'val hueso regla mae', 'val hueso regla rmse',
                            's por paso', 'mem gpu max gb', 'fecha'])

    def registra(ep: int, l1_tr: float, s_paso: float) -> None:
        modelo.eval()
        l1v, mv, qv = mide_val(modelo, val, canales, args.dispositivo, args.lote)
        modelo.decoder.train()
        mem = torch.cuda.max_memory_allocated() / 2**30 if args.dispositivo.startswith('cuda') else math.nan
        s_curva[1].writerow({'paso': paso, 'epoca': ep, 'l1 train': round(l1_tr, 6), 'l1 val': round(l1v, 6),
                             'val hueso regla mae': round(mv, 3), 'val hueso regla rmse': round(qv, 3),
                             's por paso': round(s_paso, 3), 'mem gpu max gb': round(mem, 2),
                             'fecha': time.strftime('%Y-%m-%dT%H:%M:%S')})
        s_curva[0].flush()
        print(f'paso {paso} epoca {ep}: l1 train {l1_tr:.5f} val {l1v:.5f} | val hueso regla MAE {mv:.2f} '
              f'RMSE {qv:.2f} HU | {s_paso:.2f} s/paso | mem {mem:.1f} GB', flush=True)

    def guarda(ruta: Path, completo: bool) -> None:
        est = {'config': cfg, 'paso': paso, 'hash_encoder': h_enc, 'hash_decoder_preentrenado': h_dec_pre,
               'post_quant_conv': modelo.post_quant_conv.state_dict(), 'decoder': modelo.decoder.state_dict(),
               'args': {k: str(v) for k, v in vars(args).items()}}
        if completo:
            est['hash_decoder'] = hash_estado(modelo.post_quant_conv, modelo.decoder)
        else:
            est['opt'] = opt.state_dict()
        tmp = ruta.with_suffix('.tmp')
        torch.save(est, tmp)
        tmp.replace(ruta)

    if paso == 0:
        registra(0, math.nan, math.nan)
    rng = np.random.default_rng(args.semilla + paso)  # al reanudar el orden de cortes no se reproduce: declarado
    datos = cortes_train(tr, rng, args.buffer)
    t_ini, t_bloque, acum, n_acum = time.time(), time.time(), 0.0, 0
    modelo.decoder.train()
    ep = 0
    try:
        while paso < args.pasos:
            lote_hu = []
            for _ in range(args.lote_entreno):
                c, ep = next(datos)
                lote_hu.append(c)
            hu = np.stack(lote_hu)
            if hu.shape[1] % 8 or hu.shape[2] % 8:
                raise SystemExit(f'ERROR: corte {hu.shape[1:]} no multiplo de 8; el entrenamiento no rellena.')
            x = torch.from_numpy(codifica(hu, canales)).to(args.dispositivo) * 2.0 - 1.0
            with torch.no_grad():
                z = modelo.encode(x).latent_dist.mean
            y = modelo.decode(z).sample
            perdida = torch.nn.functional.l1_loss(y, x)
            opt.zero_grad(set_to_none=True)
            perdida.backward()
            torch.nn.utils.clip_grad_norm_(entrenables, 1.0)
            for g in opt.param_groups:
                g['lr'] = args.lr * min(1.0, (paso + 1) / max(1, args.warmup))
            opt.step()
            paso += 1
            acum += float(perdida.detach())
            n_acum += 1
            if paso % args.cada_val == 0 or paso == args.pasos:
                registra(ep, acum / n_acum, (time.time() - t_bloque) / n_acum)
                acum, n_acum, t_bloque = 0.0, 0, time.time()
            if paso % args.cada_ckpt == 0 and paso < args.pasos:
                guarda(ckpt, completo=False)
            if args.horas_max and time.time() - t_ini > args.horas_max * 3600 and paso < args.pasos:
                guarda(ckpt, completo=False)
                print(f'INCOMPLETO: {paso}/{args.pasos} pasos al llegar a --horas-max. Relanzar para seguir.',
                      flush=True)
                return
        if hash_estado(modelo.encoder, modelo.quant_conv) != h_enc:
            raise SystemExit('CONTROL encoder FALLA: los pesos del encoder cambiaron durante el entrenamiento.')
        guarda(final, completo=True)
        if ckpt.exists():
            ckpt.unlink()
        print(f'COMPLETO: {final} ({paso} pasos). CONTROL encoder congelado: hash identico.', flush=True)
    finally:
        s_curva[0].close()


# -------------------------------------------------------------------------------------------- evaluacion
def indices_bdelta(arr: np.ndarray, zooms: tuple[float, ...], mm: float) -> tuple[np.ndarray, int]:
    """Indices planos de la banda `B_delta` (distancia 3D <= mm al metal, sin el metal) y su tamano total."""
    from scipy.ndimage import distance_transform_edt

    metal = arr > METAL_HU
    if not metal.any():
        return np.empty(0, dtype=np.int64), 0
    margen = [int(math.ceil(mm / z)) + 1 for z in zooms]
    nz = np.nonzero(metal)
    sl = tuple(slice(max(0, int(c.min()) - m), min(s, int(c.max()) + m + 1))
               for c, m, s in zip(nz, margen, arr.shape))
    del nz
    sub = metal[sl]
    banda = np.zeros(arr.shape, dtype=bool)
    banda[sl] = (distance_transform_edt(~sub, sampling=zooms) <= mm) & ~sub
    total = int(banda.sum())
    return indices_roi(banda, 0.5), total


def fabrica_pesos(pesos: Path, modelo_base: Path, dispositivo: str, configs: tuple[str, ...]) -> tuple[Fabrica, list[dict]]:
    """Carga el VAE base una vez y cambia `post_quant_conv` + `decoder` segun la configuracion."""
    import torch

    modelo = cargar_vae(modelo_base, dispositivo)
    h_enc = hash_estado(modelo.encoder, modelo.quant_conv)
    h_pre = hash_estado(modelo.post_quant_conv, modelo.decoder)
    estados, filas = {}, []
    for cfg in configs:
        ruta = pesos / nombre_pesos(cfg)
        if not ruta.exists():
            raise SystemExit(f'ERROR: falta {ruta} (entrenamiento de {cfg} sin terminar).')
        est = torch.load(ruta, map_location='cpu', weights_only=False)
        estados[cfg] = est
        for nombre, ok in (('encoder congelado (hash base = hash al entrenar)', est['hash_encoder'] == h_enc),
                           ('decodificador afinado distinto del preentrenado',
                            est['hash_decoder'] != h_pre and est['hash_decoder_preentrenado'] == h_pre)):
            filas.append({'control': nombre, 'Caso': '-', 'columna': cfg, 'valor': est['paso'],
                          'referencia': '-', 'coincide': ok})
    activo: list[str | None] = [None]

    def fabrica(cfg: str) -> IdaVuelta:
        if activo[0] != cfg:
            modelo.post_quant_conv.load_state_dict(estados[cfg]['post_quant_conv'])
            modelo.decoder.load_state_dict(estados[cfg]['decoder'])
            if hash_estado(modelo.post_quant_conv, modelo.decoder) != estados[cfg]['hash_decoder']:
                raise RuntimeError(f'hash del decodificador de {cfg} no coincide tras cargarlo')
            modelo.eval()
            activo[0] = cfg
        return ida_vuelta_torch(modelo, dispositivo)
    return fabrica, filas


def campos() -> list[str]:
    """Columnas de la tabla por volumen y modelo."""
    base = ['Caso', 'Dataset', 'Grupo paciente', 'Metal', 'particion', 'modelo', 'forma', 'eje_axial', 'spacing',
            'n hueso', 'n metal', 'n bdelta', 'n bdelta total', 'segundos']
    return base + [f'{c} {d} {r}{suf}' for c in CONFIGS for d in DECODIFICADORES for r in ROIS
                   for suf in ('', SUF_RMSE)]


def analizar(path: Path, meta: dict[str, str], cfgs: dict, fabrica: Fabrica | None, lote: int,
             etiqueta: str, bdelta_mm: float, configs: tuple[str, ...] = CONFIGS) -> dict:
    """Una fila por volumen y modelo: MAE y RMSE por configuracion, decodificador de HU y ROI (como E6b + bdelta)."""
    t0 = time.time()
    img = nib.load(path)
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = tuple(float(z) for z in img.header.get_zooms()[:3])
    fila: dict[str, object] = {k: meta[k] for k in ('Caso', 'Dataset', 'Grupo paciente', 'Metal', 'particion')}
    fila.update({'modelo': etiqueta, 'forma': ' '.join(map(str, arr.shape)), 'eje_axial': eje,
                 'spacing': ' '.join(f'{z:.4f}' for z in zooms)})
    idx = {'hueso': indices_roi(arr, BONE_HU), 'metal': indices_roi(arr, METAL_HU)}
    idx['bdelta'], fila['n bdelta total'] = indices_bdelta(arr, zooms, bdelta_mm)
    plano = arr.ravel()
    vals = {r: plano[i] for r, i in idx.items()}
    for r, umbral in (('hueso', BONE_HU), ('metal', METAL_HU)):
        if not np.array_equal(submuestrea(arr[arr > umbral]), vals[r]):
            raise RuntimeError(f'los indices del ROI de {r} no dan los voxeles de E6c')
    del plano
    for r in ROIS:
        fila[f'n {r}'] = int(vals[r].size)
    movido = np.moveaxis(arr, eje, 0)

    for cfg in configs:
        canales = cfgs[cfg]
        for r in ROIS:
            if vals[r].size:
                us = {n: ida(vals[r]) for n, (ida, _) in canales.items()}
                for dec, e in zip(('identidad oraculo', 'identidad regla'), errores(vals[r], us, canales)):
                    m, q = mae_rmse(e)
                    fila[f'{cfg} {dec} {r}'], fila[f'{cfg} {dec} {r}{SUF_RMSE}'] = round(m, 4), round(q, 4)
        if fabrica is None:
            continue
        f = fabrica(cfg)
        nombres = list(canales)
        dec = np.empty((len(nombres),) + movido.shape, dtype=np.float32)
        for k0 in range(0, movido.shape[0], lote):
            bloque = movido[k0:k0 + lote]
            dec[:, k0:k0 + bloque.shape[0]] = f(codifica(bloque, canales)).transpose(1, 0, 2, 3)
        us_roi: dict[str, dict[str, np.ndarray]] = {r: {} for r in ROIS}
        for c, n in enumerate(nombres):
            plano_c = np.moveaxis(dec[c], 0, eje).ravel()
            for r in ROIS:
                us_roi[r][n] = plano_c[idx[r]]
            del plano_c
        del dec
        for r in ROIS:
            if vals[r].size:
                for d, e in zip(('vae oraculo', 'vae regla'), errores(vals[r], us_roi[r], canales)):
                    m, q = mae_rmse(e)
                    fila[f'{cfg} {d} {r}'], fila[f'{cfg} {d} {r}{SUF_RMSE}'] = round(m, 4), round(q, 4)
    fila['segundos'] = round(time.time() - t0, 1)
    return fila


def evaluar(args: argparse.Namespace) -> None:
    """Recorre los volumenes de la particion pedida con cada modelo; reanudable por (Caso, modelo)."""
    out = args.out.expanduser()
    out.mkdir(parents=True, exist_ok=True)
    filas = [f for f in leer_particion(args.particion) if f['particion'] in args.particiones]
    if args.casos:
        filas = [f for f in filas if f['Caso'] in set(args.casos)]
    ubic = rutas(filas, args.data)
    faltan = [f['Caso'] for f in filas if f['Caso'] not in ubic]
    if faltan:
        print(f'AVISO: {len(faltan)} volumenes no encontrados: {faltan}', flush=True)
    hechos: set[tuple[str, str]] = set()
    for nombre in (CSV_EVAL, CSV_ERR):
        ruta = out / nombre
        if ruta.exists() and ruta.stat().st_size > 0:
            with ruta.open(encoding='utf-8') as h:
                hechos |= {(r['Caso'], r['modelo']) for r in csv.DictReader(h)}

    fabricas: dict[str, Fabrica | None] = {}
    ctrl_pesos: list[dict] = []
    if set(args.vaes) & {'eco', 'sd15', 'afinado'}:
        import torch
        if args.dispositivo.startswith('cuda') and not torch.cuda.is_available():
            raise SystemExit('ERROR: se pidio cuda y torch no ve ninguna GPU.')
        print(f'torch {torch.__version__}; dispositivo {args.dispositivo}'
              + (f' ({torch.cuda.get_device_name(0)})' if args.dispositivo.startswith('cuda') else ''), flush=True)
    for v in args.vaes:
        if v == 'identidad':
            fabricas[v] = None
        elif v == 'eco':
            f_eco = ida_vuelta_torch(None, args.dispositivo)
            fabricas[v] = lambda cfg, f_eco=f_eco: f_eco
        elif args.modelo is None:
            raise SystemExit(f'ERROR: --vaes {v} necesita --modelo.')
        elif v == 'sd15':
            f_sd = ida_vuelta_torch(cargar_vae(args.modelo.expanduser(), args.dispositivo), args.dispositivo)
            fabricas[v] = lambda cfg, f_sd=f_sd: f_sd
        else:
            if args.pesos is None:
                raise SystemExit('ERROR: --vaes afinado necesita --pesos.')
            fabricas[v], ctrl_pesos = fabrica_pesos(args.pesos.expanduser(), args.modelo.expanduser(),
                                                    args.dispositivo, tuple(args.configs))
    if ctrl_pesos:
        with (out / 'p1_control_pesos.csv').open('w', encoding='utf-8', newline='') as h:
            w = csv.DictWriter(h, fieldnames=list(ctrl_pesos[0]))
            w.writeheader()
            w.writerows(ctrl_pesos)
        for c in ctrl_pesos:
            print(f'CONTROL {c["control"]} [{c["columna"]}, paso {c["valor"]}]: '
                  f'{"OK" if c["coincide"] else "FALLA"}', flush=True)
    print(f'{len(filas)} volumenes ({", ".join(args.particiones)}); modelos {args.vaes}; '
          f'{len(hechos)} pares ya hechos', flush=True)

    cfgs = configuraciones()
    s_res, s_err = abrir(out / CSV_EVAL, campos()), abrir(out / CSV_ERR, ['Caso', 'modelo', 'Error'])
    nuevos = 0
    try:
        for meta in filas:
            caso = meta['Caso']
            if caso not in ubic:
                continue
            for v in args.vaes:
                if (caso, v) in hechos:
                    continue
                if args.max is not None and nuevos >= args.max:
                    break
                nuevos += 1
                try:
                    fila = analizar(ubic[caso], meta, cfgs, fabricas[v], args.lote, v, args.bdelta_mm,
                                    tuple(args.configs))
                except Exception as exc:  # un volumen roto no detiene la cohorte
                    s_err[1].writerow({'Caso': caso, 'modelo': v, 'Error': f'{type(exc).__name__}: {exc}'})
                    s_err[0].flush()
                    print(f'{caso} [{v}]: ERROR {exc}', flush=True)
                    traceback.print_exc()
                    continue
                s_res[1].writerow(fila)
                s_res[0].flush()
                print(f'{caso} [{v}]: ok {fila["segundos"]} s | hueso MAE vae regla '
                      + ' '.join(f'{c}={fila.get(f"{c} vae regla hueso", "-")}' for c in CONFIGS)
                      + f' | n bdelta {fila["n bdelta"]}', flush=True)
    finally:
        for h, _ in (s_res, s_err):
            h.close()
    control(out, args.e6c, args.e6b)
    resumen(out, args.pesos.expanduser() if args.pesos else None, args.particion)


# --------------------------------------------------------------------------------------- control e informe
def control(out: Path, e6c: Path | None, e6b: Path | None) -> None:
    """Identidad frente a E6c, eco frente a identidad, sd15 frente a E6b, y controles de pesos si existen."""
    import pandas as pd

    d = pd.read_csv(out / CSV_EVAL)
    filas: list[dict] = []

    def compara(nombre: str, casos, a, b, columna: str, tol: float) -> None:
        for caso, x, y in zip(casos, a, b):
            if pd.isna(x) and pd.isna(y):
                continue
            filas.append({'control': nombre, 'Caso': caso, 'columna': columna, 'valor': x, 'referencia': y,
                          'coincide': bool(pd.notna(x) and pd.notna(y) and abs(x - y) <= tol)})

    ident = d.drop_duplicates('Caso')
    medidas = [c for c in CONFIGS if d[f'{c} identidad oraculo hueso'].notna().any()]  # --configs parcial
    if e6c is not None:
        m = ident.merge(pd.read_csv(e6c), on='Caso', how='inner')
        for cfg in medidas:
            for r in ('hueso', 'metal'):
                compara('identidad frente a E6c float', m['Caso'], m[f'{cfg} identidad oraculo {r}'],
                        m[f'{cfg} float {r}'], f'{cfg} {r}', TOLERANCIA_CONTROL)
    eco = d[d['modelo'] == 'eco']
    for cfg in medidas:
        for dec in ('oraculo', 'regla'):
            for r in ROIS:
                compara('eco frente a identidad', eco['Caso'], eco[f'{cfg} vae {dec} {r}'],
                        eco[f'{cfg} identidad {dec} {r}'], f'{cfg} {dec} {r}', TOLERANCIA_CONTROL)
    if e6b is not None:
        m = d[d['modelo'] == 'sd15'].merge(pd.read_csv(e6b), on='Caso', how='inner', suffixes=('', ' e6b'))
        for cfg in medidas:
            for dec in ('vae oraculo', 'vae regla'):
                for r in ('hueso', 'metal'):
                    col = f'{cfg} {dec} {r}'
                    if f'{col} e6b' in m:
                        compara('sd15 frente a E6b', m['Caso'], m[col], m[f'{col} e6b'], col, TOLERANCIA_E6B)
    pesos = out / 'p1_control_pesos.csv'
    if pesos.exists():
        filas += pd.read_csv(pesos).to_dict('records')
    if not filas:
        print('CONTROL NO EJECUTADO: sin E6c, E6b, eco ni pesos. El resultado no esta validado.', flush=True)
        return
    c = pd.DataFrame(filas)
    c.to_csv(out / CSV_CTRL, index=False)
    for nombre, g in c.groupby('control'):
        tol = TOLERANCIA_E6B if nombre == 'sd15 frente a E6b' else TOLERANCIA_CONTROL
        print(f'CONTROL {nombre}: {int(g["coincide"].sum())} de {len(g)} coinciden (tolerancia {tol} HU)', flush=True)
        if not g['coincide'].astype(bool).all():
            print(g.loc[~g['coincide'].astype(bool), ['Caso', 'columna', 'valor', 'referencia']].to_string(index=False),
                  flush=True)


def ic95(v: np.ndarray, semilla: int = 0) -> tuple[float, float]:
    """IC95 percentil de la media, bootstrap por paciente."""
    if len(v) < 2:
        return math.nan, math.nan
    rng = np.random.default_rng(semilla)
    medias = v[rng.integers(0, len(v), size=(N_BOOTSTRAP, len(v)))].mean(axis=1)
    return float(np.percentile(medias, 2.5)), float(np.percentile(medias, 97.5))


def resumen(out: Path, pesos: Path | None, particion: Path) -> None:
    """Informe `p1_compuerta.md`: veredicto preinscrito, tablas MAE/RMSE por ROI, subgrupos y curvas."""
    import pandas as pd

    d = pd.read_csv(out / CSV_EVAL)
    err = out / CSV_ERR
    n_err = len(pd.read_csv(err)) if err.exists() and err.stat().st_size > 0 else 0
    L = ['# P1 — compuerta del Objetivo 1: VAE de SD 1.5 preentrenado frente a decodificador afinado', '',
         f'Filas: {len(d)}; con error: {n_err}. Modelos: {", ".join(sorted(d["modelo"].unique()))}. '
         f'Particiones: {", ".join(sorted(d["particion"].unique()))}. Generado por `p1_decodificador_sd15.py`.', '',
         '**Regla preinscrita (autora, 2026-09-17):** hay Go si ALGUNA combinacion modelo {sd15, afinado} x '
         'configuracion tiene **media por paciente del MAE en hueso con `vae regla` < 25 HU** sobre TODOS los '
         'pacientes de test. IC95, mediana, fallos por paciente, RMSE, metal, `bdelta` y subgrupos NO deciden.', '']
    ctrl = out / CSV_CTRL
    if ctrl.exists():
        c = pd.read_csv(ctrl)
        L += ['## Controles', '', '| Control | coinciden | total |', '|---|---|---|']
        L += [f'| {n} | {int(g["coincide"].astype(bool).sum())} | {len(g)} |' for n, g in c.groupby('control')]
        L.append('')
    else:
        L += ['> **CONTROL NO EJECUTADO.** El resultado no esta validado.', '']

    test = d[d['particion'] == 'test']
    n_test_part = sum(f['particion'] == 'test' for f in leer_particion(particion))
    L += ['## Veredicto del Go/No-Go (test)', '',
          '| Modelo | Configuracion | n | media MAE hueso regla | IC95 bootstrap | mediana | pacientes >= 25 | '
          'RMSE media | Pasa |', '|---|---|---|---|---|---|---|---|---|']
    veredictos = []
    marginal: dict[tuple[str, str], bool] = {}
    for mod in ('sd15', 'afinado'):
        g = test[test['modelo'] == mod]
        for cfg in CONFIGS:
            v = g[f'{cfg} vae regla hueso'].dropna().to_numpy() if len(g) else np.empty(0)
            if len(v) == 0:
                L.append(f'| {mod} | `{cfg}` | 0 | - | - | - | - | - | sin datos |')
                continue
            lo, hi = ic95(v)
            completo = len(v) == n_test_part
            pasa = completo and v.mean() < UMBRAL_GO
            veredictos.append((mod, cfg, completo, pasa))
            marginal[(mod, cfg)] = bool(pasa and not hi < UMBRAL_GO)
            q = g[f'{cfg} vae regla hueso{SUF_RMSE}'].dropna().to_numpy()
            L.append(f'| {mod} | `{cfg}` | {len(v)} | {v.mean():.2f} | [{lo:.2f}, {hi:.2f}] | {np.median(v):.2f} | '
                     f'{int((v >= UMBRAL_GO).sum())}/{len(v)} | {q.mean():.2f} | '
                     f'{(("SI (MARGINAL)" if marginal[(mod, cfg)] else "SI") if pasa else "NO") if completo else f"INCOMPLETO ({len(v)}/{n_test_part})"} |')
    completos = [x for x in veredictos if x[2]]
    L.append('')
    if len(completos) == 2 * len(CONFIGS):
        pasan = [(m, c) for m, c, _, p in completos if p]
        if pasan:
            elegida = next(x for x in ORDEN_OBJ3 if x in pasan)
            L.append(f'**Resultado: GO.** Pasan: {", ".join(f"{m} `{c}`" for m, c in pasan)}. '
                     f'Sigue al Objetivo 3 (orden a priori, #76): **{elegida[0]} `{elegida[1]}`**'
                     + (' (MARGINAL: IC95 superior >= 25 HU).' if marginal[elegida] else '.'))
        else:
            L.append('**Resultado: NO-GO.** Ninguna combinacion pasa: no hay Objetivo 3.')
    else:
        L.append(f'**Sin veredicto:** {len(completos)} de {2 * len(CONFIGS)} combinaciones completas en test.')
    L.append('')

    for nombre, suf in (('MAE', ''), ('RMSE', SUF_RMSE)):
        for r in ROIS:
            L += [f'## {nombre} en ROI {r} (test): media / mediana por paciente, HU', '',
                  '| Modelo | Configuracion | ' + ' | '.join(DECODIFICADORES) + ' |',
                  '|---|---|' + '---|' * len(DECODIFICADORES)]
            for mod in ('sd15', 'afinado'):
                g = test[test['modelo'] == mod]
                for cfg in CONFIGS:
                    celdas = []
                    for dec in DECODIFICADORES:
                        v = g[f'{cfg} {dec} {r}{suf}'].dropna() if len(g) else pd.Series(dtype=float)
                        celdas.append(f'{v.mean():.2f} / {v.median():.2f} (n={len(v)})' if len(v) else '-')
                    L.append(f'| {mod} | `{cfg}` | ' + ' | '.join(celdas) + ' |')
            L.append('')

    L += ['## Hueso con `vae regla` por subgrupo (test, descriptivo): media / mediana, HU', '',
          '| Modelo | Configuracion | Dataset | Metal | n | MAE | RMSE |', '|---|---|---|---|---|---|---|']
    for mod in ('sd15', 'afinado'):
        for cfg in CONFIGS:
            for (ds, mt), g in test[test['modelo'] == mod].groupby(['Dataset', 'Metal']):
                v, q = g[f'{cfg} vae regla hueso'].dropna(), g[f'{cfg} vae regla hueso{SUF_RMSE}'].dropna()
                if len(v):
                    L.append(f'| {mod} | `{cfg}` | {ds} | {mt} | {len(v)} | {v.mean():.2f} / {v.median():.2f} | '
                             f'{q.mean():.2f} / {q.median():.2f} |')
    L.append('')

    if pesos is not None:
        L += ['## Curvas de entrenamiento (ultimo registro; `val` no elige checkpoint)', '',
              '| Configuracion | paso | l1 train | l1 val | val hueso regla MAE (paso 0 -> final) | s por paso | '
              'mem GB |', '|---|---|---|---|---|---|---|']
        for cfg in CONFIGS:
            cv = pesos / f'curva_{cfg}.csv'
            if cv.exists() and cv.stat().st_size > 0:
                k = pd.read_csv(cv)
                u, p0 = k.iloc[-1], k.iloc[0]
                L.append(f'| `{cfg}` | {u["paso"]} | {u["l1 train"]} | {u["l1 val"]} | '
                         f'{p0["val hueso regla mae"]} -> {u["val hueso regla mae"]} | {u["s por paso"]} | '
                         f'{u["mem gpu max gb"]} |')
        L.append('')
    if 'segundos' in d and len(d):
        L.append(f'Tiempo por fila: mediana {d["segundos"].median():.0f} s; total {d["segundos"].sum() / 3600:.2f} h.')
    (out / 'p1_compuerta.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print(f'Escrito {out / "p1_compuerta.md"}', flush=True)
    for x in L:
        if x.startswith('**Resultado') or x.startswith('**Sin veredicto'):
            print(x, flush=True)


# ------------------------------------------------------------------------------------------------- main
def main() -> None:
    """Subcomandos `particion`, `entrenar`, `evaluar` y `resumen`."""
    aqui = Path(__file__).resolve().parent
    raiz = aqui.parents[1]
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)

    a = sub.add_parser('particion')
    a.add_argument('--revision', type=Path, default=raiz / 'experiments/exploration-3d/revision.csv')
    a.add_argument('--exclusiones', type=Path, default=raiz / 'experiments/exploration-3d/exclusiones.csv')
    a.add_argument('--out', type=Path, default=aqui / CSV_PART)
    a.add_argument('--semilla', type=int, default=SEMILLA_PARTICION)
    a.add_argument('--n-test', type=int, default=N_TEST)
    a.add_argument('--n-val', type=int, default=N_VAL)

    comunes = argparse.ArgumentParser(add_help=False)
    comunes.add_argument('--particion', type=Path, default=aqui / CSV_PART)
    comunes.add_argument('--data', type=Path, nargs='+', default=[raiz / 'data'],
                         help='raices donde buscar los .nii por nombre (Khipu: extracted y derivados)')
    comunes.add_argument('--modelo', type=Path, default=None, help='carpeta con vae/config.json y los pesos de SD 1.5')
    comunes.add_argument('--dispositivo', default='cuda')
    comunes.add_argument('--lote', type=int, default=4, help='cortes por lote en inferencia (E6b: 4)')

    t = sub.add_parser('entrenar', parents=[comunes])
    t.add_argument('--config', choices=CONFIGS, required=True)
    t.add_argument('--out', type=Path, required=True, help='carpeta de pesos, checkpoints y curvas')
    t.add_argument('--pasos', type=int, default=30_000)
    t.add_argument('--lote-entreno', type=int, default=4)
    t.add_argument('--lr', type=float, default=1e-4)
    t.add_argument('--warmup', type=int, default=500)
    t.add_argument('--buffer', type=int, default=3000, help='cortes en la reserva de mezcla')
    t.add_argument('--cada-val', type=int, default=1000)
    t.add_argument('--cada-ckpt', type=int, default=1000)
    t.add_argument('--val-por-volumen', type=int, default=8)
    t.add_argument('--horas-max', type=float, default=None, help='guarda y sale antes del limite del job')
    t.add_argument('--semilla', type=int, default=0)
    t.add_argument('--max-vol', type=int, default=None, help='solo pruebas: limita volumenes train')

    e = sub.add_parser('evaluar', parents=[comunes])
    e.add_argument('--out', type=Path, required=True)
    e.add_argument('--vaes', nargs='+', choices=MODELOS, default=['sd15', 'afinado'])
    e.add_argument('--pesos', type=Path, default=None, help='carpeta con decoder_<cfg>.pt')
    e.add_argument('--particiones', nargs='+', default=['test'])
    e.add_argument('--bdelta-mm', type=float, default=BDELTA_MM)
    e.add_argument('--e6c', type=Path, default=None)
    e.add_argument('--e6b', type=Path, default=None, help='e6b_vae_sd15.csv de la cohorte MAE (control sd15)')
    e.add_argument('--configs', nargs='+', choices=CONFIGS, default=list(CONFIGS),
                   help='solo pruebas: el Go/No-Go exige las tres')
    e.add_argument('--casos', nargs='*', default=None)
    e.add_argument('--max', type=int, default=None)

    s = sub.add_parser('resumen')
    s.add_argument('--out', type=Path, required=True)
    s.add_argument('--pesos', type=Path, default=None)
    s.add_argument('--e6c', type=Path, default=None)
    s.add_argument('--e6b', type=Path, default=None)
    s.add_argument('--particion', type=Path, default=aqui / CSV_PART)
    args = p.parse_args()

    for ref in (getattr(args, 'e6c', None), getattr(args, 'e6b', None), getattr(args, 'particion', None)):
        if args.cmd != 'particion' and ref is not None and not ref.expanduser().exists():
            raise SystemExit(f'ERROR: no existe {ref}. Nada se ejecuto (se comprueba antes de cargar modelos).')
    if args.cmd == 'particion':
        particion(args.revision, args.exclusiones, args.out, args.semilla, args.n_test, args.n_val)
    elif args.cmd == 'entrenar':
        entrenar(args)
    elif args.cmd == 'evaluar':
        evaluar(args)
    else:
        out = args.out.expanduser()
        control(out, args.e6c, args.e6b)
        resumen(out, args.pesos.expanduser() if args.pesos else None, args.particion)


if __name__ == '__main__':
    main()
