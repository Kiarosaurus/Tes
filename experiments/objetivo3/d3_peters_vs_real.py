"""D3 - perfil radial de Peters (Ti y Fe) frente al real (D1) y al sintetico (D2), con la MISMA metrica que D1.

Pregunta (DEC 2026-11-24 (23)): cuanto se aleja el protocolo fisico de la amplitud real por anillo, y donde queda lo real
respecto de Peters y del modelo. Es DESCRIPTIVO (sin regla de decision) y no sustituye a E-A2.

Metrica (la de D1, `d1_alcance_rayas.py`): exceso = amplitud de Peters (5 % superior - 5 % inferior) de la imagen con metal
menos la de la misma imagen sin metal, en los mismos pixeles de cuerpo fuera de `M`, por anillo de 2 mm de distancia en el
plano a `M`. Peters: salidas de `a19` (`outputs/obj3_pose/peters_final` = 13 de prueba y `peters_val` = 2 de validacion),
condicion A (`Ti_A`, `Fe_A`) frente a `limpia_A`; hasta `--max-cortes` cortes por paciente (mediana), luego mediana de pacientes.
Real: `outputs/d1_tornillo/d1_por_paciente.csv` (componentes de tamano tornillo, D1). Sintetico: `outputs/d2/d2_perfil.csv` (D2,
`run04_mejor`, validacion 0101/0102, mediana de los dos pacientes).

Limites: pacientes distintos en cada columna (Peters 15, real 18, sintetico 2); la referencia real es otro corte del mismo
paciente, la de Peters y el sintetico es el mismo corte sin metal; no se conoce material ni reconstruccion de los tornillos reales.

EXTENSION (2026-11-24, 2.a version): ademas del exceso (a) de D1 se calcula la amplitud de la desviacion (b) = amplitud(img - ref), la
definicion de A20 pero en anillos AXIALES, para Peters Ti y el sintetizador evaluado (`run04_mejor`, 5 semillas) en los MISMOS 13
pacientes de prueba (`outputs/obj3_pose/final/run04_mejor` y `peters_final`). El real solo tiene (a) (no hay imagen sin metal del mismo corte).
No sustituye a E-A2 (anillos perpendiculares a `u`, preinscrito); es un analisis de sensibilidad a estadistico y geometria.

Salida: `outputs/d3/d3_peters_real_modelo.csv` y `d3_resumen.md`. Resumen versionado: `d3_peters_vs_real_resultado.md`.

USO
---
    python experiments/objetivo3/d3_peters_vs_real.py [--max-cortes 8]
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import os
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

from d1_alcance_rayas import BORDES_MM, MIN_PIX, amplitud, cuerpo_2d, perfil

_AQUI = Path(__file__).resolve().parent
ANILLOS = 12          # 0-24 mm


def pixel(j: dict) -> tuple[float, float]:
    p = j['pixel_mm']
    return (float(p[0]), float(p[1])) if isinstance(p, list) else (float(p), float(p))


def peters(max_cortes: int) -> tuple[dict[str, np.ndarray], list[str]]:
    res: dict[str, list[np.ndarray]] = {'Ti': [], 'Fe': []}
    nombres: list[str] = []
    archivos = (sorted(glob.glob(str(_AQUI / 'outputs/obj3_pose/peters_final/a19_*.npz')))
                + sorted(glob.glob(str(_AQUI / 'outputs/obj3_pose/peters_val/a19_*.npz'))))
    for f in archivos:
        z = np.load(f)
        j = json.load(open(f[:-4] + '.json'))
        px = pixel(j)
        nombres.append(os.path.basename(f)[4:-4])
        n = len(z['ks'])
        idx = list(range(n))[::max(1, n // max_cortes)][:max_cortes]
        for mat in ('Ti', 'Fe'):
            por_corte = []
            for i in idx:
                m = z['M'][i]
                if m.sum() < 20:
                    continue
                dist = ndi.distance_transform_edt(~m, sampling=px)
                valido = cuerpo_2d(z['original'][i]) & ~m
                por_corte.append(perfil(z[mat + '_A'][i], z['limpia_A'][i], dist, valido))
            res[mat].append(np.nanmedian(np.stack(por_corte), 0) if por_corte else np.full(BORDES_MM.size - 1, np.nan))
    return {k: np.stack(v) for k, v in res.items()}, nombres


def anillos_ab(img: np.ndarray, ref: np.ndarray, m: np.ndarray, px: tuple[float, float], valido: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """(a) exceso D1 y (b) amplitud de img - ref por anillo de 2 mm, en el plano axial, mismos pixeles."""
    dist = ndi.distance_transform_edt(~m, sampling=px)
    a = np.full(ANILLOS, np.nan)
    b = np.full(ANILLOS, np.nan)
    for i in range(ANILLOS):
        sel = valido & (dist > BORDES_MM[i]) & (dist <= BORDES_MM[i + 1])
        if sel.sum() >= MIN_PIX:
            a[i] = amplitud(img[sel]) - amplitud(ref[sel])
            b[i] = amplitud((img - ref)[sel])
    return a, b


def mismos_13(max_cortes: int, d: Path, semillas: tuple[int, ...] = (0, 1, 2, 3, 4), shard: tuple[int, int] | None = None) -> dict[str, np.ndarray]:
    """Peters Ti y sintetizador (a) y (b) en los 13 pacientes de prueba: mediana de cortes, de semillas y de pacientes."""
    sal = {k: [] for k in ('mod_a', 'mod_b', 'pet_a', 'pet_b')}
    archivos = sorted(glob.glob(str(d / 'a15_*_G.nii.gz')))
    if shard:
        archivos = archivos[shard[0]::shard[1]]
    for gf in archivos:
        caso = os.path.basename(gf)[4:-len('_G.nii.gz')]
        oi = nib.load(str(d / f'a15_{caso}_original.nii.gz'))
        O = np.asarray(oi.dataobj).astype(np.float32)
        M = np.asarray(nib.load(str(d / f'a15_{caso}_M.nii.gz')).dataobj) > 0
        ax = [i for i, c in enumerate(nib.aff2axcodes(oi.affine)) if c in 'SI'][0]
        z = oi.header.get_zooms()[:3]
        px = tuple(float(z[i]) for i in range(3) if i != ax)
        cnt = M.sum(axis=tuple(i for i in range(3) if i != ax))
        ks = list(np.nonzero(cnt >= 20)[0])
        ks = [ks[i] for i in np.unique(np.linspace(0, len(ks) - 1, min(max_cortes, len(ks))).round().astype(int))]
        por_semilla_a, por_semilla_b = [], []
        for s in semillas:
            S = np.asarray(nib.load(str(d / f'a15_{caso}_run04_mejor_s{s}_sintetica.nii.gz')).dataobj).astype(np.float32)
            A, B = [], []
            for k in ks:
                m = np.take(M, k, axis=ax)
                a, b = anillos_ab(np.take(S, k, axis=ax), np.take(O, k, axis=ax), m, px, cuerpo_2d(np.take(O, k, axis=ax)) & ~m)
                A.append(a); B.append(b)
            por_semilla_a.append(np.nanmedian(np.stack(A), 0)); por_semilla_b.append(np.nanmedian(np.stack(B), 0))
        sal['mod_a'].append(np.nanmedian(np.stack(por_semilla_a), 0)); sal['mod_b'].append(np.nanmedian(np.stack(por_semilla_b), 0))
        zf = _AQUI / f'outputs/obj3_pose/peters_final/a19_{caso}.npz'
        zz = np.load(zf)
        j = json.load(open(str(zf)[:-4] + '.json'))
        pp = pixel(j)
        A, B = [], []
        n = len(zz['ks'])
        for i in list(range(n))[::max(1, n // max_cortes)][:max_cortes]:
            m = zz['M'][i]
            if m.sum() < 20:
                continue
            a, b = anillos_ab(zz['Ti_A'][i], zz['limpia_A'][i], m, pp, cuerpo_2d(zz['original'][i]) & ~m)
            A.append(a); B.append(b)
        sal['pet_a'].append(np.nanmedian(np.stack(A), 0)); sal['pet_b'].append(np.nanmedian(np.stack(B), 0))
        print('  13 de prueba:', caso, flush=True)
    return {k: np.stack(v) for k, v in sal.items()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--max-cortes', type=int, default=8)
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'd3')
    ap.add_argument('--shard', default=None, help='k/n: calcula solo los casos k, k+n, ... de los 13 y guarda outputs/d3/t13_shard<k>.npz (paralelizar)')
    ap.add_argument('--merge', action='store_true', help='une los t13_shard*.npz en vez de recalcular los 13')
    ap.add_argument('--final', type=Path, default=_AQUI / 'outputs/obj3_pose/final/run04_mejor',
                    help='salidas de a15 de los 13 de prueba (original, M, G y cinco semillas de run04_mejor)')
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    if not a.merge and not list(a.final.glob('a15_*_G.nii.gz')):
        raise SystemExit(f'ABORTA: no hay salidas de a15 en {a.final}; pasa --final con la carpeta correcta')
    if a.shard:
        k, n = (int(v) for v in a.shard.split('/'))
        Ts = mismos_13(a.max_cortes, a.final, shard=(k, n))
        np.savez(a.out_dir / f't13_shard{k}.npz', **Ts)
        print('shard', k, 'de', n, 'guardado', {x: y.shape for x, y in Ts.items()})
        return
    P, nombres = peters(a.max_cortes)
    if a.merge:
        partes = [np.load(f) for f in sorted(glob.glob(str(a.out_dir / 't13_shard*.npz')))]
        T = {x: np.concatenate([q[x] for q in partes]) for x in ('mod_a', 'mod_b', 'pet_a', 'pet_b')}
    else:
        T = mismos_13(a.max_cortes, a.final)
    real = list(csv.DictReader(open(_AQUI / 'outputs/d1_tornillo/d1_por_paciente.csv')))
    mod = {r['anillo_mm']: r for r in csv.DictReader(open(_AQUI / 'outputs/d2/d2_perfil.csv'))}
    filas = []
    for i in range(ANILLOS):
        lab = f'{int(BORDES_MM[i])}-{int(BORDES_MM[i + 1])}'
        rv = np.array([float(x[lab]) for x in real if x[lab] not in ('', 'nan')])
        ti, fe = P['Ti'][:, i], P['Fe'][:, i]
        r = float(np.median(rv))
        m = float(mod[lab]['run04_mejor_med']) if lab in mod else float('nan')
        filas.append(dict(anillo_mm=lab, peters_ti=np.nanmedian(ti), peters_ti_min=np.nanmin(ti), peters_ti_max=np.nanmax(ti),
                          peters_fe=np.nanmedian(fe), real_tornillo=r, real_ic90_lo=float(np.percentile(rv, 5)),
                          real_ic90_hi=float(np.percentile(rv, 95)), modelo_run04_mejor=m,
                          ti_sobre_real=np.nanmedian(ti) / r if r > 50 else float('nan'),
                          modelo_sobre_real=m / r if r > 50 else float('nan'),
                          n_peters=int(np.isfinite(ti).sum()), n_real=int(rv.size),
                          t13_peters_exceso=np.nanmedian(T['pet_a'][:, i]), t13_modelo_exceso=np.nanmedian(T['mod_a'][:, i]),
                          t13_peters_ampdelta=np.nanmedian(T['pet_b'][:, i]), t13_modelo_ampdelta=np.nanmedian(T['mod_b'][:, i]),
                          n_t13=int(T['pet_a'].shape[0])))
    with open(a.out_dir / 'd3_peters_real_modelo.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    L = ['# D3 - Peters frente a real y modelo, por anillo (generado por `d3_peters_vs_real.py`)', '',
         f'Peters: {len(nombres)} pacientes ({", ".join(nombres[:2])}, ...); real tornillo: n = {filas[0]["n_real"]}; '
         'modelo: D2, mediana de 0101/0102. Exceso de amplitud (HU).', '',
         '| anillo (mm) | Peters Ti | Peters Fe | real tornillo | modelo | Ti/real | modelo/real |', '|---|---|---|---|---|---|---|']
    for r in filas:
        f1 = lambda v: '-' if not np.isfinite(v) else f'{v:.0f}'
        f2 = lambda v: '-' if not np.isfinite(v) else f'{v:.2f}'
        L.append(f'| {r["anillo_mm"]} | {f1(r["peters_ti"])} | {f1(r["peters_fe"])} | {f1(r["real_tornillo"])} | '
                 f'{f1(r["modelo_run04_mejor"])} | {f2(r["ti_sobre_real"])} | {f2(r["modelo_sobre_real"])} |')
    L += ['', 'Razones solo donde el real supera 50 HU. Pacientes distintos por columna; ver limites en el docstring.', '',
          f'## Mismos {filas[0]["n_t13"]} pacientes de prueba, plano axial (2.a version)', '',
          '(a) exceso = amplitud(img) - amplitud(ref); (b) amplitud(img - ref). Peters Ti y sintetizador `run04_mejor` (5 semillas); real solo (a).', '',
          '| anillo (mm) | Ti (a) | sintetizador (a) | real tornillo (a) | Ti (b) | sintetizador (b) |', '|---|---|---|---|---|---|']
    for r in filas:
        L.append(f'| {r["anillo_mm"]} | {r["t13_peters_exceso"]:.0f} | {r["t13_modelo_exceso"]:.0f} | {r["real_tornillo"]:.0f} | '
                 f'{r["t13_peters_ampdelta"]:.0f} | {r["t13_modelo_ampdelta"]:.0f} |')
    (a.out_dir / 'd3_resumen.md').write_text('\n'.join(L), encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
