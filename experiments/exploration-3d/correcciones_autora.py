"""Correcciones puntuales de `revision.csv` confirmadas por la autora, con registro.

Cada correccion declara el valor ESPERADO antes del cambio. Si la celda no tiene ese valor
(y tampoco el nuevo), el script aborta sin escribir: nunca pisa algo que no conoce.
Idempotente: una celda que ya tiene el valor nuevo se deja igual.

Respaldo en `revision.pre-correcciones.csv` (una sola vez). Verifica que solo cambien las
celdas listadas.
"""
from __future__ import annotations

import csv
import shutil
from pathlib import Path

# (Caso, columna, valor esperado antes, valor nuevo, fuente)
CORRECCIONES: list[tuple[str, str, str, str, str]] = [
    ('dataset7_CLINIC_metal_0068_data', 'Notas',
     'Material ortopedico presente (regla de la autora para dataset7) y ademas: zipper '
     '(cursor) y accesorios.',
     'SIN material ortopedico: confirmado por la autora el 2026-09-10 tras E8 (#21, #46); '
     'excepcion observada a la regla de dataset7. Contenido = zipper (cursor) y accesorios.',
     'autora 2026-09-10; 01-decisiones.md'),
    ('dataset7_CLINIC_metal_0068_data', 'Procedencia metal', 'autora-regla', 'autora-3D',
     'autora 2026-09-10: presencia de metal (zipper) observada, no derivada de regla'),
]


def main() -> None:
    """Aplica, registra y verifica."""
    ruta = Path(__file__).with_name('revision.csv')
    with ruta.open(encoding='utf-8-sig', newline='') as h:
        reader = csv.DictReader(h)
        campos = list(reader.fieldnames or [])
        filas = list(reader)
    por_caso = {f['Caso']: f for f in filas}

    cambios: list[tuple[str, str]] = []
    for caso, col, antes, nuevo, fuente in CORRECCIONES:
        fila = por_caso[caso]
        actual = fila[col]
        if col == 'Notas':
            # La nota tiene bloque de la autora y bloque de agente separados por ' || '.
            autora, sep, agente = actual.partition(' || ')
            if autora == nuevo:
                continue
            if autora != antes:
                raise SystemExit(f'ABORTADO: {caso}/{col} no tiene el valor esperado:\n{autora}')
            fila[col] = nuevo + sep + agente
        else:
            if actual == nuevo:
                continue
            if actual != antes:
                raise SystemExit(f'ABORTADO: {caso}/{col} = {actual!r}, esperado {antes!r}')
            fila[col] = nuevo
        cambios.append((caso, col))
        print(f'{caso} / {col}: corregido ({fuente})')

    if not cambios:
        print('Nada que cambiar: las correcciones ya estaban aplicadas.')
        return
    respaldo = ruta.with_name('revision.pre-correcciones.csv')
    if not respaldo.exists():
        shutil.copy2(ruta, respaldo)
    with respaldo.open(encoding='utf-8-sig', newline='') as h:
        original = {f['Caso']: f for f in csv.DictReader(h)}
    with ruta.open('w', encoding='utf-8-sig', newline='') as h:
        w = csv.DictWriter(h, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)
    permitidas = {(c, col) for c, col, *_ in CORRECCIONES}
    ajenas = [(f['Caso'], k) for f in filas for k in campos
              if (f['Caso'], k) not in permitidas and original[f['Caso']].get(k, '') != f[k]]
    if ajenas:
        raise SystemExit(f'ERROR: cambiaron celdas no listadas: {ajenas[:5]}')
    print(f'Celdas corregidas: {len(cambios)}; celdas ajenas alteradas: 0.')


if __name__ == '__main__':
    main()
