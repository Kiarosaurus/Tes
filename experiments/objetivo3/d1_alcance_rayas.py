"""D1 (#176) - hasta donde llega el artefacto metalico REAL alrededor del implante, en el plano axial.

POR QUE
-------
El sintetizador solo puede generar dentro de `G = M U B_delta`, con `B_delta` = 12 mm; fuera, copia el original. Si
el artefacto real llega mas lejos, la banda es un techo para el realismo (hipotesis H2 de #176). `a12` midio el
perfil real solo hasta 13.5 mm y con la mediana del anillo, que no ve rayas (son direccionales y ocupan las colas).

QUE MIDE
--------
Para cada componente metalico real (> 2500 HU, >= 500 mm3, conectividad 6) de los pacientes de ENTRENAMIENTO (los 39
de `a5_manifiesto_train_run04.csv`) y VALIDACION (`a5_manifiesto_val.csv`). Prueba no se toca.

1. Cortes axiales donde el componente aparece y ningun otro metal (> 2500 HU) esta en el corte (sin contaminacion).
2. **Corte de referencia** del mismo paciente, a 15-40 mm, sin metal y con area de cuerpo dentro de +-20 %: aproxima
   la anatomia sin artefacto. No es la verdad sin metal (no existe en estos pacientes): es una aproximacion
   declarada; la anatomia cambia entre cortes.
3. Anillos de 2 mm (0-60 mm) por distancia euclidea en el plano al componente, sobre los pixeles de cuerpo
   (> -400 HU, componente mayor, huecos rellenos) de los dos cortes. Estadistico de Peters (2.5, p. 5) por anillo:
   promedio del 5 % superior menos el del 5 % inferior de HU. **Exceso** = amplitud(corte con metal) -
   amplitud(referencia), con los mismos pixeles.
4. **Nulo:** lo mismo entre la referencia y otro corte sin metal a la misma distancia, del otro lado (cuanto cambia
   la amplitud solo por la anatomia).
5. Agregacion por medianas: cortes -> componente -> paciente; IC90 por remuestreo de pacientes (2000 remuestreos).

Salida: `outputs/d1/d1_exceso_por_anillo.csv`, `d1_por_paciente.csv`, `d1_resumen.md`.

USO
---
    python experiments/objetivo3/d1_alcance_rayas.py [--max-cortes 8] [--max-casos N]
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import nibabel as nib
import numpy as np
from scipy import ndimage as ndi

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]

METAL_HU = 2500.0
CUERPO_HU = -400.0
VOL_MIN_MM3 = 500.0
BORDES_MM = np.arange(0.0, 60.01, 2.0)
DZ_MM = (15.0, 40.0)
MIN_PIX = 50
SEMILLA = 20261013


def amplitud(x: np.ndarray) -> float:
    """Estadistico de Peters: promedio del 5 % superior menos el del 5 % inferior."""
    x = np.sort(x.astype(np.float64))
    m = max(1, int(round(0.05 * x.size)))
    return float(x[-m:].mean() - x[:m].mean())


def cuerpo_2d(sl: np.ndarray) -> np.ndarray:
    """Cuerpo en un corte: > -400 HU, componente mayor, huecos rellenos (como `a4.mascara_cuerpo`, en 2D)."""
    c = sl > CUERPO_HU
    lab, n = ndi.label(c)
    if n == 0:
        return c
    tam = np.bincount(lab.ravel())
    tam[0] = 0
    return ndi.binary_fill_holes(lab == int(tam.argmax()))


def perfil(img: np.ndarray, ref: np.ndarray, dist: np.ndarray, valido: np.ndarray) -> np.ndarray:
    """Exceso de amplitud por anillo (img - ref) sobre los mismos pixeles; NaN si el anillo tiene pocos pixeles."""
    out = np.full(BORDES_MM.size - 1, np.nan)
    for i, (lo, hi) in enumerate(zip(BORDES_MM[:-1], BORDES_MM[1:])):
        sel = valido & (dist > lo) & (dist <= hi)
        if sel.sum() >= MIN_PIX:
            out[i] = amplitud(img[sel]) - amplitud(ref[sel])
    return out


def casos() -> list[tuple[str, str, Path]]:
    """(caso, particion, ruta) de entrenamiento de run04 y de validacion, con la ruta de `grupos.csv`."""
    rutas = {}
    with open(_RAIZ / 'experiments' / 'exploration-3d' / 'grupos.csv', encoding='utf-8-sig') as fh:
        for f in csv.DictReader(fh):
            rutas[f['Caso']] = _RAIZ / f['Archivo']
    out = []
    for nombre, part in (('a5_manifiesto_train_run04.csv', 'train'), ('a5_manifiesto_val.csv', 'val')):
        with open(_AQUI / nombre, encoding='utf-8') as fh:
            vistos = sorted({f['Caso'] for f in csv.DictReader(fh)})
        out += [(c, part, rutas[c]) for c in vistos]
    return out


def analiza(ruta: Path, max_cortes: int) -> tuple[list[np.ndarray], list[np.ndarray], int]:
    """Perfiles de exceso (uno por componente) y nulos, de un volumen."""
    img = nib.load(str(ruta))
    vol = np.asarray(img.dataobj, dtype=np.float32)
    sx, sy, sz = (float(z) for z in img.header.get_zooms()[:3])
    metal = vol > METAL_HU
    lab, n = ndi.label(metal)
    if n == 0:
        return [], [], 0
    vox_mm3 = sx * sy * sz
    tam = np.bincount(lab.ravel())
    metal_por_corte = metal.reshape(-1, metal.shape[2]).sum(0)
    cuerpo_area = {}

    def area(k: int) -> np.ndarray:
        if k not in cuerpo_area:
            cuerpo_area[k] = cuerpo_2d(vol[:, :, k])
        return cuerpo_area[k]

    perf_comp, nulos, ncomp = [], [], 0
    for c in range(1, n + 1):
        if tam[c] * vox_mm3 < VOL_MIN_MM3:
            continue
        mc = lab == c
        por_corte = mc.reshape(-1, mc.shape[2]).sum(0)
        ks = [k for k in np.nonzero(por_corte >= 20)[0] if metal_por_corte[k] == por_corte[k]]
        if not ks:
            continue
        ks = [ks[i] for i in np.unique(np.linspace(0, len(ks) - 1, min(max_cortes, len(ks))).round().astype(int))]
        perf_k = []
        for k in ks:
            b = area(k)
            cand = []
            for sgn in (-1, 1):
                for d in range(int(np.ceil(DZ_MM[0] / sz)), int(DZ_MM[1] / sz) + 1):
                    kk = k + sgn * d
                    if 0 <= kk < vol.shape[2] and metal_por_corte[kk] < 5:
                        bb = area(kk)
                        if abs(int(bb.sum()) - int(b.sum())) <= 0.2 * b.sum():
                            cand.append((d, sgn, kk))
                            break
            if not cand:
                continue
            cand.sort()
            kr = cand[0][2]
            dist = ndi.distance_transform_edt(~mc[:, :, k], sampling=(sx, sy))
            valido = b & area(kr) & ~metal[:, :, k] & ~metal[:, :, kr]
            perf_k.append(perfil(vol[:, :, k], vol[:, :, kr], dist, valido))
            if len(cand) == 2:                                   # nulo: referencia frente al otro lado
                k2 = cand[1][2]
                v2 = valido & area(k2) & ~metal[:, :, k2]
                nulos.append(perfil(vol[:, :, k2], vol[:, :, kr], dist, v2))
        if perf_k:
            perf_comp.append(np.nanmedian(np.stack(perf_k), 0))
            ncomp += 1
    return perf_comp, nulos, ncomp


def ic_pacientes(m: np.ndarray, rng: np.random.Generator, B: int = 2000) -> tuple[np.ndarray, np.ndarray]:
    """IC90 de la mediana entre pacientes, por remuestreo de filas (pacientes)."""
    idx = rng.integers(0, m.shape[0], size=(B, m.shape[0]))
    with np.errstate(all='ignore'):
        meds = np.nanmedian(m[idx], axis=1)
    return np.nanpercentile(meds, 5, axis=0), np.nanpercentile(meds, 95, axis=0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--max-cortes', type=int, default=8)
    ap.add_argument('--max-casos', type=int, default=None)
    ap.add_argument('--out-dir', type=Path, default=_AQUI / 'outputs' / 'd1')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    lista = casos()[:args.max_casos]
    por_pac, nul_pac, filas = [], [], []
    for i, (caso, part, ruta) in enumerate(lista, 1):
        perf, nul, ncomp = analiza(ruta, args.max_cortes)
        print('[%d/%d] %s (%s): %d componentes, %d nulos' % (i, len(lista), caso, part, ncomp, len(nul)), flush=True)
        if perf:
            p = np.nanmedian(np.stack(perf), 0)
            por_pac.append(p)
            filas.append([caso, part, ncomp] + ['%.1f' % v for v in p])
        if nul:
            nul_pac.append(np.nanmedian(np.stack(nul), 0))
    rng = np.random.default_rng(SEMILLA)
    P, N = np.stack(por_pac), np.stack(nul_pac)
    med, (lo, hi) = np.nanmedian(P, 0), ic_pacientes(P, rng)
    nmed, (nlo, nhi) = np.nanmedian(N, 0), ic_pacientes(N, rng)
    centros = ['%g-%g' % (a, b) for a, b in zip(BORDES_MM[:-1], BORDES_MM[1:])]
    with open(args.out_dir / 'd1_por_paciente.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['caso', 'particion', 'componentes'] + centros)
        w.writerows(filas)
    with open(args.out_dir / 'd1_exceso_por_anillo.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(['anillo_mm', 'n_pacientes', 'exceso_med', 'ic90_lo', 'ic90_hi', 'nulo_med', 'nulo_ic90_lo',
                    'nulo_ic90_hi'])
        for j, c in enumerate(centros):
            w.writerow([c, int(np.isfinite(P[:, j]).sum()), '%.1f' % med[j], '%.1f' % lo[j], '%.1f' % hi[j],
                        '%.1f' % nmed[j], '%.1f' % nlo[j], '%.1f' % nhi[j]])
    supera = [j for j in range(len(centros)) if np.isfinite(lo[j]) and lo[j] > nhi[j]]
    ultimo = BORDES_MM[max(supera) + 1] if supera else 0.0
    L = ['# D1 — alcance del artefacto real por anillo (#176)', '',
         'Generado por `d1_alcance_rayas.py`. %d pacientes con perfil (%d de nulo); entrenamiento de run04 y '
         'validacion. Exceso = amplitud de Peters (5 %% superior - 5 %% inferior) en el corte con metal menos en un '
         'corte de referencia sin metal a 15-40 mm. Nulo = lo mismo entre dos cortes sin metal.' % (P.shape[0], N.shape[0]),
         '', '| anillo (mm) | n | exceso mediano | IC90 | nulo mediano | IC90 nulo |', '|---|---|---|---|---|---|']
    for j, c in enumerate(centros):
        L.append('| %s | %d | %.0f | [%.0f, %.0f] | %.0f | [%.0f, %.0f] |' % (
            c, int(np.isfinite(P[:, j]).sum()), med[j], lo[j], hi[j], nmed[j], nlo[j], nhi[j]))
    L += ['', '**Anillo mas lejano cuyo IC90 inferior supera el IC90 superior del nulo: hasta %g mm** '
          '(referencia: `B_delta` = 12 mm).' % ultimo, '',
          'Limites: la referencia es otro corte (la anatomia cambia); solo cortes sin otro metal; la amplitud por '
          'anillo mezcla rayas claras y oscuras con la variacion anatomica del anillo.']
    (args.out_dir / 'd1_resumen.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L[-4:]))


if __name__ == '__main__':
    sys.exit(main())
