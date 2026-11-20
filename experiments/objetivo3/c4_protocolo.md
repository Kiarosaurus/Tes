# C4 — anisotropía angular del artefacto (protocolo declarado ANTES de calcular; 2026-11-20)
Estatus: **exploratorio / post-hoc**, descriptivo (N pequeño, sin p-values). No decide nada de v3 ni sustituye a E-A2.
Motivo: observación de la autora (real = patrón direccional tipo "astigmatismo"; sintético = halo liso). Ninguna métrica radial existente (a17, A28, D1/D2) ve ángulos (brecha B7).

## Métrica principal
Anillo 2–10 mm alrededor del centroide de `M` en el plano axial; píxeles de cuerpo (HU>-300 en la referencia), sin `M` ni otro metal.
1. Por cada anillo de 1 mm, restar la mediana (quita el perfil radial).
2. Agrupar en K=24 sectores de 15°. **η²** = varianza entre sectores / varianza total (0 = isotrópico, 1 = puramente angular).
3. Corregir por azar: **η²_exc = η² − (K−1)/(N−1)** (N = píxeles del corte).
4. Imagen antes de η²: HU recortados a [-500, 1300] (la misma ventana del ciego C2).
Se reporta también la desviación estándar del anillo (amplitud), porque el ruido baja η².

## Brazos (todo local, solo lectura)
| Brazo | Fuente | Modo "residuo" (sin anatomía) |
|---|---|---|
| run04_mejor, run05a_mejor, run05b_mejor | `obj3_pose/delta/<brazo>/` NIfTI, 0101/0102, todas las semillas disponibles | sintética − original (mismo corte) |
| Peters Ti | `peters_val/*.npz`, `Ti_A` | Ti_A − limpia_A |
| Real | `metal_0039`, 2 tornillos, todos sus cortes con el componente | no existe → solo modo "crudo" |
Modos: **crudo** (HU del corte; incluye anatomía; comparable entre los 5 brazos) y **residuo** (solo sintéticos y Peters).
Cortes: los de Peters (`ks`) con `M` presente, igual para todos los brazos sintéticos.
**Controles de anatomía** (sin metal): corte `original` de cada paciente; y para real, cortes del mismo paciente a ≥15 mm axiales del componente, centrados en el mismo (y,x). Un brazo solo muestra estructura angular "del artefacto" si su η²_exc supera el control.

## Agregación y lectura
Corte → semilla → paciente (mediana) → brazo (mediana, con rango entre pacientes). Se informa TODO, también lo desfavorable.
Sensibilidad (se reporta, no decide): K=12 y K=48; recorte [-1000, 3000].
Lectura permitida: "el η²_exc de X es mayor/menor que el real y que el control". Prohibido: afirmar causa del defecto, equivalencia o mejora.
## Limitaciones declaradas
Real = otro paciente y escáner; 2 tornillos; 2 pacientes sintéticos de validación (usados en calibración); el modo crudo mezcla anatomía; η² no distingue rayas de bordes anatómicos radiales; semillas run05b incompletas (lo que haya).

## ENMIENDA v2 (2026-11-20, DESPUÉS de ver el resultado v1 — declarada, no preinscrita)
- **v1 (anillos por radio al centroide) quedó invalidada:** el control sin metal dio η²_exc≈0.49 (igual que casi todos los brazos) y un halo perfectamente liso alrededor de un `M` elíptico dio 0.805. La métrica medía la forma de `M` (tornillo oblicuo), no las rayas. Se conserva tal cual en `c4/c4_resumen_v1_centroide.md`.
- **v2:** los anillos de 1 mm se definen por **distancia en el plano a `M`** (transformada de distancia), igual que a17/D2; el ángulo sigue siendo respecto al centroide. Todo lo demás igual.
- **Controles de validez de la métrica (C0)** en `c4_anisotropia.py::validez()`: halo liso −0.01; liso + ruido 150 HU 0.008; 8 rayas ±30 % 0.556; rayas + ruido 0.240. La v1 daba 0.57–0.81 en los cuatro casos. El ruido baja η²: la amplitud de ruido del difusor (std de anillo ~245 HU) puede ocultar rayas reales.
- Cambio dependiente de datos: la v2 se eligió por el fallo de la v1, no por lo que favorece a un brazo. Resultados completos en `c4/c4_resumen_distancia.md` (4 tablas: principal y 3 sensibilidades).
