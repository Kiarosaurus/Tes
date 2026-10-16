# Revision guia CS — capitulo1 — r10

Entrada: `overleaf/secciones/capitulo1.tex`, lint `capitulo1-r10-lint.md` (PASA; GAP dato=2), respuesta
`capitulo1-r09-respuesta.md` (un RECHAZADO, guia-7, que pedia corregir el cap. 3 y no se reabre), encargo
`redaccion/ENCARGO_2026-10-15c.md`. Fuentes cotejadas: `docs/01-decisiones.md` 2026-10-15 y 2026-10-15 (4),
`experiments/registro/registro_metodos_2026-10-15.md` §1, §6, §8 y §9, fichas `walker2011understanding` y
`lakens2017equivalence`. Para coherencia se leyo `capitulo3.tex` (:413-447, :529-535).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-B4, G-B2, G-T4 | capitulo1.tex:46 | Patron PAT-19 reincide (y PAT-122). El `\GAPDATO` dice que la forma y los parametros de la compresion arcoseno hiperbolico «solo constan en el codigo». El registro §1 los fija ahora: $u=(\operatorname{asinh}(\mathrm{clip}(h,-1000,20000)/s)-a)/(b-a)$, con $s=500$ HU, $a=\operatorname{asinh}(-2)$ y $b=\operatorname{asinh}(40)$. Es la representacion que el sintetizador adopta, asi que sin esa forma el lector no puede verificar los canales del cap. 3. | Retirar la marca y dar la compresion como ecuacion numerada, paralela a la Ec. `eq:ventana`, con $s$, el intervalo de saturacion, la inversa y el rango [0, 1], citando el registro §1 como fuente. Una frase sobre su efecto: resolucion fina cerca de 0 HU y gruesa en el rango alto. Sin la cifra de resultado del Obj 1 (encargo: ya esta en el cap. 3). |
| guia-2 | media | G-T4, G-B2 | capitulo1.tex:134 | Patron PAT-19 reincide (y PAT-168). La oracion «El repositorio no registra con que programa ni con que convencion...» y su `\GAPDATO` quedaron atrasados frente al registro §6 (DEC 2026-10-15 (4) pto 4). Segun el registro, las cuatro cifras (1.000, 0.272, 0.264, 0.109) se reproducen con `scipy.stats.fisher_exact` bilateral (scipy 1.15.3), cuya convencion es la *minlike*. El programa original no consta. | Quitar la marca y reescribir esa oracion: el programa original no consta, pero los cuatro valores coinciden al recalcularlos con la convencion *minlike*, con remision al registro. No atribuir a Fay la conducta de scipy: su ficha solo documenta `fisher.test` de `stats` 2.11.0 (PAT-166, PAT-167). La conducta de scipy se apoya en el registro, no en `\cite{fay2010two}`. |
| guia-3 | media | G-B2, G-B3 | capitulo1.tex:130 (frente a capitulo3.tex:421-423) | DEC 2026-10-15 (4) pto 1 pone en el cap. 1 la definicion de «no concluyente» y la de «a la baja». La primera es el nombre propio de la tesis para «equivalencia no establecida y no equivalencia no demostrada» (Walker y Nowacki). La segunda es la diferencia significativa del escenario B de Lakens. Hoy :130 define los tres desenlaces sin fuente, y la correspondencia esta solo en el metodo (cap. 3 :421-423), que ademas remite a :130 como lugar de la definicion. :130 lee la direccion con el IC90, mientras que Lakens decide la diferencia frente a cero con el IC95, y el marco no lo dice (PAT-165). | Agregar en :130 dos o tres oraciones con `\cite{walker2011understanding}` y `\cite{lakens2017equivalence}`. «No concluyente» es nombre de este trabajo (ninguna ficha usa *inconclusive*: E-R6) para la equivalencia no establecida en que la no equivalencia no puede descartarse. La direccion que informa la regla corresponde al escenario B de Lakens solo si tambien el IC95 excluye el cero. En el cap. 3 queda solo la lectura, con remision, sin repetir el mapeo (PAT-102). |
| guia-4 | baja | G-B2, G-T1 | capitulo1.tex:124 y :132 | Patron PAT-180 reincide. El marco justifica el remuestreo de pacientes solo porque el paciente es la unidad del Obj 1. Ademas, :124 dice que ninguna distribucion del Obj 2 tiene al paciente como unidad. El registro §8 (DEC 2026-10-15 (4) pto 4) añade para la distancia de Wasserstein-1 un IC95 por remuestreo de pacientes, descriptivo, que el cap. 3 incorporara (:531). Con el texto actual, ese uso parece contradecir :124. | Una oracion en :132: en el Obj 2 se remuestrean pacientes con todas sus poses, como bloques, y el intervalo resultante es descriptivo. Remitir a `sec:amenazas`. Sin cifras en el marco. |
| guia-5 | baja | G-B2 | capitulo1.tex:126-140 (frente a capitulo3.tex:441-445) | Patron PAT-129 reincide (afin a PAT-165). El metodo usa y define por primera vez el analisis de acuerdo de Bland y Altman y la prueba de Pitman y Morgan (DEC 2026-10-15 pto 22). El marco estadistico no los nombra, aunque :11 promete reunir los conceptos que el cap. 3 usa sin volver a definirlos. Son analisis descriptivos, por eso la severidad es baja (G-B3 admite citar los auxiliares). | Elegir una de dos salidas. (a) Una oracion en `sec:mt-estadistica` que los nombre como lectura descriptiva de acuerdo y remita a `sec:ap-analisis`. (b) Acotar :11 para que diga que las herramientas descriptivas auxiliares se presentan donde se usan. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple, salvo lo señalado en guia-4 |
| G-T2 | cumple |
| G-T3 | cumple (sin $\alpha$ en :128; notacion de difusion propia en :101 y :110) |
| G-T4 | no cumple (guia-1, guia-2) |
| G-T5 | cumple (orden justificado en :13, coherente con `fig:mt-conceptos`) |
| G-T6 | cumple (lint PASA; `walker2011understanding` y `lakens2017equivalence` estan en `referencias.bib`) |
| G-B1 | cumple |
| G-B2 | no cumple (guia-3, guia-4, guia-5) |
| G-B3 | no cumple (guia-3) |
| G-B4 | no cumple (guia-1: el `\GAPDATO` ya es cerrable con el registro §1) |
| P-MT1 | cumple, salvo guia-1 y guia-3 |
| P-MT2 | cumple (`fig:mt-conceptos` alineada con los objetivos; remision a `fig:pipeline`) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| `\GAPDATO` que un registro de metodos nuevo ya cierra sigue en la seccion | G-T4 | «que solo constan en el código del experimento y no en un registro» | PAT-19 |
| Prosa fuera de la marca que repite el hueco ya cerrado | G-T4 | «El repositorio no registra con qué programa ni con qué convención» | PAT-168 |
| Una DEC asigna una definicion al marco y esta sigue solo en el metodo | G-B2, G-B3 | mapeo Walker/Lakens solo en cap. 3 :421-423 | PAT-165 |
| Uso nuevo de una tecnica del marco (remuestreo en Obj 2) no recotejado contra la unidad declarada | G-B2 | «porque son la unidad de análisis del Objetivo~1» | PAT-180 |

TOTAL alta=0 media=3 baja=2
