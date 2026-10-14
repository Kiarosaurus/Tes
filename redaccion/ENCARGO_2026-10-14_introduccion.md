# Encargo de redaccion — introduccion, 2026-10-14

Pedido por la autora en el chat: "Actualiza lo de T06 (00-tesis.md y tesis/main.tex), cierra T05 dado que ya fue la
comparacion con Peters y lanza un ciclo para introduccion". Lo ejecuta `/ciclo-redaccion introduccion` con **tope de 1
ronda** (r06). El redactor, en modo `corregir`, atiende este encargo ADEMAS de los hallazgos de los revisores.

Origen: hallazgo guia-4 de `redaccion/rondas/capitulo3-r19-guia.md` (ESCALADO): la introduccion anuncia un Objetivo 3
que ya no es el del capitulo 3.

**Alcance: SOLO `introduccion.tex`.** El capitulo 3 (r19) es la referencia de contenido para el Objetivo 3 y no se
toca. Capitulos 1, 2 y 4 tampoco.

Fuentes, en este orden: `overleaf/secciones/capitulo3.tex` (§Sintetizador, §Version 2 del sintetizador `sec:v2`,
§Apariencia, §Analisis estadistico, §Amenazas); `experiments/objetivo3/resultados_validacion_pose.md` §3;
`experiments/objetivo3/resultados_prueba_v1.md`; `experiments/objetivo3/v2_plan.md`; `docs/00-tesis.md` (actualizado
el 2026-10-14, T06); `docs/04-implicancias.md` #90 (CERRADA 2026-10-14), #174 (DECIDIDA), #175, #177, #182;
`docs/01-decisiones.md` 2026-10-13, 2026-10-14 y 2026-10-14 (2).

## I1. Desfases a corregir (guia-4)

- **:48** dice que el margen `Delta` esta "aun sin medir". Esta medido en validacion: 196.3 HU (`Delta = max(s, r)`,
  `s` del difusor; `run04_60k` 115.8 HU como sensibilidad). Se da como hecho medido, con remision al capitulo 3.
- **:56** dice que el protocolo de Peters et al. se ejecutara "sobre las poses del muestreador" y "segun el plazo".
  Se ejecuto, sobre el eje del corredor sin perturbar, en los 13 pacientes de prueba sin metal, como contraste
  primario. La razon de evaluar sobre el eje y no sobre las poses sigue siendo un `\GAPDEC` del capitulo 3: aqui va
  solo el hecho, sin inventar la razon. La consecuencia (no cubre las poses del muestreador) puede ir en una frase.
- **:90** (o donde diga que el modelo final no esta elegido): el punto de control esta elegido (`run04_mejor`, paso
  16 500, regla de cotejo fijada antes; 13 de 24 cascaras frente a 7).
- **`\GAPDEC` de la contingencia de plazo (#90):** #90 quedo CERRADA el 2026-10-14 por ejecucion. Se retira la marca y
  se dice el hecho: la comparacion de equivalencia se ejecuto.

## I2. Resultado del Objetivo 3 (version 1) y version 2, sin adelantar el capitulo 4

- Como ya se hace con el Objetivo 1, la introduccion puede decir el resultado medido en una o dos frases, con
  remision: en prueba no se concluye equivalencia con el protocolo fisico con titanio (diferencia media -301.0 HU,
  IC90 [-477.0, -124.9], `Delta` 196.3; el sintetizador da rayas mas debiles) y supera la copia y pegado (Wilcoxon
  p = 0.000122). #177 esta ABIERTA: entra como medicion, no como interpretacion.
- Version 2: una frase, a lo sumo. Es posterior al resultado de prueba de la version 1 y exploratoria; por la regla
  aprobada antes de generar "no mejora" (#182); el modelo principal sigue siendo la version 1. Sus resultados de
  prueba no existen aun: si hace falta nombrarlos, `\GAPDATO`.

## Lo que NO se toca

- Los demas `\GAPDEC`, `\GAPLIT` y `\GAPDATO` (hay propuestas en curso para los GAPDEC y GAPLIT; no se aplican aqui).
- El Objetivo 1, el Objetivo 2 ni el encabezado DESFASADO por #126, salvo contradiccion directa con lo de arriba.
- Implicancias ABIERTAS #176, #178-#182: no se afirma su lectura como hecho.
