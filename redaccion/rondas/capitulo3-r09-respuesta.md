# capitulo3 — r09 (encargo acotado `redaccion/ENCARGO_2026-10-10.md`, sin revisores)

Alcance: solo diseno. Ninguna cifra de la corrida final en prueba (jobs 55453-55455: `a15_final`, `a19_final`,
`a23_final`, `a20`/`a24` sobre test). Las cifras de validacion que entran (`a20`, `a21`, sonda) son de diseno.

## Punto por punto

| Punto | Decision | Detalle (donde quedo en `capitulo3.tex`) |
|---|---|---|
| D1 Material | APLICADO | §Apariencia, tres parrafos tras la sonda: brazo con hierro (Fe) y titanio (Ti), replicas A y B, misma geometria y `M`, uno de cada dos cortes que toca `G`; hierro preinscrito por la analogia de tamano de Peters et al. (Tabla 2, ficha l. 68); cronologia explicita (se vio en validacion que el sintetizador queda mas cerca de Ti -> cambiar por eso seria elegir la referencia -> regla escrita antes, sin el sintetizador, contra los 2 tornillos reales -> gana Ti 7 de 24 frente a 0 de 24); "un cambio posterior a ver la comparacion en validacion"; los dos materiales "se reportan juntos y con el mismo detalle". Limitacion: los dos exageran el artefacto (9895 / 5390 HU frente a 3092-3838 HU; Ti sobre lo real en 13 de 24), el brazo es referencia y no la verdad, un paciente de referencia descarta y no prueba. Ademas: parrafo nuevo en §Amenazas, validez de constructo (dos brazos desplazados en sentidos opuestos; la equivalencia no implica cercania a lo real) y una oracion en validez interna (ancho de cascara y material cambiados tras ver validacion, sin pacientes de prueba) |
| D2 `Delta` | APLICADO | §Apariencia, parrafo propio: `Delta = max(s, r)` fijada antes de ver valores; `s` = rango entre 5 semillas; `r` = |A - B| con hierro (material preinscrito cuando se fijo la formula); por paciente y promediado sobre los 2 receptores de validacion; otro receptor fuera por corredor de 1.6 mm; s = 188.7, r = 23.2, `Delta` = 188.7 HU; "lo fija la variabilidad del propio sintetizador ... un margen mayor facilita concluir equivalencia". Repetido como amenaza en validez de la conclusion (2 pacientes; margen fijado por el sintetizador). Retirado el `\GAPDATO` de `Delta` en §Sintetizador y la frase "queda pendiente de preinscripcion" en §Resumen del diseno; quitado "3 pacientes con implante real" (version anterior de la definicion) |
| D3 Cortes de solo banda | APLICADO | §Apariencia, parrafo propio, sin el nombre de la opcion: el sintetizador genera todos los cortes que toca `G`; sin eso la desviacion valdria cero por construccion y la amplitud quedaria sesgada a la baja; 51 cortes con region frente a 25 generados en un paciente de validacion; cada brazo se mide en los cortes que produce, mismo dominio que `Delta` |
| D4 E-A2, n = 13 | APLICADO | §Apariencia: 14 sin metal -> fuera uno sin eje del corredor (pixel 1.62 mm) -> 13 ("sintesis sobre pelvis sin metal"); pose = eje del corredor sin perturbar (diseno_A §0; ver contradiccion 2); tres corredores mas angostos que el tornillo (3.1, 3.6, 4.7 mm frente a 4.91 mm) entran y se declaran, sensibilidad n = 10; TOST pareado frente a Ti, IC del 90 % con *t* de Student, n = 13, margen [-188.7, +188.7] HU; valor por paciente = mediana de 5 semillas / de replicas A y B; sensibilidad con hierro; Wilcoxon de cordura sobre los 13; declaracion de potencia (puede no concluirse equivalencia). "14" de E-A2 eliminado en el capitulo (antiguas l. 264, 266, 312). Tabla de diseno, fila 3, actualizada |
| D5 E-A1 y metricas adaptadas | APLICADO | §Apariencia, dos parrafos ("reconstruccion de implantes reales"): 19 de prueba con metal, 11 y 8 por separado (los 8 fuera de la distribucion de entrenamiento); unidad = componente > 2500 HU y >= 500 mm3 (entrenamiento admitia 10 mm3; 500 = umbral de la referencia del cotejo); tope de 24 cortes (sin el, > 15 h de GPU); MAE en `G`, `M` y `B_delta`; integridades adaptadas; salto en el borde de `G`; sin *streak amplitude*; agregacion por medianas; entro como enmienda antes de correr, con la errata del umbral. Parrafo de integridades reescrito: coeficiente de Sorensen-Dice y cambio relativo de volumen, hueso > 150 HU fuera de `M` y dentro de `G`, metal > 2500 HU; referencias por evaluacion; la escala 0-4 ya estaba excluida en el parrafo previo |
| D6 Referencia de realismo por regla | APLICADO | §Apariencia: realismo frente a los tornillos aislados reales de prueba, no frente a todos los implantes; parrafo de la regla (entra con >= 1 tornillo intraoseo aislado de cualquier tipo segun la revision de la autora; incierto sin tornillo confirmado fuera y declarado; solo tornillos aislados, placas y fijadores excluidos de las cascaras; fraccion de cascaras por paciente + desglose por tipo; no depende del material). `\GAPDEC` de #155 (2) CERRADO; `\GAPDATO` nuevo con la lista pendiente. La lista del agente no se escribio. El desglose se dice "por tipo de tornillo" y no "IS/TS frente a otros", porque el capitulo no define TS |
| D7 Fantoma desde el repositorio (#158) | ESCALADO | §Apariencia, parrafo nuevo con los hechos de #158 (el articulo no menciona la conversion en mapas de material, el tejido bajo el metal ni como entra el metal a lo largo del eje, con `\cite{peters2025hybrid}`; densidad `(HU + 1000)/1000` y realce de frecuencias tomados de los guiones del desafio AAPM del repositorio de ejemplos; `M` binaria identica; cuatro desviaciones). `\GAPDEC{si el repositorio del desafio AAPM se cita como fuente de la implementacion ... (implicancia 158)}`. Sin cita ni URL. El `\GAPLIT` previo de la referencia del repositorio se mantiene |
| D8 Sonda de Peters | APLICADO | §Apariencia, tres parrafos: criterios V1-V3 nombrados como primer, segundo y tercer criterio; salidas fijadas; corrida 1 fallida por 2 errores (relleno de -2048 HU en el realce, camilla) corregidos sin tocar criterios; corrida 2; VIABLE con submuestreo de un corte de cada dos; la sonda no calculo la amplitud del sintetizador. Cifras de `sonda_peters.md`, que coincide con #159; `EXPERIMENTOS.md` no las trae (contradiccion 4) |
| D9 HU de copia y pegado | APLICADO | §Apariencia: 5373 HU, mediana de 1 978 270 voxeles de metal de los 17 149 parches de entrenamiento (47 casos), corte central y mascara del componente; ningun paciente de validacion ni de prueba interviene; "solo fija la linea base del control de cordura". `\GAPDATO` CERRADO |

Correcciones al lado (no pedidas, porque el encargo las rompia):
- §Vision general, `\GAPDATO` del Obj 3: decia "el modelo final no esta elegido", falso desde checkpoint-r01 (PAT-122). Ahora: el punto de control esta elegido y los resultados sobre prueba no estan disponibles.
- §Sintetizador, `\GAPDATO` del suelo de -1000 HU: decia "`Delta`, aun no medido". Ahora: `Delta` esta fijado, la comparacion de la perdida con el no esta registrada (ni #141 ni DEC registran ese desenlace).
- §Resumen del diseno: el Obj 3 dice que el diseno de la evaluacion se congelo el 9 de octubre de 2026 antes de tocar prueba, y que lo congelado es la evaluacion y no el modelo, entrenado antes (diseno_A, encabezado de la seccion 0).
- §Apariencia, primer parrafo de inversion: la remision a las integridades pasa a "despues de las dos evaluaciones", porque su parrafo se movio tras la reconstruccion de implantes reales.

## Fuente de cada cifra

| Cifra | Fuente |
|---|---|
| 5373 HU; 1 978 270 voxeles; 17 149 parches; 47 casos | DEC 2026-10-09 (8) pto 5; `diseno_A.md` l. 64 (5373) |
| s = 188.7 HU, r = 23.2 HU, `Delta` = 188.7 HU | `a20_resultados.md` l. 23, 34, 38; DEC 2026-10-09 (4) (formula) |
| 815 / 1229 HU (sintetizador), 5380 / 2205 (Fe), 2051 / 1279 (Ti) | `a20_resultados.md`, tabla "Lectura en validacion" (validacion, no prueba) |
| 51 frente a 25 cortes | DEC 2026-10-09 (4) pto 1; #160 |
| 1.6 mm (receptor excluido) | DEC 2026-10-09 (4) pto 4 |
| 7 de 24 (Ti), 0 de 24 (Fe), Fe sobre lo real en 24, Ti sobre lo real en 13 de 24 | `a21_resultado.md` tabla; DEC 2026-10-09 (5) Resultado; #161 |
| 9895 HU (Fe), 5390 HU (Ti), 3092 a 3838 HU | `sonda_peters.md` l. 151-152 (exactas; el encargo da ~9900/~5400/3100-3800) |
| Tabla 2 de Peters: acero, implantes espinales 2.5-10 mm | ficha `peters2025hybrid.md` l. 68 |
| 2 % (desviacion de la validacion de Peters) | ficha `peters2025hybrid.md` l. 42 (3.1, p. 6); `sonda_peters.md` l. 57 |
| 72 h, +/-20 HU, 3 veces, 12-15 mm | `sonda_peters.md` l. 56-58 |
| +237 / +276 HU; -2048 HU; -1000 HU | `sonda_peters.md` l. 124-131 |
| +3.9 / +6.5 HU; 72.8 veces; 10 166 / 140 HU; 108.9 h; unas 54 h; k = 2 | `sonda_peters.md` l. 139-146; #159 |
| 459 mm | `sonda_peters.md` l. 104 |
| 13 pacientes; 1.62 mm; 3.1 / 3.6 / 4.7 mm; n = 10 | `diseno_A.md` §0 l. 50-56; DEC 2026-10-09 (8) ptos 3-4 |
| 19 = 11 + 8; 500 mm3; 10 mm3; 24 cortes; 15 h | DEC 2026-10-09 (8) ptos 1 y 6; `diseno_A.md` §0 l. 83-100 |
| 150 HU / 2500 HU en las integridades adaptadas | DEC 2026-10-09 (8) pto 2; `diseno_A.md` §0 l. 71-81 |
| 9 de octubre de 2026 (congelamiento) | DEC 2026-10-09 (6); `diseno_A.md` l. 14 |

## GAP

- Cerrados: `\GAPDATO` del HU de copia y pegado; `\GAPDATO` de `Delta` (§Sintetizador); `\GAPDEC` de la referencia de realismo (#155 (2)).
- Nuevos: `\GAPDEC` de como se cita el repositorio AAPM (#158); `\GAPDATO` de la lista de pacientes de la referencia de realismo.
- Reformulados: `\GAPDATO` del Obj 3 (§Vision general); `\GAPDATO` del suelo de -1000 HU.
- Totales del capitulo: 2/15/3 -> 2/14/3 (lit/dato/dec). Sin `\GAPLIT` nuevo, asi que `_candidatos.md` no cambia.

## Contradicciones entre fuentes (para la autora)

1. **n = 14 de E-A2 fuera de `capitulo3`, no tocado:** `capitulo1.tex`:122 ("Las pruebas pareadas se calculan sobre los 14 valores de los pacientes de prueba sin metal"). Tambien `docs/ESTADO.md` l. 57 y DEC 2026-10-09 (6) pto 2 dicen n = 14; manda (8).
2. **Poses de E-A2:** `diseno_A.md` §0 fija la pose del eje del corredor sin perturbar y excluye las poses perturbadas del muestreador. `introduccion.tex`:56 y `capitulo2.tex`:106 dicen que el protocolo fisico se ejecuta "sobre las poses del muestreador". No tocados; el cap. 3 ya sigue a `diseno_A.md`.
3. **Cabeza del tornillo:** `diseno_A.md` §0 dice "cilindro de 4.91 mm con cabeza, como en a11/a15"; `capitulo3` Tabla de geometrias y §Geometria dicen que `M` es un cilindro uniforme y que la cabeza es variante de sensibilidad. No tocado (fuera del encargo): decidir cual describe lo corrido.
4. **`experiments/objetivo3/EXPERIMENTOS.md` desfasado:** dice que `diseno_A.md` es BORRADOR y que falta `Delta`, da la sonda como pendiente y no tiene filas para `a18`-`a24`. Las cifras de D8 salen de `sonda_peters.md` (lo autoriza el encargo); la regla 5 de `overleaf/CLAUDE.md` nombra `EXPERIMENTOS.md` como fuente de cifras propias.
5. **Region de las integridades:** DEC 2026-10-08 pto 10 decia "en las mismas regiones que la *streak amplitude*"; `diseno_A.md` §0 y DEC 2026-10-09 (8) las calculan dentro de `G`, con 2500 HU para el metal. Se aplico lo posterior.
6. **Salto en el borde de `G`:** `capitulo3` §Sintetizador (DEC 2026-10-08 pto 7) dice que se mide en E-A2 "para los dos brazos que generan artefacto"; `diseno_A.md` §0 solo lo pone en E-A1. No tocado.
7. **"Mismo peso" de Fe:** el encargo pide reportar Fe "con el mismo peso" que Ti; `diseno_A.md` §0 da la fila de Fe como "descriptivo". Se escribio "se reportan juntos y con el mismo detalle", y la decision sigue recayendo en el contraste con Ti.
8. **Cifras de validacion del brazo fisico frente al sintetizador** (815/1229 frente a 5380/2205 y 2051/1279 HU): entran como hecho de diseno, porque explican la cronologia del material (#161 DECIDIDA). Si la autora prefiere no adelantarlas, basta con quitar esa oracion.
9. `redaccion/MAPA.md`, fila del `\GAPDEC` "tipo de implante de los 3 pacientes de referencia": esa marca ya no esta en el capitulo (la autora confirmo en cortes; tornillos-r01). La fila sigue abierta en MAPA; no la toque porque no es de esta ronda.

## Decisiones de redaccion

- E-A1 = "**reconstruccion de implantes reales**"; E-A2 = "**sintesis sobre pelvis sin metal**" (negrita en su primera aparicion). Las etiquetas E-A1/E-A2 no aparecen en el texto.
- Materiales: "hierro (Fe)" y "titanio (Ti)" la primera vez; despues, solo la palabra.
- Repeticiones del brazo completo = "replicas A y B"; "corrida" queda para las corridas de la sonda y la corrida final (evita PAT-14).
- `a18` = "**sonda de viabilidad**"; sus criterios V1-V3 = "primer, segundo y tercer criterio".
- Una opcion de linea de comandos (`--incluir-banda`) se describe por lo que hace, sin su nombre.
- El repositorio AAPM = "los guiones del desafio AAPM incluidos en el repositorio de ejemplos"; sin cita ni URL mientras #158 este abierta.
- Cambio de diseno posterior a ver validacion: se dice como hecho ("un cambio posterior a ver la comparacion en validacion"), sin "y asi se declara" (PAT-5).
