# Resumen de la exploración 3D

Unidad: volumen CT, no corte. Rangos = mínimo–máximo. Spacing en mm;
dimensiones en vóxeles y ejes nativos del archivo. Candidato HU ≠ metal confirmado.

| Dataset | Volúmenes | Candidatos HU | Metal sí revisado | Pendientes |
|---|---:|---:|---:|---:|
| dataset6 | 103 | 38 | 0 | 103 |
| dataset7 | 75 | 75 | 0 | 75 |

| Dataset | Medida | Mediana [mín–máx] |
|---|---|---|
| dataset6 | Spacing x mm | 0.839 [0.64–1.129] |
| dataset6 | Spacing y mm | 0.839 [0.64–1.129] |
| dataset6 | Spacing z mm | 0.799988 [0.79895–0.801025] |
| dataset6 | Dim x | 512 [512–512] |
| dataset6 | Dim y | 512 [512–512] |
| dataset6 | Dim z | 350 [294–388] |
| dataset7 | Spacing x mm | 0.82 [0.601–1.266] |
| dataset7 | Spacing y mm | 0.82 [0.601–1.266] |
| dataset7 | Spacing z mm | 0.800049 [0.79895–0.801025] |
| dataset7 | Dim x | 512 [512–512] |
| dataset7 | Dim y | 512 [512–512] |
| dataset7 | Dim z | 350 [187–351] |

Grupos de duplicados exactos por vóxeles: 6.
Volúmenes únicos por contenido: 172 (no equivale a pacientes únicos).
Errores de lectura: 0.
Máscaras locales vinculadas por nombre: 0.

## Elegibilidad provisional

- pendiente: 166
- resolver duplicado: 12

La asignación definitiva requiere revisión, resolver duplicados y agrupar por paciente.
Las máscaras se vinculan por nombre; aún deben verificarse alineación y etiquetas.
No se infiere ausencia de metal a partir del nombre dataset6 ni del filtro HU.
