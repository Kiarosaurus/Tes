# Revisión de estilo — capitulo1 — r07

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S1 | media | E-M4 | `overleaf/secciones/capitulo1.tex:31` | «limitación que interviene en el endurecimiento del haz» | Las fuentes médicas son policromáticas; esa desviación del supuesto monoenergético produce endurecimiento del haz. |
| S2 | media | E-R5, E-T1 | `overleaf/secciones/capitulo1.tex:130` | «El remuestreo bootstrap toma muestras» | El remuestreo con reemplazo toma muestras de igual tamaño y recalcula en cada réplica el estadístico de interés. |

## Impresión general
La sección conserva un registro sobrio y explicativo, y las fuentes nuevas quedan integradas sin inflar su alcance. Los dos desvíos están en una consecuencia física poco explícita y en el cambio de nombre de un concepto estadístico ya presentado como «remuestreo».

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un término inglés se agrega al nombre español ya fijado y crea una segunda denominación | E-R5, E-T1 | «remuestreo bootstrap» | nuevo |
