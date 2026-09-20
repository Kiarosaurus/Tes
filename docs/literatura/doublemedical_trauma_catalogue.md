# doublemedical_trauma_catalogue — Double Medical, Trauma Catalogue (Edition 2021)

**Profundidad: documentacion tecnica del fabricante, no revisada por pares; lectura dirigida a la seccion de tornillos canulados**

- **DOI / URL:** NO ENCONTRADO EN EL PDF
- **Nivel de lectura:** 3 (contexto)
- **Leido a fondo por la autora:** no
- **PDF:** papers/Double Medical - Trauma Catlogue 2021-2-18.pdf

## Nota de lectura y de forma

Catalogo comercial de 305 paginas de PDF (cada pagina de PDF contiene dos paginas
impresas, salvo portada, indice, portadillas de seccion y la ultima). La numeracion
impresa es **por seccion** (`5/6` = seccion 5, pagina 6), no correlativa. Por eso toda
cita de abajo lleva **pagina impresa + pagina del PDF**.

**Las tablas no son texto extraible:** una busqueda de la cadena `Cannulated` sobre el
archivo no devuelve ninguna coincidencia, y las paginas se leyeron como imagen
renderizada. Todo lo transcrito aqui se leyo sin ambiguedad en el render; donde el
render deja duda, se marca. Se leyeron **solo** la portada, el indice y la seccion 5
(`Cannulated Screw Set`); placas, clavos, fijadores y el resto del catalogo no se
revisaron.

## Datos bibliograficos

| Campo | Valor | Frase / celda textual | Pagina impresa | Pagina PDF |
|---|---|---|---|---|
| Titulo impreso | Trauma Catalogue | *"Trauma Catalogue"* | portada (sin numero) | 1 |
| Fabricante | Double Medical | *"DOUBLE MEDICAL"* (logo) y *"Dedicated to Rehabilitation"* | portada | 1 |
| Ano / edicion | Edition 2021 | *"Edition 2021"* | portada | 1 |
| Codigo de catalogo | NO ENCONTRADO EN EL PDF | — | — | — |
| Copyright | NO ENCONTRADO EN EL PDF | — | — | — |
| Direccion / pais / contacto | NO ENCONTRADO EN EL PDF | — | — | — |
| Aviso legal unico hallado | *"Images for reference only."* | pie de pagina | Index | 2 |

La cadena `2021-2-18` proviene del **nombre del archivo**, no de una fecha impresa dentro
del PDF. No hay contraportada con datos de la empresa: el archivo termina en la pagina
impresa `13/14` (PDF 305).

## Que hace (3 lineas maximo)

Catalogo de producto de un fabricante de implantes de trauma: lista referencias (REF),
dimensiones declaradas y material de cada familia de implantes e instrumental.
La seccion 5, `Cannulated Screw Set`, cubre tornillos canulados de 3.0 a 7.3 mm y sus
arandelas.

## Restriccion o supuesto clave

No es una fuente cientifica: no hay metodo, medicion, tolerancia ni norma declarada.
Publica **el diametro nominal, el diametro de cabeza, el hexagono de accionamiento y el
material**, y omite paso de rosca, diametro de nucleo, diametro de fuste, altura de
cabeza, longitud de rosca en mm y **diametro de canulacion**. Para una mascara 3D de
tornillo, el catalogo aporta contorno externo y arandela, no la geometria interna.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Dimensiones publicadas del sistema 6.5 / 7.3 mm

Cada producto trae un bloque de especificacion (texto libre) y una tabla `REF |
Length (mm)`. **No existe una tabla unica de especificaciones por diametro**: lo que
sigue es la transcripcion completa, celda a celda, de los bloques del 7.3 mm y del
6.5 mm y de los encabezados de sus tablas.

### 7.3 mm (pagina impresa 5/6, PDF 98)

| Producto | Diameter | Head Diameter | Hexagonal Socket | Material | Encabezados de tabla | REF (primera-ultima) | Length (mm) |
|---|---|---|---|---|---|---|---|
| 7.3mm Cannulated Screw, long threaded | 7.3mm | 8.0mm | 4.0mm | Titanium Alloy | `REF` \| `Length (mm)` | 060070050 - 060070110 | 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110 |
| 7.3mm Cannulated Screw, short threaded | 7.3mm | 8.0mm | 4.0mm | Titanium Alloy | `REF` \| `Length (mm)` | 060080050 - 060080110 | 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110 |

### 6.5 mm (pagina impresa 5/5, PDF 97)

| Producto | Diameter | Head Diameter | Hexagonal Socket | Material | Encabezados de tabla | REF (primera-ultima) | Length (mm) |
|---|---|---|---|---|---|---|---|
| 6.5mm Cannulated Screw, fully threaded | 6.5mm | 8.0mm | 4.0mm | Titanium Alloy | `REF` \| `Length (mm)` | 060060040 - 060060110 | 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110 |
| 6.5mm Cannulated Screw, half threaded | 6.5mm | 8.0mm | 4.0mm | Titanium Alloy | `REF` \| `Length (mm)` | 060050045 - 060050110 | 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110 |

`Hexagonal Socket: 4.0mm` es el **hueco hexagonal de accionamiento** (destornillador
`hexagonal, cannulated, φ4.0`, REF 110201100, pagina impresa 5/38, PDF 114). **No es el
diametro de canulacion.**

### Arandelas (pagina impresa 5/7, PDF 98)

| Producto | Thickness | Width | Material | REF |
|---|---|---|---|---|
| Washer for 6.5mm/7.3mm Cannulated Screw | 1.5mm | 13.0mm | Titanium Alloy | 060090000 |
| Spiked Washer for 6.5mm/7.3mm Cannulated Screw | 5.5mm | 13.0mm | Titanium Alloy | 060100000 |

Para contraste, las del sistema de 4.0 mm (pagina impresa 5/4, PDF 97):
`Washer for 4.0mm Cannulated Screw` Thickness 1.0mm / Width 7.0mm (REF 060030000) y
`Spiked Washer for 4.0mm Cannulated Screw` Thickness 3.5mm / Width 8.0mm (REF 060040000).

El catalogo publica **espesor** y **"Width"** (13.0 mm, diametro exterior). **El diametro
interior de la arandela NO ENCONTRADO EN EL PDF.**

## Las dos incognitas del encargo

1. **ESPESOR de arandela (6.5/7.3 mm): ENCONTRADO.**
   - Arandela plana: *"Thickness: 1.5mm"* (5/7, PDF 98).
   - Arandela con puas (`Spiked Washer`): *"Thickness: 5.5mm"* (5/7, PDF 98).
   Son dos productos distintos: el 5.5 mm incluye las puas, no es el espesor del disco.
2. **DIAMETRO DE CANULACION del tornillo (7.3 mm y 6.5 mm): NO ENCONTRADO EN EL PDF.**
   El bloque de especificacion del 7.3 mm publica solo Diameter, Head Diameter,
   Hexagonal Socket y Material; no hay campo de canulacion, `cannulation`, `inner
   diameter` ni `bore` en la seccion 5. Las unicas cifras cercanas son **instrumental**,
   no implante: guia y broca (ver abajo).

### Instrumental (NO es el agujero del tornillo)

| Sistema | Item | Cifra | Pagina impresa | Pagina PDF |
|---|---|---|---|---|
| 7.3 mm | *"Guide Wire φ 2.5, length 250 mm, with threaded tip"* (REF 110170500) | φ2.5 mm | 5/39 | 114 |
| 7.3 mm | *"Guide Wire, φ 2.5, length 250mm"* (REF 110071700) | φ2.5 mm | 5/38 | 114 |
| 7.3 mm | *"Drill Bit, φ5.0, length 250mm, cannulated"* (REF 110200700) | φ5.0 mm | 5/37 | 113 |
| 7.3 mm | *"Fixation Sleeve φ5.0, for Cannulated Drill Bits"* (REF 110201700) | φ5.0 mm | 5/39 | 114 |
| 7.3 mm | *"Tap for Cannulated Screws φ7.3, cannulated"* (REF 110201000) | φ7.3 mm | 5/38 | 114 |
| 6.5 mm | *"Guide Wire, Φ2.0, length 250mm"* (REF 110030300) | Φ2.0 mm | 5/34 | 112 |
| 6.5 mm | *"Drill Bit, Φ4.5, length 250mm, cannulated"* (REF 115190500) | Φ4.5 mm | 5/35 | 112 |
| 6.5 mm | *"Tap for Cannulated Screws Φ6.5, cannulated"* (REF 115190700) | Φ6.5 mm | 5/35 | 112 |

El catalogo **no dice** que la canulacion del tornillo iguale al diametro de la guia. Esa
inferencia no esta en el PDF y no debe escribirse como dato del fabricante.

## Material e indicacion

- Material declarado de los tornillos canulados de 6.5 y 7.3 mm y de ambas arandelas:
  *"Material: Titanium Alloy"* (5/5 y 5/6-5/7, PDF 97-98). **No se especifica la aleacion
  concreta** (Ti-6Al-4V u otra): NO ENCONTRADO EN EL PDF.
- **Asociacion con fijacion iliosacra o sacroiliaca: NO ENCONTRADO EN EL PDF.** Las
  paginas de la seccion 5 no nombran indicacion anatomica alguna; el indice de la seccion
  (5/1, PDF 95) solo lista `Cannulated Screw Set`, `Headless Compression Screw`,
  `Headless Screw` y sets de instrumental. No hay mencion de sacro, pelvis ni articulacion
  sacroiliaca en lo leido.

## Aviso de procedencia (obligatorio al citar)

Double Medical es **otro fabricante**: no es Synthes/DePuy Synthes ni Acumed. Sus
dimensiones describen **sus** referencias de catalogo y **no pueden atribuirse a los
implantes de otro fabricante** ni tratarse como un estandar del tornillo iliosacro de
7.3 mm. Si el espesor de arandela de 1.5 mm se usa en la tesis, debe citarse como
"arandela de Double Medical para tornillo canulado de 6.5/7.3 mm", no como "la arandela
de 7.3 mm". Ademas, el documento no es revisado por pares, no declara tolerancias y
advierte *"Images for reference only."* (Index, PDF 2).

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Espesor arandela 6.5/7.3 mm = 1.5 mm | *"Thickness: 1.5mm"* | Cannulated Screw Set, impresa 5/7, PDF 98 |
| Diametro exterior arandela = 13.0 mm | *"Width: 13.0mm"* | Cannulated Screw Set, impresa 5/7, PDF 98 |
| Arandela con puas = 5.5 mm de espesor | *"Thickness: 5.5mm"* | Cannulated Screw Set, impresa 5/7, PDF 98 |
| Cabeza del 7.3 mm = 8.0 mm | *"Head Diameter: 8.0mm"* | Cannulated Screw Set, impresa 5/6, PDF 98 |

## Donde entra en mi tesis

Solo como dato geometrico de apoyo para la **mascara** del tornillo sintetico: aporta el
espesor de arandela que faltaba (1.5 mm, plana) y confirma diametro de cabeza 8.0 mm y
diametro exterior de arandela 13.0 mm en un sistema comercial de 6.5/7.3 mm. **No cierra
el diametro de canulacion**, que sigue sin fuente. No es fuente clinica ni anatomica.

## Dudas para el asesor

- Si el modelo 3D del tornillo se construye como solido sin canulacion interna, el
  diametro de canulacion deja de ser necesario; conviene decidirlo antes de seguir
  buscando la cifra.
- La arandela con puas (5.5 mm) cambia bastante la huella metalica frente a la plana
  (1.5 mm). Cual de las dos representa el caso iliosacro que se quiere sintetizar?
- Se acepta citar un catalogo comercial sin revision por pares en la tesis, o solo como
  respaldo interno de la parametrizacion?

## Evidencia textual

| Item | Valor | Frase / celda textual (<=15 palabras) | Pagina impresa | Pagina PDF |
|---|---|---|---|---|
| Titulo | Trauma Catalogue | *"Trauma Catalogue"* | portada | 1 |
| Edicion | 2021 | *"Edition 2021"* | portada | 1 |
| Fabricante | Double Medical | *"DOUBLE MEDICAL — Dedicated to Rehabilitation"* | portada | 1 |
| Aviso general | reference only | *"Images for reference only."* | Index | 2 |
| Seccion 5 del indice general | Cannulated Screw Set = 5 | *"Cannulated Screw Set    5"* | Index | 2 |
| Subsecciones de la seccion 5 | 5/2, 5/9, 5/19 | *"Cannulated Screw Set 5/2; Headless Compression Screw 5/9; Headless Screw 5/19"* | 5/1 | 95 |
| Set de instrumental 7.3 | pagina 5/38 | *"7.3mm Cannulated Screw Instrument Set    5/38"* | 5/1 | 95 |
| Set de instrumental 6.5 | pagina 5/35 | *"6.5mm Cannulated Screw Instrument Set    5/35"* | 5/1 | 95 |
| 7.3 long threaded — diametro | 7.3 mm | *"Diameter: 7.3mm"* | 5/6 | 98 |
| 7.3 long threaded — cabeza | 8.0 mm | *"Head Diameter: 8.0mm"* | 5/6 | 98 |
| 7.3 long threaded — hexagono | 4.0 mm | *"Hexagonal Socket: 4.0mm"* | 5/6 | 98 |
| 7.3 long threaded — material | Aleacion de titanio | *"Material: Titanium Alloy"* | 5/6 | 98 |
| 7.3 long threaded — longitudes | 50 a 110 mm, paso 5 | *"REF 060070050 ... 50 ... 060070110 ... 110"* | 5/6 | 98 |
| 7.3 short threaded — diametro | 7.3 mm | *"Diameter: 7.3mm"* | 5/6 | 98 |
| 7.3 short threaded — cabeza | 8.0 mm | *"Head Diameter: 8.0mm"* | 5/6 | 98 |
| 7.3 short threaded — hexagono | 4.0 mm | *"Hexagonal Socket: 4.0mm"* | 5/6 | 98 |
| 7.3 short threaded — longitudes | 50 a 110 mm, paso 5 | *"060080050 ... 50 ... 060080110 ... 110"* | 5/6 | 98 |
| 6.5 fully threaded — diametro | 6.5 mm | *"Diameter: 6.5mm"* | 5/5 | 97 |
| 6.5 fully threaded — cabeza | 8.0 mm | *"Head Diameter: 8.0mm"* | 5/5 | 97 |
| 6.5 fully threaded — hexagono | 4.0 mm | *"Hexagonal Socket: 4.0mm"* | 5/5 | 97 |
| 6.5 fully threaded — longitudes | 40 a 110 mm, paso 5 | *"060060040 ... 40 ... 060060110 ... 110"* | 5/5 | 97 |
| 6.5 half threaded — longitudes | 45 a 110 mm, paso 5 | *"060050045 ... 45 ... 060050110 ... 110"* | 5/5 | 97 |
| Arandela 6.5/7.3 — espesor | 1.5 mm | *"Thickness: 1.5mm"* | 5/7 | 98 |
| Arandela 6.5/7.3 — ancho | 13.0 mm | *"Width: 13.0mm"* | 5/7 | 98 |
| Arandela 6.5/7.3 — material y REF | Ti alloy, 060090000 | *"Material: Titanium Alloy"*; *"REF 060090000"* | 5/7 | 98 |
| Arandela con puas 6.5/7.3 — espesor | 5.5 mm | *"Thickness: 5.5mm"* | 5/7 | 98 |
| Arandela con puas 6.5/7.3 — ancho y REF | 13.0 mm, 060100000 | *"Width: 13.0mm"*; *"REF 060100000"* | 5/7 | 98 |
| Arandela 4.0 — espesor / ancho | 1.0 mm / 7.0 mm | *"Thickness: 1.0mm"*; *"Width: 7.0mm"* | 5/4 | 97 |
| Arandela con puas 4.0 — espesor / ancho | 3.5 mm / 8.0 mm | *"Thickness: 3.5mm"*; *"Width: 8.0mm"* | 5/4 | 97 |
| Guia 7.3 (INSTRUMENTAL) | φ2.5 mm | *"Guide Wire φ 2.5, length 250 mm, with threaded tip"* | 5/39 | 114 |
| Guia 7.3 lisa (INSTRUMENTAL) | φ2.5 mm | *"Guide Wire, φ 2.5, length 250mm"* | 5/38 | 114 |
| Broca 7.3 (INSTRUMENTAL) | φ5.0 mm | *"Drill Bit, φ5.0, length 250mm, cannulated"* | 5/37 | 113 |
| Camisa de fijacion 7.3 (INSTRUMENTAL) | φ5.0 mm | *"Fixation Sleeve φ5.0, for Cannulated Drill Bits"* | 5/39 | 114 |
| Macho de terraja 7.3 (INSTRUMENTAL) | φ7.3 mm | *"Tap for Cannulated Screws φ7.3, cannulated"* | 5/38 | 114 |
| Destornillador 7.3 (INSTRUMENTAL) | φ4.0 mm | *"Screwdriver, hexagonal, cannulated, φ4.0"* | 5/38 | 114 |
| Guia 6.5 (INSTRUMENTAL) | Φ2.0 mm | *"Guide Wire, Φ2.0, length 250mm"* | 5/34 | 112 |
| Broca 6.5 (INSTRUMENTAL) | Φ4.5 mm | *"Drill Bit, Φ4.5, length 250mm, cannulated"* | 5/35 | 112 |
| Camisa de fijacion 6.5 (INSTRUMENTAL) | Φ4.5 mm | *"Fixation Sleeve, Φ4.5, for Cannulated Drill Bits"* | 5/35 | 112 |
| Macho de terraja 6.5 (INSTRUMENTAL) | Φ6.5 mm | *"Tap for Cannulated Screws Φ6.5, cannulated"* | 5/35 | 112 |
| Codigo del set 6.5 | 115040000 | *"Instruments    115040000"* | 5/34 | 112 |
| Codigo del set 7.3 | 110730000 | *"Instruments 110730000"* | 5/37 | 113 |
| Guias de titanio opcionales | φ0.8 a φ3.0, 125-250 mm | *"Titanium Guide Wire ... φ0.8 ... 150 ... φ3.0 ... 250"* | 5/40 | 115 |
| **Diametro de canulacion del tornillo 7.3** | **NO ENCONTRADO EN EL PDF** | — | — | — |
| **Diametro de canulacion del tornillo 6.5** | **NO ENCONTRADO EN EL PDF** | — | — | — |
| Paso de rosca (pitch) 7.3 / 6.5 | NO ENCONTRADO EN EL PDF | — | — | — |
| Longitud de rosca en mm (16/32) | NO ENCONTRADO EN EL PDF (solo *"long threaded"* / *"short threaded"*) | — | 5/6 | 98 |
| Diametro de nucleo (core) | NO ENCONTRADO EN EL PDF | — | — | — |
| Diametro de fuste (shaft) | NO ENCONTRADO EN EL PDF | — | — | — |
| Altura de cabeza | NO ENCONTRADO EN EL PDF | — | — | — |
| Forma / angulo de la cabeza | NO ENCONTRADO EN EL PDF | — | — | — |
| Diametro interior de la arandela | NO ENCONTRADO EN EL PDF | — | — | — |
| Numero y altura de puas de la arandela | NO ENCONTRADO EN EL PDF | — | — | — |
| Aleacion exacta de titanio | NO ENCONTRADO EN EL PDF | — | — | — |
| Norma (ISO/ASTM) del material | NO ENCONTRADO EN EL PDF | — | — | — |
| Indicacion iliosacra / sacroiliaca | NO ENCONTRADO EN EL PDF | — | — | — |
| Mencion de sacro o pelvis en la seccion 5 | NO ENCONTRADO EN EL PDF | — | — | — |
| Tolerancias dimensionales | NO ENCONTRADO EN EL PDF | — | — | — |
| Codigo de catalogo del documento | NO ENCONTRADO EN EL PDF | — | — | — |
| Copyright | NO ENCONTRADO EN EL PDF | — | — | — |
| Direccion del fabricante | NO ENCONTRADO EN EL PDF | — | — | — |
| URL o contacto | NO ENCONTRADO EN EL PDF | — | — | — |
| Fecha impresa (dia/mes) | NO ENCONTRADO EN EL PDF (`2021-2-18` viene del nombre del archivo) | — | — | — |
| Marcado CE / registro sanitario | NO ENCONTRADO EN EL PDF | — | — | — |
