"""Manifiesto de volumenes RETIRADOS del conjunto de trabajo. Genera `exclusiones.csv`.

Principio (autora, 2026-09-10): **ningun `.nii.gz` se borra ni se mueve.** Un volumen fuera
de uso queda en `data/` y se declara aqui, con motivo, evidencia, decision y quien lo
decidio. Todo script que construya cohortes lee este archivo en vez de listar a mano.

Este manifiesto es de nivel **conjunto de datos** (el volumen no se usa en ningun objetivo
porque es redundante con otro del mismo paciente). La elegibilidad **por objetivo** (#35)
es otra cosa y vive en `grupos.csv`.

ESTADOS
-------
- `retirado`: copia exacta o subconjunto exacto de otro volumen que se conserva.
- `fusionado`: sus voxeles estan integros en un volumen derivado sin perdida.
- `secundario`: otra adquisicion del mismo paciente; no cuenta en cohortes, se conserva
  como par de reproducibilidad.

Lee `revision.csv` (spacing y cortes para la regla del primario). Escribe `exclusiones.csv`.
"""
from __future__ import annotations

import csv
from pathlib import Path

D7 = 'dataset7_CLINIC_metal_{}_data'
D6 = 'dataset6_CLINIC_{}_data'
UNION = 'data/derivados/dataset7_CLINIC_metal_0059u0071_union.nii.gz'

# (caso, estado, sustituido por, motivo, evidencia, decision, estado de la decision)
FIJAS: list[tuple[str, str, str, str, str, str, str]] = [
    *[(D6.format(a), 'retirado', D7.format(b),
       'copia exacta de un volumen de dataset7; prevalece dataset7',
       'SHA256 voxeles (Grupo duplicado)', '01-decisiones.md 2026-09-07', 'decidida')
      for a, b in (('0037', '0061'), ('0048', '0036'), ('0070', '0064'))],
    *[(D7.format(b), 'retirado', D7.format(a),
       'copia exacta interna de dataset7; se conserva el de indice menor',
       'SHA256 voxeles (Grupo duplicado)', '#20; autora 2026-09-10',
       'decidida (autora 2026-09-10: indice menor; contenido identico)')
      for a, b in (('0012', '0021'), ('0013', '0043'), ('0046', '0074'))],
    (D7.format('0034'), 'retirado', D7.format('0011'),
     'subconjunto exacto (350 de 351 cortes); el corte restante no aporta',
     'duplicados_parciales.csv (350 cortes identicos)', '01-decisiones.md 2026-09-10', 'decidida'),
    (D6.format('0038'), 'retirado', D6.format('0090'),
     'subconjunto exacto (331 de 350 cortes); los cortes restantes no aportan',
     'duplicados_parciales.csv (331 cortes identicos)', '01-decisiones.md 2026-09-10', 'decidida'),
    (D7.format('0059'), 'fusionado', UNION,
     'mismo escaneo con FOV solapado; aporta los cortes superiores',
     'duplicados_parciales.csv (216 cortes); union_0059_0071.md', '01-decisiones.md 2026-09-10',
     'decidida'),
    (D7.format('0071'), 'fusionado', UNION,
     'mismo escaneo con FOV solapado; aporta los cortes inferiores',
     'duplicados_parciales.csv (216 cortes); union_0059_0071.md', '01-decisiones.md 2026-09-10',
     'decidida'),
]
# Adquisiciones distintas del mismo paciente: el primario sale de una regla a priori.
PARES_ADQUISICION = [(D7.format('0065'), D7.format('0066'))]


def primario(a: dict[str, str], b: dict[str, str]) -> tuple[dict, dict, str]:
    """Regla a priori: menor spacing en plano; empate -> mas cortes. Nunca por el metal."""
    clave = lambda f: (float(f['Spacing x mm']), -int(float(f['Dim z'])))  # noqa: E731
    p, s = (a, b) if clave(a) <= clave(b) else (b, a)
    motivo = (f'otra adquisicion del mismo paciente; primario = {p["Caso"]} por regla a priori '
              f'(spacing en plano {float(p["Spacing x mm"]):.3f} vs '
              f'{float(s["Spacing x mm"]):.3f} mm; empate -> mas cortes)')
    return p, s, motivo


def main() -> None:
    """Construye el manifiesto y comprueba que todos los casos existen."""
    aqui = Path(__file__).parent
    with (aqui / 'revision.csv').open(encoding='utf-8-sig', newline='') as h:
        filas = {f['Caso']: f for f in csv.DictReader(h)}

    salida: list[dict[str, str]] = []

    def fila(caso: str, estado: str, por: str, motivo: str, evid: str, dec: str,
             est: str) -> dict[str, str]:
        if caso not in filas:
            raise SystemExit(f'{caso} no esta en revision.csv. No se escribio nada.')
        f = filas[caso]
        return {'Caso': caso, 'Archivo': f'data/{f["Dataset"]}/{caso}.nii.gz',
                'Dataset': f['Dataset'], 'Grupo paciente': f.get('Grupo paciente', ''),
                'Estado': estado, 'Sustituido por': por, 'Motivo': motivo, 'Evidencia': evid,
                'Decision': dec, 'Estado decision': est, 'Archivo borrado': 'no'}

    for args in FIJAS:
        salida.append(fila(*args))
    for a, b in PARES_ADQUISICION:
        p, s, motivo = primario(filas[a], filas[b])
        salida.append(fila(s['Caso'], 'secundario', p['Caso'], motivo,
                           'observacion visual de la autora; sin voxeles compartidos; E8 '
                           'test-retest (#45)',
                           '01-decisiones.md 2026-09-10',
                           'decidida (regla propuesta por el asistente, aplicada por orden '
                           'de la autora)'))

    grupos = {r['Grupo paciente'] for r in salida}
    for r in salida:
        por = r['Sustituido por']
        if por in filas and filas[por]['Grupo paciente'] != r['Grupo paciente']:
            raise SystemExit(f'{r["Caso"]} y {por} no comparten Grupo paciente. Abortado.')
    campos = list(salida[0].keys())
    with (aqui / 'exclusiones.csv').open('w', encoding='utf-8-sig', newline='') as h:
        w = csv.DictWriter(h, fieldnames=campos)
        w.writeheader()
        w.writerows(salida)
    conteo: dict[str, int] = {}
    for r in salida:
        conteo[r['Estado']] = conteo.get(r['Estado'], 0) + 1
    print(f'{len(salida)} volumenes en exclusiones.csv ({len(grupos)} pacientes): {conteo}')


if __name__ == '__main__':
    main()
