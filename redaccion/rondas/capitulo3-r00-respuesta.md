# capitulo3 — r00 (redaccion inicial) — respuesta del redactor

Modo: redactar. Archivo: `overleaf/secciones/capitulo3.tex` (estaba en esqueleto). No hay reportes de
revision en esta etapa, asi que no hay tabla de hallazgos; se documenta lo redactado, la fuente de
cada cifra, los GAP y las decisiones de redaccion.

## 1. Resumen de lo redactado

Se respetaron los siete `\section` del esqueleto, sin cambiar titulos. Se anadieron `\subsection`
dentro de "Muestreador" (marco y corredor; aplicabilidad del marco con metal; geometria del implante;
distribucion de poses preinscrita) y de "Protocolo de evaluacion" (SAP; coherencia de apariencia;
resumen del diseno experimental).

| Seccion | Criterios de rubrica que cubre | Contenido |
|---|---|---|
| Parrafo de apertura + Vision general | G-C1, P-MM1, P-MM2 | Dos componentes + compuerta; los cuatro objetivos; definicion de `M`, `B_delta`, `G`; Figura `fig:pipeline` (diagrama de la cadena con `\fbox`, sin TikZ); fuera de alcance (Dice/HD95) y por que; estado de ejecucion; rediseno del Obj 3 declarado como posterior al No-Go |
| Datos y auditoria | G-C2, P-MM3, G-T4 | Inventario local 178/1184, correspondencia inferida, reconstruccion desconocida, cribado 2500 HU, unidad = paciente, grupos 1-3, regla de aislamiento, embudo 103->91->72 y 49, funciones de los 65 con metal |
| Validacion multiventana | G-C1, G-C5, G-C6, G-C8 | Por que existe la compuerta; ida y vuelta; Ec. (MAE por paciente); anclaje de 25 HU; 2 x 3 combinaciones; regla, IC bootstrap, orden a priori, No-Go; banda descriptiva; extension a MAISI por cota inferior. **Sin resultados** (van al cap. 4) |
| Muestreador | G-C1, G-C2, P-MM3 | Marco de Kaiser; mascaras TS (version, tarea, recortes, limpieza); envolvente osea; diametro; viabilidad 10 mm como convencion; caracterizacion del corredor en la cohorte; marco con metal (57/48/29); Tabla `tab:geometrias`; Ec. de pose y Tabla `tab:preinscripcion`; falsabilidad; segundo corredor; densidad como componente reportado |
| Sintetizador | G-C1, G-C2 | Inpainting de `G`, entradas/salidas, copia fuera de `G`; por que no ControlNet; `B_delta` y Karageorgos; pares de entrenamiento, unidad = componente, criterio R1-R3 (cualitativo), tres desplazamientos de dominio; arquitectura no congelada (GAPDEC) |
| Protocolo de evaluacion | G-C3 a G-C6, G-C8, G-C9 | Ec. de brecha, grados, tramo, grado 3 a lo no oseo, resolucion; Ec. de Wasserstein-1 ordinal; series clinicas; estratificacion post hoc y rechazo de restringir cohorte; metricas de Peters, criterio primario, tres brazos, adaptacion del protocolo fisico, Wilcoxon y TOST; preservacion fuera de `B_delta`; Tabla `tab:diseno` |
| Amenazas a la validez | G-C7 | Interna, constructo, externa y conclusion, cada una ligada a una decision o a un GAP |

## 2. Fuente de cada cifra

Cifras propias: de `tesis/main.tex` (TM), `experiments/objetivo2/preinscripcion_muestreador.md` (PRE),
`experiments/objetivo2/EXPERIMENTOS.md` (EXP), `docs/02-datos.md` (DAT) o `docs/01-decisiones.md` (DEC).
Cifras ajenas: con `\cite` y ficha en `docs/literatura/`.

| Cifra en el texto | Fuente |
|---|---|
| 1 184 volumenes de CTPelvic1K | `liu2021ctpelvic1k` (DAT cita Tabla 1, p. 3) |
| 178 locales; 103 en dataset6, 75 en dataset7; correspondencia inferida | DAT |
| 2500 HU de cribado | DAT; TM *Implant geometry*; DEC 2026-09-11 (3) |
| 178 volumenes = 168 pacientes; grupos 65 / 37 / 66; 10 excluidos; 1 de reproducibilidad | DAT (actualizacion 2026-09-10) |
| Grupo 2 = objetos no ortopedicos; grupo 3 = sin objeto | TM *Corridor measurement* ("11 of 34 patients with non-orthopaedic objects and 7 of 57 clean") + DEC 2026-09-14 (3) ("grupo 2: 11 de 34; grupo 3: 7 de 57") |
| 34 pacientes de prueba | TM Obj 1 |
| 103 -> 91 -> 72; 11 de 34; 7 de 57; 1 por borde del FOV; 49 de sensibilidad | TM *Corridor measurement*; DEC D-O2.2 |
| 30 casos (15 + 15) del cribado de fractura | #125 (solo dentro del `\GAPDATO`) |
| 150 HU | `peters2025hybrid` (ficha: Sec. 2.5, p. 5), `haneda2025aapm`; TM Obj 1 |
| 25 HU | TM Obj 1 |
| 20.2 HU (RMSE del algoritmo NMAR) y 12.3 HU | `karageorgos2024ddpm` (ficha: Tabla I, p. 28) |
| 12.74 HU | `yun2026simulationdriven`; TM Obj 1 |
| Ventanas [-1000, 2000], [-320, 480], [-160, 240] HU | `wang2025adaptiveweighting` (ficha); TM Obj 1 |
| Techo 20 000 HU; arcsinh sobre [-1000, 20 000] HU; techo de 2000 HU recorta metal | TM Obj 1 |
| IC 95 %, seis combinaciones | TM Obj 1 |
| 5 mm de holgura; 6.3 a 8 mm; 1 a 2 mm; 10 mm | `kaiser2014dysmorphism`; TM |
| 0.42 (fraccion <= 150 HU) | TM *Corridor measurement* |
| TotalSegmentator 2.18.0; 0.1 %; 104 estructuras | TM Obj 2; `wasserthal2023` |
| Cierre morfologico de 2 mm; estructuras de la envolvente; diametro = 2 x distancia libre minima | DEC D-O2.3 |
| Mediana 9.5 mm (RIC 7.4-11.7); 29 de 72 y 27; hasta 5 % | TM *Corridor measurement* |
| 16 casos en que difieren los recortes | #123; EXP §4 |
| 69 pacientes sin metal; 65 / 57 / 48 / 29; 7 por truncamiento; 17 con tornillo; 3 contaminados | TM *Field limitation* |
| 61 de 61 | #124 (solo dentro del `\GAPDEC`) |
| 6.5 a 8.0 mm | `gardner2010safezones` |
| 4.91 mm (cuerpo, mediana medida) | EXP §3 (E11, "de aqui sale el cilindro de 4.91 mm (D3)"); DEC 2026-09-20 (2) D3; TM ("4.91 ... sensitivity") |
| 4.8 mm de fuste; nucleo = fuste; 316L y Ti-6Al-7Nb | `synthes2003guide` (ficha `synthes_cannulated_65_73_guide.md`) |
| 4.9 mm de fuste y 4.7 mm de nucleo | `gardner2015screw` |
| 7.3 mm en la rosca, 4.8 mm en el fuste | `zhu2022optimalposition` |
| 7.0 mm (calibre); 4.91 y 7.3 como sensibilidad | `zwingmann2009navigated`; TM; DEC D-O2.4 |
| Cabeza 8.0 x 4.5 mm | `sayres2014comparison` |
| Arandela 1.5 mm | `doublemedical2021trauma` (ficha `doublemedical_trauma_catalogue.md`) |
| "mas del doble" de seccion | TM *Implant geometry* ("by more than a factor of two") |
| 22 de septiembre de 2026 (congelamiento) | PRE, encabezado |
| h = 5.0 mm; sigma_t = 2.5 mm; sigma_a por caso; 2.07 grados; L mediana 138 mm; 3 sigma; 50 poses; semilla 20260922 | PRE §3.1; TM *Pre-registration* (2.5 mm, 2.07, 50) |
| 4 grados (tolerancia no usada) | TM *Pre-registration*; PRE §3.1 |
| 18 volumenes; 13 / 4 / 1; 39, 36 y 33 mm | TM Obj 2 |
| ~12 mm de `B_delta` | TM Obj 3 |
| 7.57; 11.45 y 11.63 (1.4 y 1.8); 54.82 y 57.69 (0.7 y 0.5) | `karageorgos2024ddpm`; TM Obj 3 |
| 2500 HU para la mascara de entrenamiento; semimaximo como sensibilidad | DEC 2026-09-20 (2) D1 |
| 8 mm por extremo; 0.083 mm; grados (0,2), [2,4], (4, inf) | TM Expected Results; PRE §4 |
| Seis controles | EXP §5 (`e12_sap_control`, C1-C6) |
| 69/15/8/8 y 40/37/11.5/11.5 | `zwingmann2009navigated`; PRE §5 |
| 26 tornillos / 24 pacientes; 35 / 32 | `zwingmann2009navigated` (ficha: Abstract, p. 1833) |
| 150 HU, 5 % (definiciones de metricas de Peters) | `peters2025hybrid` (ficha: Sec. 2.5, pp. 5-6) |
| Alfa 0.05; IC 90 % del TOST | DEC 2026-09-20 (2) D4 (parametros de diseno, no resultados) |
| 2.5 y 5.0 mm; P = 0.3 | `tejwani2014`; TM |
| 5 a 20 mm; 36 a 90 %; seis pelvis; zona II; Tile B y C | `reilly2003effect`; TM *Field limitation* |

## 3. GAP abiertos, por tipo (texto literal de la marca)

**`\GAPDATO` (7)**

1. el sintetizador no ha generado todavía ninguna muestra sintética, así que no existe resultado del Objetivo~3 — (#116, ya en MAPA)
2. constancia de que la revisión multiplanar completa de cortes está hecha; el registro de datos solo acredita la revisión tridimensional — (NUEVO; `docs/02-datos.md`)
3. cribado ciego de fractura en 30 casos (15 de corredor estrecho y 15 de control), preparado y no realizado — (#125, ya en MAPA)
4. descripción del algoritmo de búsqueda del eje del corredor, que hoy solo consta en el código — (NUEVO; P-MM3)
5. revisión de la autora de los 16 casos en que los dos recortes difieren; la decisión que fijó el recorte por defecto quedó condicionada a ella — (#123, ya en MAPA)
6. eje medido del segundo corredor, necesario para muestrear poses en él; la corrida que lo mide no se ha lanzado — (NUEVO; PRE §7, D-O2.5)
7. implementación y resultados del brazo físico de Peters et al., no realizados — (#17, ya en MAPA)

**`\GAPDEC` (8)**

1. si se declara la segunda lectura del nivel S1 hecha por la autora sobre láminas, con su acuerdo de 61 de 61, y con qué límites — (#124, ya en MAPA)
2. definición operativa, por pose, de la fracción por zona de densidad que SAP reporta — (NUEVO; D-O2.6)
3. congelar la preinscripción del diseño del sintetizador: arquitectura, entrenamiento, muestreo y margen de equivalencia, hoy en borrador — (NUEVO; D4, `diseno_A.md`)
4. si SAP incorpora la dimensión angular de la escala de Smith et al. o declara que usa solo la de perforación, y con qué justificación — (NUEVO; #11)
5. definición operativa de la inversión de cada métrica de Peters et al. para evaluar síntesis — (NUEVO; #17, #16)
6. definición operativa de la inserción por copia y pegado, en particular el valor de HU asignado a $M$ — (NUEVO; `diseno_A.md` §7 en borrador)
7. si el brazo de equivalencia frente al protocolo físico se mantiene o pasa a trabajo futuro, contingencia de plazo registrada por la autora — (NUEVO; #90)
8. si se añade a la distancia de Wasserstein-1 un intervalo por remuestreo de pacientes, como análisis no preinscrito — (NUEVO; G-C8/G-C11)

**`\GAPLIT` (0).** No se abrio ninguno; `docs/literatura/_candidatos.md` no se toco.

## 4. Discrepancias entre fuentes que la autora deberia mirar

No se resolvio ninguna eligiendo por cuenta propia; se siguio el orden de autoridad de `MAPA.md`.

1. **Densidad.** `tesis/main.tex` (Obj 2, pregunta) dice que el muestreador esta *"constrained by bone
   density"*; D-O2.6 (`01-decisiones.md`) dice que la densidad es componente **reportado** de SAP y **no
   condiciona** el muestreo. Se redacto segun D-O2.6 (mayor autoridad). Conviene alinear `main.tex`.
2. **Cabeza del tornillo.** `main.tex` dice *"The head is modelled from ... sayres2014comparison"*; D3
   (2026-09-20 (2)) la deja como **variante de sensibilidad**. Se redacto como "cuando se modela" + sensibilidad.
3. **Tamanos de cohorte.** `main.tex` *Local cohort audit* aun dice *"Final cohort sizes remain pending this
   audit"*, pero las cohortes estan fijadas y usadas (DAT, D-O2.2). Se usaron las cifras; la frase de
   `main.tex` parece desfasada.
4. **Tamanos de prueba y validacion del Obj 3** (20 con metal, 14 sin metal, 3 de validacion con implante)
   constan en `01-decisiones.md` y `diseno_A.md`, no en `main.tex` ni en `EXPERIMENTOS.md`. Por la regla 5
   de `overleaf/CLAUDE.md` no se copiaron; el texto dice "pocos pacientes de validacion" y "muestras
   pequenas". Si la autora quiere las cifras en el documento, basta con declararlas en `main.tex`.
5. **Proporcion de parches de solo banda** (0.62 frente a 1.40): misma situacion que el punto 4; el texto
   la describe cualitativamente, como `main.tex`.

## 5. Lint

`python scripts/lint_redaccion.py capitulo3 --compilar`: compila (52 paginas el documento entero),
**alta 0, media 1, baja 4**; GAP lit/dato/dec = 0/7/8. `LINT: FALLA` solo por el hallazgo medio:

- **E-T3 "AI" (falso positivo).** Aparece dentro de la expansion del nombre propio del modelo,
  `MAISI (\emph{Medical AI for Synthetic Imaging})`, tomada de la ficha `guo2025maisi.md`. No es una
  sigla del documento. No se reescribio para esquivarlo.
- Bajas E-P1 (lineas con 34 pacientes, 2.5D, 12 mm, 8 mm): son cifras propias ya trazadas arriba o
  parametros de diseno; se dejaron.
- "NMAR" se retiro del texto: ninguna ficha da su expansion y definirla habria sido completar con
  conocimiento propio. Se describe como "el algoritmo que ancla la escala del protocolo de Peters et al.".

## Decisiones de redaccion

- **Compuerta (Go/No-Go):** *gate* del Objetivo 1 se traduce "compuerta", con *Go/No-Go* en cursiva la
  primera vez; el veredicto negativo se dice "veredicto negativo" o "No-Go".
- **Recortes de TotalSegmentator:** *default crop* = "recorte por defecto"; *robust crop* = "recorte
  alternativo" (evita "robusto", lista negra E-IA).
- **Segundo corredor:** siempre "segundo corredor bajo S1", nunca "S2" (TM Obj 2, #121).
- **Envolvente osea** para *bone envelope*; **diametro del corredor** para `D_TS_max`.
- **arcsinh** = "compresion arcoseno hiperbolico".
- **Referencia clinica / conjunto clinico de referencia** para el *benchmark* de Zwingmann; se evita
  "benchmark" en el texto corrido.
- **test-retest** = "prueba y reprueba"; **downstream segmentation** = "evaluacion de segmentacion posterior".
- **TOST** = "dos pruebas unilaterales de equivalencia (TOST, *two one-sided tests*)".
- **NMAR** no se nombra como sigla mientras ninguna ficha de su expansion.
- **Fuentes de fabricante** (`synthes2003guide`, `doublemedical2021trauma`) se senalan en el texto como
  "documentacion tecnica no revisada por pares" (P-EA1).
- **Resultados fuera del capitulo 3:** el cap. 3 describe la regla y el diseno; los veredictos
  (61.72 HU, distancias de Wasserstein-1, estratificacion) se dejan para el cap. 4. La caracterizacion de
  la cohorte (corredor, marco con metal, embudo) si va en el cap. 3, porque describe los datos de entrada.
