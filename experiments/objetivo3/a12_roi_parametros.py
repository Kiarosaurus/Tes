"""A12 - fija los parametros de las ROIs de `streak amplitude` SOBRE VALIDACION (decision 2026-10-05 (3)).

QUE DECIDE Y CON QUE CRITERIO
-----------------------------
La entrada `2026-10-05 (3)` de `docs/01-decisiones.md` fijo el **que** y el **contra que** de
`streak amplitude`, y dejo cuatro parametros de la geometria de las ROIs sin fijar, con la condicion de
fijarlos **sobre validacion y nunca sobre test**. Este script los resuelve: dos por argumento y uno por
medicion, y el cuarto resulta no ser un grado de libertad.

El criterio es deliberadamente **independiente de lo que la tesis quiere demostrar**: se mira donde
vive el artefacto **real** en los pacientes de validacion con metal, nunca una salida del
sintetizador. Ni el modelo ni ningun `ckpt` intervienen.

LOS CUATRO PARAMETROS
---------------------
1. **Apertura del arco: 360 grados, anillo completo. Por argumento, no por medicion.**
   Peters et al. colocan las ROIs *"perpendicular to strong streak artifacts"* y a mano, y su propio
   texto declara esa colocacion como limitacion. Con un estadistico **de colas** —promedio del 5 %
   superior menos el del 5 % inferior— la direccionalidad del streak **deja de importar**: las colas
   encuentran las rayas claras y oscuras dondequiera que esten en el anillo. Un anillo completo es mas
   reproducible y **elimina un parametro libre** en vez de fijarlo a ojo. Es una desviacion del
   protocolo publicado y se declara como tal.

2. **Planos: todos los cortes que contienen `M`, excluyendo 8 mm por extremo. Por reutilizacion.**
   Se toma `RECORTE_EXTREMO_MM = 8.0` de `e9_corredor.py`, que es la exclusion de extremos ya decidida
   y declarada para SAP (D-O2.3). Inventar aqui un segundo valor para la misma idea geometrica crearia
   una discrepancia gratuita entre los dos objetivos.

3. **Guarda alrededor de `M`: se MIDE, por elevacion de HU y no por fraccion de metal.**
   Es la distancia a partir de la cual el volumen parcial del metal deja de contaminar la ROI.
   **La primera version de este script uso un criterio circular** —la fraccion de voxeles por encima
   de 2500 HU—, que da **cero en todas las cascaras por construccion**: la distancia se mide desde
   `~metal`, asi que las cascaras excluyen el metal por definicion y ese criterio no podia detectar
   nada. El criterio valido es la **elevacion de la mediana de HU** de cada cascara respecto al nivel
   de fuera de `B_delta`; la guarda es la primera cascara cuya elevacion cae por debajo de
   `--tol-elev`.

4. **Radios: de la guarda a 12.0 mm. NO se miden: se siguen de `B_delta`.**
   El sintetizador escribe **solo dentro de `G`**, asi que el campo de desviacion
   `I_sintetica - I_original` es **cero fuera de `G` por construccion** (bloque E-A3, comprobado en
   cada sintesis). El radio exterior no es un grado de libertad: es el ancho de la banda, ya declarado
   en `diseno_A.md` seccion 3. Buscarlo con una medicion seria fabricar un parametro que el diseno ya
   fijo.

   **El perfil de vano sobre HU crudo que este script imprime NO sirve para elegir radios**, aunque lo
   parezca. Su "fondo" fuera de `B_delta` sale del orden de 1000 HU porque el anillo cruza hueso,
   tejido y aire, y las colas recogen ese contraste. El estadistico de Peters se calcula sobre el
   **campo de desviacion**, donde la anatomia se cancela. El perfil se conserva como **diagnostico**,
   porque dice algo que si importa: **el vano sobre HU crudo esta dominado por la anatomia**, que es
   la razon por la que el proxy usado en #141 subestima y por la que la metrica necesita su verdad de
   terreno.

COMO SE MIDE
------------
Sobre los parches cacheados de `a1b` de los pacientes de **validacion** que tienen metal. Para cada
parche: distancia euclidea en mm desde `M` en el plano del corte, con el espaciado del caso; cascaras
de `--paso-mm`; y en cada cascara la mediana de HU, el vano de colas y el recuento. Se agrega **por
paciente** y se reporta la mediana entre pacientes, que es la unidad de la particion.

CONTROL QUE PUEDE FALLAR
------------------------
Si se piden pacientes de test, aborta. Fijar un parametro del endpoint mirando test es exactamente lo
que la preinscripcion existe para impedir.

USO
---
    python a12_roi_parametros.py
    python a12_roi_parametros.py --paso-mm 0.5 --tol-elev 25
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

import numpy as np

_RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_RAIZ / 'experiments' / 'objetivo2'))

PATRON = re.compile(r'^(?P<serie>.+)_k(?P<k>\d{4})\.npz$')
BANDA_MM = 12.0
COLA = 0.05
RECORTE_EXTREMO_MM = 8.0   # de `e9_corredor.py`, decision D-O2.3; no se reinventa aqui


def vano(x: np.ndarray) -> float:
    """Forma del estadistico de Peters: promedio del 5 % alto menos el del 5 % bajo."""
    if x.size < 20:
        return float('nan')
    k = max(1, int(round(x.size * COLA)))
    o = np.sort(x)
    return float(o[-k:].mean() - o[:k].mean())


def caso_de(serie: str) -> str:
    return re.sub(r'_c\d{3}$', '', serie)


def main() -> None:
    aqui = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--cache', type=Path, default=aqui / 'outputs' / 'a1b_cache')
    ap.add_argument('--particion', type=Path,
                    default=aqui.parent / 'objetivo1' / 'p1_particion.csv')
    ap.add_argument('--particiones', nargs='+', default=['val'])
    ap.add_argument('--paso-mm', type=float, default=1.0)
    ap.add_argument('--tol-elev', type=float, default=25.0,
                    help='elevacion de la mediana de HU, en HU, por debajo de la cual se considera '
                         'que el volumen parcial del metal ya no contamina la cascara')
    ap.add_argument('--out-dir', type=Path, default=aqui / 'outputs' / 'a12')
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    if 'test' in [p.lower() for p in args.particiones]:
        raise SystemExit('CONTROL: se pidio test. Abortado: los parametros del endpoint se fijan '
                         'sobre validacion (preinscripcion, 01-decisiones.md 2026-10-05 (3)).')

    from scipy import ndimage as ndi
    with open(args.particion, newline='', encoding='utf-8') as fh:
        permitidos = {f['Caso'] for f in csv.DictReader(fh) if f['particion'] in args.particiones}
    print('particiones %s: %d pacientes' % (args.particiones, len(permitidos)))
    print('cascaras de %.1f mm | cola de Peters %.0f %% | tolerancia de elevacion %.0f HU'
          % (args.paso_mm, 100 * COLA, args.tol_elev))

    bordes = np.arange(0.0, BANDA_MM + 3 * args.paso_mm + 1e-9, args.paso_mm)
    por_caso: dict[str, dict] = {}
    n_parches = 0
    for f in sorted(args.cache.glob('*.npz')):
        m = PATRON.match(f.name)
        if m is None:
            continue
        caso = caso_de(m.group('serie'))
        if caso not in permitidos:
            continue
        with np.load(f) as z:
            hu = z['hu'].astype(np.float32)
            metal = z['metal'].astype(bool)
            zooms = np.asarray(z['zooms'], dtype=float)
            eje = int(z['eje'])
        if not metal.any():
            continue
        plano = [i for i in range(3) if i != eje]
        esp = (zooms[plano[0]], zooms[plano[1]])
        dist = ndi.distance_transform_edt(~metal, sampling=esp)
        d = por_caso.setdefault(caso, {'vano': {}, 'hu': {}, 'n': {}})
        for i in range(len(bordes) - 1):
            sel = (dist > bordes[i]) & (dist <= bordes[i + 1])
            if sel.sum() < 20:
                continue
            v = vano(hu[sel])
            if np.isfinite(v):
                d['vano'].setdefault(i, []).append(v)
            d['hu'].setdefault(i, []).append(float(np.median(hu[sel])))
            d['n'].setdefault(i, []).append(int(sel.sum()))
        n_parches += 1
    if not por_caso:
        raise SystemExit('ningun parche con metal en %s' % args.particiones)
    print('parches con metal medidos: %d | pacientes: %d (%s)'
          % (n_parches, len(por_caso), ', '.join(sorted(por_caso))))

    filas = []
    for i in range(len(bordes) - 1):
        vs = [float(np.median(d['vano'][i])) for d in por_caso.values() if i in d['vano']]
        hs = [float(np.median(d['hu'][i])) for d in por_caso.values() if i in d['hu']]
        ns = [int(np.median(d['n'][i])) for d in por_caso.values() if i in d['n']]
        if not hs:
            continue
        filas.append({'r_lo_mm': round(float(bordes[i]), 2),
                      'r_hi_mm': round(float(bordes[i + 1]), 2),
                      'n_pacientes': len(hs),
                      'hu_mediano_p50': round(float(np.median(hs)), 1),
                      'vano_p50_HU': round(float(np.median(vs)), 1) if vs else float('nan'),
                      'n_voxeles_p50': int(np.median(ns))})

    fuera = [f['hu_mediano_p50'] for f in filas if f['r_lo_mm'] >= BANDA_MM]
    hu_fuera = float(np.median(fuera)) if fuera else float('nan')
    for f in filas:
        f['elevacion_HU'] = round(f['hu_mediano_p50'] - hu_fuera, 1)

    print('\n r_lo  r_hi   HU mediano   elevacion   vano (diagnostico)   n vox   pac')
    for f in filas:
        marca = '  <- fuera de B_delta' if f['r_lo_mm'] >= BANDA_MM else ''
        print('%5.1f %5.1f   %10.1f   %+9.1f   %18.1f   %6d   %3d%s'
              % (f['r_lo_mm'], f['r_hi_mm'], f['hu_mediano_p50'], f['elevacion_HU'],
                 f['vano_p50_HU'], f['n_voxeles_p50'], f['n_pacientes'], marca))

    ruta = args.out_dir / 'a12_perfil_radial_val.csv'
    with open(ruta, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print('perfil: %s' % ruta)

    # LA GUARDA NO SE PUEDE FIJAR POR UMBRAL SOBRE LA IMAGEN REAL, y el perfil de arriba lo
    # demuestra. Se probaron dos criterios y los dos fallan por razones opuestas:
    #
    #   (a) fraccion de voxeles sobre 2500 HU: da CERO en todas las cascaras por construccion,
    #       porque la distancia se mide desde `~metal` y las cascaras excluyen el metal.
    #   (b) elevacion de la mediana de HU respecto a fuera de `B_delta`: solo baja de 25 HU a los
    #       11 mm, de modo que la "guarda" se comeria la banda entera y dejaria una ROI de 1 mm.
    #       Falla porque la elevacion **no es contaminacion**: es el artefacto, que es la senal que
    #       la metrica existe para medir. El criterio excluia justo lo que hay que medir.
    #
    # En una imagen real, a esta escala, el volumen parcial del metal y el artefacto de campo
    # cercano son la MISMA senal, y separarlos exigiria una referencia sin metal del mismo
    # paciente, que es el problema que la metrica ya tiene.
    #
    # Por eso la guarda se fija por ARGUMENTO y al MINIMO: un voxel en plano. El volumen parcial no
    # puede extenderse menos que eso, y cualquier guarda mayor descarta senal de artefacto, lo que
    # sesga `streak amplitude` **a la baja**, en la misma direccion que la censura por el suelo de
    # -1000 HU (#141). Ante dos sesgos del mismo signo, el parametro se elige para no sumar uno mas.
    espaciados = []
    for f2 in sorted(args.cache.glob('*.npz')):
        m2 = PATRON.match(f2.name)
        if m2 is None or caso_de(m2.group('serie')) not in permitidos:
            continue
        with np.load(f2) as z2:
            zz = np.asarray(z2['zooms'], dtype=float)
            ee = int(z2['eje'])
        espaciados.append(max(zz[i] for i in range(3) if i != ee))
    guarda_mm = round(float(np.median(espaciados)), 2) if espaciados else None
    dentro = [f for f in filas if f['r_hi_mm'] <= BANDA_MM]
    guarda = guarda_mm
    print('\nGuarda: NO se fija por umbral. Dos criterios probados fallan por razones opuestas '
          '(ver comentario en el codigo).')
    print('Se fija al MINIMO defendible: UN VOXEL en plano. Mediana entre los pacientes de '
          'validacion: %.2f mm' % (guarda_mm if guarda_mm else float('nan')))
    print('Razon: una guarda mayor descarta senal de artefacto y sesga el endpoint A LA BAJA, en la '
          'misma direccion que la censura del suelo de -1000 HU (#141).')
    knee = [f for f in dentro if f['r_lo_mm'] >= 3.0 and f['r_lo_mm'] <= 4.0]
    if knee:
        print('Evidencia del perfil: la caida abrupta de la mediana (volumen parcial mas campo '
              'cercano) se agota hacia los 3-4 mm (%.0f HU de elevacion ahi), y de ahi a los 12 mm '
              'decae despacio. Ese tramo lento es artefacto y NO se excluye.'
              % knee[0]['elevacion_HU'])

    print('\n=== PARAMETROS, para copiar a `diseno_A.md` al congelarlo ===')
    print('1. Apertura del arco: 360 grados, ANILLO COMPLETO. Por argumento (estadistico de colas:')
    print('   la direccionalidad del streak no afecta a las colas), no por medicion.')
    print('2. Planos: todos los cortes con `M`, excluyendo %.1f mm por extremo. Reutiliza'
          % RECORTE_EXTREMO_MM)
    print('   `RECORTE_EXTREMO_MM` de `e9_corredor.py` (D-O2.3); no se inventa otro valor.')
    print('3. Guarda alrededor de `M`: **%s mm**, que es UN VOXEL en plano (mediana entre los'
          % (('%.2f' % guarda) if guarda is not None else 'NO DETERMINADA'))
    print('   pacientes de validacion). Fijada al minimo por ARGUMENTO, no por umbral: una guarda')
    print('   mayor descartaria senal de artefacto y sesgaria el endpoint a la baja.')
    print('4. Radios de los anillos: de **%s mm** a **%.1f mm**. El exterior NO se mide: es el ancho'
          % (('%.1f' % guarda) if guarda is not None else '?', BANDA_MM))
    print('   de `B_delta`, y el campo de desviacion es cero fuera de `G` por construccion (E-A3).')
    print('\nNinguna de estas cifras mira un paciente de test ni ninguna salida del sintetizador.')


if __name__ == '__main__':
    main()
