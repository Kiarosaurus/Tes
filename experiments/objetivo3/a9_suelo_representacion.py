"""A9 - cuanto recorta el suelo de -1000 HU de la representacion, medido sin modelo (#141).

POR QUE EXISTE
--------------
#141 nacio de UN componente de UN paciente: el 23.4 % de los voxeles de `G` caian por debajo de
-1000 HU y la representacion los devolvia todos al suelo. Con una sola serie no se puede decidir si
eso es una nota al pie o una amenaza al criterio de exito del Objetivo 3. Este script mide la
prevalencia sobre **todos** los parches cacheados de entrenamiento y validacion, y mide ademas el
efecto sobre la magnitud que de verdad importa.

NO USA EL MODELO. La medicion es de **ida y vuelta por la representacion**: HU -> codificacion
multiventana -> HU, con la `regla` congelada del Objetivo 1. Lo que sale de aqui es el techo que la
representacion impone, aislado del renderizador, y no depende de `run01`, de `run02` ni de ningun
`ckpt`.

POR QUE LA BANDA SE SEPARA DE LA MASCARA
----------------------------------------
Dentro de `M` el suelo casi no importa: el metal es brillante y el recorte afecta a pocos voxeles.
En la banda `G \\ M` es donde vive el *undershoot* de la inanicion de fotones, que es la parte del
artefacto que la tesis debe generar. Mezclar las dos regiones diluye el efecto justo donde se mide.

POR QUE SOLO ENTRENAMIENTO Y VALIDACION
---------------------------------------
El cache contiene tambien pacientes de **test**. Usarlos para una decision de diseno meteria
estadisticos del test en el diseno, que es lo que la *Strict Isolation Rule* (`main.tex`:111)
prohibe. Se filtra por `p1_particion.csv` igual que `datos.ParchesMetal`.

LAS DOS MEDICIONES
------------------
1. **Prevalencia del recorte.** Por paciente: fraccion de voxeles de `G`, de `M` y de `G \\ M` con
   HU < -1000; percentil 1 de HU en la banda; y el **minimo de HU del volumen de origen**, porque la
   cohorte es heterogenea en hasta donde deja bajar los valores (se vieron -2048 en un parche y
   -7159 en otro) y el recorte atribuible a la representacion depende de eso.

2. **Compresion del vano de streak.** `peters2025hybrid` define *streak amplitude* como
   **la diferencia entre el promedio del 5 % superior y el promedio del 5 % inferior** de la
   desviacion respecto a la verdad de terreno, dentro de ROIs perpendiculares al streak
   (`docs/literatura/peters2025hybrid.md`:56, :173, :174). Es decir, **el vano entre el lobulo claro
   y el lobulo oscuro**: exactamente lo que un suelo recorta por abajo.

   **SUSTITUCION DECLARADA, y hay que leerla antes de citar cualquier cifra de aqui.** La definicion
   de Peters se calcula sobre la **desviacion respecto a la verdad de terreno**, y para un paciente
   real con metal esa verdad no existe (es justo lo que E-A2 resuelve usando casos de test sin
   metal). Ademas, la inversion de las metricas de Peters para sintesis sigue siendo un `\\GAPDEC`
   abierto (#16, #17). Asi que aqui se mide la **forma** del estadistico, no la metrica:

       S = promedio(5 % superior de HU) - promedio(5 % inferior de HU),  dentro de `G \\ M`

   y se compara `S` del parche real contra `S` del mismo parche tras la ida y vuelta. El cociente
   `S_ida_vuelta / S_real` es **cuanto del vano sobrevive a la representacion**. NO es streak
   amplitude y no debe presentarse como tal: es un proxy de la misma forma, calculado sobre HU en
   lugar de sobre desviacion, y con la banda `G \\ M` en lugar de ROIs perpendiculares trazadas a
   mano.

SALIDAS
-------
- `a9_suelo_por_parche.csv`   una fila por parche
- `a9_suelo_por_paciente.csv` una fila por paciente, que es la unidad de la particion
- resumen por consola, con la mediana y el rango intercuartil entre pacientes

USO
---
    python a9_suelo_representacion.py
    python a9_suelo_representacion.py --particiones train val --max-parches 500
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'src'))

from common.ventanas import canales_diseno_a, codifica_bloque, decodifica_bloque  # noqa: E402

PATRON = re.compile(r'^(?P<serie>.+)_k(?P<k>\d{4})\.npz$')
SUELO = -1000.0        # `asinh_canal(-1000.0, 20000.0)`, e6c_techo_lw.py:81; su `ida` aplica np.clip
COLA = 0.05            # el 5 % de Peters et al.


def caso_de(serie: str) -> str:
    return re.sub(r'_c\d{3}$', '', serie)


def lee_particion(ruta: Path, particiones: tuple[str, ...]) -> set[str]:
    with open(ruta, newline='', encoding='utf-8') as fh:
        return {f['Caso'] for f in csv.DictReader(fh) if f['particion'] in particiones}


def vano(x: np.ndarray) -> float:
    """Forma del estadistico de streak de Peters et al.: promedio del 5 % alto menos el del 5 % bajo.

    Con menos de 20 voxeles el 5 % no llega a un voxel y el estadistico no esta definido; se
    devuelve NaN en vez de un numero que no significa nada.
    """
    n = x.size
    if n < 20:
        return float('nan')
    k = max(1, int(round(n * COLA)))
    o = np.sort(x)
    return float(o[-k:].mean() - o[:k].mean())


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--particiones', nargs='+', default=['train', 'val'],
                    help='NUNCA test: seria meter estadisticos del test en una decision de diseno')
    ap.add_argument('--max-parches', type=int, default=0, help='0 = todos')
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a9')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    if 'test' in [p.lower() for p in args.particiones]:
        raise SystemExit('CONTROL: se pidio la particion de test. Abortado por la Strict Isolation '
                         'Rule (main.tex:111): no se miden estadisticos del test para decidir diseno.')

    permitidos = lee_particion(args.particion, tuple(args.particiones))
    canales = canales_diseno_a()
    print(f'particiones {args.particiones}: {len(permitidos)} pacientes permitidos')
    print(f'suelo de la representacion: {SUELO:.0f} HU | cola de Peters: {100*COLA:.0f} %')

    archivos = sorted(args.cache.glob('*.npz'))
    filas = []
    saltados = 0
    for f in archivos:
        m = PATRON.match(f.name)
        if m is None:
            continue
        serie = m.group('serie')
        caso = caso_de(serie)
        if caso not in permitidos:
            saltados += 1
            continue
        with np.load(f) as z:
            hu = z['hu'].astype(np.float32)
            g = z['g'].astype(bool)
            metal = z['metal'].astype(bool)
        if not g.any():
            continue
        banda = g & ~metal
        vuelta = decodifica_bloque(codifica_bloque(hu, canales))

        hu_g, hu_m, hu_b = hu[g], hu[metal], hu[banda]
        fila = {
            'caso': caso, 'serie': serie, 'corte': int(m.group('k')),
            'n_G': int(g.sum()), 'n_M': int(metal.sum()), 'n_banda': int(banda.sum()),
            # 1. prevalencia del recorte
            'frac_G_bajo_suelo': round(float((hu_g < SUELO).mean()), 6),
            'frac_M_bajo_suelo': round(float((hu_m < SUELO).mean()), 6) if metal.any() else '',
            'frac_banda_bajo_suelo': round(float((hu_b < SUELO).mean()), 6) if banda.any() else '',
            'p1_banda_real': round(float(np.percentile(hu_b, 1)), 1) if banda.any() else '',
            'min_G_real': round(float(hu_g.min()), 1),
            'min_parche_real': round(float(hu.min()), 1),
            # 2. compresion del vano, forma de Peters sobre HU en la banda
            'vano_real': round(vano(hu_b), 1) if banda.any() else '',
            'vano_ida_vuelta': round(vano(vuelta[banda]), 1) if banda.any() else '',
        }
        vr, vv = fila['vano_real'], fila['vano_ida_vuelta']
        fila['vano_sobrevive'] = (round(vv / vr, 4)
                                  if isinstance(vr, float) and isinstance(vv, float)
                                  and np.isfinite(vr) and np.isfinite(vv) and vr > 0 else '')
        filas.append(fila)
        if args.max_parches and len(filas) >= args.max_parches:
            break
        if len(filas) % 2000 == 0:
            print(f'  {len(filas)} parches...', flush=True)

    if not filas:
        raise SystemExit('ningun parche de las particiones pedidas')
    print(f'parches medidos: {len(filas)} | saltados por particion: {saltados}')

    ruta_p = args.out_dir / 'a9_suelo_por_parche.csv'
    with open(ruta_p, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print(f'por parche: {ruta_p}')

    # --- agregado por PACIENTE, que es la unidad de la particion
    por_caso: dict[str, list[dict]] = {}
    for r in filas:
        por_caso.setdefault(r['caso'], []).append(r)

    def num(rs, col):
        return np.array([r[col] for r in rs if isinstance(r[col], float) and np.isfinite(r[col])])

    pac = []
    for caso, rs in sorted(por_caso.items()):
        nG = sum(r['n_G'] for r in rs)
        nB = sum(r['n_banda'] for r in rs)
        # la fraccion por paciente se pondera por voxeles, no se promedia por parche: un parche de
        # 138 voxeles de G no puede pesar igual que uno de 48 000.
        vg = sum(r['frac_G_bajo_suelo'] * r['n_G'] for r in rs)
        vb = sum(r['frac_banda_bajo_suelo'] * r['n_banda']
                 for r in rs if isinstance(r['frac_banda_bajo_suelo'], float))
        sob = num(rs, 'vano_sobrevive')
        pac.append({
            'caso': caso, 'parches': len(rs), 'n_G': nG, 'n_banda': nB,
            'frac_G_bajo_suelo': round(vg / nG, 6) if nG else '',
            'frac_banda_bajo_suelo': round(vb / nB, 6) if nB else '',
            'min_parche_real': round(min(r['min_parche_real'] for r in rs), 1),
            'vano_sobrevive_p50': round(float(np.median(sob)), 4) if sob.size else '',
            'vano_sobrevive_p05': round(float(np.percentile(sob, 5)), 4) if sob.size else '',
        })
    ruta_c = args.out_dir / 'a9_suelo_por_paciente.csv'
    with open(ruta_c, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(pac[0].keys()))
        w.writeheader()
        w.writerows(pac)
    print(f'por paciente: {ruta_c}')

    def resume(col, etiqueta, pct=False, dec=1):
        v = np.array([p[col] for p in pac if isinstance(p[col], float)])
        if not v.size:
            print(f'  {etiqueta}: sin datos')
            return
        f = 100.0 if pct else 1.0
        q = np.percentile(v * f, [0, 25, 50, 75, 100])
        u = ' %' if pct else ''
        print(f'  {etiqueta}: p50 {q[2]:.{dec}f}{u} | IQR {q[1]:.{dec}f} a {q[3]:.{dec}f} | '
              f'rango {q[0]:.{dec}f} a {q[4]:.{dec}f} | n = {v.size} pacientes')

    print(f'\n--- RESUMEN entre {len(pac)} pacientes (unidad de la particion) ---')
    resume('frac_G_bajo_suelo', 'voxeles de G bajo el suelo', pct=True)
    resume('frac_banda_bajo_suelo', 'voxeles de la BANDA bajo el suelo', pct=True)
    resume('min_parche_real', 'minimo de HU del parche', dec=0)
    resume('vano_sobrevive_p50', 'fraccion del vano que SOBREVIVE (mediana del paciente)', dec=3)
    resume('vano_sobrevive_p05', 'fraccion del vano que sobrevive (p5 del paciente)', dec=3)
    afectados = sum(1 for p in pac
                    if isinstance(p['frac_banda_bajo_suelo'], float)
                    and p['frac_banda_bajo_suelo'] > 0)
    print(f'  pacientes con ALGUN voxel de banda bajo el suelo: {afectados} de {len(pac)}')
    print('\nLas cifras del vano son un PROXY de la forma de streak amplitude, no la metrica. '
          'Ver la sustitucion declarada en el encabezado antes de citarlas.')


if __name__ == '__main__':
    main()
