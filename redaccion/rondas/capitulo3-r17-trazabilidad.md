# Auditoria de trazabilidad — capitulo3 — r17

Entrada: `overleaf/secciones/capitulo3.tex` (406 lineas, estado tras la correccion r16), `capitulo3-r16-respuesta.md`
(sin RECHAZADO; T02 y T03 ESCALADOS), `capitulo3-r17-lint.md` (PASA; 12 bajas E-P1, cifras propias con fuente abajo).

Comprobaciones de esta ronda:
- **Hallazgos r16 aplicados:** T01 (`:54`, sin orden antes/despues), T03 (`:381`, `\GAPDEC` de #162 (3) repuesto), T04
  (`:212`, "Ninguna cifra"), T05 (`:54`, "el recuento del 11 de octubre, que las aplica"), T06 (`:60`, "de la primera
  auditoria"). Coinciden con su fuente. T02 se reviso de nuevo: ver T04 de esta ronda.
- **Sensibilidad del Obj 1 sin `0072` (guia-1 r16):** `:56` coincide con `experiments/objetivo1/p1_sin_0072.md`:20
  (61.08 HU; IC95 [54.23, 68.57]; n = 32).
- **Hecho nuevo desde r16:** IMP #172 (:11928-11937) registra la recalibracion **hecha**: 0.030 para `run04_mejor` y
  0.050 para `run04_60k`, con su consecuencia. El log existe (`experiments/objetivo3/outputs/a16_run04.log`:43, :59).
  El capitulo sigue diciendo que la calibracion "esta en curso" (T01, T02, T03).

Abreviaturas: DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; TES = `docs/00-tesis.md`; DAT =
`docs/02-datos.md`; EXP = `experiments/objetivo3/EXPERIMENTOS.md`; DAE = `experiments/objetivo3/diseno_A.md`; A17r4 =
`a17_cotejo_resultado_run04.md`; A20r4 = `a20_resultados_run04.md`; ESTADO = `docs/ESTADO.md`; R16 = fila del
inventario de `capitulo3-r16-trazabilidad.md`, con texto sin cambios y cotejada de nuevo.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-2, OC-3 | `capitulo3.tex:202` (y `:212`) | "Su calibración con el modelo evaluado está en curso \GAPDATO{...hasta entonces rige 0.05...}" | IMP #172 (:11928-11937: "Recalibracion hecha (2026-10-11)"; `run04_mejor` **0.030**, `run04_60k` **0.050**; "Pendiente de la autora: como aplicar el resultado"); `outputs/a16_run04.log`:43 ("ELEGIDO por el criterio: 0.030"), :59 (0.050); DAE:46 (diseno congelado: `delta = 0.05`) | **Patron PAT-122 reincide** (y PAT-11). La calibracion ya no esta en curso: termino y su resultado no es 0.05 para el modelo evaluado. El `\GAPDATO` dice que falta un dato que ya existe, y oculta la consecuencia que #172 registra. El cotejo (12 de 24), $s_{\mathrm{sem}}$ = 163.8 HU y la corrida final del principal se leyeron con 0.05 y no con su 0.030. Las cifras del estado final (100.3 HU, cotejo) si quedan con su valor calibrado. Lo que falta ahora es una decision de la autora, no un dato. `:212` repite el estado viejo ("hoy en recalibración") | `:202`: "Su calibración con el modelo evaluado, hecha con el mismo criterio, da 0.030 para el punto de control elegido y 0.050 para el estado final. Las cifras del estado final quedan así con su límite calibrado; las del elegido se calcularon con 0.05 \GAPDEC{cómo se aplica el límite calibrado de 0.030 al punto de control elegido, cuyo cotejo, margen $\Delta$ y corrida final se leyeron con 0.05, y si el diseño congelado, que fija 0.05, se enmienda (implicancia 172)}". `:212`: "y el límite de la lectura de HU, después recalibrado con el modelo evaluado" |
| T02 | alta | OC-3, G-T4 | `capitulo3.tex:38` (dentro del `\GAPDATO`), `:206`, `:228` | "el modelo que pasa a la evaluación ya está elegido" | IMP #172 ABIERTA (:11934-11935: "Como el cotejo elige el punto de control, la eleccion misma podria cambiar"); DEC 2026-10-11 (2) (regla del cotejo); A17r4:15-18 (12 frente a 10, leidos con 0.05) | Una implicancia ABIERTA reabre la eleccion del punto de control, y el texto la da por cerrada en tres lugares. `:228` es un hecho de registro solo si se lee con 0.05, pero el parrafo no lo condiciona y la condicion queda cuatro parrafos antes (`:202`). Nada en el capitulo dice que el resultado del cotejo puede cambiar con el limite calibrado | `:38`: "...y el modelo que pasa a la evaluación se eligió con el límite de lectura anterior a su recalibración (Sección~\ref{sec:sintetizador})". `:228`: "Con esa regla, y con la lectura de 0.05, gana el punto de control del paso 16\,500...". La remision de `:202` al `\GAPDEC` de T01 cubre que la eleccion podria cambiar; no hace falta un GAP nuevo |
| T03 | alta | G-T4, OC-5 | `experiments/objetivo3/EXPERIMENTOS.md`:47 frente a IMP #172 | (fuente) "`a16_calibrar_delta.py` ... CORRIDO: `delta = 0.05`" | EXP:47; IMP #172 (:11928-11931); `outputs/a16_run04.log`; EXP:11-13 ("Modelo vigente: run04"; lo medido con run01/run02 "no es citable") | **Patron PAT-138 reincide.** Las dos fuentes de contenido discrepan. EXP, que se declara al dia con run04, da 0.05 como resultado de `a16` sin decir que ese valor salio de un modelo archivado. No registra la corrida `a16_run04` (0.030 / 0.050). Un redactor que copie EXP (regla 5) escribiria un valor que el registro ya supero. El capitulo no copia EXP, pero la discrepancia es alta por regla del auditor | Escalar a la autora: actualizar EXP:47 ("CORRIDO con run04: 0.030 para `run04_mejor`, 0.050 para `run04_60k`, `outputs/a16_run04/`; la corrida con run01/run02, 0.05, archivada") y anadir la fila de `a16_run04`. No se toca el capitulo por esto |
| T04 | media | G-T4, OC-2 | `capitulo3.tex:66` | "\GAPDEC{qué adquisición de ese paciente lleva el implante femoral ... (implicancia 156) ... (implicancia 163)}" | IMP #164 (:11656-11659, aplicado el 2026-10-10 en las fuentes: `exclusiones.csv`, motivo de `metal_0053` "sin '0053 tiene ademas un implante femoral' (el clavo femoral es de `0054`)"); IMP #163 DECIDIDA (:11574: "`0054` tiene ademas un clavo femoral"); `experiments/exploration-3d/exclusiones.csv`:13 (`0053` secundario, sin implante femoral); IMP #156 (:11249, nota de origen del 2026-10-08) | **Patron PAT-19 reincide.** La discrepancia que motivo el escalado de r16 ya esta resuelta en el repositorio. El registro corrigio el 2026-10-10 la nota de origen de #156 y la fuente de datos: el clavo femoral es de `0054`, la adquisicion primaria, que sigue en entrenamiento. #163, que lo afirma, esta DECIDIDA. El `\GAPDEC` declara abierta una pregunta con respuesta registrada | Quitar el `\GAPDEC` y escribir: "Uno de esos pacientes tiene tres adquisiciones, y la primaria, que sigue en entrenamiento, lleva además un clavo femoral." Avisar a la autora de que el punto 1 de "Para la autora" de r16 queda resuelto por #164 :11658-11659. Actualizar MAPA (-1 `\GAPDEC`) |
| T05 | baja | G-T4, E-M4 | `capitulo3.tex:56` | "Como con el paciente del párrafo anterior, esa fuga solo puede favorecer un aprobado." | `:52` (`0053`/`0054`, dos parrafos antes); `:54` (el paciente compartido, el mismo de `:56`); `p1_sin_0053.md`; `p1_sin_0072.md`:22-23 | **Patron PAT-34 reincide.** El parrafo anterior (`:54`) trata del mismo paciente compartido que `:56`, no de otro. El paciente con el que se compara es el de `:52`. Ademas, `:52` no dice que su fuga solo pueda favorecer un aprobado: da solo la diferencia de 2.3 HU. La remision apunta a un parrafo que no contiene lo que se le atribuye | "Como con el paciente de la revisión en cortes, cuya otra adquisición también estaba en entrenamiento, esa fuga solo puede favorecer un aprobado." |

## Inventario

Una fila por unidad verificable, en el orden del `.tex`. "R16" indica texto sin cambios desde r16, cotejado contra
la fuente de la fila de r16.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9-15, Fig. `fig:pipeline` | Dos componentes; compuerta; cuatro objetivos; SAP unica metrica propia; `M`, `B_delta`, `G` | R16 | si (R16) |
| :36 | Dice/HD95 y ablaciones fuera; 14 de 75; 178 de 1 184 | TES *Fuera de alcance*; `liu2021ctpelvic1k` | si (R16) |
| :38 | Compuerta negativa; Obj 2 ejecutado; cadena sobre dos pacientes de validacion; congelado 9-10; enmienda 11-10 antes de procesar prueba; regla de realismo con informacion de prueba | DEC 2026-10-09 (6), (7); DAE:21-40; ESTADO:17 | si |
| :38 | "el modelo que pasa a la evaluación ya está elegido" | IMP #172 (:11934-11935) ABIERTA | **no (T02)** |
| :42-46 | 103/75; correspondencia inferida; MAR no reportada (Selles et al.); 2500 HU; revision 3D de 178; `\GAPDATO` multiplanar | R16; DAT:162 | si (R16) |
| :48 | SHA256; 168 = 65/37/66; 179 unidades; 10 + 1; primera auditoria | DAT:120, :136-137 | si (R16) |
| :50 | Aislamiento; validacion 8, prueba 34; Obj 3 reutiliza la particion; Obj 2 con grupos 2 y 3 | R16 | si (R16) |
| :52 | `0053` = `0054`, mismo implante pelvico; primaria por espaciado = entrenamiento; 33; 2.3 HU | IMP #156 (:11251-11252: 0.785 frente a 0.820 mm); `p1_sin_0053.md` (164.76 - 162.51 = 2.25) | si |
| :54 | Auditorias de identidad de paciente; recuento del 11-10; 7 secundarios sin fuga; paciente compartido sin orden; primario el de prueba | DEC 2026-10-11 (4) pto 1; DEC 2026-10-11 (:2434-2436); IMP #166 | si |
| :56 | Fuga del paciente compartido en la compuerta; afinado ajustado con el retirado; n = 32; 61.08 HU; IC95 54.23-68.57 HU; NO-GO sin cambio | `p1_sin_0072.md`:3-6, :20, :22; IMP #172 adenda (:11925-11927) | si |
| :56 | "Como con el paciente del párrafo anterior" | `:52`, `:54` | remision **(T05)** |
| :58 | 166 volumenes = 159 pacientes; 118 (125), 8, 33; 20 + 13; 9/10/14; 59/41/66 por volumen | DEC 2026-10-11 (4) pto 2; DAT:149-160 | si (R16) |
| :60 | 103 de la primera auditoria -> 91 -> 72; control de nivel (dos situaciones); 11 de 34; 7 de 57; 1 en el borde; 49 | IMP #132, #136 | si |
| :62-64 | 20 de 30 (67 %); 10/15 y 10/15; caso dudoso aparte; medico recien egresado; 18 + 12; 7 y 5 | IMP #132, #155 | si (R16) |
| :66 | Cuatro funciones; par de reproducibilidad "cuyas dos adquisiciones conservan el mismo implante"; demas repetidas secundarias o fuera | IMP #163 (:11531-11538); DAT:158 | si |
| :66 | Tres adquisiciones y una con implante femoral + `\GAPDEC` (#156 frente a #163) | IMP #164 (:11656-11659); IMP #163 (:11574); `exclusiones.csv`:13 | GAP injustificado **(T04)** |
| :66 | Tornillos fragmentados por umbral; fuste con HU bajos en tres pacientes | IMP #155 | si (R16) |
| :70-87 | Compuerta; exploracion previa; VAE SD 1.5; lectura del Obj 1; 150 HU; MAE; 25 HU; 20.2/12.3/12.74 HU; 2 x 3; dos volumenes de entrenamiento = adquisiciones de prueba; `\GAPDATO` del decodificador; ventanas de Wang; 20 000 HU; arcsinh; IC 95 %; orden a priori; 12 mm/2500 HU; Rombach; Guo | fichas `karageorgos2024ddpm`, `yun2026simulationdriven`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi`; IMP #156, #166 | si |
| :91-115 | Zwingmann; Ziran 7-25 % y 140 %; Kaiser 5 y 10 mm; 0.42; TS 2.18.0; 6/3 mm; 0.1 %; 104 estructuras; 2 mm; 72; 8 mm; 9.5 (7.4-11.7) mm; 65.3/23.6 y 62.5/20.8 %; 29 y 27; 5 %; 16 = 14/2/0; `\GAPDATO` (eje, sensibilidad, heuristica); 69 frente a 66; 64 antes del recuento del 11-10; 57/7/6/48/29/17/3; 0 TS de la autora; 61 de 61; 12 de 16 | R16 fila :87-111 y :109; IMP #156 (:11260-11261); IMP #167 | si (R16) |
| :119-143, Tabla `tab:geometrias` | Ilion a ilion; McLaren; 4.91 mm; 7.0 mm; cabeza 8.0 x 4.5 mm; 4.8/4.9/4.7 mm; 79 de 43; 30 y 12 mm; `\GAPDEC` de la cabeza; 1.5 mm; 316L y Ti-6Al-7Nb; fabricantes como documentacion no revisada por pares (P-EA1) | R16 | si (R16) |
| :147-188, Tabla `tab:preinscripcion` | 22-09-2026; anclaje; Ec. de pose; parametros; 95 %; 4 grados; tres controles; 18 = 13/4/1; 39/36/33 mm; 69 de 72 + `\GAPDATO`; Arand; Gardner | R16 | si (R16) |
| :192-196 | *Inpainting* 2.5D; arcsinh float32; regla del suelo con percentil 5 y `\GAPDEC`; ControlNet sustituido | R16; IMP #141 ABIERTA | si (R16) |
| :198 | U-Net 64 (1, 2, 4, 8); $v$ + `\GAPLIT`; coseno 1000; AdamW 1e-4; lote 16 + `\GAPDEC` (#162 (1)); 256; 3 cortes; DDIM 50; LeFusion | R16 | si (R16) |
| :200 | 5 semillas; misma porcion; porcion compartida; control bit a bit | IMP #170 (:11880-11882) | si (R16) |
| :202 | Mezcla; 0.01 y 0.05; caso particular; 0.05 fijado con modelos anteriores y criterio previo; cotejo, $\Delta$ y corrida final con 0.05 | DEC 2026-10-07; DAE:46; IMP #172 (:11932-11935) | si |
| :202 | "Su calibración ... está en curso" + `\GAPDATO` "hasta entonces rige 0.05" | IMP #172 (:11928-11937); `a16_run04.log`:43, :59 | **no (T01)** |
| :204 | 12 mm; RMSE 7.57/11.45/11.63/54.82/57.69 HU; 1.4/1.8/0.7/0.5 | ficha `karageorgos2024ddpm` | si (R16) |
| :206 | 2500 HU; semimaximo + `\GAPDEC`; componente; eje sin perturbar; punto de control "elegido por el cotejo"; sin prueba | R16; IMP #172 | hecho de registro con 0.05; eleccion reabierta **(T02)** |
| :208 | Tres reglas; 0.62 + `\GAPDATO`; supuesto no verificado; 5 de 40 | DEC 2026-09-21 | si (R16) |
| :210 | 14 182 parches de 39 casos; 896 de 3; secundarios; 3 componentes | EXP:26-27; IMP #167 | si (R16) |
| :212 | Reentrenamiento; modelos afectados; prueba evaluada con uno; repetidos cotejo, $\Delta$ y copia y pegado; corrida final en curso; "Ninguna cifra"; heredados (cascara, cotejo, limite) | IMP #171; EXP:76; R16 | si |
| :212 | "el límite de la lectura de HU, hoy en recalibración" | IMP #172 (:11928) | estado viejo **(T01)** |
| :214-216 | Tres desplazamientos; 0.62 frente a 1.40; 9 de 57; 4.91 mm; salto + `\GAPDEC`; una medicion con otro punto de control | DEC 2026-10-08 A.6-A.7; IMP #139 | si (R16) |
| :218 | 60 000 pasos; minimo en 16 500; candidatos 16 500 y 60 000 fijados antes; solo dos; 39 casos | IMP #168; DEC 2026-10-11 (2) pto 1; EXP:34 | si (R16) |
| :220-226 | Tarea de sintesis; dos receptores con $D \geq 9$ mm, uno con cremallera; 1.6 mm; `\GAPDEC` de `0066`; cascaras 1 mm; 0.896 mm; p50/p95 sobre 12-15 mm; medianas; p50/p75/p95 > 2500 HU; 2 tornillos de un paciente; intervalo; desempates | R16; ESTADO:305 (`0019`, 1.6 mm) | si (R16) |
| :228 | 12 de 24 frente a 10; sin empate; 342 frente a 243 HU | A17r4:15-18 | cifras si; sin la condicion de 0.05 **(T02)** |
| :230 | p95 bajo lo real en 8 y 10 de 12; `\GAPDEC` (#157); 3297/4641 frente a 3465/5283 HU; 810 frente a 160 HU | A17r4:11, :15-16, :26-28 | si (R16) |
| :232 | Sensibilidad con el estado final; 749/1076 frente a 977/1238 HU; Ti 2051/1279 HU; el elegido mas cerca; lectura conservadora | A20r4:17-20; IMP #171 correccion (:11898-11903) | si (R16) |
| :235-263 | SAP, $D \geq 9$ mm; Smith; Ec. de brecha; 0/2/4 mm; tramo $T$ y 8 mm; 1 + 5 controles; 0.083 mm; 69/15/8/8 y 40/37/11.5/11.5 %; W1; 0.29/0.07/0.035 -> 0.395; 26 en 24 y 35 en 32; 15 de 72; restriccion rechazada | R16 fila :231-259 | si (R16) |
| :269-271 | Tres metricas; 150 HU; Sorensen-Dice; umbral adaptativo; 5 %; limitacion de Peters; escala 0-4; `\GAPDEC` de RMSE/SSIM | ficha `peters2025hybrid` | si (R16) |
| :275 | 33; 19 = 9 + 10; 14 sin metal; uno fuera por 1.62 mm; 13 | DEC 2026-10-11 (4) pto 3; DAT:154, :157 | si (R16) |
| :277-283 | Anillos de 360 grados; guarda de un voxel; 12 mm; 8 mm; suelo; pose sin perturbar + `\GAPDEC`; 3.1/3.6/4.7 mm; n = 10; 51 frente a 25; uno de cada dos | R16; IMP #160 | si (R16) |
| :287-291 | Cohorte de diseno 19; MAE en `G`/`M`/`B_delta`; integridades; salto; >= 500 mm3; 10 mm3; 6 sin componentes; 13 = 9 + 4; 24 cortes; > 15 h; enmienda con errata; lectura de las integridades | DEC 2026-10-11 (4) pto 3; DEC 2026-10-09 (8) ptos 1-2, 6 | si (R16) |
| :295-297 | Primario unico; sin lector clinico; control visual + `\GAPDEC`; tres contrastes; cordura | R16 | si (R16) |
| :301 | Tres brazos; 5371 HU; 1 781 741 voxeles; 14 182 parches; 39 casos; CatSim/XCIST; AAPM | EXP:48; DEC 2026-10-11 (3) pto 5; IMP #169 | si (R16) |
| :303-317 | 2D/MAR; 900 columnas; 1 000 vistas; 64; 138 mm; fractales; fantoma; tres materiales; $(\mathrm{HU}+1000)/1000$; cinco desviaciones; 459 mm; $[0.5, 3]$; `\GAPDEC` #158; `4cf3544`, `4993e87`, BSD; `\GAPLIT`; sonda (72 h; +/-20 HU; 2 %; triple; -2048; +237/+276; +3.9/+6.5; 72.8 = 10 166/140; 114.7 h; 108.9 h; ~54 h) | ficha `peters2025hybrid`; `sonda_peters.md`; IMP #146, #158 ABIERTA | si (R16) |
| :319 | Fe y Ti; A y B; uno de cada dos cortes; 2.5-10 mm; Fe preinscrito; 13; simulacion ya corrida; `\GAPDATO` de su evaluacion | DEC 2026-10-09 (3); EXP:68 | si (R16) |
| :321-325 | Observacion con un modelo afectado; se mantiene con run04; 5380/2205 y 2051/1279 HU; 901-1057 y 1188-1360 HU; regla del material; Ti 7 de 24, Fe 0 de 24; 9895/5390 frente a 3092-3838 HU; 13 de 24 | `a20_resultados.md` (filas de Peters); A20r4:17-18; `a21_resultado.md`; `sonda_peters.md` | si (R16) |
| :329 | Wilcoxon una cola, 0.05, pareado; 13; `\GAPDEC` del tamano de efecto | DEC D4 pto 2 | si (R16) |
| :331 | TOST frente a Ti; `\GAPDEC` #90; medianas; IC 90 % con *t*; 163.8 HU; `\GAPDEC` x 2; sensibilidades | DEC 2026-10-11 (3); DAE:30-34; IMP #90 ABIERTA | si; 163.8 leido con 0.05 (cubierto por la correccion de T01) |
| :333-335 | Formula previa; $s_{\mathrm{sem}}$ 163.8; $r_{\mathrm{rep}}$ 23.2 con Fe; Ti 0.4 y 5.2 HU; estado final 100.3 HU; dos lecturas | A20r4:4, :17-27; DEC 2026-10-09 (4); IMP #172 (100.3 con su limite calibrado) | si |
| :339-341 | Realismo; tornillos aislados de prueba; regla; incierto fuera; placas fuera; `\GAPDATO` de la lista | DEC 2026-10-09 (7); IMP #167 | si (R16) |
| :345, Tabla `tab:diseno` | Grado de cierre; congelado y enmendado; run04 entrenado antes de la enmienda; fila 3 con 13 y "13 de los 19"; $\Delta$ = 163.8 HU | DAE:21-23; DEC 2026-10-11 (2)-(4) | si |
| :367-371 | Circularidad; post hoc Obj 2; 11 de 34; 7 de 57; 91; 10/15; 7 de 15 frente a 2 de 15; $p = 0.109$; exploracion Obj 1; fuga del afinado sin cambio de veredicto; Guo | R16; `p1_sin_0072.md` | si |
| :373-377 | Percentil 5; sonda dos veces; cortes de solo banda; cascara y cotejo antes de run04; material; sensibilidad por la distancia en `M`; regla de realismo con 3 de 11 | R16; DEC 2026-10-09 (7) | si (R16) |
| :379 | Seis decisiones posteriores, con la recalibracion; cuatro con criterio previo (incluido el de 0.05); dos sin regla; conservadora; componentes identificados antes | IMP #171 (:11892-11897); IMP #172 (:11928-11929: "mismo criterio preinscrito"); IMP #167 | si |
| :381 | Tres elecciones sobre dos receptores; sentido de las tres; 163.8 frente a 100.3 HU; `\GAPDEC` de #162 (3) | IMP #162 (3) ABIERTA; IMP #171 correccion; A20r4:26-27 | si |
| :383-389 | Protrusion; `\GAPDATO` x 2; 2 mm; Tejwani 2.5/5.0 mm, $p = 0.3$; S1 asumido; equiespaciado; $h = 2\sigma$; 19 de 39; Lin, Li | fichas `smith2006iliosacral`, `tejwani2014`, `lin2019`, `li2024`; IMP #167 | si (R16) |
| :391-395 | Supuesto del dominio de imagen; suelo; una sola ejecucion; dos materiales exageran; p95 bajo lo real | IMP #141 ABIERTA; A17r4:30 | si (R16) |
| :397 | Tile B y C; Reilly 6 pelvis, 5-20 mm, 36-90 %; 20 de 30 | ficha `reilly2003effect`; IMP #155 | si (R16) |
| :399 | Fraccion local; S1 sin exactitud; 2D; desplazamientos; poses perturbadas fuera; 0 TS en 56; candidatos por forma | IMP #165, #167 | si (R16) |
| :401-405 | 26 y 35; W1 sin prueba; `\GAPDATO`; multiplicidad; septimo candidato; $\Delta$ sobre 2 pacientes; corredores viables; 3 angostos; objeto; cortes distintos; 13 | R16 | si (R16) |
| fuente | EXP:47 (`a16` "CORRIDO: delta = 0.05") frente a IMP #172 | EXP:47; IMP #172; `a16_run04.log` | discrepancia **(T03)** |
| global | Ninguna cifra de modelos afectados ni de #164 | busqueda (188.7, 5373, 815, 1229, 37 500, 140 000, 47 casos, -497.9) | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigentes, "31-60 %", BFC/ISC) | `CLAUDE.md` raiz; TES | ausente; solo como exclusion (`:36`) o sustitucion (`:196`, figura) |
| global | Implicancias ABIERTAS (#90, #141, #157, #158, #162, #164, #165, #166, #167, #168, #170, #172) | revision del texto | todas como GAP, limitacion o hecho de registro, salvo #172 (estado viejo, T01; eleccion cerrada, T02) |
| global | Claves `\cite` en `overleaf/referencias.bib`; E-F3; apellido = primer autor | sin claves ni citas nuevas desde r16 | si |
| global | Fabricantes y repositorios (P-EA1) | `:143`; repositorio AAPM con `\GAPDEC` y `\GAPLIT` | si |
| global | Patrones VIGENTES de BITACORA §1 en mi dominio (PAT-11, 19, 20, 31, 34, 39, 116, 120-123, 133, 134, 138-149) | revision del texto | Reinciden PAT-122 y PAT-11 (T01), PAT-138 (T03), PAT-19 (T04), PAT-34 (T05). No reinciden PAT-20, 31, 39, 116, 120, 121, 123, 133, 134, 139-149 |
| global | Decisiones de BITACORA §2 respetadas | §2 2026-10-08 (hecho de implicancia ABIERTA dentro de la marca), 2026-10-10, 2026-10-11 (r15, r16) | si; la correccion de T01 sigue §2 2026-10-08 y §2 r16 ("parametro en recalibracion") |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que da "en curso" una medicion que ya termino, y calla el resultado y su consecuencia | OC-2, G-T4 | "Su calibración con el modelo evaluado está en curso" | PAT-122 |
| Una seleccion se da por cerrada aunque la recalibracion posterior de un parametro del que depende la reabre | OC-3, G-T4 | "el modelo que pasa a la evaluación ya está elegido" | nuevo |
| `EXPERIMENTOS.md` conserva el resultado del modelo archivado para un script que ya se corrio con el vigente | G-T4, OC-5 | "`a16_calibrar_delta.py` ... CORRIDO: `delta = 0.05`" | PAT-138 |
| Un GAP escalado por dos fuentes que se contradicen sigue abierto despues de que una entrada posterior corrigio una de ellas | OC-2, G-T4 | `\GAPDEC` del implante femoral (#156 frente a #163), corregido en #164 | PAT-19 |
