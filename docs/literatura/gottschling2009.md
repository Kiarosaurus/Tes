# gottschling2009 — A System for Performing Automated Measurements on Large Bone Databases

- **DOI / URL:** NO ENCONTRADO EN EL PDF
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/gottschling2009.pdf

## Que hace (3 lineas maximo)

Describe un sistema para medir automaticamente distancias, angulos y diametros
sobre bases de datos grandes de huesos ya segmentados (superficies poligonales),
usando "landmark features" (deteccion automatica de puntos/planos anatomicos) y
"correspondence features" (mapeo de deformacion no-rigida entre una forma
plantilla y cada muestra). Probado sobre 1265 fémures y 805 tibias; NO hay
ninguna mencion a pelvis, sacro, corredor transsacro, tornillo ni implante en
todo el texto — el paper trata exclusivamente fémur y tibia.

## Restriccion o supuesto clave

No aplica: no es un paper de sintesis generativa de implantes metalicos, es un
sistema de medicion geometrica automatica sobre huesos ya segmentados.

**Sobre reimplementabilidad (pregunta del encargo):** el paper da la formulacion
matematica general (ecuacion 1: `x_S = surf ∘ deform ∘ affine(x_T)`, y la funcion
de energia a minimizar sobre transformadas de distancia con signo, seccion II.B,
p. 911-912) y nombra la referencia externa de la que toma el metodo de
deformacion no-rigida ("[4] Huang X, Paragios N, Metaxas D (2006) Shape
Registration in Implicit Spaces...", p. 913). Sin embargo, NO da: numero de
puntos de control de la retícula de deformacion, criterio de convergencia,
tasa de aprendizaje/paso del descenso de gradiente, ni el nombre del software
propio usado para implementarlo. Solo se nombra software de terceros
("commercial CAD software (Pro/E)") usado por los ingenieros humanos para la
comparacion manual, no para el sistema automatico. Conclusion: el metodo esta
descrito a nivel de formulacion matematica y de referencias externas, pero
**no da parametros de implementacion suficientes para reproducirlo
directamente sin recurrir a las referencias [4], [5] y [6] citadas**.

## Que toco de aqui
- [x] solo contexto

## Numeros que cito de este paper
Ver tabla en "Evidencia textual".

## Donde entra en mi tesis

Este paper llego al proyecto como "el algoritmo que McLaren (mclaren2021corridor)
usa y no describe" para extraccion de contorno oseo y medicion de corredores
transsacros. **Hallazgo clave:** el texto completo de este paper no contiene
ninguna referencia a pelvis, sacro, corredor, cilindro inscrito ni trayectoria
de tornillo — es un sistema generico de medicion (landmark + correspondence
matching) aplicado y validado solo sobre fémur y tibia. Si McLaren cita este
paper como base del algoritmo de corredor sacro, la aplicacion al sacro/corredor
transsacro no esta documentada aqui; como mucho, este paper aporta el marco
metodologico general (deteccion de landmarks + mapeo de correspondencia por
deformacion no-rigida) que McLaren pudo haber adaptado, sin que este texto lo
confirme.

## Dudas para el asesor

- Confirmar en mclaren2021corridor si efectivamente cita a Gottschling et al.
  2009 para el paso de extraccion de contorno oseo / medicion del corredor, y
  si esa cita es sobre el marco metodologico general (landmark + correspondence
  matching) o sobre un uso especifico no descrito en este paper.
- Este paper no reporta resolucion de las imagenes CT de origen ni el software
  propio (nombre) del sistema automatico: verificar si existe una version
  extendida o un paper posterior de los mismos autores (Gottschling, Reimers,
  Fischer, Homeier, Burgkart — Stryker Trauma GmbH) con mas detalle de
  implementacion, dado que esto es un proceedings paper de 4 paginas (WC 2009).

## Evidencia textual

| Cifra / definicion / criterio | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Tamano de base de datos: 1265 fémures + 805 tibias | "tested on a database containing 1265 femur and 805 tibia datasets" | III. Results, p. 912 |
| Tiempo de preprocesamiento por muestra | "took approximately 1-2 minutes per sample" | III. Results, p. 912 |
| Hardware usado | "2.67 GHz Intel Core2 Duo CPU with an NVidia GeForce 8 graphics card" | III. Results, p. 912 |
| Tamano de muestra de validacion | "Ten femur samples were randomly chosen from the database" | III. Results, p. 912 |
| Definicion de "head diameter" | "distance of two points located on opposing sides of the femur head" | III. Results, p. 912 |
| Definicion de "femur length" | "distance between the most proximal point on the greater trochanter, and the distal center of the facies patellaris" | III. Results, p. 912 |
| Diferencia S1-S2, diametro de cabeza femoral | "Head Diameter 1.74±0.69 mm" (S1-S2) | Table 2, p. 913 |
| Diferencia S1-AM, diametro de cabeza femoral | "1.93±1.04 mm" (S1-AM) | Table 2, p. 913 |
| Diferencia S2-AM, diametro de cabeza femoral | "0.73±0.53 mm" (S2-AM) | Table 2, p. 913 |
| Diferencia S1-S2, longitud femoral | "Femur Length 1.64±0.91 mm" (S1-S2) | Table 2, p. 913 |
| Diferencia S1-AM, longitud femoral | "1.04±0.67 mm" (S1-AM) | Table 2, p. 913 |
| Diferencia S2-AM, longitud femoral | "1.76±1.43 mm" (S2-AM) | Table 2, p. 913 |
| Robustez del metodo de generacion de plantilla (mean shape) | "maximum surface deviation of less than 2mm" | II.B Correspondence Features, p. 912 |
| Formula de mapeo de correspondencia (ecuacion 1) | "x_S = map(x_T) = surf ∘ deform ∘ affine(x_T)" | II.B, ecuacion (1), p. 911 |
| Base de la deformacion no-rigida (referencia externa) | "implemented following the approach described in [4]" | II.B, p. 911 |
| Software usado por ingenieros humanos (no el sistema propio) | "using a commercial CAD software (Pro/E)" | III. Results, p. 913 |
| Base de datos / origen de las muestras (vago, sin especificar procedencia exacta) | "bone samples in surface representation drawn from the database" | II. Materials and Methods, p. 910 |
| Corredor transsacro / cilindro inscrito / trayectoria de tornillo | NO ENCONTRADO EN EL PDF | — |
| Resolucion de las imagenes CT de origen | NO ENCONTRADO EN EL PDF | — |
| Nombre propio del software / disponibilidad publica o propietaria | NO ENCONTRADO EN EL PDF | — |
| Estado de los huesos (sanos/intactos vs. con implante o fractura) | NO ENCONTRADO EN EL PDF | — |
