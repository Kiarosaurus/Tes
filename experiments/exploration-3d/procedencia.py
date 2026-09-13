"""Implicancia #37 — anade procedencia por campo a `revision.csv`.

Problema: las 178 filas comparten un unico `Revisor` y ningun campo declara su autor.
La unica forma de saber si un dato lo puso la autora o un agente era leer el texto libre
de `Notas`. Eso ya provoco un error real (ver correccion de #34/#35).

Este script NO revisa ningun volumen y NO modifica ninguna columna existente: solo lee
`Notas` fila por fila y anade columnas `Procedencia *` derivadas de la evidencia que ya
esta escrita ahi. Es idempotente: correrlo dos veces deja el mismo resultado.

Vocabulario de procedencia (cerrado):

- `autora-3D`      observacion per-volumen de la autora en revision 3D.
- `autora-regla`   NO es observacion per-volumen: se deriva de una regla general que la
                   autora enuncio ("fila en blanco en dataset7 = hay material
                   ortopedico"). Vale como decision, no como hallazgo medido.
- `agente-laminas` propuesta de un agente `clasificador-metal` leyendo laminas PNG.
                   No certifica; sus `no` son ausencia de evidencia en pocos cortes.
- `script`         calculado por `explorar.py` / `sensibilidad_hu.py` sobre el NIfTI.
- `sin dato`       campo vacio.

Reparto de columnas por eje (documentado en #37 y verificado contra `Notas`):

| Eje              | Columnas cubiertas                                        |
|------------------|-----------------------------------------------------------|
| observacion      | Tipo de estructura observada, Cantidad aprox.             |
| artefacto        | Artefactos, Severidad                                     |
| localizacion     | Ubicacion anatomica, Lateralidad, Confianza               |
| metal            | Metal, Objeto extrano, Revision 3D y cortes               |
| instrumental     | Spacing/Dim/HU/Umbral/Voxeles/Candidato/SHA256/Grupo dup. |
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
from pathlib import Path

EJES: dict[str, tuple[str, ...]] = {
    'observación': ('Tipo de estructura observada', 'Cantidad aprox.'),
    'artefacto': ('Artefactos', 'Severidad'),
    'localización': ('Ubicación anatómica', 'Lateralidad', 'Confianza'),
    'metal': ('Metal', 'Objeto extraño', 'Revisión 3D y cortes'),
}
INSTRUMENTAL: tuple[str, ...] = (
    'Spacing x mm', 'Spacing y mm', 'Spacing z mm', 'Dim x', 'Dim y', 'Dim z',
    'HU mínimo', 'HU máximo', 'Umbral HU', 'Vóxeles sobre umbral', 'Candidato HU',
    'SHA256 vóxeles', 'Grupo duplicado',
)
NUEVAS: tuple[str, ...] = (
    *(f'Procedencia {eje}' for eje in EJES),
    'Procedencia instrumental',
    'Validado por autora (artefacto)',
)

RE_AUTORA = re.compile(r'\bAutora\b')
RE_AGENTE = re.compile(r'\bAgente\s*:')
# Dos redacciones de la MISMA regla general de la autora sobre dataset7, mas la regla de
# duplicados del 2026-09-07 (dataset7 prevalece y queda sin material ortopedico).
RE_REGLA = re.compile(r'fila en blanco en dataset7|regla de la autora', re.IGNORECASE)
# Marcas de que, ademas de la regla, la autora SI miro ese volumen y anoto algo suyo.
RE_OBS_PROPIA = re.compile(r'y ademas\s*:|observado en 3D|Autora\s*:', re.IGNORECASE)


def procedencia(row: dict[str, str]) -> dict[str, str]:
    """Deriva la procedencia de cada eje leyendo solo `Notas` y los campos ya presentes."""
    notas = row.get('Notas') or ''
    autora = bool(RE_AUTORA.search(notas))
    agente = bool(RE_AGENTE.search(notas))
    regla = bool(RE_REGLA.search(notas))
    obs_propia = bool(RE_OBS_PROPIA.search(notas))

    def vacio(eje: str) -> bool:
        return not any((row.get(col) or '').strip() for col in EJES[eje])

    # El eje `metal` nunca esta vacio: las 178 filas traen si/no y `3D completa`.
    if regla:
        metal = 'autora-regla'
    elif autora:
        metal = 'autora-3D'
    else:
        metal = 'sin declarar'

    # Una fila puede llevar la regla general Y una observacion per-volumen de la autora
    # ("... y ademas: 2 zippers"). En ese caso manda la observacion, que es lo medido.
    if vacio('observación'):
        observacion = 'sin dato'
    elif obs_propia:
        observacion = 'autora-3D'
    elif regla:
        observacion = 'autora-regla'
    elif autora:
        observacion = 'autora-3D'
    else:
        observacion = 'agente-laminas'

    # #34/#35, correccion de procedencia del 2026-09-09: la autora NUNCA lleno estos dos
    # ejes. Vienen siempre de laminas, incluidas las afirmaciones de ausencia.
    artefacto = 'sin dato' if vacio('artefacto') else 'agente-laminas'
    localizacion = 'sin dato' if vacio('localización') else 'agente-laminas'

    return {
        'Procedencia observación': observacion,
        'Procedencia artefacto': artefacto,
        'Procedencia localización': localizacion,
        'Procedencia metal': metal,
        'Procedencia instrumental': 'script' if any(
            (row.get(col) or '').strip() for col in INSTRUMENTAL) else 'sin dato',
        # Bloqueo declarado el 2026-09-09: nada del eje artefacto esta validado todavia.
        'Validado por autora (artefacto)': 'no',
        '_agente': agente,  # solo para el resumen; no se escribe
    }


def anotar(ruta: Path, respaldo: bool) -> None:
    """Reescribe `revision.csv` con las columnas de procedencia anadidas al final."""
    with ruta.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        campos = list(reader.fieldnames or [])
        filas = list(reader)
    if not filas:
        raise SystemExit(f'{ruta} vacio. No se escribio nada.')

    faltan = [col for grupo in EJES.values() for col in grupo if col not in campos]
    if faltan:
        raise SystemExit(f'Faltan columnas esperadas: {faltan}. No se escribio nada.')

    salida = [c for c in campos if c not in NUEVAS] + list(NUEVAS)
    resumen: dict[str, dict[str, int]] = {c: {} for c in NUEVAS}
    for fila in filas:
        marcas = procedencia(fila)
        marcas.pop('_agente')
        fila.update(marcas)
        for col, val in marcas.items():
            resumen[col][val] = resumen[col].get(val, 0) + 1

    if respaldo and not ruta.with_suffix('.csv.bak').exists():
        shutil.copy2(ruta, ruta.with_suffix('.csv.bak'))
    with ruta.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=salida, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(filas)

    print(f'{len(filas)} filas, {len(salida)} columnas ({len(NUEVAS)} nuevas).')
    for col, conteo in resumen.items():
        detalle = ', '.join(f'{k}={v}' for k, v in sorted(conteo.items()))
        print(f'  {col}: {detalle}')


def main() -> None:
    """Punto de entrada de linea de comandos."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', type=Path,
                        default=Path(__file__).parent / 'revision.csv')
    parser.add_argument('--sin-respaldo', action='store_true')
    args = parser.parse_args()
    anotar(args.csv, respaldo=not args.sin_respaldo)


if __name__ == '__main__':
    main()
