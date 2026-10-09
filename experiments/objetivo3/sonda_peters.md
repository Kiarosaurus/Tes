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
