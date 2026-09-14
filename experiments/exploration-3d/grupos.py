"""Asignacion de cada unidad de trabajo a un grupo por objetivo. Genera `grupos.csv`.

VERSION POR PACIENTE (2026-09-10, `01-decisiones.md`). La unidad de independencia es el
paciente. Una fila por volumen de `revision.csv` mas una fila por volumen derivado.

Lo que SI esta decidido y se aplica tal cual
--------------------------------------------
- **Volumenes fuera de uso**: los lista `exclusiones.csv` (`exclusiones.py`), con motivo y
  decision. Aqui salen como `excluido` (retirado o fusionado) o `reproducibilidad`
  (secundario). Ningun archivo se borra.
- **Duplicados cruzados** (2026-09-07): prevalece dataset7 y ese volumen queda SIN material
  ortopedico (`metal_0036`, `metal_0061`, `metal_0064`).
- **`metal_0068` SIN material ortopedico** (2026-09-10): excepcion observada a la regla
  "fila vacia en dataset7 = material ortopedico".
- **Union `metal_0059` + `metal_0071`** (2026-09-10): el volumen derivado es la unidad del
  paciente `P158`.

- **#20** (2026-09-10): en las copias exactas internas de dataset7 se conserva el indice
  menor (contenido identico: la eleccion no cambia ningun voxel).

Lo que NO esta decidido y va marcado
------------------------------------
- **#35, reparto por objetivo**: CERRADA por la autora el 2026-09-14, junto con #52 (a). Cada
  objetivo tiene su elegibilidad; el Objetivo 2 usa pelvis sin osteosintesis (grupos 2 y 3).
  Sigue fragil la **evidencia** de `Elegible Obj3`: el eje de artefacto viene de agente bajo
  bloqueo declarado (#34/#37). Cerrar #35 fija la regla, no esa evidencia.

Regla de la particion unica (cada unidad a su consumidor mas escaso), en orden:
- `excluido` / `reproducibilidad`  segun `exclusiones.csv`.
- `grupo 1`   material ortopedico presente.
- `grupo 3`   sin metal y sin ningun objeto observado.
- `grupo 2`   el resto: geometria osea intacta con objeto no ortopedico presente.

Lee `revision.csv` y `exclusiones.csv`; no toca ningun volumen ni modifica `revision.csv`.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

SIN_ORTOPEDICO: dict[str, str] = {
    'dataset7_CLINIC_metal_0061_data': 'representante de duplicado cruzado (2026-09-07)',
    'dataset7_CLINIC_metal_0036_data': 'representante de duplicado cruzado (2026-09-07)',
    'dataset7_CLINIC_metal_0064_data': 'representante de duplicado cruzado (2026-09-07)',
    'dataset7_CLINIC_metal_0068_data': 'observado por la autora (2026-09-10)',
}
DERIVADOS: list[dict[str, str]] = [{
    'Caso': 'dataset7_CLINIC_metal_0059u0071_union',
    'Dataset': 'dataset7 (derivado)',
    'Archivo': 'data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz',
    'Origen': 'dataset7_CLINIC_metal_0059_data',  # hereda anotacion de la autora
}]


def clasificar(fila: dict[str, str]) -> dict[str, str]:
    """Grupo, elegibilidad por objetivo y motivo para una unidad no excluida."""
    caso = fila['Caso']
    ds7 = fila['Dataset'].startswith('dataset7')
    tipo = (fila.get('Tipo de estructura observada') or '').strip()
    metal = (fila.get('Metal') or '').strip().lower().startswith('s')
    ortopedico = ds7 and caso not in SIN_ORTOPEDICO
    limpio = (not metal) and not tipo
    if ortopedico:
        grupo, motivo, eleg = 'grupo 1', 'material ortopedico presente', ('si', 'no', 'no')
    elif limpio:
        grupo, motivo, eleg = 'grupo 3', 'sin metal y sin objeto observado', ('si', 'si', 'si')
    else:
        extra = f' ({SIN_ORTOPEDICO[caso]})' if caso in SIN_ORTOPEDICO else ''
        grupo = 'grupo 2'
        motivo = f'objeto no ortopedico presente: {tipo or "no descrito"}{extra}'
        eleg = ('si', 'si', 'no')
    return {'Grupo': grupo, 'Elegible Obj1': eleg[0], 'Elegible Obj2': eleg[1],
            'Elegible Obj3': eleg[2], 'Motivo': motivo,
            'Regla': 'reparto por objetivo (#35 CERRADA 2026-09-14)', 'Estado regla': 'decidida #35'}


def generar(csv_in: Path, excl: Path, csv_out: Path) -> None:
    """Escribe `grupos.csv` y el recuento por grupo en volumenes y pacientes."""
    with csv_in.open(encoding='utf-8-sig', newline='') as h:
        filas = list(csv.DictReader(h))
    with excl.open(encoding='utf-8-sig', newline='') as h:
        excluidos = {r['Caso']: r for r in csv.DictReader(h)}
    por_caso = {f['Caso']: f for f in filas}
    if not filas or any(c not in por_caso for c in excluidos):
        raise SystemExit('revision.csv vacio o exclusiones.csv con casos desconocidos.')

    unidades: list[dict[str, str]] = []
    for f in filas:
        u = dict(f)
        u['Archivo'] = f'data/{f["Dataset"]}/{f["Caso"]}.nii.gz'
        unidades.append(u)
    for d in DERIVADOS:
        u = dict(por_caso[d['Origen']])
        u.update({'Caso': d['Caso'], 'Dataset': d['Dataset'], 'Archivo': d['Archivo'],
                  'Grupo duplicado': ''})
        unidades.append(u)

    salida: list[dict[str, str]] = []
    for u in unidades:
        if u['Caso'] in excluidos:
            e = excluidos[u['Caso']]
            marca = {'Grupo': 'reproducibilidad' if e['Estado'] == 'secundario' else 'excluido',
                     'Elegible Obj1': 'no', 'Elegible Obj2': 'no', 'Elegible Obj3': 'no',
                     'Motivo': f'{e["Estado"]}: {e["Motivo"]} -> {e["Sustituido por"]}',
                     'Regla': f'exclusiones.csv ({e["Decision"]})',
                     'Estado regla': e['Estado decision']}
        else:
            marca = clasificar(u)
        salida.append({'Caso': u['Caso'], 'Dataset': u['Dataset'],
                       'Grupo paciente': u.get('Grupo paciente', ''), 'Archivo': u['Archivo'],
                       **marca, 'Metal': u.get('Metal', ''),
                       'Tipo de estructura observada': u.get('Tipo de estructura observada', ''),
                       'Artefactos': u.get('Artefactos', ''),
                       'Procedencia artefacto': u.get('Procedencia artefacto', ''),
                       'Procedencia metal': u.get('Procedencia metal', ''),
                       'Grupo duplicado': u.get('Grupo duplicado', '')})

    # Cada paciente debe tener exactamente una unidad en uso.
    en_uso: dict[str, list[str]] = {}
    for s in salida:
        if s['Grupo'].startswith('grupo'):
            en_uso.setdefault(s['Grupo paciente'], []).append(s['Caso'])
    dobles = {p: c for p, c in en_uso.items() if len(c) > 1}
    if dobles:
        raise SystemExit(f'Pacientes con mas de una unidad en uso: {dobles}. Abortado.')

    campos = list(salida[0].keys())
    with csv_out.open('w', encoding='utf-8-sig', newline='') as h:
        w = csv.DictWriter(h, fieldnames=campos)
        w.writeheader()
        w.writerows(salida)

    print(f'{len(salida)} unidades -> {csv_out}')
    for g in sorted({s['Grupo'] for s in salida}):
        sel = [s for s in salida if s['Grupo'] == g]
        print(f'  {g}: {len(sel)} unidades, {len({s["Grupo paciente"] for s in sel})} pacientes')
    for obj in ('Obj1', 'Obj2', 'Obj3'):
        print(f'  elegibles {obj}: {sum(s[f"Elegible {obj}"] == "si" for s in salida)}')
    print(f'  pacientes con unidad en uso: {len(en_uso)}')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    aqui = Path(__file__).parent
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--csv', type=Path, default=aqui / 'revision.csv')
    parser.add_argument('--exclusiones', type=Path, default=aqui / 'exclusiones.csv')
    parser.add_argument('--out', type=Path, default=aqui / 'grupos.csv')
    args = parser.parse_args()
    generar(args.csv, args.exclusiones, args.out)


if __name__ == '__main__':
    main()
