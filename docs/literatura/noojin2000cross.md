# noojin2000cross — Geometria transversal del ala sacra para tornillos iliosacros (modelo CT)

- **DOI / URL:** NO ENCONTRADO EN EL PDF (el PDF solo trae la referencia: J Orthop Trauma, Vol. 14, No. 1, pp. 31-35, 2000)
- **Nivel de lectura:** 3 (contexto). Nivel PROPUESTO por Claude, no confirmado por la autora.
- **Leido a fondo por la autora:** no
- **PDF:** papers/noojin2000cross.pdf

## Que hace (3 lineas maximo)
Toma CT pelvicas de 13 pacientes de trauma con pelvis intacta, las reformatea en planos sagitales oblicuos paralelos a la articulacion SI y
busca el corte de menor area del ala sacra (el "sacral pedicle", craneal al primer foramen sacro). Mide la altura y el ancho maximos por
el centro geometrico de ese contorno, y la pendiente alar con goniometro. Informa medias y rangos (sin DE).

## Restriccion o supuesto clave
No es un paper de sintesis generativa. El supuesto clave para esta tesis es que la medida es la extension de un contorno cortical en UN
plano paralelo a la articulacion SI, de UN lado, y no el diametro de un corredor perpendicular al eje del tornillo. Frase: "sagittal
oblique views through the pelvis parallel to the SI joint" (p. 32). Ademas, la seguridad depende de estar en el centro: "must be
positioned in the geometric center of the sacral ala" (p. 31, Conclusion). La caida de dimensiones fuera del centro se afirma, pero no
se cuantifica.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito (solo como contexto, con la advertencia de que no se puede comparar con D_TS)
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| n = 13 (6 F, 7 M) | "thirteen trauma patients averaging thirty-five years of age" / "six females and seven males" | Materials and Methods, pp. 31-32 |
| Ancho medio 28.05 mm (rango 22.10-34) | "was 28.05 millimeters (range 22.10 to 34 millimeters)" | Results, p. 32 |
| Altura media 27.76 mm (rango 22.8-35.9) | "was 27.76 millimeters (range 22.8 to 35.9 millimeters)" | Results, p. 33 |
| Pendiente media 45.08 grados (rango 25-65) | "sacral slope, which ranged from 25 to 65 degrees (mean 45.08" | Results, p. 33 |

## Donde entra en mi tesis
Objetivo 2 (muestreador en S1), como contexto anatomico de la zona segura alar (el "sacral pedicle", craneal al primer foramen sacro,
delimitado por la raiz L5 y los vasos iliacos por delante y por la raiz S1 por detras). Es una definicion cualitativa de la region, no una
fuente operacional para la implicancia #7: no da un diametro de corredor perpendicular al eje, no da una DE, no separa por lado y no
cuantifica cuanto espacio queda fuera del centro. Sus 28 mm no se pueden comparar directamente con el D_TS local (mediana 9.5 mm):
- Plano: el corte es paralelo a la articulacion SI (sagital oblicuo). No es perpendicular al eje de un tornillo iliosacro ni transsacro (p. 32, Fig. 1).
- Magnitud: altura y ancho son extensiones del contorno cortical que pasan por el centro geometrico. No son el diametro maximo inscrito. En un contorno inclinado (pendiente media de 45 grados), el circulo inscrito es menor que la altura y el ancho.
- Alcance: mide un solo nivel (el mas estrecho) de una sola ala, en el tramo del ala entre la articulacion SI y S1. D_TS exige un cilindro continuo a traves de ambas alas y del cuerpo de S1, alineado en los dos lados. Por eso D_TS es, por construccion, menor o igual.
- Inferencia de Claude, no del paper: 28 mm funciona a lo sumo como cota superior de un corte unilateral. Que los numeros sean distintos no indica que haya contradiccion.

## Dudas para el asesor
- Discrepancia interna del PDF. El texto dice "smallest measurements in height and width were 22.1 and 22.9" (p. 33), pero la Tabla 1 (paciente 6) da altura 22.9 y ancho 22.1. Ademas, el rango de altura del texto empieza en 22.8, que en la tabla corresponde al paciente 1. Hay que decidir que valor citar si se cita el minimo.
- Discrepancia en el metodo: los reformateos se hicieron "at three-millimeter intervals" (p. 32), pero tambien "Images were created every two millimeters from the SI joint" (p. 32). El espaciado real no queda claro.
- El paper no dice que lado (izquierdo o derecho) se midio ni si se midieron ambos.
- Conviene saber si una referencia con n = 13, sin DE y con cortes de 5 mm alcanza para citarla como zona segura, o si solo sirve como antecedente historico.

## Respuestas a las preguntas del encargo
1. Definiciones (p. 32). El ala sacra es "that portion of the sacrum between the SI joint and the first vertebral segment". El sacral pedicle es la "junction between the sacral body and the alar wing, cephalad to the first sacral foramen". Plano: reformateo sagital oblicuo "parallel to the SI joint". Se elige la imagen "with the smallest cross-sectional area", se circunscriben los margenes corticales y se miden la altura y el ancho "through the geometric center". La pendiente es el angulo entre una linea vertical y una linea paralela a la cortical anterior del ala (Fig. 4, p. 33; "goniometer", p. 32). El paper no define ningun eje de tornillo como referencia: la unica referencia es el plano paralelo a la articulacion SI y la vertical para la pendiente. No define la orientacion exacta de la altura y el ancho respecto del contorno: NO ENCONTRADO EN EL PDF.
2. Cifras (pp. 32-33 y Tabla 1). Los rangos estan arriba. DE: NO ENCONTRADO EN EL PDF (la Tabla 1 trae los valores individuales). n = 13. Por sexo: "no significant differences ... between males and females" (p. 33), sin valores p ni medias por sexo. Por lado: NO ENCONTRADO EN EL PDF.
3. La caida fuera del centro no se cuantifica (pp. 31 y 35). Ancho util a X mm del centro: NO ENCONTRADO EN EL PDF.
4. No es comparable (ver "Donde entra en mi tesis"). Mide un corte iliosacro unilateral, no un corredor transsacro.
5. Calibre del tornillo: NO ENCONTRADO EN EL PDF. Margen de seguridad: NO ENCONTRADO EN EL PDF. Solo dice que hay "ample cross-sectional area to accommodate two iliosacral lag screws" (p. 35). CT: Philips Tomoscan, cortes de 5 mm, pitch 1.0 (p. 32). Kernel: NO ENCONTRADO EN EL PDF. Umbral de hueso: NO ENCONTRADO EN EL PDF. Contorneo: "circumscribed on the computer" (p. 32). No dice explicitamente si fue manual o automatico: NO ENCONTRADO EN EL PDF.
6. Pacientes: "CT scans of intact pelves" de pacientes de trauma, con edades de 20 a 67 anos (pp. 31-32). Dismorfismo: NO ENCONTRADO EN EL PDF como termino. Solo se cita a Routt: en 3 de 10 cadaveres, el segmento sacro superior estaba al nivel de la densidad cortical iliaca (p. 34).

## Evidencia textual
| Dato | Frase original (<=15 palabras) | Seccion / pagina |
|---|---|---|
| Objetivo | "measure the dimensions of the narrowest portion of the sacral ala" | Abstract, p. 31 |
| n | "Thirteen adult patients underwent pelvic CT imaging." | Abstract, p. 31 |
| Pelvis intactas | "Axial CT scans of intact pelves were reformatted in the sagittal plane" | Abstract, p. 31 |
| Edad media 35, rango 20-67 | "averaging thirty-five years of age (range 20 to 67 years)" | Methods, pp. 31-32 |
| Sexo | "there were six females and seven males" | Methods, p. 32 |
| Corte axial de 5 mm | "original CT scans were made as axial cuts at five-millimeter intervals" | Methods, p. 32 |
| Reformateo cada 3 mm, paralelo a la articulacion SI | "reformatted in the sagittal plane of the sacrum at three-millimeter intervals parallel to the SI joint" (recortada) | Methods, p. 32 |
| Imagenes cada 2 mm (discrepancia) | "Images were created every two millimeters from the SI joint" | Methods, p. 32 |
| Escaner y pitch 1.0 | "Phillips Tomoscan ... set at five-millimeter cut dimensions and a pitch of 1.0" | Methods, p. 32 |
| Definicion del ala sacra | "portion of the sacrum between the SI joint and the first vertebral segment" | Methods, p. 32 |
| Definicion del sacral pedicle | "junction between the sacral body and the alar wing, cephalad to the first sacral foramen" | Methods, p. 32 |
| Criterio de seleccion del corte | "the image with the smallest cross-sectional area was magnified" | Methods, p. 32 |
| Contorneo | "cortical margins of the sacral ala ... were circumscribed on the computer" | Methods, p. 32 |
| Medidas por el centro geometrico | "height, width, and slope) through the geometric center of this narrow portion" | Methods, p. 32 |
| Metodo de la pendiente | "goniometer positioned vertically and parallel to the anterior portion of the sacral ala" | Methods, p. 32 |
| Definicion de la pendiente (figura) | "angle was measured between a line drawn vertically and a second line" | Fig. 4, p. 33 |
| Ancho medio 28.05 mm | "was 28.05 millimeters (range 22.10 to 34 millimeters)" | Results, p. 32 |
| Altura media 27.76 mm | "was 27.76 millimeters (range 22.8 to 35.9 millimeters)" | Results, p. 33 |
| Pendiente de 25-65 grados, media 45.08 | "sacral slope, which ranged from 25 to 65 degrees (mean 45.08 degrees)" | Results, p. 33 |
| Localizacion constante | "narrowest portion ... occurred at the junction between the sacral body and the alar wings" | Results, p. 33 |
| Sin diferencias por sexo, talla ni peso | "no significant differences in alar height, width, or slope between males and females" | Results, p. 33 |
| Minimos 22.1 / 22.9 mm (discrepancia con Tabla 1) | "smallest measurements in height and width were 22.1 and 22.9 millimeters" | Results, p. 33 |
| Valores individuales (Tabla 1): altura, ancho y pendiente de los pacientes 1-13 | "Sacral alar measurements for the individual patients studied" | Tabla 1, p. 33 |
| Ejemplo de la Fig. 3 (paciente 13): 35.9 x 23.4 mm | "35.9 mm" / "23.4 mm" (rotulos de la figura) | Fig. 3, p. 33 |
| Limites anatomicos del pedicle | "bounded by the fifth lumbar (L5) nerve root and iliac vessels anteriorly" | Discussion, p. 33 |
| Limite posterior | "the first sacral (S1) nerve root posteriorly and caudad" | Discussion, p. 33 |
| Trayectoria requerida | "must pass through the outer table of the ilium and traverse through the sacral ala" | Discussion, p. 33 |
| Caida fuera del centro (no cuantificada) | "outside the geometric center there was a sharp decrease in height and width" | Abstract, p. 31 |
| Criterio de seguridad | "must be positioned in the geometric center of the sacral ala" | Abstract, p. 31 |
| Capacidad para dos tornillos | "ample cross-sectional area to accommodate two iliosacral lag screws if correctly positioned" | Discussion, p. 35 |
| Jackson y McManus: ancho de alrededor de 28 mm | "average width twenty-eight millimeters) were similar to ours" | Discussion, p. 34 |
| Routt: 7/10 cadaveres con anatomia normal | "seven of ten cadavers displayed \"normal\" sacral alar anatomy" | Discussion, p. 34 |
| Routt: 3/10 con anatomia distinta | "three of ten cadavers had different anatomy" | Discussion, p. 34 |
| Routt: 1 lesion de L5 en 52 pacientes | "one L5 nerve root injury among fifty-two patients" | Discussion, p. 34 |
| Tasa de 3.8% | "There was a 3.8 percent rate of screw-related problems" | Discussion, p. 34 |
| Reduccion abierta en 17/63 (27%) | "open reduction was required for seventeen out of sixty-three (27 percent)" | Discussion, p. 34 |
| Mortalidad de 10-20% (contexto) | "still ranges from 10 to 20 percent" | Introduction, p. 31 |
| Raf: 52% | "Raf reported that 52 percent of patients" | Introduction, p. 31 |
| Tile: 60% | "Tile reported that 60 percent of the patients" | Introduction, p. 31 |
| Holdsworth: 12/27 y 2/15 | "only twelve of twenty-seven ... only two of fifteen" | Introduction, p. 31 |
| Prioridad declarada | "the first to use CT imaging in the sagittal plane" | Discussion, p. 35 |
| DE de las medidas | NO ENCONTRADO EN EL PDF | — |
| Lado medido | NO ENCONTRADO EN EL PDF | — |
| Kernel de reconstruccion | NO ENCONTRADO EN EL PDF | — |
| Umbral de hueso (HU) | NO ENCONTRADO EN EL PDF | — |
| Calibre del tornillo o margen de seguridad | NO ENCONTRADO EN EL PDF | — |

## Candidatos de snowballing
| Cita tal como aparece | N. ref | Por que |
|---|---|---|
| Jackson RP, McManus AC. The iliac buttress: a computed tomographic study of sacral anatomy. Spine 1993;18:1318-1328. | 4 | Mide por CT (n = 50) las masas sacras laterales para colocar barras trans-sacras. Reporta diferencias entre lados y por sexo. |
| Routt ML, Simonian PT, Agnew SG, Mann FA. Radiographic recognition of the sacral alar slope for optimal placement of iliosacral lag screws: a cadaveric and clinical study. J Orthop Trauma 1996;10:171-177. | 17 | Fuente original de la "safe zone" alar, craneal al primer foramen sacro. Describe variantes anatomicas (3/10). Es radiografica, no CT. |
