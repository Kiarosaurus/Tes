# capitulo4-r01-puntual2 — respuesta del redactor

Correccion puntual sin revisores, pedida por el orquestador para alinear con `conclusiones-r01` (T01) y la decision 2026-10-16 (6). Sin cifras ni citas nuevas.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| 1. cap. 4 l. 236: "Se examinaron dos autoencoders [...] el de Guo et al." da a entender que el de Guo se ejecuto | orquestador | APLICADO | Ahora: se evaluo el de Stable Diffusion~1.5 (preentrenado o con decodificador adaptado) y ninguna de sus dos variantes alcanzo la tolerancia; el de Guo et al. no llego a correrse porque la sola saturacion a su rango de salida ya superaba el criterio sin modelo alguno. Coherente con `conclusiones.tex` l. 14 y con cap. 4 l. 45 (fuente del hecho). |
| 2. cap. 4 l. 238: "porque solo se examinaron dos autoencoders" | orquestador | APLICADO | Ahora: "porque solo se evaluaron las dos variantes del autoencoder de Stable Diffusion~1.5 y, en el de Guo et al., la cota por saturacion", misma formulacion que `conclusiones.tex` l. 14. |
| 3. cap. 3 l. 93: "Antes de correr ese modelo se comprobo su rango de salida" | orquestador | APLICADO | Se agrego "en el codigo de su paquete distribuido"; sin cifra ni `\cite` nuevo (el detalle, `maisi_ct_generative` y `scripts/sample.py`, queda en cap. 4 l. 45). |

Lint: `capitulo4 --compilar` PASA (alta=0 media=0 baja=0; 189 paginas). `capitulo3` PASA (alta=0 media=0 baja=34, todas E-P1 preexistentes; ninguna en la l. 93 editada).

GAP abiertos: ninguno. GAP cerrados: ninguno.

## Decisiones de redaccion

- El autoencoder de Guo et al. se describe siempre como **no corrido**: lo que se hizo fue la cota por saturacion a su rango de salida. "Examinar/evaluar dos autoencoders" no se usa; la formula es "las dos variantes del autoencoder de Stable Diffusion~1.5 y, en el de Guo et al., la cota por saturacion".
