"""Llena `Grupo paciente` en `revision.csv` (implicancias #20 y #45; autorizado 2026-09-10).

Decision de la autora (2026-09-10): la unidad de independencia es el paciente. Mismo
paciente = mismo `Grupo paciente` = mismo lado del split.

FUENTES DE VINCULO (se registran en la columna nueva `Procedencia paciente`, convencion #37)
-------------------------------------------------------------------------------------------
- `hash-volumen`: mismo `SHA256 vóxeles` (copias exactas; 6 grupos ya en `Grupo duplicado`).
- `hash-corte + autora`: comparten cortes axiales identicos bit a bit
  (`duplicados_parciales.csv`) y la autora confirmo el mismo paciente el 2026-09-10.
- `autora-visual + agente`: `metal_0065`/`metal_0066`. No comparten ningun voxel; la autora
  observa misma anatomia y artefactos con un hueso ligeramente rotado (dos adquisiciones).
- `sin vinculo detectado`: el resto. **No afirma que sea otro paciente**: solo que ningun
  hash lo vincula. Dos reconstrucciones distintas de un mismo paciente serian invisibles.

Los IDs (`P001`...) son etiquetas neutras numeradas por orden de fila: no indican cual
volumen es el representante.

Respalda en `revision.pre-paciente.csv` (una sola vez). Solo modifica `Grupo paciente` y
anade `Procedencia paciente`; verifica que ninguna otra celda cambie. Idempotente.
"""
from __future__ import annotations

import csv
import shutil
from pathlib import Path

VINCULO_AUTORA_VISUAL = [('dataset7_CLINIC_metal_0065_data', 'dataset7_CLINIC_metal_0066_data')]
CONFIRMADOS_AUTORA_CORTE = {
    frozenset({'dataset7_CLINIC_metal_0011_data', 'dataset7_CLINIC_metal_0034_data'}),
    frozenset({'dataset6_CLINIC_0038_data', 'dataset6_CLINIC_0090_data'}),
    frozenset({'dataset7_CLINIC_metal_0059_data', 'dataset7_CLINIC_metal_0071_data'}),
}
PROC = 'Procedencia paciente'


def main() -> None:
    """Agrupa, escribe y verifica."""
    here = Path(__file__).resolve().parent
    ruta = here / 'revision.csv'
    with ruta.open(encoding='utf-8-sig', newline='') as h:
        reader = csv.DictReader(h)
        campos = list(reader.fieldnames or [])
        filas = list(reader)
    casos = [f['Caso'] for f in filas]

    padre = {c: c for c in casos}

    def raiz(c: str) -> str:
        while padre[c] != c:
            padre[c] = padre[padre[c]]
            c = padre[c]
        return c

    def unir(a: str, b: str) -> None:
        padre[raiz(a)] = raiz(b)

    fuente: dict[frozenset, str] = {}
    por_sha: dict[str, list[str]] = {}
    for f in filas:
        if f['Grupo duplicado']:
            por_sha.setdefault(f['Grupo duplicado'], []).append(f['Caso'])
    for miembros in por_sha.values():
        for m in miembros[1:]:
            unir(miembros[0], m)
        fuente[frozenset(miembros)] = 'hash-volumen'

    with (here / 'duplicados_parciales.csv').open(encoding='utf-8', newline='') as h:
        for r in csv.DictReader(h):
            par = frozenset({r['Caso A'], r['Caso B']})
            if par in fuente:
                continue  # ya cubierto por SHA256
            if par not in CONFIRMADOS_AUTORA_CORTE:
                raise SystemExit(f'Par con cortes compartidos sin confirmar por la autora: '
                                 f'{sorted(par)}. No se escribio nada.')
            unir(*par)
            fuente[par] = 'hash-corte + autora'
    for a, b in VINCULO_AUTORA_VISUAL:
        unir(a, b)
        fuente[frozenset({a, b})] = 'autora-visual + agente'

    grupos: dict[str, list[str]] = {}
    for c in casos:
        grupos.setdefault(raiz(c), []).append(c)
    ids: dict[str, str] = {}
    etiqueta: dict[str, str] = {}
    for n, c in enumerate(dict.fromkeys(raiz(c) for c in casos), start=1):
        miembros = frozenset(grupos[c])
        ids[c] = f'P{n:03d}'
        etiqueta[c] = fuente.get(miembros, 'sin vinculo detectado')
        if len(miembros) > 1 and miembros not in fuente:
            raise SystemExit(f'Grupo sin fuente unica: {sorted(miembros)}')

    respaldo = here / 'revision.pre-paciente.csv'
    if not respaldo.exists():
        shutil.copy2(ruta, respaldo)
    for f in filas:
        r = raiz(f['Caso'])
        f['Grupo paciente'] = ids[r]
        f[PROC] = etiqueta[r]
    salida = campos if PROC in campos else campos + [PROC]
    with ruta.open('w', encoding='utf-8-sig', newline='') as h:
        w = csv.DictWriter(h, fieldnames=salida)
        w.writeheader()
        w.writerows(filas)

    # Verificacion contra el respaldo: solo cambian las dos columnas.
    with respaldo.open(encoding='utf-8-sig', newline='') as h:
        original = list(csv.DictReader(h))
    alteradas = sum(1 for o, f in zip(original, filas) for k in campos
                    if k not in ('Grupo paciente', PROC) and o[k] != f[k])
    if alteradas or len(original) != len(filas):
        raise SystemExit(f'ERROR: {alteradas} celdas ajenas cambiaron.')

    multi = {r: g for r, g in grupos.items() if len(g) > 1}
    print(f'Filas: {len(filas)}; pacientes: {len(grupos)}; grupos con > 1 volumen: {len(multi)}; '
          f'celdas ajenas alteradas: {alteradas}.')
    for r, g in sorted(multi.items(), key=lambda t: ids[t[0]]):
        print(f'  {ids[r]} [{etiqueta[r]}]: ' + ', '.join(g))


if __name__ == '__main__':
    main()
