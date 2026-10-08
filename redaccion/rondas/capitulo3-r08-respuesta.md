# capitulo3 — r08 — respuesta del redactor

Ronda **acotada**, como r07: no hubo reportes de `revisor-guia-cs`, `revisor-estilo` ni
`auditor-trazabilidad`. Las filas son los puntos del bloque A de `redaccion/ENCARGO_2026-10-07.md`
mas el hallazgo del lint. Fuentes de autoridad: `docs/01-decisiones.md` **2026-10-07**,
**2026-10-07 (2)** y **2026-10-05 (6)**, que entran como hechos (regla 3 de `overleaf/CLAUDE.md`).
Ninguna cifra de #149, #150, #151 ni #152 (ABIERTAS) entra al texto. El bloque B no se toca.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| A1. Lectura de HU del Obj 3 con `regla_suave`, `delta = 0.05`; la del Obj 1 como caso particular | orquestador (encargo) | APLICADO | Parrafo nuevo en §Sintetizador (`capitulo3.tex`:186), tras el de ControlNet. Describe la mezcla con el canal de ventana ancha como ancla, el peso por distancia al borde de la ventana (nulo bajo 0.01, lineal, completo desde 0.05) y el caso particular con los dos limites en 0.01. Verificado contra `src/common/ventanas.py`:67-91 (`peso_borde`, `regla_suave`) y `experiments/objetivo1/e6b_vae_sd15.py`:75 (`EPS = 0.01`) y :111-118 (`regla` v1). El motivo va en una oracion sin cifras, como pide el encargo. **No se usa el simbolo $\delta$**: ya designa el ancho de $B_{\delta}$ (PAT-14); se habla de "limite" de la rampa. **No se da el numero de pacientes de la calibracion**: DEC 2026-10-07 dice 5, y DEC 2026-10-05 (6) §2 fija la validacion en 3 (mismo criterio que r07, D11). Texto y cifras del Obj 1 (`capitulo3.tex`:62) intactos; el parrafo lo dice en su ultima oracion |
| A2. Criterio de seleccion del punto de control (DEC 2026-10-05 (6), detallada por 2026-10-07 (2)) | orquestador (encargo) | APLICADO, con `\GAPDEC` | Tres parrafos nuevos al cierre de §Sintetizador (`capitulo3.tex`:196-200): por que no la perdida de validacion ni la reconstruccion de implantes reales (DEC (6) §1); tarea de sintesis; perfil radial (cascaras de 0.5 mm, 0-12 mm, anillo completo, mediana y percentil 95 como elevacion sobre el anillo de 12-15 mm, agregacion corte -> paciente -> entre pacientes); histograma dentro de `M` (percentiles 50, 75 y 95 sobre voxeles > 2500 HU); las dos razones pedidas (fraccion > 2500 HU solo como control porque la mascara real se define con ese umbral; percentil 95 porque las rayas ocupan las colas); referencia = 3 pacientes de validacion con implante real; regla por envolvente con desempate y empate persistente a la autora; "con 3 pacientes el cotejo descarta, no prueba"; `\GAPDEC` por el tipo de implante no verificado; "ningun punto de control esta elegido" |
| A3. GAP del Obj 3 en §Vision general | orquestador (encargo) | APLICADO | `capitulo3.tex`:38. El hecho de la ejecucion va **dentro** del `\GAPDATO` (las tres implicancias que lo sostienen estan ABIERTAS): la cadena se ejecuto sobre dos pacientes de validacion y no existe aun resultado porque el modelo final no esta elegido, con remision a §Sintetizador. "Pose muestreada en S1" pasa a "pose sobre el corredor medido": #149 acredita el tornillo sobre el eje del corredor, no una pose perturbada. No se nombran `0101`/`0102` ni se dice "sin metal": `0102` tiene metal no ortopedico (cremallera, `docs/04-implicancias.md` l. 7725); se dice "pelvis sin osteosintesis" |
| A3 bis. Mismo arreglo en `introduccion` §Alcance y `capitulo2` §Comparacion critica y brecha | orquestador (encargo) | APLICADO, cambio minimo | Solo el texto del `\GAPDATO` (`introduccion.tex`:88, `capitulo2.tex`:102). Ambos dicen ahora que el sintetizador genero muestras sobre componentes metalicos reales (#133, #139) y que la cadena completa se ejecuto sobre pacientes de validacion, pero que no existe resultado del Obj 3 porque el modelo final no esta elegido. Nada mas se toco en esas secciones |
| Lint, E-O1 media, `capitulo3.tex`:198 (oracion de 52 palabras, mia) | lint r08 | APLICADO | Partida en dos |
| Lint, E-P1 baja, `capitulo3.tex`:198 | lint r08 | NO APLICADO | Son parametros de diseno de DEC 2026-10-07 (2), que no tiene clave bibliografica; ninguna marca GAP corresponde. Los otros cuatro E-P1 bajos (l. 73, 192, 217, 290) son anteriores y estan fuera del encargo |

Efecto colateral corregido al minimo, y se declara: escribir que la perdida de validacion no ordena
los puntos de control (DEC 2026-10-05 (6) §1) dejaba sin aviso la oracion de los 30 000 pasos, que
se apoya en el minimo de esa curva. Se anade, en el primer parrafo de A2, la consecuencia que DEC
(6) §3 registra: el argumento queda mas debil, la cifra se mantiene y se revisara cuando el
criterio este medido. El parrafo de los 30 000 pasos (`capitulo3.tex`:190) no se toco.

## GAP cerrados, reformulados y abiertos

| Marca | Que | Estado |
|---|---|---|
| `\GAPDATO` resultado del Obj 3 | ya no dice "no se ha ejecutado nunca" (cap. 3) ni "no ha generado ninguna muestra" (introduccion, cap. 2) | **REFORMULADO** en los tres sitios |
| `\GAPDATO` resultado citable de la calibracion del limite 0.05 sobre validacion | nuevo; las cifras de `a16` estan en #152, ABIERTA | **ABIERTO** |
| `\GAPDEC` verificacion del tipo de implante de los 3 pacientes de referencia | nuevo; DEC 2026-10-07 (2) la deja PENDIENTE | **ABIERTO** |

Totales del lint: `capitulo3` `alta=0 media=0 baja=5`, `GAP lit=1 dato=10 dec=24`, **PASA**
(antes `lit=1 dato=9 dec=23`). `capitulo2` `alta=0 media=0 baja=0`, `lit=1 dato=2 dec=10`, **PASA**
(sin cambio de totales). `introduccion` `alta=0 media=3 baja=1`, `lit=0 dato=5 dec=16`, **FALLA**
por tres E-O1 en las lineas 7, 13 y 21 (encabezado y formulacion, DESFASADO por #126), anteriores a
esta ronda y no tocados; la linea 88 editada no genera hallazgo. El orquestador instalo LaTeX y compilo el documento entero despues de esta respuesta: compila, 116
paginas, un Overfull de 4 pt en `capitulo3.tex`:200; la etapa queda cerrada (`redaccion/.build/etapas/capitulo3-r08.pdf`).

## Pendientes para la autora (no se resolvieron aqui)

1. **Pacientes de la calibracion de la rampa.** DEC 2026-10-07 dice "5 pacientes, 2 checkpoints";
   DEC 2026-10-05 (6) §2 fija la validacion en 3. El texto no da el numero.
2. **30 000 pasos frente a los puntos de control candidatos.** El capitulo fija el entrenamiento en
   30 000 pasos, y los candidatos de #149 estan en los pasos 37 500 y 140 000. No se escribio nada
   sobre ello (#149 ABIERTA), pero un lector que conozca los dos numeros vera la tension.
3. **Validacion "con implante real" frente a pelvis de validacion sin osteosintesis.** DEC (6) §2
   define el conjunto de validacion como los 3 pacientes de CLINIC-metal, y la cadena se corrio sobre
   dos pacientes de validacion de `dataset6`. El texto los distingue por su papel (receptores frente
   a referencia), sin afirmar a que conjunto pertenecen formalmente los receptores.

## Decisiones de redaccion

| Decision | Por que | Donde debe aplicarse igual |
|---|---|---|
| *checkpoint* se traduce **punto de control** (negrita y cursiva en su primera aparicion, `capitulo3` §Sintetizador) | no habia traduccion fijada; E-T2 | `capitulo4`, `conclusiones`, y cualquier mencion futura |
| El parametro `delta` de `regla_suave` no recibe el simbolo $\delta$: se nombra "limite" de la rampa (0.01 y 0.05, en la escala normalizada del canal) | $\delta$ ya es el ancho de $B_{\delta}$ (PAT-14) | `capitulo1` §TC y HU si se describe la lectura, `capitulo4` |
| La regla de lectura se nombra por su funcion ("lectura del Objetivo~1", "mezcla de canales"), no por el nombre del codigo (`regla`, `regla_suave`, v1, v2) | los nombres de funciones no son terminos del documento | todo el documento |
| Un hecho que solo sostienen implicancias ABIERTAS pero que el encargo autoriza a mencionar (la cadena se ejecuto) va **dentro** de la marca `\GAPDATO`, no en la prosa | regla 3 de `overleaf/CLAUDE.md`; mismo tratamiento que r06 dio a #133/#139 | `capitulo4`, `conclusiones` |
| p95, p50 se escriben "percentil~95", "percentiles~50, 75 y~95" | evita abreviatura sin definir | todo el documento |
