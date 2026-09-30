# Mapa de redaccion: de donde sale cada capitulo

> Lo mantiene Claude. Dice, por archivo de `overleaf/secciones/`, que bloque de la guia cubre,
> de que fuentes del repositorio se redacta y en que estado esta. Las filas "Estado" y
> "Ultima ronda" se actualizan al cerrar cada `/ciclo-redaccion`.
>
> **Orden de autoridad** cuando dos fuentes discrepan: `docs/01-decisiones.md` >
> `tesis/main.tex` > `docs/00-tesis.md` > `docs/04-implicancias.md` (solo entradas APLICADAS o
> CERRADAS) > `experiments/*/EXPERIMENTOS.md` > `docs/ESTADO.md`. Una implicancia ABIERTA **no**
> se redacta como hecho: se redacta como `\GAPDEC` o `\GAPDATO`.

## Orden del documento (decision de la autora, 2026-09-29: orden de la guia)

| Archivo | Bloque (guia) | Capitulo | Fuentes principales | Estado | Ultima ronda |
|---|---|---|---|---|---|
| `introduccion.tex` | (a) | Introduccion | `tesis/main.tex` secciones Problem Statement, Recognized Gap, Research Question, Hypothesis, Objectives, Out of scope; `docs/00-tesis.md` | Objetivos, Justificacion y Alcance: con decisiones pendientes (TOPE en r05; 16 \GAPDEC, ver #128). Encabezado y Formulacion: DESFASADO (#126) | r05 (3 subsecciones) |
| `capitulo1.tex` | (b) teorico | Marco teorico | `docs/03-glosario.md`; fichas de `docs/literatura/` de fisica de artefactos (`deman1999`, `glover1980nonlinear`), difusion (`ho2020denoising`, `song2021ddim`, `rombach2022latentdiffusion`, `lugmayr2022repaint`), fijacion iliosacra (`kaiser2014dysmorphism`, `mclaren2021corridor`, `gardner2010safezones`, `smith2006iliosacral`) | esqueleto | — |
| `capitulo2.tex` | (b) comparativo | Estado del arte y brecha | `tesis/main.tex` Problem Statement y Recognized Gap; `docs/literatura/_index.md`; implicancias de tipo GAP y RIESGO | esqueleto | — |
| `capitulo3.tex` | (c) formal + diseno | Propuesta y metodologia | `tesis/main.tex` Objectives, Expected Results (columna metrica), Pre-registration, Datasets; `experiments/objetivo2/preinscripcion_muestreador.md`; `docs/02-datos.md` | con decisiones pendientes (TOPE en r05; 22 GAPDEC, ver #127) | r05 |
| `capitulo4.tex` | (c) empirico | Resultados y discusion | `tesis/main.tex` Measured outcome (Obj 1), Placement result (Obj 2); `experiments/*/EXPERIMENTOS.md` | esqueleto | — |
| `conclusiones.tex`, `trabajosFuturos.tex` | (d) | Conclusiones, trabajo futuro | todo lo anterior, ya redactado | plantilla | — |
| `resumen.tex`, `abstract.tex` | — | Resumen / Abstract | se escriben **al final** | plantilla | — |

## Contenido que hoy solo puede entrar como GAP

No es una lista cerrada: el redactor agrega aqui cada GAP que abre, y lo quita cuando se resuelve.

| Marca | Que falta | Origen |
|---|---|---|
| `\GAPDATO` | Todo resultado del Objetivo 3: el sintetizador nunca genero una muestra. Tambien en `introduccion` §Alcance | #116 |
| `\GAPDATO` | Resultados del protocolo fisico de `peters2025hybrid` (brazo de comparacion) | #17 |
| `\GAPDATO` | Revision de la autora de los 16 casos del recorte de 6 mm (14 por diferencia de diametro, 2 por caja desplazada); condiciona **todas** las cifras del Obj 2. Tambien en `introduccion` §Alcance | #123 |
| `\GAPDATO` | Cribado ciego de fractura, 30 casos; puede cambiar como se interpreta el estrato estrecho. Tambien en `introduccion` §Alcance | #125 |
| `\GAPDEC` | Si la frase del acuerdo 61 de 61 entra | #124 |
| `\GAPDEC` | Titulo del documento: el de `main.tex` de overleaf contradice el alcance vigente | #126 |
| `\GAPDATO` | Constancia de la revision multiplanar completa de cortes (el registro solo acredita la 3D). En `capitulo3` §Datos | `docs/02-datos.md`; `tesis/main.tex` *Local cohort audit* |
| `\GAPDATO` | Descripcion completa del algoritmo de busqueda del eje del corredor; consta en el codigo y, en parte, en #121 (P-MM3). En `capitulo3` §Corredor | capitulo3-r00; texto ajustado en r01 (T16) |
| `\GAPDATO` | Preinscripcion y corrida del muestreo de poses en el segundo corredor bajo S1 (el eje YA esta medido en 69 de los 72 pacientes de la cohorte primaria, `e9ts_ejes_*.csv`). En `capitulo3` §Poses. Tambien en `introduccion` §Alcance (desde r02, T04/guia-9) | `preinscripcion_muestreador.md` §7; #121 act. 2026-09-22 (7); corregido en r01 (T05) |
| `\GAPDEC` | Fuente y definicion operativa de la fraccion por zona de densidad de SAP: D-O2.6 la calcula sobre E9b, que la decision 2026-09-14 (#50) retiro como evidencia de densidad; la definicion solo consta en `src/muestreador/sap.py`. Tambien en `introduccion` §Objetivos, Obj 4 (desde r03, guia-4) | D-O2.6 frente a DEC 2026-09-14 #50; texto corregido en r02 (T03) |
| `\GAPDEC` | Congelar la preinscripcion del sintetizador (codificacion multiventana, que el borrador supone arcsinh, y su error de ida y vuelta sin autoencoder; arquitectura, entrenamiento, muestreo, numero de semillas por caso, margen Delta); `diseno_A.md` en borrador. Tambien en `introduccion` §Objetivos, solo el error de ida y vuelta sin autoencoder (desde r03, T01) | D4; #100, #106; ampliado en capitulo3-r02 (guia-2) y r03 (T06, semillas) |
| `\GAPDEC` | Si SAP incorpora la dimension angular de `smith2006iliosacral` o declara solo la de perforacion | #11 |
| `\GAPDEC` | Definicion operativa de la inversion de cada metrica de `peters2025hybrid` para sintesis. Tambien en `introduccion` §Objetivos, Obj 4 (desde r02, guia-3) | #17 (pendiente tecnico), #16 |
| `\GAPDEC` | Definicion operativa de la insercion por copia y pegado (HU asignado a `M`) | `diseno_A.md` §7 (borrador) |
| `\GAPDEC` | Si el brazo TOST frente a Peters se mantiene o pasa a trabajo futuro (contingencia de plazo). Tambien en `introduccion` §Alcance | #90 |
| `\GAPDEC` | Si se anade a Wasserstein-1 un intervalo por remuestreo de pacientes, como analisis no preinscrito | capitulo3-r00 (G-C8, G-C11) |
| `\GAPDATO` | Descripcion de la heuristica de localizacion de referencias anatomicas (crestas, espinas, S1), hoy en el codigo y en parte en `r1_landmarks.md` (P-MM3). En `capitulo3` §Marco con metal | capitulo3-r01 (guia-7); texto corregido en r02 (T07) |
| `\GAPDEC` | Alinear la pregunta y los objetivos de la introduccion con los cuatro objetivos del cap. 3 (G-C4). En `capitulo3` §Vision general. **Objetivos ya alineados en introduccion-r00; falta la pregunta**, por eso el GAP de capitulo3 no se cierra todavia | capitulo3-r01 (guia-1); #126 |
| `\GAPDEC` | Justificacion de la convencion `h = 2 sigma`, que fija toda la escala del muestreador (G-C1). En `capitulo3` §Poses. Tambien en `introduccion` §Alcance, cuarta convencion (desde r02, guia-2) | capitulo3-r01 (guia-4); PRE §3.1 |
| `\GAPDEC` | Que evidencia verifica el Objetivo 4 mas alla de los seis controles de SAP, o si se declara no evaluado experimentalmente (G-A7). En `capitulo3` §Protocolo y en `introduccion` §Objetivos; en la introduccion se amplio con si la adopcion de las metricas de Peters et al. cuenta como parte evaluable | capitulo3-r01 (guia-3); introduccion-r01 (guia-3) |
| `\GAPDEC` | Escala de lectura de Wasserstein-1 o que resultado contaria como fallo del muestreador; hoy el Obj 2 no tiene regla de decision (G-C6, G-A8). En `capitulo3` §SAP y en `introduccion` §Objetivos | capitulo3-r01 (guia-2); PRE §6 |
| `\GAPDEC` | Numero de pacientes del subconjunto del protocolo fisico de Peters (P-MM3). En `capitulo3` §Apariencia | capitulo3-r01 (guia-8); DEC 2026-09-17 B.2; renombrado en r03 (S15) |
| `\GAPDEC` | Como se agregan por paciente poses y regiones de rayas antes de Wilcoxon y TOST (G-C8). En `capitulo3` §Apariencia | capitulo3-r01 (guia-5); D4 |
| `\GAPDATO` | Parametros del ajuste del decodificador adaptado de la compuerta (numero de cortes, perdida, optimizador, criterio de parada); DEC 2026-09-17 D.1 solo dice "cortes multi-ventana de pacientes de entrenamiento" (P-MM3). En `capitulo3` §Compuerta | capitulo3-r02 (guia-8) |
| `\GAPDEC` | Calibre con que SAP evalua la viabilidad: D-O2.4 fija el calibre nominal 6.5-8.0 mm (antes "envolvente", renombrado en r03, S06), E13 corrio con 4.91/7.0/7.3 mm y holgura 1 mm (G-T4). En `capitulo3` §SAP. Tambien en `introduccion` §Objetivos, Obj 4 (desde r04, T02) | capitulo3-r02 (T01) |
| `\GAPDEC` | Que resultado de la prueba de superioridad frente a copia y pegado contaria como fallo, o si la prueba decisiva del Obj 3 es la TOST (G-C9, G-A8). En `capitulo3` §Apariencia y en `introduccion` §Objetivos | capitulo3-r02 (guia-1) |
| `\GAPDEC` | Justificacion del valor de 8 mm de la exclusion de extremos (corredor y tramo `T` de SAP); DEC D-O2.3 pto 4 justifica excluir extremos, no el valor; `e9_corredor.py` `RECORTE_EXTREMO_MM = 8.0` (G-T4). En `capitulo3` §SAP | capitulo3-r04 (T02) |
| `\GAPDATO` | Comprobacion de que la envolvente osea (cierre de 2 mm; el relleno de cavidades no se corrio, ver fila siguiente) deja fuera el canal sacro y los foramenes; si no, una perforacion hacia ellos da brecha nula (G-C1). En `capitulo3` §Amenazas, validez de constructo. Tambien en `introduccion` §Alcance, limitaciones de colocacion (desde r03, guia-3) | capitulo3-r04 (guia-2); texto corregido en r05 (T01) |
| `\GAPDEC` | Discrepancia en la envolvente osea: DEC D-O2.3 pto 1 fija cierre de 2 mm **y relleno de cavidades cerradas en 3D**; `e9ts_corredor.py`:307 y `e12_sap_control.py`:112 (usado por E13) solo aplican el cierre (el relleno solo existe en `e9_corredor.py`:99, version por HU). El texto describe lo corrido (G-T4, OC-5). En `capitulo3` §Corredor | capitulo3-r05 (T01); #127 |
| `\GAPDEC` | Metrica y analisis de dos desplazamientos de dominio del sintetizador: mascara umbralizada frente a cilindro liso (#95) y continuidad de valores de TC en el borde de `B_delta` (#96); `diseno_A.md` §7 (borrador) propone el salto de HU en el borde (G-C5). En `capitulo3` §Sintetizador. Tambien en `introduccion` §Alcance, limitaciones de apariencia (desde r03, guia-3) | capitulo3-r05 (guia-3) |
| `\GAPDEC` | Ubicacion de las regiones de medicion de la streak amplitude respecto de `B_delta`; fuera de la banda el sintetizador da amplitud nula por construccion; `diseno_A.md` §7 (borrador) mide dentro de `G` (G-C7, G-C5). En `capitulo3` §Apariencia | capitulo3-r05 (guia-2) |
| `\GAPDEC` | Metrica y analisis de la comparacion del realismo contra observaciones reales de artefacto (`tesis/main.tex`:127); `diseno_A.md` §7 E-A1 (borrador) propone resintetizar implantes reales de prueba (G-C5). En `capitulo3` §Apariencia. Tambien en `introduccion` §Objetivos, Obj 3 (desde r04, guia-5) | capitulo3-r05 (guia-3) |
| `\GAPDEC` | Que cambia entre dos corridas repetidas del protocolo fisico (componente "test-retest del brazo fisico" de `Delta`, D4 pto 4) (G-T2, P-MM3). En `capitulo3` §Apariencia | capitulo3-r05 (guia-1) |
| `\GAPDEC` | Reformular la pregunta de `introduccion` §Formulacion del problema (aun promete sintesis 2D, Dice, HD95 y comparacion con aumento convencional) para que coincida con los cuatro objetivos, y decidir si la Justificacion pasa antes de la Formulacion (embudo G-A9). En `introduccion` §Objetivos | introduccion-r00; ampliado en introduccion-r01 (guia-5); #126 |
| `\GAPDEC` | Por que la coherencia fisica y quirurgica debe establecerse antes de medir la utilidad para segmentacion, o si se justifica por si misma; ninguna fuente (TM, `docs/00-tesis.md`) da ese eslabon entre la necesidad y lo evaluado (G-A9). En `introduccion` §Justificacion | introduccion-r01 (guia-4, S04) |
| `\GAPDEC` | Que restricciones del muestreador cubriria la ablacion restriccion por restriccion excluida del alcance; el muestreador vigente perturba el eje del corredor y no condiciona por densidad (`capitulo3` §Poses), y ni `docs/00-tesis.md` punto 10 ni DEC 2026-09-17 B.1 las enumeran (G-A10, G-T2). En `introduccion` §Alcance | introduccion-r02 (guia-5) |
| `\GAPDEC` | Por que hace falta un sintetizador aprendido si la simulacion fisica de `peters2025hybrid` puede correrse sobre las poses del muestreador, como ya hace la comparacion del Obj 3 (`capitulo3` l. 219); ninguna fuente (TM, `docs/00-tesis.md`, DEC) lo escribe (G-A3, G-A4). En `introduccion` §Justificacion | introduccion-r03 (guia-1) |
| `\GAPDEC` | Razon declarada para restringir el implante al tornillo iliosacro y dejar fuera placas y otros tornillos; DEC 2026-09-11 (#41) fija la geometria parametrica pero no da la razon del tipo de implante (G-A10). En `introduccion` §Alcance | introduccion-r03 (guia-5) |
