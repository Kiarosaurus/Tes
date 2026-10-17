# Revision guia CS — conclusiones — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-D1, P-CO2 | conclusiones.tex:10, :22 | La subseccion responde por separado los cuatro objetivos especificos y la pregunta, pero no evalua explicitamente hasta que punto se cumplio el objetivo general de `introduccion.tex:32`. Su respuesta puede reconstruirse de la sintesis y de los parrafos posteriores, pero no se puede senalar con el dedo como exige G-D1. | Agregar antes de los objetivos especificos una respuesta breve al objetivo general: distinguir la cadena disenada e implementada, la lectura descriptiva de la coherencia quirurgica y la coherencia de apariencia que no se establecio frente al protocolo fisico. |
| guia-2 | media | G-D2 | conclusiones.tex:34 | La frase «El perfil por anillos y la variabilidad entre pacientes separaron [...] al sintetizador del protocolo fisico donde la media no lo hacia» introduce una relacion que el capitulo de resultados no demuestra en esos terminos. `capitulo4.tex:252` concluye que la amplitud media no distingue un modelo aprendido de uno analitico, mientras `capitulo4.tex:254` presenta la variabilidad como una dimension adicional; no afirma que la media no separara al sintetizador del protocolo fisico. | Alinear la sintesis con la discusion: decir que el perfil por anillos y la variabilidad agregan dimensiones que la comparacion de medias no recoge, sin afirmar que esta ultima no separo al sintetizador del protocolo fisico. |

TOTAL alta=0 media=2 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple: la seccion identifica la contribucion, las condiciones de evaluacion, los resultados y sus limites con remisiones al documento |
| G-T2 | cumple: conserva los terminos tecnicos definidos en los capitulos anteriores |
| G-T3 | cumple: mantiene los significados de $G$, $M$, $B_{\delta}$ y $\Delta$ |
| G-T4 | cumple: las cifras remiten a tablas o secciones de resultados; la comprobacion material de las fuentes corresponde al auditor de trazabilidad |
| G-T5 | no evaluable: la progresion desde resultados hacia conclusiones es justificable, pero `trabajosFuturos.tex` aun es plantilla y no permite evaluar el enlace con la seccion siguiente |
| G-T6 | cumple: `peters2025hybrid`, `guo2025maisi` y `liu2021ctpelvic1k` estan en `refs.bib` |
| G-D1 | no cumple (guia-1): responde los cuatro objetivos especificos y la pregunta, pero deja implicita la evaluacion del objetivo general |
| G-D2 | no cumple (guia-2): el parrafo inicial sintetiza propuesta, ejecucion y resultados, pero la interpretacion de `conclusiones.tex:34` no coincide con la formulada en resultados |
| G-D3 | no evaluable: `conclusiones.tex:28-30` declara limitaciones como tales, pero su distincion completa respecto del trabajo futuro no puede juzgarse mientras `trabajosFuturos.tex` siga en plantilla |
| G-D4 | no evaluable: `trabajosFuturos.tex` sigue en plantilla |
| P-CO1 | cumple: solo concluye sobre hallazgos y evaluaciones del propio trabajo |
| P-CO2 | no cumple (guia-1): presenta logros y limitaciones y evalua los objetivos especificos, pero no explicita el grado de cumplimiento del objetivo general |

## Propuestas de criterio

Ninguna.

## Patrones

sin patrones
