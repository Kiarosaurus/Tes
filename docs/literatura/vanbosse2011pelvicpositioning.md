# vanbosse2011pelvicpositioning — Posicionamiento pelvico crea error en mediciones acetabulares por CT

- **DOI / URL:** 10.1007/s11999-011-1827-9 (Clin Orthop Relat Res 2011;469:1683-1691)
- **Nivel de lectura:** 3 (contexto) — ver seccion "Verificacion de nivel"
- **Leido a fondo por la autora:** no
- **PDF:** papers/vanbosse2011pelvicpositioning.pdf

## Que hace (3 lineas maximo)
Monta un modelo radiopaco de pelvis (Sawbones) en un marco ajustable dentro de un CT y varia oblicuidad, rotacion y tilt pelvicos en incrementos de 5°, de -20° a 20°.
Mide en cada pose cuatro variables acetabulares angulares (anteversion AA por dos referencias, y los angulos de sector AASA, PASA, HASA) y cuantifica cuanto cambian respecto a la posicion anatomica de McKibbin.
Concluye que oblicuidad y tilt producen cambios lineales y aditivos en esas mediciones, que la rotacion no tiene efecto, y publica ecuaciones predictivas del cambio.

## Restriccion o supuesto clave
No es un paper de sintesis generativa. Su supuesto limitante para esta tesis es que **todo lo medido es angular y relativo, no absoluto**: "All acetabular variable measurements were recorded as the variance from the measurement obtained at the anatomic position defined by McKibbin" (Materials and Methods, p. 1685), y "we report on the change in those variables, not their absolute measurements" (Discussion, p. 1686). Ademas usa un solo modelo de pelvis sin tejidos blandos y sin implante metalico: "we used one pelvis model, rather than several different human pelves" (Discussion, p. 1686). No dice nada sobre metal, artefacto, ni sobre posicion de tornillos dentro del volumen.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Umbral de error aceptable: ±3° | "We defined an acceptable measurement error as +/- 3° variance" | Materials and Methods, p. 1686 |
| Por cada 1° de oblicuidad, AA cambia -0.4° | "For each 1°-increase in pelvic obliquity, AA changed -0.4°" | Abstract, p. 1683 |
| Por cada 1° de tilt, AA cambia 0.8° | "For each 1°-increase in pelvic tilt, AA changed 0.8°" | Abstract, p. 1683 |
| Rotacion pelvica: sin efecto | "Rotation had no affect on the variables." | Abstract, p. 1683 |
| Marco anatomico de referencia (McKibbin) | "the top of the symphysis pubis in the same vertical plane as the anterior superior spine" | Discussion, p. 1686 |
| Rango de poses evaluado: -20° a 20°, pasos de 5° | "varied by increments of 5°, from -20° to 20°" | Materials and Methods, p. 1685 |
| 5° de oblicuidad = 15-20 mm de diferencia de altura de cresta iliaca | "5° pelvic obliquity translates into 15- to 20-mm height difference between the iliac crest" | Discussion, p. 1689 |

## Donde entra en mi tesis
Solo como caveat metodologico de redaccion, en la seccion donde se define el marco de coordenadas en que se reporta la pose 3D del implante. Justifica declarar explicitamente que la pose se reporta en el marco del CT (voxel/escaner) y no en un marco anatomico normalizado, y que cualquier metrica angular referida a la anatomia (si SAP llegara a usar angulos acetabulares o de version) heredaria sensibilidad al posicionamiento del paciente. No aporta cifras para SAP, BFC ni ISC, ni tasas de malposicion.

## Dudas para el asesor
- La pose del implante en MetalSynth-Pelvis se reporta en el marco del CT. Si en algun momento se reporta en un marco anatomico (p. ej. plano pelvico anterior), habria que adoptar una definicion reproducible; este paper ofrece la de McKibbin. Vale la pena fijar eso ahora o dejarlo en el marco del CT?
- SAP evalua admisibilidad quirurgica: incluira algun criterio angular referido a la anatomia pelvica? Si si, este paper aporta el umbral de ±3° como orden de magnitud de tolerancia clinica en mediciones acetabulares; si no, el paper no toca la metrica.

## Evidencia textual

| Cifra / umbral / definicion / criterio | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Los dos metodos de medir AA difieren 1° a 4° | "yielded values differing by 1° to 4° but correlated (r = 0.981)" | Abstract, p. 1683 |
| Correlacion entre metodos r = 0.981 | "otherwise were correlated (r = 0.981) across the spectrum of pelvis positioning" | Results, p. 1686 |
| Por 1° de oblicuidad: AA -0.4°; AASA 1.93°; PASA 0.99°; HASA 2.80° | "AA changed -0.4°, and AASA, PASA, and HASA changed 1.93°, 0.99°, and 2.80°" | Abstract, p. 1683 |
| Por 1° de tilt: AA 0.8°; AASA -1.07°; PASA 0.52°; HASA -0.51° | "AA changed 0.8°, and AASA, PASA, and HASA changed -1.07°, 0.52°, and -0.51°" | Abstract, p. 1683 |
| Por 1° de oblicuidad AA disminuye ~0.4° (p<0.001) | "measured AAIschial and AAFemoral decreased (p < 0.001) by approximately 0.4°" | Results, p. 1686 |
| Por 1° de tilt: AA_Femoral 0.77°, AA_Ischial 0.75° | "AAFemoral changed 0.77° and AAIschial changed 0.75° (p < 0.001...)" | Results, pp. 1686-1687 |
| Error de medicion aceptable definido: ±3° | "We defined an acceptable measurement error as +/- 3° variance" | Materials and Methods, p. 1686 |
| Oblicuidad maxima admisible para AA: menos de 7° | "would require keeping the obliquity less than 7°" | Results, p. 1686 |
| Tilt maximo admisible para AA: menos de 4° | "would require keeping the tilt at less than 4°" | Results, p. 1687 |
| Oblicuidad maxima admisible: AASA ±1.6°, PASA ±3.0°, HASA ±1.1° | "would occur for an obliquity of +/- 1.6°, 3.0°, and 1.1°, respectively" | Results, p. 1686 |
| Tilt maximo admisible: AASA ±2.8°, PASA ±5.8°, HASA ±5.9° | "would occur for a tilt of +/- 2.8°, 5.8°, and 5.9°, respectively" | Results, p. 1687 |
| Tabla 1, cambio admisible AA_I: oblicuidad ±6.8°, tilt ±3.9° | "AAI ... Obliquity +/- 6.8° ... Tilt +/- 3.9°" | Table 1, p. 1687 |
| Tabla 1, cambio admisible AA_F: oblicuidad ±7.1°, tilt ±4.0° | "AAF ... Obliquity +/- 7.1° ... Tilt +/- 4.0°" | Table 1, p. 1687 |
| Tabla 1, cambio admisible AASA: oblicuidad ±1.6°, tilt ±2.8° | "AASA ... Obliquity +/- 1.6° ... Tilt +/- 2.8°" | Table 1, p. 1687 |
| Tabla 1, cambio admisible PASA: oblicuidad ±3.0°, tilt ±5.8° | "PASA ... Obliquity +/- 3.0° ... Tilt +/- 5.8°" | Table 1, p. 1687 |
| Tabla 1, cambio admisible HASA: oblicuidad ±1.1°, tilt ±5.9° | "HASA ... Obliquity +/- 1.1° ... Tilt +/- 5.9°" | Table 1, p. 1687 |
| Valores en posicion anatomica: AA_I 28°, AA_F 24°, AASA 67°, PASA 115°, HASA 182° | "AAI 28° ... AAF 24° ... AASA 67° ... PASA 115° ... HASA 182°" | Table 1, p. 1687 |
| Rangos netos observados: AA_I 51°, AA_F 48°, AASA 95°, PASA 55°, HASA 132° | "-7° to 44° (51°) ... -5° to 43° (48°) ... 41° to 136° (95°)" | Table 1, p. 1687 |
| Tilt explica 62% de la varianza de AA | "It was responsible for 62% of the observed measurement variance for AA." | Results, p. 1686 |
| Contribucion de varianza por tilt: AA_I 62.0%, AA_F 65.1% | "Tilt 62.0 <0.0001 ... Tilt 65.1 <0.0001" | Table 1, p. 1687 |
| Contribucion de varianza por oblicuidad: AA_I 11.5%, AA_F 10.4%, AASA 41.1%, PASA 39.7%, HASA 53.7% | "Obliquity 11.5 ... 10.4 ... 41.1 ... 39.7 ... 53.7" | Table 1, p. 1687 |
| Rotacion: contribucion de varianza 0.0-0.8%, no significativa (p 0.93, 0.70, 0.55, 0.0538, 0.18) | "Rotation 0.0 0.93 NS" | Table 1, p. 1687 |
| Rotacion pelvica no afecta AA ni angulos de sector | "Changing pelvic rotation had no effect on the AAs measured." | Results, p. 1686 |
| Ecuaciones predictivas AA_I y AA_F | "-0.44 x obliquity (°) + 0.75 x tilt (°) = dAAIschial" | Table 2, p. 1688 |
| Ecuaciones predictivas AASA, PASA, HASA | "1.93 x obliquity (°) - 1.07 x tilt (°) = dAASA" | Table 2, p. 1688 |
| Protocolo de variacion: pasos de 5°, de -20° a 20° | "varied by increments of 5°, from -20° to 20°" | Materials and Methods, p. 1685 |
| Adquisicion: cortes cada 3 mm, GE HiSpeed Advantage RP spiral | "CT images ... obtained at 3-mm increments using a GE HiSpeed Advantage RP spiral scanner" | Materials and Methods, p. 1685 |
| 729 combinaciones posibles de variables orientacionales | "A total of 729 combinations of orientational variables were possible." | Materials and Methods, p. 1685 |
| Solo 369 secuencias necesarias por simetria de signo | "only 369 sequences needed to be completed to create all the combinations" | Materials and Methods, p. 1685 |
| Muestra final: 182 secuencias, 324 posiciones acetabulares | "A total of 182 sequences (324 acetabular positions) met the criteria" | Results, p. 1686 |
| Un solo observador realizo las mediciones | "One of us (HvB) measured AA, AASA, PASA, and HASA for each sequence." | Materials and Methods, p. 1686 |
| Modelo: pelvis radiopaca Sawbones, no paciente real | "We mounted a radiopaque model of a human pelvis (Sawbones, Vashon, WA, USA)" | Materials and Methods, p. 1684 |
| Definicion de posicion anatomica (McKibbin) | "the top of the symphysis pubis in the same vertical plane as the anterior superior spine" | Discussion, p. 1686 |
| Convencion de signo de oblicuidad | "the hemipelvis that moved cephalad moved in a positive direction" | Results/Fig. 2 text, p. 1685 |
| Convencion de signo de tilt | "positive direction was defined as tilting the superior pelvis anteriorly (pelvic extension)" | p. 1685 |
| Convencion de signo de rotacion | "the hemipelvis that moved anteriorly moved in a positive direction" | p. 1685 |
| Mediciones registradas como varianza, no valor absoluto | "recorded as the variance from the measurement obtained at the anatomic position" | Materials and Methods, p. 1685 |
| AA por cabezas femorales da valores 1° a 4° menores que por isquion | "using the center of the femoral heads as a baseline ... yielded 1° to 4° smaller values" | Discussion, p. 1689 |
| Malorientacion de 10° tilt y 5° oblicuidad: AA 10°, AASA 20°, PASA 10° | "malorientation of 10° tilt and 5° obliquity would alter acetabular anteversion by 10°" | Discussion, p. 1689 |
| 5° de oblicuidad = 15-20 mm de diferencia de altura de cresta iliaca | "5° pelvic obliquity translates into 15- to 20-mm height difference between the iliac crest" | Discussion, p. 1689 |
| 5° de oblicuidad cambia AASA ~10° y HASA 14° | "would change the AASA by nearly 10° and the HASA by 14°" | Discussion, p. 1689 |
| Cambios pequenos de orientacion considerados: 5°-10° | "small (eg, 5°-10°) changes in pelvic orientation were related to statistically significant changes" | Discussion, p. 1689 |
| Reproducibilidad intraobservador reportada por terceros: 95% dentro de 3.5° | "a 95% intraobserver reproducibility within 3.5° for acetabular anteversion" | Discussion, p. 1686 (cita [27]) |
| ICC intraobservador 0.79-0.87 (terceros) | "intraobserver intraclass coefficients (ICC) ranging from 0.79 and 0.87" | Discussion, p. 1686 (cita [23]) |
| ICC interobservador medio 0.96 (terceros) | "mean interobserver ICC of 0.96 for measures including acetabular anteversion" | Discussion, p. 1686 (cita [13]) |
| Tilt pelvico de pie: 4° a 7° mas posterior que supino (terceros) | "tilted posteriorly ... on average between 4° and 7° compared with the supine position" | Discussion, p. 1688 |
| Variabilidad intersujeto de tilt: 25° de pie, 26° supino (terceros) | "intersubject pelvic tilt measurements ranged 25° for standing and 26° for supine" | Discussion, p. 1688 (cita [14]) |
| Rango de tilt supino -17° a 3°, de pie -27° a 3° (terceros) | "range of supine pelvic tilt from -17° to 3°, and standing ... -27° to 3°" | Discussion, p. 1688 (cita [32]) |
| Variabilidad de tilt >60° en un estudio (terceros) | "ranging greater than 60° in one study" | Discussion, p. 1688 (cita [39]) |
| Aumento de 15° en AA de pie a acostado con 20° de extension pelvica (terceros) | "increase in measured acetabular anteversion of 15° when going from simulated standing" | Discussion, p. 1689 (cita [61]) |
| AA aumenta 0.5°-0.7° por cada 1° de tilt (terceros) | "between 0.5° and 0.7° for every 1° of pelvic tilt" | Discussion, p. 1689 |
| Anda: 0.5° en anteversion y 0.7° en angulos de sector por 1° de tilt (terceros) | "change of 0.5° in anteversion and 0.7° in acetabular sector angles for every 1°-change" | Introduction, p. 1684 |
| Anda: AASA y PASA cambian 0.7° y -0.5° por 1° de tilt (terceros) | "proportionally changed AASA and PASA by 0.7° and -0.5°, respectively" | Discussion, p. 1689 |
| Abel: AA disminuyo 30° entre 15° de tilt posterior y 35° anterior (terceros) | "anteversion decreased 30° as pelvic tilt was varied from 15° posterior to 35° anterior" | Introduction, p. 1684 |
| Tonnis: grados en incrementos de 5°, Grado 1 (normal) 15°-20° | "categorized acetabular anteversion in 5°-increments, starting with Grade 1 (normal) at 15° to 20°" | Discussion, p. 1689 (cita [52]) |
| Tonnis: Grado -2 = 10°-14°, Grado 2 = 21°-25° | "from Grade -2 (10°-14°) to Grade 2 (21°-25°)" | Discussion, p. 1689 |
| Anda: rango normal de AASA 48° a 75° (terceros) | "the normal range for AASA was 48° to 75°" | Discussion, p. 1689 (cita [7]) |
| Anda: diferencia dysplasico vs normal 16° en AASA y 30° en HASA (terceros) | "the mean AASAs for dysplastic and normal hips was 16°, and 30° for HASAs" | Discussion, p. 1689 |
| Tsumura: transposicion optima dentro de 5° (terceros) | "transposing the acetabular fragment to within 5° of the optimal transposition point" | Introduction, p. 1684 (cita [55]) |
| Supervivencia 72% a 87% a 9 anos o mas (terceros) | "report survival rates of 72% to 87% at 9 years or greater" | Introduction, p. 1684 |
| Thawrani: Tonnis grado 0 pasa de 11% preop a 41% (terceros) | "increased from 11% preoperatively to 41% at greater than 2 years" | Introduction, p. 1684 (cita [50]) |
| Criterio de exclusion de secuencias | "some measurements could not be made owing to the absence of the required anatomy" | Results, p. 1685-1686 |
| Analisis estadistico: Pearson r y regresion multiple, SPSS 10.0 | "using the Pearson Product Moment Correlation Coefficient (r)" / "multiple regression analysis (SPSS 10.0" | Materials and Methods, p. 1686 |

## Verificacion de nivel

Criterio de la autora: Nivel 1 = critico; Nivel 2 = afecta la redaccion; Nivel 3 = apoyo.
Clasificacion vigente: NIVEL 2, promovido desde 3 sin leer el PDF.

**1. Cuanto error de medicion reporta, en grados o milimetros, y para que magnitud?**
Todo el error reportado esta en **grados** y todo corresponde a **variables acetabulares angulares**: anteversion acetabular (AA, con dos referencias: AA_Ischial y AA_Femoral) y los tres angulos de sector (AASA anterior, PASA posterior, HASA horizontal). El HASA/AASA es lo que el paper usa como proxy de cobertura acetabular.
- Oblicuidad: "For each 1°-increase in pelvic obliquity, AA changed -0.4°, and AASA, PASA, and HASA changed 1.93°, 0.99°, and 2.80°, respectively" (Abstract, p. 1683).
- Tilt: "For each 1°-increase in pelvic tilt, AA changed 0.8°, and AASA, PASA, and HASA changed -1.07°, 0.52°, and -0.51°, respectively" (Abstract, p. 1683). En Results desagrega: "AAFemoral changed 0.77° and AAIschial changed 0.75°" (pp. 1686-1687).
- Entre metodos de medir AA: "yielded values differing by 1° to 4° but correlated (r = 0.981)" (Abstract, p. 1683).
- Rangos totales de variacion observados sobre todo el barrido (Table 1, p. 1687): AA_I 51°, AA_F 48°, AASA 95°, PASA 55°, HASA 132° de rango neto.
- Caso compuesto (Discussion, p. 1689): "malorientation of 10° tilt and 5° obliquity would alter acetabular anteversion by 10°, AASA by 20°, and PASA by 10°".
- Unica cifra en milimetros del paper, y no es un error de medicion sino una equivalencia de posicionamiento: "For an average adult pelvis, 5° pelvic obliquity translates into 15- to 20-mm height difference between the iliac crest" (Discussion, p. 1689).
No hay ninguna cifra de error en milimetros sobre distancias medidas dentro del volumen: NO ENCONTRADO EN EL PDF.

**2. Que rango de inclinacion o rotacion pelvica produce ese error?**
- Rango barrido experimentalmente: "The orientational variables were varied by increments of 5°, from -20° to 20°" (Materials and Methods, p. 1685).
- Umbral de tolerancia definido: "We defined an acceptable measurement error as +/- 3° variance from the value at the anatomic position" (Materials and Methods, p. 1686).
- Rangos maximos de malposicion tolerables para no exceder ±3° (Table 1, p. 1687): oblicuidad ±6.8° (AA_I), ±7.1° (AA_F), ±1.6° (AASA), ±3.0° (PASA), ±1.1° (HASA); tilt ±3.9° (AA_I), ±4.0° (AA_F), ±2.8° (AASA), ±5.8° (PASA), ±5.9° (HASA).
- En texto: "would require keeping the obliquity less than 7°" (Results, p. 1686) y "keeping the tilt at less than 4°" (Results, p. 1687).
- Rotacion: no produce error en ningun rango evaluado. "Changing pelvic rotation had no effect on the AAs measured" (Results, p. 1686); Table 1 da contribuciones de varianza de 0.0-0.8% con p = 0.93, 0.70, 0.55, 0.0538, 0.18.
- El paper senala que el rango clinicamente plausible que motiva el problema es 5°-10°: "small (eg, 5°-10°) changes in pelvic orientation were related to statistically significant changes" (Discussion, p. 1689).

**3. Angular acetabular, o tambien distancias y posiciones absolutas dentro del volumen?**
**Solo angular acetabular, y explicitamente relativo, no absoluto.** Es la respuesta decisiva para esta tesis. Evidencia:
- "All acetabular variable measurements were recorded as the variance from the measurement obtained at the anatomic position defined by McKibbin" (Materials and Methods, p. 1685).
- "they are not an absolute number, but were instead the amount of change attributable to the pelvic positioning" (Materials and Methods, p. 1685).
- "we report on the change in those variables, not their absolute measurements" (Discussion, p. 1686).
- Y sobre la rotacion, el paper razona que reorientar la pelvis equivale a reorientar el corte, sin alterar la geometria real: "as the pelvis rotates, it would be as if rotating the CT scan slice, but not changing the actual view of the pelvis" (Discussion, p. 1689).
El paper **no reporta ningun error sobre distancias, longitudes, ni posiciones absolutas de puntos dentro del volumen CT**: NO ENCONTRADO EN EL PDF. El mecanismo que describe es que el plano transverso del escaner deja de coincidir con el plano anatomico, de modo que un angulo medido *sobre el corte* cambia. Una pose rigida (posicion + orientacion) de un tornillo expresada en el marco del CT no se ve afectada por este mecanismo, porque hueso e implante rotan juntos dentro del mismo volumen.

**4. Propone correccion, normalizacion o marco de referencia anatomico reproducible?**
Si, tres cosas, en orden de utilidad para definir el marco de la pose:
- **Definicion de posicion anatomica de McKibbin**, que el paper adopta como cero: "the top of the symphysis pubis in the same vertical plane as the anterior superior spine" (Discussion, p. 1686); operacionalizada en Methods como "the top of the symphysis pubis in the same coronal plane as the anterior-superior iliac spines, and the anterior-superior iliac spines in the same transverse plane" (p. 1684). Esto **si es material reutilizable**: define un marco anatomico a partir de tres landmarks oseos identificables en CT (sinfisis pubica y ambas EIAS).
- **Ecuaciones de correccion** en Table 2 (p. 1688), lineales y aditivas en oblicuidad y tilt, una por variable acetabular. Aplican solo a las cinco variables angulares del paper, no a poses.
- **Tecnicas de estandarizacion citadas de terceros**: inclinometro sobre la pelvis, ultrasonido para el espesor de partes blandas, radiografia lateral "shoot-through" en la mesa del CT, y "obtaining a three-dimensional CT scan so that the reconstructed pelvis can be reoriented anatomically before making measurements" (Discussion, p. 1689). Esta ultima es la mas directamente aplicable: reorientar el volumen 3D al marco anatomico antes de medir.

**5. CT real, fantoma o simulacion? Tamano de muestra?**
Fantoma fisico escaneado en CT real. "We mounted a radiopaque model of a human pelvis (Sawbones, Vashon, WA, USA) on a frame in a CT scanner" (Methods, p. 1684); escaner GE HiSpeed Advantage RP spiral, cortes de 3 mm (p. 1685). **N = 1 modelo de pelvis**, reconocido como limitacion: "we used one pelvis model, rather than several different human pelves" (Discussion, p. 1686). Sin pacientes, sin tejidos blandos ("The CT images were made from a model without soft tissues", p. 1686), sin implante metalico. Un solo observador: "One of us (HvB) measured AA, AASA, PASA, and HASA" (p. 1686). Unidades analizadas: 729 combinaciones posibles, 369 secuencias necesarias, 182 secuencias / 324 posiciones acetabulares utilizables (pp. 1685-1686).

**6. Nivel que sostiene la evidencia**
**NIVEL 3.** El PDF no sostiene el nivel 2 tal como fue justificado. La justificacion previa asumia que el error de posicionamiento contamina la pose 3D medida en el marco del CT; el paper demuestra algo mas estrecho: que **angulos acetabulares medidos sobre cortes transversos** cambian cuando el plano del escaner no coincide con el plano anatomico, y lo reporta siempre como cambio relativo, nunca como error absoluto de posicion. Nada de eso alcanza la pose rigida de un tornillo dentro del volumen, ni BFC (brecha cortical, una medida local hueso-implante en el mismo volumen), ni ISC.
Matiz honesto: hay **un unico elemento** de valor nivel-2, y no son las cifras de error sino la definicion de McKibbin y la sugerencia de reorientar el volumen 3D antes de medir. Si la tesis decidiera reportar la pose en un marco anatomico pelvico en vez del marco del CT, ese material seria citable en metodo. Mientras la pose se reporte en el marco del CT, el paper es **apoyo de discusion**: sirve para justificar por escrito *por que* se eligio el marco del CT y no uno anatomico, en una o dos frases.
Recomendacion: **degradar a NIVEL 3**, conservando la cita para una nota de discusion sobre eleccion de marco de coordenadas.

## Candidatos de snowballing detectados

| Cita como aparece en el PDF | Por que podria importar |
|---|---|
| [36] McKibbin B. Anatomical factors in the stability of the hip joint in the newborn. J Bone Joint Surg Br. 1970;52:148-159. | Fuente original de la definicion de posicion anatomica pelvica usada como cero en este paper; es el unico marco de referencia anatomico reproducible citable si la tesis normaliza la pose fuera del marco del CT. |
| [4] Anda S, Svenningsen S, Dale LG, Benum P. The acetabular sector angle of the adult hip determined by computed tomography. Acta Radiol Diagn. 1986;27:443-447. | Fuente original de la definicion y de los rangos normativos de los angulos de sector acetabular (AASA/PASA/HASA), umbrales citables. |
| [7] Anda S, Terjesen T, Kvistad KA, Svenningsen S. Acetabular angles and femoral anteversion in dysplastic hips in adults: CT investigation. J Comput Assist Tomogr. 1991;15:115-120. | Fuente del rango normal AASA 48°-75° y de las diferencias dysplasico/normal (16° AASA, 30° HASA); umbrales de admisibilidad anatomica potencialmente utiles para SAP. |
| [52] Tonnis D, Heinecke A. Acetabular and femoral anteversion: relationship with osteoarthritis of the hip. J Bone Joint Surg Am. 1999;81:1747-1770. | Fuente original de la escala graduada de anteversion en incrementos de 5° (Grado 1 normal 15°-20°); escala clinica citable con umbrales explicitos. |
| [55] Tsumura H, Kaku N, Ikeda S, Torisu T. A computer simulation of rotational acetabular osteotomy... J Orthop Sci. 2005;10:145-151. | Simulacion computacional que define un "punto optimo de transposicion" con tolerancia de 5°; metodo de optimizacion de colocacion que compite conceptualmente con el muestreador y aporta un umbral de admisibilidad. |
| [27] Kim SS, Frick SL, Wenger DR. Anteversion of the acetabulum in developmental dysplasia of the hip: analysis with computed tomography. J Pediatr Orthop. 1999;19:438-442. | Fuente de la reproducibilidad intraobservador (95% dentro de 3.5°); referencia de ruido de medicion humana, util como piso de tolerancia para validar metricas geometricas. |
| [23] Jacobsen S, Romer L, Soballe K. Degeneration in dysplastic hips: a computer tomography study. Skeletal Radiol. 2005;34:778-784. | Fuente de los ICC intraobservador 0.79-0.87 para AASA/PASA/HASA/AA; estadistico de acuerdo citable para validar concordancia de metricas. |
| [13] Dandachli W, Kannan V, Richards R, Shah Z, Hall-Craggs M, Witt J. Analysis of cover of the femoral head in normal and dysplastic hips: new CT-based technique. J Bone Joint Surg Br. 2008;90:1428-1434. | Metrica de cobertura femoral basada en CT 3D con ICC interobservador 0.96; metrica geometrica alternativa que podria informar el diseno de una medida tipo BFC/ISC. |
| [1] Abel MF, Sutherland DH, Wenger DR, Mubarak SJ. Evaluation of CT scans and 3-D reformatted images for quantitative assessment of the hip. J Pediatr Orthop. 1994;14:48-53. | Fuente de la cifra de 30° de cambio en anteversion por variacion de tilt, y del metodo de reorientar el volumen 3D antes de medir; relevante para definir marco de pose. |
| [14] Eddine TA, Migaud H, Chantelot C, Cotten A, Fontaine C, Duquennoy A. Variations of pelvic anteversion in the lying and standing positions... Surg Radiol Anat. 2001;23:105-110. | Fuente de la variabilidad intersujeto de tilt pelvico (25° de pie, 26° supino) y de la radiografia lateral en mesa de CT; cuantifica el rango real de malposicion en poblacion. |
| [32] Lembeck B, Mueller O, Reize P, Wuelker N. Pelvic tilt makes acetabular cup navigation inaccurate. Acta Orthop. 2005;76:517-523. | Reporta rangos de tilt supino (-17° a 3°) y de pie (-27° a 3°) y documenta el impacto sobre navegacion de implantes; es el caso mas cercano a "malposicion de implante por error de referencia". |
| [61] Zilber S, Lazennec JY, Gorin M, Saillant G. Variations of caudal, central, and cranial acetabular anteversion according to the tilt of the pelvis. Surg Radiol Anat. 2004;26:462-465. | Fuente del aumento de 15° en anteversion medida con 20° de extension pelvica; cifra original de sensibilidad al tilt. |
| [39] Nishihara S, Sugano N, Nishii T, Ohzono K, Yoshikawa H. Measurements of pelvic flexion angle using three-dimensional computed tomography. Clin Orthop Relat Res. 2003;411:140-151. | Metodo de medicion de angulo de flexion pelvica sobre CT 3D y fuente del rango >60° de variabilidad; metodo candidato para normalizar orientacion pelvica en un pipeline automatico. |
| [44] Salter RB, Dubos JP. The first fifteen year's personal experience with innominate osteotomy... Clin Orthop Relat Res. 1974;98:72-103. | Fuente del criterio para localizar el centro de la cabeza femoral (corte donde es mayor y mas circular); criterio operativo de landmarking reproducible. |
| [50] Thawrani D, Sucato DJ, Podeszwa DA, DeLaRocha A. Complications associated with the Bernese periacetabular osteotomy for hip dysplasia in adolescents. J Bone Joint Surg Am. 2010;92:1707-1714. | Reporta tasas clinicas (11% a 41% Tonnis grado 0) y complicaciones de un procedimiento de reorientacion; posible fuente de tasas de resultado subotimo. |
| [54] Trousdale RT, Cabanela ME. Lessons learned after more than 250 periacetabular osteotomies. Acta Orthop Scand. 2003;74:119-126. | Serie clinica grande citada como evidencia de que la malposicion produce malos resultados; posible fuente de tasa de malposicion. |
