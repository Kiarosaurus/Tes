# Revision de estilo — capitulo4 — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-01 | media | E-P3 | `overleaf/secciones/capitulo4.tex:214` | "cuya ida y vuelta sin autoencoder es exacta en el hueso" | "El veredicto descartó la difusión latente, pero no la codificación multiventana, cuya ida y vuelta sin autoencoder tuvo un error medio de 0.00~HU en el hueso con la compresión arcoseno hiperbólico." La fuente registra 0.00~HU a la precisión reportada, no exactitud (`experiments/objetivo1/p1_compuerta.md:34-35`). |
| ES-02 | media | E-R2, E-M4 | `overleaf/secciones/capitulo4.tex:204` | "la del modelo con canal se sostiene en parte" | "Con el límite de 0.030, el modelo con canal queda por debajo del modelo evaluado en 9 de 13 pacientes; el modelo con sobremuestreo lo hace en 4 de 13." |
| ES-03 | baja | E-R2 | `overleaf/secciones/capitulo4.tex:208` | "Las direcciones que esos resultados abren se recogen" | "Las evaluaciones que no se ejecutaron se proponen en el capítulo de trabajos futuros." |
| ES-04 | media | E-R2, E-M4 | `overleaf/secciones/capitulo4.tex:232` | "Su caso negativo coincide con la condición que motivó reportar los grupos" | "La concordancia fue menor en los objetos no ortopédicos, que están fuera de la distribución de entrenamiento: el coeficiente de Sørensen-Dice del metal bajó de 0.928 a 0.753." |
| ES-05 | media | E-R2 | `overleaf/secciones/capitulo4.tex:236` | "Lo medido sobre ese realismo es negativo o parcial" | eliminar |
| ES-06 | media | E-R2, E-M4 | `overleaf/secciones/capitulo4.tex:238` | "Los resultados de los Objetivos~2 y~3 son, así, independientes entre sí" | "Por ello, este capítulo evalúa por separado el muestreador y el sintetizador." |

TOTAL alta=0 media=5 baja=1

## Impresion general
Leído de corrido, el capítulo mantiene una voz sobria y presenta resultados densos sin perder sus condiciones de medición. El desajuste dominante aparece en algunos cierres de la discusión: después de cifras precisas, varias frases vuelven a una valoración vaga o metadiscursiva. No se detecta informalidad ni un patrón general de prosa inflada.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una comparación cuantificada cierra con una valoración imprecisa en vez de nombrar la condición observada | E-R2, E-M4 | "la del modelo con canal se sostiene en parte" | nuevo |
| El cierre metadiscursivo anuncia la función de otro capítulo sin precisar el contenido remitido | E-R2 | "Las direcciones que esos resultados abren se recogen" | nuevo |
