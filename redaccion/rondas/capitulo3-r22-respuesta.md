# Respuesta del redactor — capitulo3 — r22

Archivo: `overleaf/secciones/capitulo3.tex`. Ronda unica (encargo `redaccion/ENCARGO_2026-10-15.md`, seccion
"capitulo3"). Se atienden los reportes `-guia`, `-estilo`, `-trazabilidad` y `-lint` de r22, el encargo (16 `\GAPDEC`
cerradas con DEC 2026-10-15, puntos 1-22; asimetrias de #186 en Amenazas) y el aviso de capitulo1-r09 sobre
$\sigma_t$. Lint final: PASA (0/0/24 bajas E-P1 preexistentes o de prosa con cifras ya fuenteadas; GAP lit=1, dato=22,
dec=0), compilado, sin referencias indefinidas.

Regla aplicada a las mediciones nuevas (encargo): se describen como metodo, posteriores para v1 y previas solo al TOST
de prueba de v2, sujetas a la regla asimetrica; su resultado va en `\GAPDATO`.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| Encargo :143 cabeza | encargo | APLICADO | Desviacion de D3 declarada; sensibilidad sin ROIs a < 20 mm del extremo con cabeza, dos brazos (DEC pto 2). |
| Encargo :198 suelo | encargo | APLICADO | Regla no aplicable, tres razones, 225.0 / 1.2 HU frente a Delta = 196.3 HU (DEC pto 1; #186); sustituto simetrico en §Analisis. |
| Encargo :204 lote | encargo | APLICADO | "lotes de 16" + error de registro en prosa, sin GAP (pto 3). |
| Encargo :214 semimaximo | encargo | APLICADO | No se entrena por costo; diferencia de diametro como `\GAPDATO` (pto 4). |
| Encargo :228 costura | encargo | APLICADO | Dos brazos, restituida tras el congelamiento; perfil 8-16 mm en §Analisis; `\GAPDATO` (pto 5). |
| Encargo :232 `CLINIC_0066` | encargo | APLICADO | Grupo 2, sin cambio de receptores (pto 6). |
| Encargo :242 p95 | encargo | APLICADO | Diagnostico con su regla (>= 4 de 7 cascaras; control < mitad); `\GAPDATO` del desenlace (pto 7). |
| Encargo :317 preservacion | encargo | APLICADO | Caracterizacion de la referencia (RMSE, SSIM [-1000, 2000] HU, fuera de `G`, dentro del cuerpo), no resultado del sintetizador; `\GAPDATO` (pto 8). |
| Encargo :327 pose | encargo | APLICADO | Dos razones + exploratorio de 5 poses con expectativa fijada; `\GAPDATO` (pto 9). Sin la cifra de 108.9 h: BITACORA §2 2026-10-12 deja la sonda sin cifras. |
| Encargo :341 QC | encargo | APLICADO | Regla de muestra, cuatro defectos, no ciego para run04; comparacion a ciegas aparte, con su protocolo en `sec:v2` (pto 10). |
| Encargo :355 AAPM | encargo | APLICADO | Cita `xcist2026main`/`xcist2025example` en :353 y :351; Tabla `tab:desviaciones` con las cinco desviaciones (pto 11). Sin `\GAPLIT` nuevo. |
| Encargo :375 tamano de efecto | encargo | APLICADO | Degeneracion declarada (copia y pegado = 0; $p$ minimo $2^{-13}$), sin tamano de efecto (pto 12). Comparador parametrico en §Brazos. |
| Encargo :377 contingencia | encargo | APLICADO | Marca retirada sin prosa (pto 13). |
| Encargo :377 supuesto *t* | encargo | APLICADO | Supuesto enunciado; IC exacto por permutacion como sensibilidad posterior (pto 14). |
| Encargo :377 desenlaces | encargo | APLICADO | Tres desenlaces con remision a `sec:mt-estadistica` (definidos alli en capitulo1-r09), direccion, confirmatorio solo run04, multiplicidad, incertidumbre de Delta aparte (pto 15). |
| Encargo :433 margen | encargo | APLICADO | Margen minimo y margen comun 196.3 HU; sentido conjunto; 0.80-1.25 descartado con su motivo (pto 16). |
| Encargo: asimetrias #186 | encargo | APLICADO | Parrafo en validez de la conclusion: 62 341 frente a 124 679 voxeles, ruido de Peters 184 HU, suelo solo en el difusor; sensibilidades de ptos 1, 17 y 18. CV 0.076/0.241 (#185) como motivo de la lectura de acuerdo (pto 22), sin interpretacion. |
| Encargo: v2 margen comun y E-A1 0.03 | encargo | APLICADO | En :277, como metodo (ptos 16 y 19). |
| Aviso capitulo1-r09 ($\sigma_t$) | orquestador | APLICADO | :202 usa la notacion de `sec:mt-difusion`: $\mathbf{v}_n = a_n\boldsymbol{\xi} - s_n\mathbf{x}_0$ y $s_n^2 = 1 - a_n^2$ (ficha `salimans2022progressive`, fila "Relacion de varianzas"). $\sigma_t$ queda solo para el muestreador. |
| guia-1 | guia | APLICADO | Igual que "asimetrias #186". |
| guia-2 | guia | APLICADO | Parrafo nuevo en validez interna con lo fijado el 15-oct, lo visto (inventario fechado) y la regla general; :419 acotado a "decisiones de validacion"; :391 actualizado. |
| guia-3 | guia | APLICADO | :377 con los tres desenlaces; :453 reescrito ("se leeria como no equivalencia"); :463 sustituido. |
| guia-4 | guia | APLICADO | Igual que encargo supuesto *t*. |
| guia-5 | guia | APLICADO | Igual que encargo contingencia. |
| guia-6 | guia | APLICADO | Degeneracion + artefacto parametrico en §Brazos, posterior y descriptivo. |
| guia-7 | guia | APLICADO | :198, :419, :451 y :325 (fraccion de Peters bajo el suelo). |
| guia-8 | guia | APLICADO | :143 y §Analisis. |
| guia-9 | guia | APLICADO | :204. |
| guia-10 | guia | APLICADO | :214 y limitacion en validez de constructo (:447), sin cifra. |
| guia-11 | guia | APLICADO | :228 y §Analisis. |
| guia-12 | guia | APLICADO | :232. |
| guia-13 | guia | APLICADO | Parrafo nuevo tras :242. |
| guia-14 | guia | APLICADO | :317. |
| guia-15 | guia | APLICADO | :327 y :457. |
| guia-16 | guia | APLICADO | Parrafo nuevo tras :341. |
| guia-17 | guia | APLICADO | :351, :353, tabla. La fila de BITACORA §2 del 2026-10-10 ("sin cita ni URL") queda sin objeto (ver Decisiones). |
| guia-18 | guia | APLICADO | §Analisis y :433. |
| guia-19 | guia | APLICADO | §Analisis, con `\GAPLIT` de las fuentes de Bland-Altman y Pitman-Morgan (no hay ficha). |
| guia-20 | guia | APLICADO | :277 (ptos 16 y 19) y estado de :38 y del `\GAPDATO` de v2 ("interrumpido en validacion, espera relanzarse"). |
| T01 | trazabilidad | APLICADO | :248: "no concluyente respecto de la equivalencia, con una diferencia significativa a la baja"; el IC cruzo el limite inferior. |
| T02 | trazabilidad | APLICADO | Igual que guia-3. |
| T03 | trazabilidad | APLICADO | Igual que guia-7; se dice que el percentil 5 de la fraccion es el 95 de la perdida. |
| T04 | trazabilidad | APLICADO | :38, :248, :391 y parrafo nuevo en Amenazas. |
| T05 | trazabilidad | ESCALADO | `diseno_A.md`:29-33 conserva 163.8 / 23.2 / 100.3 HU; el `.tex` ya usa 196.3 / 6.1 / 115.8. Fuera de los archivos editables: la autora debe actualizar la ENMIENDA. |
| T06 | trazabilidad | ESCALADO | `00-tesis.md`:91, :174, :186-188, :319-321; `EXPERIMENTOS.md`:39-40; `resultados_prueba_v1.md`:27 quedan detras de la DEC (PAT-138). Los actualiza la autora (regla 14 raiz). |
| T07-T20 | trazabilidad | APLICADO | Cada uno como su fila de encargo. |
| T21 | trazabilidad | APLICADO | Artefacto parametrico en §Brazos, fuera de la tabla de diseno, con `\GAPDATO`. |
| T22 | trazabilidad | APLICADO EN PARTE | Asimetrias y sensibilidades aplicadas. RECHAZADO solo "la cifra de 184 HU no debe entrar": el encargo de la autora (`ENCARGO_2026-10-15.md`, Amenazas) pide expresamente 62 341 / 124 679 y la mediana de 184 HU, y BITACORA §2 2026-10-12 admite cifras medidas de una implicancia que la autora manda usar, sin su lectura interpretativa. Se dan sin la lectura de #186 ("del orden de Delta"). |
| T23 | trazabilidad | APLICADO | Lectura de acuerdo en §Analisis. El CV de #185 entra como motivo, por el encargo (misma base que T22). |
| T24 | trazabilidad | APLICADO | Igual que guia-20; E-A1 de v2 solo dentro del `\GAPDATO`. |
| T25 (baja) | trazabilidad | APLICADO | :242 da los valores por tornillo (3838 / 3092 HU; 5262 / 5304 HU) en lugar de medianas derivadas. |
| S1 | estilo | APLICADO | Park, Hwang y Seo: forma desde la mascara, $\lambda$ estimado por imagen (ficha `park2016MAR`). |
| S2 | estilo | APLICADO | "prueba de admision" (negrita en su definicion) en :265, :269 y en el `\GAPDATO`. |
| S3 | estilo | APLICADO | "ningun modelo de la version 2 reemplaza ...: los dos bajan $E$, pero no pasan la salvaguarda". |
| S4 | estilo | APLICADO | Causa del desenlace corregida (igual que T01). |
| S5 | estilo | APLICADO | :248 abre con el defecto. |
| S6 | estilo | APLICADO | "El orden va del modelo con menos cambios al que tiene mas". |
| S7 | estilo | APLICADO | :263 sin metadeclaracion; :269 "Esas cifras indican un efecto moderado" (no se repite 0.116, para no caer en PAT-86). |
| S8 | estilo | APLICADO | Causa y valor del sobremuestreo separados. |
| S9 | estilo | APLICADO | :357 dice el hecho. |
| S10 | estilo | APLICADO | "revisiones (*commits*)". |
| S11 | estilo | APLICADO | "guion de simulacion". |
| S12 | estilo | APLICADO | :425 partido; segunda remision eliminada. |
| S13 | estilo | APLICADO | :463 sustituido por el parrafo de tamano de muestra y multiplicidad. |
| S14 | estilo | APLICADO | "de modo que" quitado en :66, :68, :305, :309, :317, :325, :335, :357, :457, :463 y en dos oraciones nuevas; quedan 12 apariciones no senaladas. |
| S15 | estilo | APLICADO | "expresan ... pero sostienen que ... no quedan restringidos a la traza"; el canal no representa esas tres contribuciones (ficha `xia2024pndnet`). |
| S16-S21, S23 (bajas) | estilo | APLICADO | S16 con "Se probaron dos intervenciones"; S17, S18, S19 (frase de copia y pegado retirada de :248), S20, S21, S23. |
| S22 (baja) | estilo | NO APLICADO | "licencia BSD de tres clausulas" hace que el lint marque BSD como sigla sin definir (E-T3), y su desarrollo no consta en la ficha `xcist2025example`. Se mantiene "licencia de tres clausulas (BSD 3-Clause)". |
| S24 (baja) | estilo | NO APLICADO | "anillo" ya designa en el capitulo una banda de distancia (anillo de 12-15 mm) y la DEC usa "anillos de 2 mm"; cambiar a "cascara" tocaria tambien los pasajes de D1/D2 sin hallazgo. |
| guia-21, guia-22 (bajas) | guia | APLICADO | Categoria nombrada en :248; celda de Analisis de `tab:diseno`. |

Ademas, por longitud (lint E-O1, 18 oraciones nuevas de mas de 40 palabras) se partieron oraciones y se separaron tres
parrafos que superaban siete oraciones (receptores del cotejo, QC visual, amplitud de solo ruido).

**Aviso a la autora (fuera del encargo):** `experiments/objetivo3/resultados_dec_2026-10-15.md` (sin seguimiento en
git) ya trae resultados de D4 (diferencia de diametro, mediana -0.24 mm) y D8 (RMSE mediana 31.4 HU, SSIM 0.9069). Por
el encargo, quedaron como `\GAPDATO`; pueden entrar en una ronda posterior cuando el archivo se versione.

GAP: cerradas 16 `\GAPDEC`; abiertos 7 `\GAPDATO` (semimaximo, costura, p95, preservacion, poses, artefacto parametrico,
analisis anadidos) y 1 `\GAPLIT` (Bland-Altman / Pitman-Morgan, dos candidatos PENDIENTES en `_candidatos.md`);
reformulado el `\GAPDATO` de v2. `MAPA.md` actualizado.

## Decisiones de redaccion

- Analisis decidido despues de ver un resultado: se presenta como metodo con fecha ("el 15 de octubre, despues de ver
  la prueba de la version 1"), con la regla asimetrica (no puede elevar la categoria del desenlace) y su resultado en
  `\GAPDATO`; si su direccion esta declarada, se dice.
- Desenlaces del TOST: el cap. 3 no los vuelve a definir en negrita; remite a `sec:mt-estadistica` (capitulo1) y nombra
  "equivalencia", "no equivalencia", "no concluyente".
- Notacion de la difusion en el cap. 3: la de `sec:mt-difusion` ($a_n$, $s_n$, $\boldsymbol{\xi}$, $\mathbf{x}_0$);
  $\sigma_t$ y $\alpha$ quedan reservados para el muestreador.
- El repositorio del desafio AAPM se cita (`xcist2025example`) como fuente de la implementacion, y Peters et al. como
  fuente del protocolo; sustituye la fila de BITACORA §2 del 2026-10-10 ("sin cita ni URL mientras #158 este abierta").
- Prueba con la que el canal entro al entrenamiento: "prueba de admision"; "compuerta" queda solo para el Objetivo 1.
- Cifras medidas de implicancias ABIERTAS que el encargo de la autora manda usar (#185, #186) entran como medidas, con
  su particion, sin la lectura interpretativa de la implicancia.
