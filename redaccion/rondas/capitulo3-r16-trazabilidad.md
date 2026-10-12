# Auditoria de trazabilidad — capitulo3 — r16

Entrada: `overleaf/secciones/capitulo3.tex` (400 lineas, estado tras la correccion r15), `capitulo3-r15-respuesta.md`
(sin RECHAZADO), `capitulo3-r16-lint.md` (PASA; 14 bajas E-P1, cifras propias con fuente abajo).

Comprobaciones de esta ronda:
- **Hallazgos r15 aplicados:** T01 (`:208`, "todavía en curso"), T02 (`:54`, `:271`, `:283-285`, Tabla), T03 (`:228`),
  T04 (`:377`), T05 (`:208`), T06 (`:317`), T07 (`:375`), T08 (`:210`), T10 (`:315`). Todos coinciden con su fuente.
- **Modelo unico (run04):** no quedan cifras de `mejor_37k`, run01/run02, 188.7, 5373, 815/1229, 47 casos ni de #164.
- **Recuentos nuevos:** coinciden con DEC 2026-10-11 (4) y DAT:149-158, salvo el orden pre/posoperatorio (T01).

Abreviaturas: DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; TES = `docs/00-tesis.md`; DAT =
`docs/02-datos.md`; EXP = `experiments/objetivo3/EXPERIMENTOS.md`; DAE = `experiments/objetivo3/diseno_A.md` ENMIENDA
2026-10-11 (:21-40); A17r4 = `a17_cotejo_resultado_run04.md`; A20r4 = `a20_resultados_run04.md`; ESTADO =
`docs/ESTADO.md`; R15 = fila del inventario de `capitulo3-r15-trazabilidad.md`, con texto sin cambios y cotejada de
nuevo.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4 | `capitulo3.tex:54` | "tenía su volumen anterior a la cirugía en entrenamiento y el posterior en prueba" | IMP #166 (:11712-11716: `0072` "fractura del ala iliaca, sin placa"; `0003` "placa con tornillos sobre esa misma ala"; "un estudio antes y otro despues de la osteosintesis"); IMP #166 pto 5 (:11741-11742: "`0003`: si [tornillo]; `0072`: no"); ESTADO:53 (`0072` pasa a grupo 2); DEC 2026-10-11 (:2434: "antes y despues de la cirugia", sin orden); DAT:146 (lista "`0003` (train) = `0072` (test), antes y después", orden ambiguo); `tesis/main.tex`:79 (sin orden) | La evidencia de #166 da el orden contrario. El volumen de entrenamiento (`0003`) tiene la placa, asi que es el posterior a la cirugia. El de prueba (`0072`) no tiene placa y hoy esta en el grupo 2, asi que es el anterior. DEC y `main.tex` no dan orden. DAT lo enumera de un modo que puede leerse al reves. El capitulo fija un orden que ninguna fuente afirma y que la evidencia contradice | "Un paciente, además, tenía un volumen en entrenamiento y otro en prueba, adquiridos antes y después de la cirugía." Si se quiere dar el orden: "el de entrenamiento, con la placa, es posterior a la cirugía, y el de prueba, anterior". Escalar a la autora: DAT:146 puede reescribirse sin orden implicito |
| T02 | media | G-T4, E-P3 | `capitulo3.tex:62` | "en el único paciente adquirido dos veces sin cambios en el implante, de par de reproducibilidad" | IMP #163 (:11531-11538: `0025`/`0026`, "Mismo montaje en las proyecciones", componentes casi iguales; :11512: `0019`/`0020`, "mismo equipo interno"); IMP #163 (:11573-11574: `0052`/`0053`/`0054`, "Tres volumenes"); IMP #156 (:11249: `0053` "tiene ademas un implante femoral") frente a IMP #163 (:11574: "`0054` tiene ademas un clavo femoral"); DAT:158 (`reproducibilidad` = 3) | **Patron PAT-39 reincide.** El parrafo `:54` ya cuenta siete adquisiciones secundarias. Al menos `0025`/`0026` es otro paciente adquirido dos veces con el mismo montaje, asi que "el único" ya no se sostiene. "Un segundo paciente adquirido dos veces" tampoco: segun #163 ese paciente tiene tres volumenes (`0052`, `0053`, `0054`). Ademas, #156 y #163 no coinciden en que adquisicion lleva el implante femoral. De eso depende que "esa adquisición queda fuera" sea cierto. Lo senalo el propio redactor (r15, "Para la autora" 2) | "...y, en un paciente adquirido dos veces sin cambios en el implante, de par de reproducibilidad. Otro paciente, con tres adquisiciones, tiene en una de ellas un implante femoral adicional, y esa adquisición queda fuera de las cohortes." Escalar a la autora: que adquisicion lleva el implante femoral (#156 dice `0053`; #163, `0054`) |
| T03 | media | OC-3, OC-2 | `capitulo3.tex:377` | "El sesgo que introducen en la prueba de equivalencia va, por tanto, hacia concluir equivalencia." | IMP #162 pto (3) (:11495-11510, **ABIERTA**: opciones (a) declarar el sesgo conjunto y (b) "ademas, reportar el TOST con un `Delta` alternativo no fijado por el difusor"); BITACORA §2 2026-10-10 (:364: "los sentidos registrados como hecho y el efecto conjunto en \GAPDEC"); respuesta r15 guia-1/T04 ("`\GAPDEC` retirado") | **Patron PAT-133 reincide.** La correccion de #171 completo el sentido del tercer elemento, que era parte del GAP. Pero #162 (3) sigue ABIERTA, y su opcion (b), una sensibilidad con un $\Delta$ no fijado por el sintetizador, no esta decidida. Al borrar el `\GAPDEC` entero, la prosa aplica la opcion (a) como si la autora la hubiera elegido y la (b) desaparece del documento. Contradice ademas la decision de redaccion de BITACORA §2. Los sentidos registrados son hechos y pueden quedar como estan | Mantener la prosa y anadir al final: `\GAPDEC{si, además de declarar el sesgo conjunto, se reporta la prueba de equivalencia con un margen no fijado por el sintetizador como sensibilidad descriptiva (implicancia 162)}`. Actualizar el estado de #162 en el documento (hoy dice tres `\GAPDEC`) |
| T04 | media | G-T4, E-P3 | `capitulo3.tex:208` | "Ninguno de los resultados que este documento presenta proviene de un modelo afectado." | IMP #171 (:11905: "ninguna cifra del modelo afectado"); `:212` (salto de borde medido "sobre ... un punto de control distinto del evaluado", `a6`, archivado por #166, IMP :11751); `:317` ("la medición del margen ... hecha con un modelo afectado, mostró que...") | **Patron PAT-39 reincide.** El mismo capitulo presenta dos resultados obtenidos con modelos afectados, aunque sin cifras: el salto de borde (`:212`) y la cercania al titanio que motivo la regla del material (`:317`). La fuente (#171) restringe la frase a las cifras | "Ninguna cifra que este documento presenta proviene de un modelo afectado." |
| T05 | baja | G-T4 | `capitulo3.tex:54` y `:109` | "Las auditorías de mismo paciente del 11 de octubre fijan los recuentos vigentes" | IMP #163 (:11514, :11590: pares observados y confirmados por la autora el 2026-10-10); IMP #166 (2026-10-11); DEC 2026-10-11 (4) (registro del recuento, 2026-10-11) | Las auditorias de #163 son del 10 de octubre y la de #166 es del 11. El 11 de octubre es la fecha del recuento que las aplica, no la de todas las auditorias | `:54`: "El recuento del 11 de octubre, que aplica las auditorías de mismo paciente, fija los recuentos vigentes." `:109`: "del recuento anterior al del 11 de octubre" |
| T06 | baja | G-T4, E-P3 | `capitulo3.tex:56` (y `:50`) | "De 103 pacientes sin osteosíntesis, 91 tenían localizado el nivel S1" | DAT:137 (grupo 2 = 37 + grupo 3 = 66 = 103, recuento de 2026-09-10); ESTADO:53 (`0010`, `0046`, `0072`, `0073` pasan del grupo 1 al 2 el 2026-10-10); DAT:158 (grupo 2 = 41) | **Patron PAT-31 reincide.** El 103 es correcto para la cohorte del Objetivo 2, construida con el recuento de la primera auditoria. Pero `:54` acaba de dar los recuentos vigentes, en los que el grupo 2 tiene 4 pacientes mas, y `:50` define la cohorte como "grupos 2 y 3" sin fecha. El lector puede esperar 107 | "De los 103 pacientes sin osteosíntesis de la primera auditoría, ..." |

Nota fuera de dominio, para el revisor de estilo o el lint: `capitulo3.tex:377` dice "da una emph{streak amplitude}",
sin la barra invertida. En el PDF sale la palabra "emph" y el termino sin cursiva.

## Inventario

Una fila por unidad verificable, en el orden del `.tex`. "R15" indica texto sin cambios desde r15, cotejado contra
la fuente de la fila de r15.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9-15, Fig. `fig:pipeline` | Dos componentes; compuerta; cuatro objetivos; SAP unica metrica propia; `M`, `B_delta`, `G` | R15 | si (R15) |
| :36 | Dice/HD95 y ablaciones fuera; 14 de 75; 178 de 1 184 | TES *Fuera de alcance*; `liu2021ctpelvic1k` | si (R15) |
| :38 | Compuerta negativa; Obj 2 ejecutado; `\GAPDATO`; congelado 9-10; enmienda 11-10 antes de procesar prueba; regla de realismo con informacion de prueba | DEC 2026-10-09 (6), (7); DAE:21-40; ESTADO:17 (`a15_final_run04` corriendo) | si |
| :42-46 | 103/75; MAR no reportada (Selles et al.); 2500 HU; revision 3D de 178; `\GAPDATO` multiplanar | R15; DAT:162 | si (R15) |
| :48 | SHA256; 168 = 65/37/66; 179 unidades; 10 + 1; "recuentos de la primera auditoria" | DAT:120, :136-137 | si |
| :50 | Aislamiento; validacion 8, prueba 34; Obj 3 reutiliza la particion; Obj 2 con grupos 2 y 3 | R15 | si; ver T06 |
| :52 | `0053` = `0054`, mismo implante pelvico; primaria por espaciado = entrenamiento; 33; 2.3 HU | IMP #156 (:11249-11259: 0.785 frente a 0.820 mm; maxima diferencia 2.25 HU) | si |
| :54 | 7 secundarios en entrenamiento, sin fuga, fuera del entrenamiento del sintetizador | DEC 2026-10-11 (4) pto 1; DAT:143-145 | si |
| :54 | Paciente compartido entre particiones; primario el de prueba; sale el de entrenamiento | DEC 2026-10-11 (:2434-2436); IMP #166 | si |
| :54 | "volumen anterior a la cirugía en entrenamiento y el posterior en prueba" | IMP #166 (:11712-11716, :11741-11742) | **no (T01)** |
| :54 | 166 volumenes = 159 pacientes; 118 (125), 8, 33; 20 + 13; 9/10/14 | DEC 2026-10-11 (4) pto 2; DAT:149-157 | si |
| :54 | 59/41/66 por volumen; conserva los secundarios | DAT:158-160 | si (59 + 41 + 66 = 166) |
| :54 | "auditorías ... del 11 de octubre" | IMP #163 (2026-10-10), #166 (2026-10-11) | precision **(T05)** |
| :56 | 103 -> 91 -> 72; control de nivel; 11 de 34; 7 de 57; 1 en el borde; 49 | IMP #132, #136 | si (R15); condicion del recuento **(T06)** |
| :58-60 | 20 de 30 (67 %); 10/15 y 10/15; medico recien egresado; 18 + 12; 7 y 5 | IMP #155 | si (R15) |
| :62 | Cuatro funciones del material ortopedico; fuste con HU bajos en tres pacientes | R15; IMP #155 | si |
| :62 | "el único paciente adquirido dos veces sin cambios"; "segundo paciente adquirido dos veces" con implante femoral | IMP #163 (:11531-11538, :11573-11574); IMP #156 (:11249) | **no (T02)** |
| :66-83 | Compuerta; exploracion previa; VAE SD 1.5; 150 HU; MAE; 25 HU; 20.2/12.3/12.74 HU; 2 x 3; ventanas; 20 000 HU; arcsinh; IC 95 %; orden a priori; 12 mm/2500 HU; Rombach; Guo; `\GAPDATO` del decodificador | fichas `karageorgos2024ddpm`, `yun2026simulationdriven`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi` | si (R15) |
| :87-111 | Zwingmann; Ziran 7-25 % y 140 %; Kaiser 5 y 10 mm; 0.42; TS 2.18.0; 6/3 mm; 0.1 %; 104 estructuras; 2 mm; 72; 8 mm; 9.5 (7.4-11.7) mm; 65.3/23.6 y 62.5/20.8 %; 29 y 27; 5 %; 16 = 14/2/0; 69 frente a 66; 61 de 61; 12 de 16; `\GAPDATO` (eje, sensibilidad, heuristica) | R15 fila :85-109 | si (R15) |
| :109 | 64 pacientes "del recuento anterior"; 57/7/6/48/29/17/3; 0 TS de la autora en CLINIC-metal | IMP #156 (:11260-11261); IMP #167 (:11806-11807) | si; fecha **(T05)** |
| :115-139, Tabla `tab:geometrias` | Ilion a ilion; McLaren; 4.91 mm; 7.0 mm; cabeza 8.0 x 4.5 mm; 4.8/4.9/4.7 mm; 79 de 43; 30 y 12 mm; `\GAPDEC` de la cabeza; 1.5 mm; 316L y Ti-6Al-7Nb; fabricantes (P-EA1) | R15 | si (R15) |
| :143-184 | 22-09-2026; anclaje; Ec. de pose; Tabla `tab:preinscripcion`; 95 %; 4 grados; 18 = 13/4/1; 39/36/33 mm; 69 de 72; `\GAPDATO`; Arand; Gardner | R15 | si (R15) |
| :188-192 | *Inpainting* 2.5D; arcsinh float32; regla del suelo y `\GAPDEC`; ControlNet sustituido | R15; IMP #141 ABIERTA | si (R15) |
| :194 | U-Net 64 (1, 2, 4, 8); $v$ + `\GAPLIT`; coseno 1000; AdamW 1e-4; lote 16 + `\GAPDEC` (#162 (1)); 256; 3 cortes; DDIM 50 | R15 | si (R15) |
| :196 | 5 semillas; misma porcion; corrida final en porcion compartida; control bit a bit | IMP #170 (:11880-11882); DAE:38-39 | si |
| :198 | Mezcla; 0.01 y 0.05; caso particular; 0.05 con modelos anteriores; calibracion con run04 en curso + `\GAPDATO` | DEC 2026-10-07; IMP #172 ABIERTA; ESTADO:14 (`a16` recalibrando, decision de la autora) | si (GAP justificado) |
| :200 | 12 mm; RMSE 7.57/11.45/11.63/54.82/57.69 HU; 1.4/1.8/0.7/0.5 | ficha `karageorgos2024ddpm` | si (R15) |
| :202 | 2500 HU; semimaximo + `\GAPDEC`; componente; eje sin perturbar; punto de control por cotejo; sin prueba | R15 | si (R15) |
| :204 | Tres reglas; 0.62 + `\GAPDATO`; supuesto no verificado; 5 de 40 | DEC 2026-09-21 | si (R15) |
| :206 | 14 182 parches de 39 casos; 896 de 3; secundarios; 3 componentes (pulsera x 2, DIU) | DEC 2026-10-11 (:2438-2440); EXP; IMP #167 (:11786-11795) | si |
| :208 | Paciente compartido; "modelos afectados"; prueba evaluada con uno; repetidos cotejo, $\Delta$ y copia y pegado; corrida final en curso | IMP #171 (:11892-11894); DEC 2026-10-11 (2) pto 4; ESTADO:17 | si |
| :208 | "Ninguno de los resultados ... proviene de un modelo afectado" | IMP #171 (:11905, "cifra"); `:212`; `:317` | **no (T04)** |
| :208 | Fijados con modelos afectados: cascara, cotejo frente a perdida, 0.05; observacion del material | IMP #157; DEC 2026-10-05 (6); IMP #172; DEC 2026-10-09 (5) | si |
| :210 | Tres desplazamientos; 0.62 (conjunto anterior) frente a 1.40 | DEC 2026-10-08 A.6-A.7 | si |
| :212 | 9 de 57; 4.91 mm; salto solo en la reconstruccion + `\GAPDEC`; una medicion con otro punto de control | IMP #139 | si (R15) |
| :214 | 60 000 pasos; minimo en 16 500; validacion sube, entrenamiento baja; candidatos 16 500 y 60 000 fijados antes; solo dos; 39 casos | IMP #168 (:11815-11818); DEC 2026-10-11 (2) pto 1 | si (#168 ABIERTA: hechos del log) |
| :216-222 | Tarea de sintesis; dos receptores con $D \geq 9$ mm, uno con cremallera; `\GAPDEC` de `0066` (#162 (2)); cascaras 1 mm; 0.896 mm; p50/p95 sobre 12-15 mm; medianas; p50/p75/p95 > 2500 HU; 2 tornillos; intervalo; desempates | R15; DEC 2026-10-11 (2) pto 1 | si (R15) |
| :224 | 12 de 24 frente a 10; sin empate; 342 frente a 243 HU | A17r4:15-18 | si |
| :226 | p95 bajo lo real en 8 y 10 de 12; `\GAPDEC` (#157); 3297/4641 frente a 3465/5283 HU; 810 frente a 160 HU | A17r4:11, :15-16, :26-28 ((3838 + 3092)/2 = 3465; (5262 + 5304)/2 = 5283) | si |
| :228 | Sensibilidad con el estado final; lectura conservadora; 749/1076 frente a 977/1238 HU; Ti 2051/1279 HU; el elegido mas cerca | A20r4:17-20; IMP #171 correccion (:11898-11903); TES Obj 3 | si |
| :231-259 | SAP, $D \geq 9$ mm; Smith; Ec. de brecha; 0/2/4 mm; tramo $T$ y 8 mm; 1 + 5 controles; 0.083 mm; 69/15/8/8 y 40/37/11.5/11.5 %; W1; 0.29/0.07/0.035 -> 0.395; 26 en 24 y 35 en 32; 15 de 72; restriccion rechazada | R15 fila :228-256 | si (R15) |
| :265-267 | Tres metricas; 150 HU; Sorensen-Dice; umbral adaptativo; 5 %; limitacion de Peters; escala 0-4; `\GAPDEC` de RMSE/SSIM | ficha `peters2025hybrid` | si (R15) |
| :271 | 33; 19 = 9 + 10; 14 sin metal; uno fuera por 1.62 mm; 13 | DEC 2026-10-11 (4) pto 3; DAT:154, :157; DEC 2026-10-09 (8) pto 3 | si |
| :273-279 | Anillos de 360 grados; guarda de un voxel; 12 mm; 8 mm; suelo; pose sin perturbar + `\GAPDEC`; 3.1/3.6/4.7 mm; n = 10; 51 frente a 25; uno de cada dos | R15; IMP #160 | si (R15) |
| :283 | Cohorte de diseno 19; MAE en `G`/`M`/`B_delta`; integridades; salto; por separado | DEC 2026-10-11 (4) pto 3; DEC 2026-10-09 (8) ptos 1-2 | si |
| :285 | >= 500 mm3; 10 mm3; 6 de dataset6 sin componentes; 13 = 9 + 4; 24 cortes; > 15 h; enmienda con errata | DEC 2026-10-11 (4) pto 3; DEC 2026-10-09 (8) pto 6; DAT:154-155 | si (10 - 6 = 4) |
| :287 | Lectura de las integridades; 150 HU fuera de `M` dentro de `G`; 2500 HU | DEC 2026-10-09 (8) pto 2 | si (R15) |
| :291-293 | Primario unico; sin lector clinico; control visual + `\GAPDEC`; tres contrastes; cordura | R15 | si (R15) |
| :297 | Tres brazos; 5371 HU; 1 781 741 voxeles; 14 182 parches; 39 casos; CatSim/XCIST; AAPM | DEC 2026-10-11 (3) pto 5; IMP #169 | si (R15) |
| :299-313 | 2D/MAR; 900 columnas; 1 000 vistas; 64; 138 mm; fractales; fantoma; tres materiales; $(\mathrm{HU}+1000)/1000$; cinco desviaciones; 459 mm; $[0.5, 3]$; `\GAPDEC` #158; `4cf3544`, `4993e87`, BSD; `\GAPLIT`; sonda (72 h; +/-20 HU; 2 %; triple; -2048; +237/+276; +3.9/+6.5; 72.8 = 10 166/140; 114.7 h; 108.9 h; ~54 h) | ficha `peters2025hybrid`; `sonda_peters.md`; IMP #146, #158 ABIERTA | si (R15) |
| :315 | Fe y Ti; A y B; uno de cada dos cortes; 2.5-10 mm; Fe preinscrito; 13; simulacion ya corrida; `\GAPDATO` de su evaluacion | DEC 2026-10-09 (3); EXP (`a19_final` CORRIDO); ESTADO:13 | si |
| :317 | Observacion con un modelo afectado; se mantiene con run04; 5380/2205 y 2051/1279 HU; 901-1057 y 1188-1360 HU | A20 (filas de Peters); A20r4:17-18; DEC 2026-10-09 (5) | si |
| :319-321 | 1 mm; replicas por semillas; Ti 7 de 24, Fe 0 de 24 (24 sobre lo real); 9895/5390 frente a 3092-3838 HU; 13 de 24 | `a21_resultado.md`; `sonda_peters.md`; A17r4:11 | si (R15) |
| :325 | Wilcoxon una cola, 0.05, pareado; 13; `\GAPDEC` del tamano de efecto | DEC D4 pto 2 | si (R15) |
| :327 | TOST frente a Ti; `\GAPDEC` #90; medianas; IC 90 % con *t*; 163.8 HU; `\GAPDEC` x 2; sensibilidades Fe, n = 10 y estado final | DEC 2026-10-11 (3); DAE:30-34; IMP #90 ABIERTA | si (R15) |
| :329 | Formula previa; $s_{\mathrm{sem}}$; $r_{\mathrm{rep}}$ con Fe; 2 receptores; 1.6 mm; 163.8 y 23.2 HU; Ti 0.4 y 5.2 HU | A20r4:4, :17-27; DEC 2026-10-09 (4) | si (R15) |
| :331 | Estado final: 100.3 HU; dos lecturas | A20r4:27; DEC 2026-10-11 (3) pto 4 | si |
| :335-337 | Realismo; tornillos aislados de prueba; regla; incierto fuera; placas fuera; `\GAPDATO` de la lista | DEC 2026-10-09 (7) (:2384-2394); IMP #167 (:11806-11807: solo da los pacientes de prueba con IS, no los de "otros aislados") | si (GAP justificado: la lista completa no consta) |
| :341, Tabla `tab:diseno` | Grado de cierre; congelado y enmendado; run04 entrenado antes de la enmienda; fila 3 con 13 sin metal y "13 de los 19" | DAE:21-23; DEC 2026-10-11 (2)-(4) | si |
| :363-367 | Circularidad; post hoc Obj 2; 11 de 34; 7 de 57; 91; 10/15; 7 de 15 frente a 2 de 15; $p = 0.109$; exploracion Obj 1; Guo | R15 | si (R15) |
| :369-371 | Percentil 5; sonda dos veces; cortes de solo banda; cascara y cotejo frente a perdida antes de run04; material; sensibilidad por la distancia en `M` | R15; IMP #169 | si |
| :373 | Regla de realismo con 3 de los 11 que entonces se contaban; tornillo no listado | DEC 2026-10-09 (7) (:2379-2380) | si |
| :375 | Prueba evaluada con un modelo afectado; cinco decisiones posteriores; tres por reglas previas; dos sin regla; conservadora; componentes identificados desde #109 | IMP #171 (:11892-11897); IMP #167 (:11789-11795); DEC 2026-09-10, 2026-10-05 (6), 2026-10-09 (4) | si |
| :377 | Tres elecciones sobre dos receptores; dos con los tornillos de un paciente; sentido registrado de las tres; 163.8 frente a 100.3 HU | IMP #162 (3); IMP #171 correccion; DEC 2026-10-09 (5); A20r4:26-27 | cifras si; GAP de #162 (3) retirado **(T03)** |
| :379-383 | Protrusion; `\GAPDATO` (canal y techo de S1); 2 mm; Tejwani 2.5/5.0 mm, $p = 0.3$; S1 asumido; equiespaciado; $h = 2\sigma$; truncamiento | fichas `smith2006iliosacral`, `tejwani2014` | si (R15) |
| :385 | Supuesto mascara-artefacto; 19 de 39 con objeto no ortopedico, en general fuera del cuerpo, sin recuento por objeto; regla por caso; Lin, Li | IMP #167 (:11777-11785), ABIERTA, como limitacion | si |
| :387-389 | Suelo; una sola ejecucion; dos materiales exageran; p95 bajo lo real; sentidos opuestos | IMP #141 ABIERTA; A17r4:30 | si (R15) |
| :391 | Tile B y C; Reilly 6 pelvis, 5-20 mm, 36-90 %; 20 de 30 | ficha `reilly2003effect`; IMP #155 | si (R15) |
| :393 | Fraccion local; S1 sin exactitud; 2D; desplazamientos; poses perturbadas fuera; 0 TS en 56; candidatos solo por forma | IMP #165, #167 (:11806-11808) | si (CSV de `0040` pendiente, T11 de r15) |
| :395-399 | 26 y 35; W1 sin prueba; `\GAPDATO`; multiplicidad; septimo candidato; $\Delta$ sobre 2 pacientes; corredores viables; 3 angostos; objeto; cortes distintos; 13 | R15 | si (R15) |
| global | Ninguna cifra de modelos afectados ni de #164 | busqueda (188.7, 5373, 815, 1229, 37 500, 140 000, 47 casos, -497.9, 0.959) | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet vigentes, "31-60 %", BFC/ISC) | `CLAUDE.md` raiz; TES | ausente; solo como exclusion (`:36`) o sustitucion (`:192`, figura) |
| global | Implicancias ABIERTAS (#90, #141, #157, #158, #162, #164, #165, #166, #167, #168, #170, #172) | revision del texto | todas como GAP, limitacion o hecho de registro, salvo #162 (3) **(T03)** |
| global | Claves `\cite` en `overleaf/referencias.bib`; E-F3; apellido = primer autor | sin claves ni citas nuevas desde r15 | si |
| global | Fabricantes y repositorios (P-EA1) | `:139`; repositorio AAPM con `\GAPDEC` y `\GAPLIT` | si |
| global | Patrones VIGENTES de BITACORA §1 en mi dominio (PAT-11, 19, 20, 31, 39, 116, 120-123, 133, 134, 138-144) | revision del texto | Reinciden PAT-39 (T02, T04), PAT-133 (T03) y PAT-31 (T06). No reinciden PAT-11, 19, 20, 116, 120-123, 134, 138-144 |
| global | Decisiones de BITACORA §2 respetadas | §2 2026-10-10 y decisiones de r15 ("modelos afectados", parametros heredados enumerados, cohorte de diseno frente a n efectivo, grupos por volumen) | si, salvo §2 :364 (efecto conjunto en `\GAPDEC`) **(T03)** |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al reescribir con un recuento nuevo, una exclusividad del recuento viejo ("el único", "un segundo") queda sin revisar | G-T4, E-P3 | "el único paciente adquirido dos veces sin cambios en el implante" (hay siete secundarios) | PAT-39 |
| Se retira entero un GAP cuya premisa se cumplio en parte, y la opcion abierta restante desaparece | OC-3, OC-2 | `\GAPDEC` del sesgo conjunto retirado con #162 (3) opcion (b) sin decidir | PAT-133 |
| Al resumir un par de la fuente ("A = B, antes y después"), el texto asigna un orden que la fuente no da | G-T4 | "su volumen anterior a la cirugía en entrenamiento y el posterior en prueba" | nuevo |
| Frase de transparencia de una implicancia que dice "cifra" se reescribe como "resultado", y el capitulo la contradice | G-T4, E-P3 | "Ninguno de los resultados ... proviene de un modelo afectado" | PAT-39 |
