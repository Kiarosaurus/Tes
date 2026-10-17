# Revisión de estilo — conclusiones — r01

## Hallazgos
| ID | Sev | Criterio | Ubicación | Texto actual (máx. 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | alta | E-R6 | `overleaf/secciones/conclusiones.tex:12` | "la sola saturación a su rango de salida ya superaba el criterio" | La cita contigua sugiere que Guo et al. publican el rango, pero la ficha `docs/literatura/guo2025maisi.md` dice que no aparece en el artículo. Propuesta: "En el autoencoder descrito por Guo et al.~\cite{guo2025maisi}, la inspección del código de \texttt{maisi_ct_generative} y \texttt{scripts/sample.py} mostró que la saturación al rango de salida ya superaba el criterio." |
| ES-02 | media | E-P4 | `overleaf/secciones/conclusiones.tex:18` | "menor que la del protocolo físico [...] y mayor junto al borde" | Patrón PAT-8 reincide: los dos comparativos omiten magnitud aunque el capítulo de resultados la da. Propuesta: "En la banda completa, la diferencia media fue de $-301.0$~HU; en los anillos de 8 a 10 y de 10 a 12~mm, la amplitud superó la del protocolo físico en $+478.0$ y $+411.7$~HU." |
| ES-03 | media | E-R2 | `overleaf/secciones/conclusiones.tex:20` | "que tampoco es una verdad física" | "Las métricas de Peters et al. se interpretaron respecto del protocolo físico, que sirve de comparación y no valida la fidelidad física." |
| ES-04 | media | E-M4 | `overleaf/secciones/conclusiones.tex:22` | "una diferencia que alcanzaría cualquier brazo que genere artefacto" | "La comparación con la inserción por copia y pegado solo confirma la presencia de rayas; no permite juzgar su calidad." |
| ES-05 | baja | E-INF | `overleaf/secciones/conclusiones.tex:26` | "su criterio no se movió" | "La regla de la compuerta se fijó antes de la prueba decisiva y su criterio se mantuvo sin cambios." |
| ES-06 | media | E-R2 | `overleaf/secciones/conclusiones.tex:30` | "La envolvente y las cifras del Objetivo~2 se mantuvieron sin corregir" | Patrón PAT-5 reincide: la oración informa una decisión de reporte en vez del efecto medido. Propuesta: "Las cifras del Objetivo~2 se calcularon con esa envolvente y no se corrigieron por este efecto." |
| ES-07 | media | E-M8 | `overleaf/secciones/conclusiones.tex:30` | "la fractura [...] es su confundidor" | El posesivo no tiene un antecedente inequívoco. Propuesta: "No se estableció qué estrecha esos corredores; la fractura, confirmada en 20 de 30 casos, confunde la atribución del estrechamiento a una causa anatómica concreta." |
| ES-08 | media | E-R2 | `overleaf/secciones/conclusiones.tex:30` | "se reporta solo como geometría" | Patrón PAT-5 reincide: la frase anuncia cómo se reporta el dato. Propuesta: "Del segundo corredor bajo S1 solo se midió el eje en 69 de 72 pacientes; no se generaron poses ni grados." |
| ES-09 | media | E-R2, E-M4 | `overleaf/secciones/conclusiones.tex:34` | "separaron [...] al sintetizador del protocolo físico donde la media no lo hacía" | Patrón PAT-205 reincide: el cierre vuelve imprecisa una comparación ya cuantificada y no identifica qué separación aporta cada medida. Propuesta: "El perfil por anillos y la variabilidad entre pacientes mostraron diferencias adicionales respecto del protocolo físico." |
| ES-10 | media | E-R2 | `overleaf/secciones/conclusiones.tex:36` | "Lo que el trabajo aporta [...] es una condición previa" | eliminar; las dos oraciones siguientes ya nombran por separado el resultado del muestreador y la falta de respaldo del sintetizador. |
| ES-11 | baja | E-M8 | `overleaf/secciones/conclusiones.tex:36` | "su apariencia no tiene realismo visual reclamado" | "El uso del sintetizador como aumento de datos queda sin respaldo en este trabajo porque no se estableció el realismo visual de su apariencia." |

TOTAL alta=1 media=8 baja=2

## Impresion general
Leída de corrido, la sección conserva un registro sobrio y distingue con cuidado resultados, decisiones posteriores y límites. El patrón dominante aparece en los cierres: después de cifras precisas, varias oraciones pasan a formulaciones vagas, metadiscursivas o sin la magnitud de la comparación. La densidad es alta, pero los párrafos se mantienen dentro de la extensión acordada.

## Patrones
| Patrón (una línea, generalizable a otras secciones) | Criterio | Ejemplo antes (máx. 15 palabras) | Ya en bitácora (PAT-n o "nuevo") |
|---|---|---|---|
| Un comparativo retoma un resultado cuantificado sin conservar la magnitud de la diferencia | E-P4 | "menor [...] y mayor junto al borde" | PAT-8 |
| Una oración anuncia que una cifra se conserva o reporta en vez de enunciar el hecho | E-R2 | "se reporta solo como geometría" | PAT-5 |
| Una comparación cuantificada cierra con una valoración imprecisa de lo que distingue | E-R2, E-M4 | "donde la media no lo hacía" | PAT-205 |
