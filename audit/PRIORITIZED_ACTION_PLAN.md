# PLAN DE ACCION PRIORIZADO (F4) — nada de esto se ha aplicado a tesis, docs ni codigo
Criterio: impacto cientifico x riesgo de reclamar de mas / coste. Etiquetas de los revisores: INDISPENSABLE (I), RECOMENDABLE (R), OPCIONAL (O), TRABAJO FUTURO (TF). Fuentes entre parentesis.

## P0 — decisiones de la autora (coste nulo, antes de leer/medir mas)
1. Escribir en 01-decisiones.md (solo la autora): alcance actual de la prueba de Turing visual (hoy el repo dice "no se hace"; la autora indico que se promete tras los experimentos) y que el bloque perceptual/post-hoc es exploratorio (E-01, F-H1, C R-7, D MED-01/08). I
2. Regla de parada de exploraciones: no abrir mas brazos; cada brazo evaluado una vez en validacion 2 y solo si pasa, una vez en prueba, como exploratorio; todo en un apendice (C R-7). I
3. Preinscribir antes de abrir resultados T/P/A y 100:0.3: que 100:0.3 tambien se juzga con el margen comun 196.3 HU (E R3); lectura de criterios (i) y (ii) (E R4). I
4. Reservar un conjunto de receptores intacto para evaluacion visual/confirmatoria (E R5, F H1). I
5. Decidir meta editorial: rango de B (~6 200 palabras netas) con guia mandando en cap2 (autora, 2026-11-24).

## P1 — verificaciones sin GPU (me puedo encargar)
- F-H5: auditoria de identidad de pacientes/adquisiciones incluyendo volumenes sin metal, antes de usar casos_val2 (F H5). I
- R-8 reformulado: gradiente axial en G excluyendo M y con Peters de referencia (C R-8). R
- Tabla de flujo de cohortes con unidad y fecha de corte (A, B, G-002/003/022). I (editorial)
- Archivar commit, hashes de pesos y comandos exactos de cada corrida (G-024/025). R

## P2 — inferencia en Khipu (ya preparada; no entrena)
R-2 (A100, corriendo/terminada), R-9 (A6000), R-4 (T4) en cola; luego R-1 (13 de prueba; datos "nulo" ya existen), R-3/R-12 tras H5. Reglas de lectura de R-3/R-12 fijadas ANTES de mirar salidas. (C) I/R

## P3 — correcciones de texto exactas (fase 6, con autorizacion; el writer usa ESTILO.md y muestras)
- cap3:230 "896 parches de 3 casos" -> la validacion que elige mejor.pt usa 256 parches de metal_0011 (C-03). VERIFICADO
- cap3:204 y similares: aclarar que G se regenera sin ver su anatomia; las etiquetas oseas dentro de G dejan de ser validas (C-01). VERIFICADO
- Formula real de sigma de muestreo con eta (C-02); pregunta de investigacion: no nombrar copia y pegado como comparador (C-08); C-09, C-10.
- Cerrar el \GAPDEC de cap3:604 con el estatus exploratorio (E R1); actualizar visto.md con lo de noviembre (E R2); reescribir c2b sin sugerir ciego/Turing (E R6).
- W1: apendice de sensibilidad a sigma (R-11), lectura condicionada a h=2sigma.

## P4 — compresion editorial (fase 6; trabajar primero secciones estables)
Presupuesto base = B; figuras: pipeline, compuerta, corredor, SAP, difusion, streaks + comparacion con valores (borrador en audit/figures). Tablas: comparativa de cap2 con la tesis como fila (G-B8). Mover resultados de intro y cap3 a cap4/anexos; apendice de exploraciones post-hoc; no tocar ecuaciones ni la receta del corredor. Medir paginas con el PDF tras cada lote.

## P5 — futuro
Prueba de Turing: piloto minimo preinscrito con 2-3 lectores externos si hay disponibilidad (E; ~214 juicios para +-10 puntos; efecto de agrupamiento), TF si no. Fantoma para fidelidad fisica (D MED-05). Nuevas arquitecturas para C-01 (TF).

## Fuera de alcance de la auditoria actual (pendiente de cobertura)
Revision editorial de 75 % de cap3 (sintetizador v2, apariencia, amenazas), cap4, trabajosFuturos, anexos, resumen/abstract. Jurado final (Opus+Codex) cuando T/P/A cierren.
