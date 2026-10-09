# Sonda de viabilidad del brazo fisico de Peters — protocolo preinscrito (2026-10-09)

Fijado **antes de correr nada**, por delegacion de la autora (`01-decisiones.md` 2026-10-09 (2)). Orden de
trabajo: 2026-10-05 (6), punto 5.2. Base: el ejemplo AAPM del repositorio XCIST ya corrio en local el
2026-10-05 (`peters/run.py`, con un parche documentado). Tardo unos 2 minutos, segun la fecha de los
archivos `out.*`.

## Pregunta

Se trata de saber si el protocolo hibrido de `peters2025hybrid` puede producir, en un corte de una pelvis de
esta tesis con el tornillo de esta tesis, un artefacto metalico **medible y fiel** que sirva de brazo de
comparacion del endpoint primario (`streak amplitude`, TOST, D4). El protocolo es 2D: un corte y una fila
de detector.

Si la respuesta es no, D4 se replantea **ahora**, antes de invertir en Peters completo.

## Entrada (fija)

- **Paciente:** `dataset6_CLINIC_0101_data` (validacion, sin metal; corredor de 10.6 mm).
- **Tornillo:** la misma pose y el mismo cilindro que en `a15` (`a11_rasterizar_tornillo`, ~4.91 mm), con el
  mismo `--semilla-pose`.
- **Corte:** el corte con mayor area de `M`.
- **Fantoma:** el corte de TC convertido a mapas de material (agua y hueso) segun el procedimiento de Peters.
  - Si la ficha o el PDF no fijan la conversion, se usa la de XCIST y se marca
    `NO ENCONTRADO EN EL PDF` en el informe.
  - El metal entra como **fraccion de volumen** del tornillo dentro del espesor del corte (0.8 mm), calculada
    sobre la mascara 3D supermuestreada. Asi la oblicuidad del tornillo respecto del plano entra como
    volumen parcial.
- **Material principal: acero inoxidable.** Peters asigna acero a los implantes espinales de 2.5-10 mm
  (Tabla 2, p. 4), la clase de tamano en que cae el tornillo. Synthes ofrece los tornillos canulados en acero
  y en titanio (`synthes_cannulated_screws`, p. 4).
  - Se usa el material del catalogo XCIST mas cercano al acero; si no hay acero, `Fe`, declarado.
  - **Titanio** se corre como sensibilidad, solo descriptiva.
- **Adquisicion:** la del ejemplo AAPM (`peters/AAPM_MAR_*.cfg`), 120 kVp y 500 mA (Peters 2.3, p. 4).
  - Unico cambio: el campo de vision cubre el corte entero (512 x 0.896 mm = 459 mm, frente a los 400 mm de
    Peters para pelvis). El detector de 900 columnas cubre unos 521 mm en el isocentro.
- **Cuatro simulaciones:**
  - sin metal, semilla de ruido A y semilla B (test-retest);
  - con acero, semilla A;
  - con titanio, semilla A.

## Medidas

- `Delta_fis = recon(paciente + metal) - recon(paciente)`, las dos con la semilla A (el par de Peters).
- `streak amplitude` con la definicion y las ROIs de E-A2 (`01-decisiones.md` 2026-10-05 (3) y (4)),
  restringida a este corte: anillos completos con un voxel de guarda hasta 12 mm.
- **Ruido de referencia:** la misma amplitud sobre `recon(semilla A) - recon(semilla B)`, sin metal.
- **Fidelidad sin metal:** mediana de `recon(paciente) - TC original` en el anillo de 12-15 mm y en el tejido
  blando del corte.
- Tiempo de pared por simulacion.

## Criterios de viabilidad (fijados antes de mirar)

| | Criterio | Pasa si |
|---|---|---|
| V1 | Ejecucion y coste | Corre sin error; el contorno del cuerpo cabe entero en la reconstruccion (sin truncamiento); el coste proyectado del brazo completo es de 72 h o menos en Khipu. Brazo completo: 14 pacientes de E-A2 x cortes con `M` menos 8 mm por extremo x 2 condiciones x 2 semillas |
| V2 | Fidelidad sin metal | Mediana de `recon - original` dentro de +/-20 HU en el anillo de 12-15 mm y en tejido blando. 20 HU es el 2 % de la escala agua-aire (1000 HU), por analogia con la validacion de Peters: *"the simulated mean deviated by less than 2%"* (3.1, p. 6). Es una eleccion de juicio y se declara |
| V3 | Artefacto medible | `streak amplitude` de `Delta_fis` (acero) mayor o igual a 3 veces la amplitud del ruido de referencia |

## Que se hace con cada resultado (fijado ahora)

- **V1, V2 y V3 pasan:** se implementa Peters completo, luego `Delta`.
- **Falla solo V1 por coste:** se submuestrean los cortes (uno de cada `k`, con `k` fijado para caber en
  72 h). Se declara y D4 no cambia.
- **Falla V1 por truncamiento, o fallan V2 o V3:** el brazo fisico no puede anclar una equivalencia.
  - El TOST contra Peters baja a contraste **secundario descriptivo**.
  - El **realismo frente a CLINIC-metal** (E-A2 iii) pasa a contraste primario.
  - Se escribe la entrada de decision correspondiente antes de seguir.
- **Titanio y acero** se reportan los dos. El material del brazo completo es acero; este resultado no lo
  cambia.

## Lo que la sonda NO decide

- El margen `Delta` (D4 (iv)), que sale de la variabilidad en validacion.
- Si el brazo fisico "se parece" al sintetico: comparar amplitudes aqui seria mirar el contraste primario
  antes de tiempo. La sonda reporta la amplitud de `Delta_fis`, **no** la del difusor en el mismo corte.

## Limitaciones declaradas

- Un paciente y un corte.
- 2D: el artefacto que en un escaner real llega desde fuera del corte (haz conico, cortes vecinos) no se
  modela. Peters tiene la misma limitacion (*"only covers two-dimensional MAR developments"*, Discussion,
  p. 9).

## Enmiendas antes de correr (2026-10-09, sin haber visto ningun resultado)

`lector-papers` encontro que el PDF de Peters **no** describe como se convierte el corte clinico en fantoma
ni como entra el metal en z (25 `NO ENCONTRADO EN EL PDF` en la ficha). Se resuelve con el repositorio
oficial del reto AAPM, que es la implementacion publicada del mismo protocolo:

- **Fantoma:** agua con densidad relativa `(HU + 1000) / 1000`.
  - Fuente: `repos/xcist-example/AAPM_datachallenge/simulation_scripts/readme.md`, *"the relative density
    with respect to water, calculated by (HU_map + 1000)/1000"*.
  - Antes, **realce de frecuencias** por imagen (`AAPM_freq_boost.docx`): cociente de las medias radiales de
    la FFT original/reconstruida, aplicado en 2D. El tope del cociente, [0.5, 3], es propio; el documento no
    da ninguno.
- **Metal: la `M` binaria del difusor**, no una fraccion de volumen. Peters tambien usa mascaras binarias
  (*"binary images of size 256 × 256"*, 2.3, p. 4), y asi la geometria es identica en los dos brazos.
  Sustituye a la fraccion de volumen de la seccion "Entrada".
- **Tejido bajo el metal:** dentro de `M` la densidad del paciente se pone a 0. `run.py` resta densidad 1,
  lo que deja hueso residual bajo el metal. Desviacion declarada.
- **Acero -> `Fe`:** el catalogo de materiales de XCIST no trae acero (`gecatsim/material/`: hay `Fe`, `Cr`,
  `Ni` y `Ti`).
- **Reconstruccion:** FOV = 512 x 0.896 mm (459 mm), para que la reconstruccion caiga sobre la rejilla del
  original. La orientacion de la salida se alinea con el original por correlacion. Es geometria, no
  resultado.
- **Anillo de V3:** en el plano axial del corte, de una guarda de un pixel a 12 mm. En E-A2 los anillos estan
  en planos perpendiculares a `u`; con un solo corte axial no hay otro.
- **Par con y sin metal con la misma semilla:** es una eleccion propia. El PDF no dice si el par de Peters
  comparte la realizacion de ruido.
- **Coste de V1:** se usan los cortes evaluables del receptor de validacion como proxy de los de test, que
  no se tocan.

Script: `a18_sonda_peters.py`.
- **Enmienda 2, tras un fallo de ejecucion y sin ningun resultado de simulacion:**
  - **Ruido independiente en todas las simulaciones.** La DLL de XCIST en Windows no exporta `setall`, asi que
    no se puede fijar la semilla del ruido de Poisson. `Delta_fis = Fe - sin metal A` y la referencia de ruido
    `sin metal A - sin metal B` llevan las dos dos realizaciones independientes, y V3 las compara con la misma
    estructura de ruido.
  - **Coste de V1:** se cuentan todos los cortes axiales que toca `G`. El tornillo va casi en el plano axial,
    asi que ocupa pocos cortes axiales, pero las ROIs de E-A2 estan en planos perpendiculares a `u` y
    necesitan el volumen simulado entero alrededor de `G`.
- **Corrida 1 (2026-10-09), conservada en `outputs/a18_corrida1/`:** NO VIABLE (V1 y V2 fallan; V3 pasa,
  39 veces el ruido). El diagnostico encontro **dos errores de implementacion**, no limites del protocolo:
  - **V2 (+237/+276 HU):** el original trae relleno de -2048 HU fuera del FOV del escaner, y el realce de
    frecuencias se calculo con ese relleno. La pasada de calibracion sin realce da +4 HU en tejido blando y +6 HU
    en hueso. **Correccion:** el relleno se lleva a -1000 HU, que es aire, antes de construir el fantoma y el
    realce.
  - **Truncamiento de V1:** los 10 pixeles fuera del circulo de reconstruccion pertenecen a componentes
    separados del cuerpo (7467 y 1925 px, frente a 62 547), compatibles con la camilla. **Correccion:**
    cuerpo = componente conexo mayor.
  - **Coste de V1 (114.7 h > 72 h):** no es error. Se aplica la salida preinscrita: submuestrear los cortes.
  - **Los criterios y umbrales no cambian.** Se corre una sola vez mas (corrida 2) y se reportan las dos.

## Resultado (corrida 2, 2026-10-09; salida en `outputs/a18/`)

| | Medida | Corrida 1 | Corrida 2 | Umbral | Corrida 2 |
|---|---|---|---|---|---|
| V1 | truncamiento del cuerpo | si (era la camilla) | no | no | PASA |
| V1 | coste del brazo completo | 114.7 h | 108.9 h (127 s x 55 cortes con `G` x 14 x 2 x 2) | <= 72 h | FALLA |
| V2 | sesgo sin metal, anillo 12-15 mm | +237 HU | **+3.9 HU** | +/-20 HU | PASA |
| V2 | sesgo sin metal, tejido blando | +276 HU | **+6.5 HU** | +/-20 HU | PASA |
| V3 | amplitud Fe / ruido | 39x | **72.8x** (10 166 / 140 HU) | >= 3x | PASA |

- **Veredicto por la regla preinscrita: VIABLE con submuestreo.** Solo falla el coste, y su salida estaba
  fijada: un corte de cada `k = 2`, unas 54 h, dentro de 72 h. D4 no cambia: el TOST contra Peters sigue como
  contraste primario.
- El script imprime "NO VIABLE" porque cuenta cualquier fallo de V1. La regla de `sonda_peters.md` separa el
  fallo solo por coste, y esa regla manda.
- La reconstruccion sin metal correlaciona 0.997 con el original.
- **Descriptivo, no es criterio:** mediana dentro de `M`, Fe 9895 HU y Ti 5390 HU. Los tornillos reales de
  `metal_0039` dan 3092-3838 HU (`a17`). Ver #159. La amplitud del difusor **no** se calculo.
