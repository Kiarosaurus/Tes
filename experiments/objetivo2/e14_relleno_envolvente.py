"""E14 — cuanto cambia la envolvente osea si se anade el relleno de cavidades cerradas (#127, pto 13).

POR QUE
-------
D-O2.3 fija la envolvente como "cierre morfologico de 2 mm, relleno de cavidades cerradas en 3D". El
codigo que midio el corredor (`e9ts_corredor.py`) y el que corrio SAP (`e12_sap_control.envolvente`)
aplican **solo el cierre**. El relleno vive unicamente en `e9_corredor.py`:99, la version por umbral de
HU que #48 reemplazo.

La pregunta no es si la desviacion existe —existe— sino **cuanto cambia**. Este script la mide, y es
mucho mas barato que volver a correr E9-TS, E12 y E13:

- **no** vuelve a buscar el corredor: reutiliza el eje `(c, u)` ya guardado en `e9ts_corredor.csv`;
- **no** toca ninguna salida existente;
- por caso compara la envolvente con cierre frente a cierre + relleno.

MEDIDO ANTES EN LOS DOS PILOTOS (2026-10-03): el relleno anadio **0** voxeles en `CLINIC_0002` y **394**
(0.025 %) en `metal_0008`, y `D_TS` no se movio en ninguno de los dos. La razon esta en el comentario de
`e9_corredor.py`:95-98: el relleno corrige el **hueco trabecular de una mascara por umbral de HU**, y
las etiquetas de TotalSegmentator ya son volumenes solidos. **Dos casos no son 152**, y por eso existe
este script.

QUE ESCRIBE (`e14_relleno.csv`, una fila por caso)
--------------------------------------------------
- `vox_cerrado`, `vox_relleno`, `vox_anadidos`, `frac_anadida`, `cm3_anadidos`;
- `D_TS_cerrado_mm`, `D_TS_relleno_mm`, `dif_D_TS_mm`: `D_TS` sobre el **mismo** eje guardado, con las
  dos envolventes. Es la cifra que decide: si no se mueve, la envolvente no cambia lo que mide SAP;
- `cruza_umbral_7mm`: si el caso cambia de lado respecto del calibre del benchmark (#122);
- `Error`.

USO
---
Khipu (ver `KHIPU.md`):
    python -u e14_relleno_envolvente.py --ts-dir ~/metalsynth/data/ts_total \\
        --ct-dir ~/metalsynth/data/ts_input --refs-dir . --out e14_relleno.csv --workers 16

Local, solo sobre los pilotos que tienen mascaras en disco:
    python -u e14_relleno_envolvente.py --ts-dir ../../data/derivados/ts_piloto --ct-dir ../../data \\
        --refs-dir . --out outputs/e14_relleno_piloto.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import ndimage as ndi

_AQUI = Path(__file__).resolve().parent
_RAIZ = _AQUI.parents[1]
sys.path.insert(0, str(_RAIZ / 'src' / 'muestreador'))
sys.path.insert(0, str(_AQUI))

import sap  # noqa: E402
from e9_corredor import CIERRE_MM  # noqa: E402
from e9ts_corredor import ESTRUCTURAS, caja_recorte, etiquetar, limpia  # noqa: E402
from r1_landmarks import cargar  # noqa: E402
from ts_piloto_qc import mascara  # noqa: E402

CAMPOS = ['Caso', 'vox_cerrado', 'vox_relleno', 'vox_anadidos', 'frac_anadida', 'cm3_anadidos',
          'D_TS_cerrado_mm', 'D_TS_relleno_mm', 'dif_D_TS_mm', 'D_TS_csv_mm',
          'cruza_umbral_7mm', 'Error']


def d_ts_sobre_eje(hueso: np.ndarray, zoom: np.ndarray, origen: np.ndarray,
                   c: np.ndarray, u: np.ndarray) -> float:
    """`D_TS` del eje dado: 2 x min del EDT interior sobre el tramo ya recortado 8 mm por extremo.

    Misma convencion que `e9_corredor.evaluar_linea`, reusando `sap`, que ya la implementa.
    """
    t = sap._span_corredor(hueso, zoom, origen, c, u)
    if t is None:
        return float('nan')
    sd = sap._muestrear_campo(sap.campo_signado(hueso, zoom), zoom, origen, sap.puntos_eje(c, u, t))
    return 2.0 * float(-sd.max())


def procesar(caso: str, ruta_ct: Path, ts_dir: Path, r1: pd.Series, fila: pd.Series) -> dict:
    """Las dos envolventes de un caso y el `D_TS` de cada una sobre el eje guardado."""
    ct, zoom = cargar(ruta_ct)
    zoom = zoom.astype(float)
    forma = np.array(ct.shape)
    s1 = np.array([r1['S1_x_mm'], r1['S1_y_mm'], r1['S1_z_mm']], dtype=float)
    sl = caja_recorte(s1, zoom, forma)
    del ct

    et = [etiquetar(mascara(ts_dir / caso / 'default6mm' / f'{e}.nii.gz')) for e in ESTRUCTURAS]
    union, _ = limpia(forma, et, 0.0)
    sin_cierre = union[sl].copy()
    del union
    it = max(1, int(round(CIERRE_MM / float(zoom.min()))))
    cerrado = ndi.binary_closing(np.pad(sin_cierre, it), iterations=it)[it:-it, it:-it, it:-it]
    relleno = ndi.binary_fill_holes(cerrado)

    origen = np.array([s.start for s in sl], dtype=np.float64) * zoom
    c = np.array([fila['c_x_mm'], fila['c_y_mm'], fila['c_z_mm']], dtype=float)
    u = np.array([fila['u_x'], fila['u_y'], fila['u_z']], dtype=float)
    u = u / np.linalg.norm(u)

    d_cer = d_ts_sobre_eje(cerrado, zoom, origen, c, u)
    d_rel = d_ts_sobre_eje(relleno, zoom, origen, c, u)
    add = int(relleno.sum() - cerrado.sum())
    return {'Caso': caso,
            'vox_cerrado': int(cerrado.sum()), 'vox_relleno': int(relleno.sum()),
            'vox_anadidos': add,
            'frac_anadida': round(add / max(int(cerrado.sum()), 1), 6),
            'cm3_anadidos': round(add * float(np.prod(zoom)) / 1000.0, 3),
            'D_TS_cerrado_mm': round(d_cer, 3), 'D_TS_relleno_mm': round(d_rel, 3),
            'dif_D_TS_mm': round(d_rel - d_cer, 3),
            'D_TS_csv_mm': float(fila['D_TS_max_mm']),
            'cruza_umbral_7mm': bool((d_cer < 7.0) != (d_rel < 7.0)),
            'Error': ''}


def trabajo(args: tuple) -> dict:
    caso, ruta, ts_dir, r1, fila = args
    try:
        return procesar(caso, ruta, ts_dir, r1, fila)
    except Exception:  # noqa: BLE001
        return {'Caso': caso, 'Error': traceback.format_exc(limit=2).replace('\n', ' | ')}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--ts-dir', type=Path, required=True)
    parser.add_argument('--ct-dir', type=Path, required=True)
    parser.add_argument('--refs-dir', type=Path, default=_AQUI)
    parser.add_argument('--out', type=Path, default=_AQUI / 'e14_relleno.csv')
    parser.add_argument('--workers', type=int, default=1)
    parser.add_argument('--casos', nargs='*', default=None)
    args = parser.parse_args()

    r1 = pd.read_csv(args.refs_dir / 'r1_landmarks.csv').set_index('Caso')
    e9 = pd.read_csv(args.refs_dir / 'e9ts_corredor.csv')
    e9 = e9[(e9.modo == 'default6mm') & (e9.F_limpieza == 0.0)
            & (e9.politica_metal == 'hueso')].drop_duplicates('Caso').set_index('Caso')
    ts_dir = args.ts_dir.expanduser()
    rutas = {p.name[:-len('.nii.gz')]: p for p in args.ct_dir.expanduser().rglob('dataset*.nii.gz')}

    casos = args.casos or list(e9.index)
    pend = []
    for c in casos:
        if c not in rutas or not (ts_dir / c / 'default6mm').is_dir():
            print(f'{c}: sin CT o sin mascaras, se salta', flush=True)
            continue
        pend.append((c, rutas[c], ts_dir, r1.loc[c], e9.loc[c]))
    print(f'{len(pend)} casos a procesar con {args.workers} procesos', flush=True)

    filas = []
    if args.workers > 1:
        with ProcessPoolExecutor(max_workers=args.workers) as ex:
            for fut in as_completed([ex.submit(trabajo, a) for a in pend]):
                filas.append(fut.result())
                print(f'  {filas[-1]["Caso"]}: anade {filas[-1].get("vox_anadidos", "?")} vox, '
                      f'dif D_TS {filas[-1].get("dif_D_TS_mm", "?")} mm', flush=True)
    else:
        for a in pend:
            filas.append(trabajo(a))
            print(f'  {filas[-1]["Caso"]}: anade {filas[-1].get("vox_anadidos", "?")} vox, '
                  f'dif D_TS {filas[-1].get("dif_D_TS_mm", "?")} mm', flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, 'w', newline='', encoding='utf-8') as h:
        w = csv.DictWriter(h, fieldnames=CAMPOS)
        w.writeheader()
        for f in sorted(filas, key=lambda x: x['Caso']):
            w.writerow({k: f.get(k, '') for k in CAMPOS})

    d = pd.DataFrame(filas)
    ok = d[d.Error == ''] if 'Error' in d else d
    print()
    print(f'=== RESUMEN ({len(ok)} casos, {len(d) - len(ok)} con error) ===')
    if len(ok):
        print(f'voxeles anadidos : max {ok.vox_anadidos.max():,}  '
              f'(mediana {int(ok.vox_anadidos.median()):,}); '
              f'fraccion max {100 * ok.frac_anadida.max():.4f} %')
        print(f'|dif D_TS|       : max {ok.dif_D_TS_mm.abs().max():.3f} mm  '
              f'(mediana {ok.dif_D_TS_mm.abs().median():.3f})')
        print(f'casos con |dif D_TS| > 0.05 mm : {int((ok.dif_D_TS_mm.abs() > 0.05).sum())}')
        print(f'casos que cruzan el umbral de 7 mm : {int(ok.cruza_umbral_7mm.sum())}')
    print(f'escrito {args.out}')


if __name__ == '__main__':
    main()
