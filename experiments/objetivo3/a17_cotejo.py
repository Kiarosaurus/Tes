"""A17 - cotejo de checkpoint contra los tornillos reales de `metal_0039` (01-decisiones.md 2026-10-07 (2), 2026-10-08 (2)).

QUE HACE
--------
1. **Referencia real.** Lee `metal_0039` (validacion), toma sus 2 componentes metalicos (> 2500 HU,
   conectividad 6, >= 500 mm3): los 2 tornillos aislados que la autora confirmo en cortes
   (`experiments/exploration-3d/tornillos_revision_autora.csv`). Para cada uno calcula el perfil 2D
   (elevacion de mediana y p95 sobre el anillo de 12-15 mm, cascaras de 0.5 mm) y el histograma dentro
   de `M`, con `common.cotejo`, la misma funcion que usa `a15` para lo sintetico. El metal del otro
   componente se excluye de las cascaras.
2. **Envolvente real:** minimo a maximo de los 2 componentes, por cascara y por curva.
3. **Sintetico:** lee los `a15_<caso>_cotejo.csv` de `--dir-sintetico`. Agregacion: semilla -> paciente
   (mediana) -> checkpoint (mediana entre pacientes). Reporta tambien el rango entre semillas.
4. **Regla (fijada antes de mirar):** gana el checkpoint con mas cascaras dentro de la envolvente, sumando
   las dos curvas. Desempate: menor |p50 - mediana real| + |p95 - mediana real| dentro de `M` (sobre
   voxeles > 2500 HU). Empate que persista: lo decide la autora. Solo cuentan las cascaras con valor en
   los dos lados; el numero de cascaras comparables se reporta.

ALCANCE: 1 paciente, 2 tornillos. Descarta checkpoints cuyo artefacto cae fuera de lo observado; no prueba
que el elegido lo reproduzca. **Este script no elige**: escribe el resultado de la regla y la autora decide.

USO
---
    python experiments/objetivo3/a17_cotejo.py --dir-sintetico experiments/objetivo3/outputs/a15_cotejo
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src'))
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo1'))

from common.cotejo import METAL_HU, agrega, bordes, histograma_m, perfil_corte  # noqa: E402

CASO_REF = 'dataset7_CLINIC_metal_0039_data'
MIN_MM3 = 500.0


def referencia_real(data: list[Path], particion: Path) -> tuple[list[np.ndarray], list[dict]]:
    """Perfil (n_cascaras, 2) e histograma de cada tornillo real de `metal_0039`."""
    import nibabel as nib
    from scipy import ndimage as ndi
    from p1_decodificador_sd15 import leer_particion, rutas
    from e6b_vae_sd15 import eje_axial

    filas = leer_particion(particion)
    fila = [f for f in filas if f['Caso'] == CASO_REF]
    if not fila or fila[0]['particion'] != 'val':
        raise SystemExit('CONTROL: %s no esta en validacion' % CASO_REF)
    ubic = rutas(fila, data)
    img = nib.load(ubic[CASO_REF])
    arr = img.get_fdata(dtype=np.float32)
    eje = eje_axial(img)
    zooms = np.array(img.header.get_zooms()[:3], dtype=float)
    plano = [i for i in range(3) if i != eje]
    vol = np.moveaxis(arr, eje, 0)
    esp2d = (zooms[plano[0]], zooms[plano[1]])
    metal = vol > METAL_HU
    lab, n = ndi.label(metal)                     # conectividad 6, igual que laminas.py
    vox_mm3 = float(np.prod(zooms))
    tam = ndi.sum(metal, lab, index=np.arange(1, n + 1)) * vox_mm3
    comps = [i + 1 for i in np.argsort(-tam) if tam[i] >= MIN_MM3]
    print('%s: %d componentes > %.0f HU; >= %.0f mm3: %s'
          % (CASO_REF, n, METAL_HU, MIN_MM3, [round(float(tam[c - 1]), 1) for c in comps]))
    if len(comps) != 2:
        raise SystemExit('CONTROL: se esperaban 2 tornillos en %s y hay %d' % (CASO_REF, len(comps)))
    perfiles, hists = [], []
    for c in comps:
        m3 = lab == c
        otro = metal & ~m3
        ks = [k for k in range(vol.shape[0]) if m3[k].any()]
        prf = agrega([perfil_corte(vol[k], m3[k], esp2d, excluir=otro[k]) for k in ks])
        h = histograma_m(vol[m3])
        h.update(componente=int(c), vol_mm3=round(float(tam[c - 1]), 1), cortes=len(ks))
        perfiles.append(prf)
        hists.append(h)
        print('  componente %d: %.0f mm3, %d cortes, M p50 %.0f p95 %.0f'
              % (c, tam[c - 1], len(ks), h['hu_p50'], h['hu_p95']))
    return perfiles, hists


def lee_sintetico(directorio: Path) -> dict:
    """{etiqueta: {caso: {semilla: (perfil, hist)}}} desde los `a15_*_cotejo.csv`."""
    datos: dict = defaultdict(lambda: defaultdict(dict))
    n_casc = len(bordes()) - 1
    rutas_csv = sorted(directorio.glob('a15_*_cotejo.csv'))
    if not rutas_csv:
        raise SystemExit('no hay a15_*_cotejo.csv en %s' % directorio)
    for ruta in rutas_csv:
        with open(ruta, newline='', encoding='utf-8') as fh:
            filas = list(csv.DictReader(fh))
        grupos = defaultdict(list)
        for f in filas:
            grupos[(f['etiqueta'], f['caso'], int(f['semilla']))].append(f)
        for (et, caso, sem), fs in grupos.items():
            fs.sort(key=lambda f: float(f['r_lo_mm']))
            if len(fs) != n_casc:
                raise SystemExit('%s: %d cascaras, se esperaban %d' % (ruta.name, len(fs), n_casc))
            prf = np.array([[float(f['elev_p50']), float(f['elev_p95'])] for f in fs])
            h = {q: float(fs[0]['M_%s' % q]) for q in ('p50', 'p75', 'p95', 'frac_sobre_2500')}
            datos[et][caso][sem] = (prf, h)
    return datos


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir-sintetico', type=Path, default=aqui / 'outputs' / 'a15_cotejo')
    ap.add_argument('--data', type=Path, nargs='+', default=[_RAIZ / 'data'])
    ap.add_argument('--particion', type=Path, default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a17')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    reales, hists = referencia_real(list(args.data), args.particion)
    R = np.stack(reales)                                   # (2, n_cascaras, 2)
    lo, hi = np.min(R, axis=0), np.max(R, axis=0)          # NaN si falta en algun componente
    med_p50 = float(np.median([h['hu_p50'] for h in hists]))
    med_p95 = float(np.median([h['hu_p95'] for h in hists]))
    b = bordes()

    datos = lee_sintetico(args.dir_sintetico)
    filas, tabla = [], []
    for et in sorted(datos):
        por_caso = []
        for caso in sorted(datos[et]):
            sems = datos[et][caso]
            por_caso.append((agrega([p for p, _ in sems.values()]),
                             {q: float(np.median([h[q] for _, h in sems.values()]))
                              for q in ('p50', 'p95', 'frac_sobre_2500')},
                             len(sems)))
        S = agrega([p for p, _, _ in por_caso])
        hs = {q: float(np.median([h[q] for _, h, _ in por_caso])) for q in ('p50', 'p95', 'frac_sobre_2500')}
        comparable = ~np.isnan(S) & ~np.isnan(lo)
        dentro = comparable & (S >= lo) & (S <= hi)
        dist = abs(hs['p50'] - med_p50) + abs(hs['p95'] - med_p95)
        # rango entre semillas (por paciente, la mayor amplitud) como lectura de ruido
        amp = []
        for caso in datos[et]:
            P = np.stack([p for p, _ in datos[et][caso].values()])
            with np.errstate(all='ignore'):
                amp.append(np.nanmax(np.nanmax(P, 0) - np.nanmin(P, 0)))
        tabla.append({'etiqueta': et, 'pacientes': len(por_caso),
                      'semillas': '/'.join(str(n) for _, _, n in por_caso),
                      'dentro_p50': int(dentro[:, 0].sum()), 'dentro_p95': int(dentro[:, 1].sum()),
                      'dentro_total': int(dentro.sum()), 'comparables': int(comparable.sum()),
                      'M_p50': round(hs['p50'], 1), 'M_p95': round(hs['p95'], 1),
                      'M_frac_sobre_2500': round(hs['frac_sobre_2500'], 4),
                      'dist_hist': round(dist, 1), 'max_rango_semillas_HU': round(float(np.nanmax(amp)), 1)})
        for i in range(len(b) - 1):
            filas.append({'etiqueta': et, 'r_lo_mm': b[i], 'r_hi_mm': b[i + 1],
                          'sint_p50': S[i, 0], 'real_lo_p50': lo[i, 0], 'real_hi_p50': hi[i, 0],
                          'sint_p95': S[i, 1], 'real_lo_p95': lo[i, 1], 'real_hi_p95': hi[i, 1]})

    tabla.sort(key=lambda t: (-t['dentro_total'], t['dist_hist']))
    empate = len(tabla) > 1 and tabla[0]['dentro_total'] == tabla[1]['dentro_total'] \
        and tabla[0]['dist_hist'] == tabla[1]['dist_hist']

    with open(args.out_dir / 'a17_perfiles.csv', 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows({k: (round(v, 2) if isinstance(v, float) else v) for k, v in f.items()} for f in filas)
    L = ['# A17 — cotejo de checkpoint contra los tornillos reales de `metal_0039`', '',
         'Generado por `a17_cotejo.py`. Referencia: 2 tornillos aislados de `metal_0039` (validacion; '
         '01-decisiones.md 2026-10-08 (2)). Regla: 01-decisiones.md 2026-10-07 (2). **No elige: informa.**', '',
         '## Referencia real', '', '| componente | mm3 | cortes | M p50 | M p75 | M p95 |', '|---|---|---|---|---|---|']
    L += ['| %d | %.0f | %d | %.0f | %.0f | %.0f |' % (h['componente'], h['vol_mm3'], h['cortes'],
                                                    h['hu_p50'], h['hu_p75'], h['hu_p95']) for h in hists]
    L += ['', '## Resultado de la regla', '',
          '| checkpoint | pacientes | semillas | dentro p50 | dentro p95 | dentro total | comparables | '
          'M p50 | M p95 | dist. hist. | rango max. entre semillas (HU) |',
          '|---|---|---|---|---|---|---|---|---|---|---|']
    L += ['| %(etiqueta)s | %(pacientes)d | %(semillas)s | %(dentro_p50)d | %(dentro_p95)d | %(dentro_total)d | '
          '%(comparables)d | %(M_p50).0f | %(M_p95).0f | %(dist_hist).0f | %(max_rango_semillas_HU).0f |' % t
          for t in tabla]
    if tabla[0]['dentro_total'] == 0:
        L += ['', '**AVISO: ningun checkpoint tiene cascaras dentro de la envolvente real.** La regla ordena '
              'solo por el histograma; el cotejo no respalda a ninguno y la decision es de la autora.']
    L += ['', ('**Empate persistente: lo decide la autora.**' if empate else
               '**Gana por la regla: `%s`.** La eleccion la confirma la autora.' % tabla[0]['etiqueta']),
          '', 'Con 1 paciente de referencia el cotejo descarta, no prueba. Cascaras comparables = con valor '
          'en lo real y en lo sintetico (con 0.5 mm y pixel de 0.7-1 mm, algunas cascaras quedan vacias). '
          'Perfiles por cascara: `a17_perfiles.csv`.']
    (args.out_dir / 'a17_cotejo.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
    print('\n'.join(L))


if __name__ == '__main__':
    main()
