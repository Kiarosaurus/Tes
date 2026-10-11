# Auditoria de trazabilidad — capitulo3 — r13

Entrada: `overleaf/secciones/capitulo3.tex` (383 lineas, estado tras r12), `capitulo3-r12-respuesta.md`,
`capitulo3-r13-lint.md` (PASA; 14 bajas E-P1, todas cifras propias con fuente abajo). En r12 no hubo RECHAZADO
(E13 de r10 sigue RECHAZADO y no se reabre).
Ya escalado y no repetido como hallazgo: desfase de `docs/00-tesis.md`, `experiments/objetivo3/EXPERIMENTOS.md`,
`docs/02-datos.md` y DEC 2026-10-08 A.3 (lote 4 frente a 16). Los cuatro escalados de la respuesta r12 tampoco se
repiten. La unica excepcion es el de los receptores, que T01 reabre con un argumento nuevo: el dato esta en el
repositorio.

Comprobaciones pedidas:
- **Corrida final en prueba (jobs 55453-55455):** ninguna de sus cifras aparece. Las cifras del Obj 3 vienen de
  validacion (`0101`, `0102`, `metal_0039`), del diseno o del entrenamiento. Los `\GAPDATO` de `:38`, `:308` y
  `:328` siguen siendo verdad: segun `docs/ESTADO.md`:9-36, las salidas no se trajeron y quedan 8 pacientes sin
  revisar.
- **#158 sigue ABIERTA:** los hechos del repositorio AAPM estan en prosa; la cita esta en `\GAPDEC` (`:298`) y en
  `\GAPLIT` (`:300`). Correcto (OC-3).

Abreviaturas: DEC = `docs/01-decisiones.md`; IMP = `docs/04-implicancias.md`; DA0 = `experiments/objetivo3/diseno_A.md`
seccion 0; SON = `sonda_peters.md`; A17/A20/A21 = `a17_cotejo_resultado.md`, `a20_resultados.md`, `a21_resultado.md`;
COR = `experiments/objetivo2/e9ts_corredor.csv`; GRU = `experiments/exploration-3d/grupos.csv`; NIV =
`experiments/objetivo2/ts_nivel_s1.csv`; R12 = fila del inventario de `capitulo3-r12-trazabilidad.md`, con texto sin
cambios y cotejada de nuevo.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | media | G-T4, OC-2 | `capitulo3.tex:208` (prosa y `\GAPDEC`), `:380` | "dos pelvis ... cuyo corredor admite el tornillo"; "cuyo descarte no consta en las decisiones registradas" | DEC 2026-10-09 (4) pto 4 (:2306-2307: "solo `0101` y `0102` tienen receptor limpio con corredor viable (`0019` no cabe: corredor de 1.6 mm)"); COR (`default6mm`, F = 0.001): `D_TS_max` = 10.6 mm (`0101`), 12.4 (`0102`), 7.0 (`0046`), 8.9 (`0066`); criterio de SAP $D \geq 9$ mm (`:228`; DEC 2026-10-08 pto 16) | **Patron PAT-19 reincide.** El `\GAPDEC` afirma que el descarte no esta registrado, pero DEC (4) pto 4 lo registra: el motivo es la viabilidad del corredor. COR lo confirma con el criterio de SAP. `0046` (7.0 mm) y `0066` (8.9 mm) no llegan a 9 mm, y `0101` y `0102` si. El calificativo de la prosa, "cuyo corredor admite el tornillo", no separa a los receptores de los excluidos. Los cuatro corredores admiten el cuerpo de 4.91 mm. Pasa lo mismo en `:380`: el margen se midio en corredores viables ($\geq 9$ mm) y no solo en corredores que admiten el tornillo. La diferencia con los tres corredores angostos de prueba (3.1-4.7 mm) es mayor de lo que el texto dice | `:208`: "dos pelvis de validación sin osteosíntesis cuyo corredor es viable con el criterio de SAP ($D \geq 9$~mm), una de ellas con ...". Retirar el `\GAPDEC` o reducirlo a lo que falta: "la decisión de los receptores no dice qué criterio de viabilidad aplica". `:380`: "solo en receptores con corredor viable". Para la autora: confirmar que "corredor viable" en DEC (4) pto 4 es $D \geq 9$ mm |
| T02 | alta | G-T4, OC-5 | `capitulo3.tex:208` (`\GAPDEC`) | "las otras dos de validación sin ningún objeto metálico" | DEC 2026-09-21 (2) (:1385: `CLINIC_0046`, `CLINIC_0066`, `CLINIC_0101` "no llevan metal"); IMP #105 (:7726, igual); GRU:67 (`CLINIC_0066` = **grupo 2**, "objeto no ortopedico presente: borde FOV", `incierto`, `autora-regla`); NIV:64 (grupo 2); el propio capitulo `:48`/`:54` (grupo 2 = objetos no ortopedicos, de donde salen los 34 del control de nivel) | Las fuentes no coinciden entre si. DEC e IMP #105 dan `0066` como paciente sin metal. La clasificacion por grupos, que es la que usa el capitulo para el reparto 65/37/66 y para el embudo del Obj 2, lo pone en el grupo 2. El texto copia DEC y contradice su propia clasificacion. Es la misma etiqueta de grupo que corrigio T02 de r12, ahora aplicada a los no receptores | Si se mantiene una marca (ver T01), no calificar a esos dos pacientes como "sin ningún objeto metálico"; decir "las otras dos de validación sin osteosíntesis". Escalar a la autora: `0066` es grupo 2 en `grupos.csv` (objeto en el borde del campo de visión, incierto) y "sin metal" en DEC 2026-09-21 (2). Hay que decidir cual manda |
| T03 | baja | G-T4 | `capitulo3.tex:38` | "se fijó por escrito el 9 de octubre de 2026, antes de tocar ningún paciente de prueba" | DEC 2026-10-09 (7) (:2379-2380: la autora ya habia revisado en cortes 3 de los 11 pacientes de prueba con material); el propio capitulo `:358` | **Patron PAT-13 reincide (ERRADICADO).** La integridad se afirma mas fuerte que el registro. Cuando se congelo el diseno, la autora ya habia revisado en cortes tres pacientes de prueba, y el mismo capitulo lo dice en `:358`. DEC (6) usa "tocar" en el sentido de procesar, pero el lector de `:38` lo entiende en sentido literal | "antes de procesar ningún paciente de prueba" (coincide con la definicion de corrida final: "la única que procesa la partición de prueba") |

## Inventario

Una fila por unidad verificable, en el orden del `.tex`. "R12" indica texto sin cambios desde r12, cotejado de nuevo
contra la fuente de la fila de r12.

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :9 | Dos componentes; compuerta previa; transilíaco-transsacro | TM:74-80; IMP #130 | si (R12) |
| :13 | Cuatro objetivos; SAP unica metrica propia; nombres publicados | TM:80, :96; DEC 2026-09-08 | si (R12) |
| :15, Fig. `fig:pipeline` | Cadena, `M`, `B_delta`, `G`; copia fuera de `G`; caja final con realismo y reconstruccion | TM:77-79; DA0:27-28; DEC 2026-10-09 (7), (8) pto 1 | si |
| :36 | Dice/HD95 y ablaciones fuera; 14 de 75; 178 de 1 184 | `docs/00-tesis.md` *Fuera de alcance*; `liu2021ctpelvic1k`; DEC 2026-10-08 pto 28 | si (R12) |
| :38 | Compuerta negativa; Obj 2 con dos cohortes; `\GAPDATO` (dos pacientes de validacion, punto de control elegido, sin resultados en prueba); congelado el 9-10-2026; corrida final | DEC 2026-10-09 (6) pto 1; DA0:14-19; `docs/ESTADO.md`:9-36 | si; "tocar" **(T03)** |
| :42-46 | 103/75; MAR y monoenergetica no reportadas (Selles et al.); cribado a 2500 HU; revision 3D de los 178; `\GAPDATO` de la revision multiplanar | `docs/02-datos.md`; ficha `selles2024marreview` | si (R12) |
| :48 | SHA256; 168 = 65/37/66; 179 unidades; 10 fuera de uso y 1 par | `docs/02-datos.md`:120, :137 | si (R12) |
| :50 | Aislamiento; validacion 8, prueba 34; Obj 3 reutiliza la particion; Obj 2 sin division | DEC 2026-09-17 (3); DEC 2026-09-21 (2):1384 | si (R12) |
| :52 | 168 -> 167; 65 -> 64; prueba 33; a lo sumo 2.3 HU | IMP #156 (:11251-11264) | si (R12) |
| :54 | 103 -> 91 -> 72; control de nivel; 11 de 34; 7 de 57; 1 en el borde; 49 | IMP #132, #136 | si (R12) |
| :56-58 | Fractura en 20 de 30 (67 %); 10/15 y 10/15; medico recien egresado y ciego; 18 + 12; 7 y 5; "no es una coleccion de pelvis sanas" | IMP #155 act.; IMP :9074 | si |
| :60 | 64 pacientes; cuatro funciones; par de reproducibilidad; femoral adicional; fuste con HU bajos en tres pacientes | IMP #155 act.; IMP #156 | si (R12) |
| :64-81 | Compuerta; exploracion previa; VAE de SD 1.5; 150 HU; MAE; 25 HU; 20.2/12.3/12.74 HU; 2 x 3; ventanas de Wang et al.; 20 000 HU; arcsinh; IC 95 %; orden a priori; 12 mm y 2500 HU; Rombach et al.; cota de Guo et al. | fichas `karageorgos2024ddpm`, `yun2026simulationdriven`, `wang2025adaptiveweighting`, `rombach2022latentdiffusion`, `guo2025maisi` | si (R12) |
| :75 | `\GAPDATO` del ajuste del decodificador | `p1_decodificador_sd15.py` | si (R12) |
| :85-109 | Zwingmann et al.; Ziran et al. 7-25 % y 140 %; Kaiser et al. 5 y 10 mm; 0.42; TS 2.18.0, 6/3 mm, 0.1 %, 104 estructuras; cierre de 2 mm; 72 sin cambio; 8 mm; $D \geq d + 2\epsilon$; 9.5 (7.4-11.7) mm; 65.3/23.6 y 62.5/20.8 %; 29 y 27; 5 %; 16 = 14/2/0; 69 frente a 66; 64/57/7/6/48/29/17/3; 61 de 61; 12 de 16 | R12 fila :85-109 | si (R12) |
| :95, :101, :105 | `\GAPDATO` del eje, de la sensibilidad sin 2 casos y de la heuristica | IMP #121; DEC 2026-10-08 pto 22; `r1_landmarks.md` | si (justificados) |
| :113-137, Tabla `tab:geometrias` | Ilion a ilion; McLaren et al.; nominal = rosca; 4.91 mm; 7.0 mm; cabeza de 8.0 x 4.5 mm; 4.8/4.9/4.7 mm; 79 componentes de 43 volumenes; 30 y 12 mm; 6.5/7.3 mm; rosca de 16 mm; `\GAPDEC` de la cabeza; variantes no programadas; 1.5 mm; 316L y Ti-6Al-7Nb; fuentes de fabricante (P-EA1) | R12 fila :113-137 | si (R12) |
| :141-178 | 22-09-2026; anclaje; Ec. de pose; Tabla `tab:preinscripcion`; 95 %; 4 grados; 18 = 13/4/1; 39/36/33 mm; 69 de 72; `\GAPDATO` del segundo corredor | `preinscripcion_muestreador.md`; IMP #121, #153 | si (R12) |
| :180 | Densidad fuera; unica fuente invalidada por error de nivel y por la geometria de la region; Arand et al. | DEC :698 (#50: "refutado por dos mecanismos: el error de nivel y la geometria de la sonda"); DEC 2026-10-08 pto 14 (:2119-2120); ficha `arand2019pelvicring` | si (E2 de r12 aplicado) |
| :182 | Gardner et al.: zona segura menor en dismorficos, con un estudio previo sin diferencia | ficha `gardner2010safezones` | si (R12) |
| :186 | *Inpainting* 2.5D en dominio de imagen; copia fuera de `G`; arcsinh en float32; primera del orden a priori; "los dos entrenamientos" | DEC 2026-10-08 A.1-A.2; DA0:25 | si |
| :188 | Regla del suelo; colas del 5 %; percentil 5 post hoc; rama inaplicable; `\GAPDEC` | DEC 2026-10-05 (:1593-1619); IMP #141 ABIERTA | si (justificado) |
| :190 | ControlNet sustituido; presupone una base congelada | ficha `zhang2023controlnet`; DEC 2026-09-19 | si (retirado, presentado como sustituido) |
| :192 | U-Net con 64 canales, (1, 2, 4, 8), atencion en el nivel mas bajo; $v$; coseno de 1000 pasos; AdamW 1e-4; parche de 256; 3 cortes; DDIM con 50 pasos; 5 semillas; no RePaint ni LeFusion | DEC 2026-10-08 A.3-A.5 (:2085-2086); `a7_entrenar.sbatch`:61-63 | si (R12) |
| :192 | **Lotes de 16** + `\GAPDEC` (DEC da 4) | `a7_entrenar.sbatch`:60 (`--lote 16`); DEC :2086 ("lote 4"); IMP #134, #148 | si (T01 de r12 aplicado; DEC escalado) |
| :192 | `\GAPLIT` de la parametrizacion $v$ | MAPA | si (justificado) |
| :194 | Lectura por mezcla; limites 0.01 y 0.05; caso particular; `\GAPDATO` de la calibracion | DEC 2026-10-07 | si (R12) |
| :196 | 12 mm; RMSE de 7.57/11.45/11.63/54.82/57.69 HU; factores 1.4/1.8/0.7/0.5 | ficha `karageorgos2024ddpm` (Tabla III) | si (R12) |
| :198 | 2500 HU; semimaximo previsto como sensibilidad + `\GAPDEC`; unidad = componente; pose = eje sin perturbar; 37 500 de 60 000 pasos, minimo de validacion; sin pacientes de prueba | DEC D1 (:1205-1208: "semimaximo local por objeto entra como analisis de sensibilidad"); DA0 (no lo programa; `diseno_A.md`:170-171, :295 solo fuera de la seccion 0); DEC D2 | si (guia-2 de r12 aplicado) |
| :200-204 | Tres reglas; 0.62; supuesto no verificado; 5 de 40; tres desplazamientos; 0.62 frente a 1.40; 9 de 57; 4.91 mm; salto medido solo en la reconstruccion + `\GAPDEC`; una medicion | DEC 2026-09-21; DEC 2026-10-08 A.6-A.7; IMP #139 | si (R12) |
| :206 | Eleccion por cotejo; 30 000 pasos; candidatos 37 500 y 140 000; 144 500 pasos con la misma semilla; solo dos | DEC 2026-10-09 (2) pto 2 (:2247-2253); IMP #148 | si (R12) |
| :208 | Tarea de sintesis; dos estadisticos; lectura por mezcla; dos receptores sin osteosintesis, uno con cremallera | DEC 2026-09-21 (2) (:1386); DEC 2026-10-08 (3) (:2194); DEC 2026-10-09 (4) pto 4 | si en `0102` (T02 de r12 aplicado) |
| :208 | "cuyo corredor admite el tornillo" + `\GAPDEC` "descarte no consta" | DEC 2026-10-09 (4) pto 4 (:2306-2307); COR (10.6/12.4 frente a 7.0/8.9 mm) | **no (T01)** |
| :208 | "otras dos de validación sin ningún objeto metálico" | DEC :1385 frente a GRU:67 y NIV:64 (`0066` en grupo 2) | **no (T02)** |
| :210 | Cascaras de 1 mm, de 0 a 12 mm, en anillo completo; p50 y p95 sobre el anillo de 12-15 mm; medianas corte -> semilla -> paciente -> entre pacientes | DEC 2026-10-09 pto 1-2 (:2205-2212); DEC 2026-10-09 (5) pto 3 | si |
| :212 | p50/p75/p95 > 2500 HU; fraccion > 2500 HU solo como control; 2 tornillos de un unico paciente; propuesto en laminas y confirmado en cortes | DEC 2026-10-08 (2) (:2179-2187); DEC 2026-10-07 (2) | si |
| :214 | Fijador externo y placas; sin otras particiones; intervalo min-max; desempates; descarta y no prueba | DEC 2026-10-08 (2) (:2181-2186) | si (R12) |
| :216 | 0.5 mm: 8 frente a 7 de 46; pixel de 0.896 mm; 1 mm: 11 frente a 5 de 24; post hoc; se reportan los dos; 324 frente a 162 HU; reproducido identico | DEC 2026-10-09 pto 2-3, 6 (:2208-2222); A17 | si (R12) |
| :218 | p95 bajo lo real en 10 u 11 de 12 cascaras; 150-200 HU; ~900 HU; `\GAPDEC` (#157) | DEC 2026-10-09 pto 4 (:2215-2218); IMP #157 | si (justificado) |
| :220 | 47 pacientes; efecto de anadir pacientes no medido; 140 000 en lugar de 37 500 | DEC 2026-10-09 (2) pto 3 (:2254-2258) | si |
| :224 | Obj 4 sin fila; controles de identidad, monotonia y resolucion | DEC 2026-10-08 pto 23 | si (R12) |
| :228-252 | Dos componentes de SAP; $d$ = 7.0, $\epsilon$ = 1, $D \geq 9$ mm; Smith et al.; Ec. de brecha; 0/2/4 mm; tramo $T$ y 8 mm; 1 + 5 controles; 0.083 mm; 69/15/8/8 y 40/37/11.5/11.5 %; Ec. W1; 0.29/0.07/0.035 -> 0.395; 26 en 24 y 35 en 32; 15 de 72; 7 de 15; restriccion rechazada | R12 fila :226-250; DEC 2026-10-08 B ptos 15-20 | si (R12) |
| :258-260 | Tres metricas; hueso > 150 HU; volumen y Sorensen-Dice; umbral adaptativo; 5 % superior e inferior; limitacion de Peters et al.; escala 0-4 no trasladada; `\GAPDEC` de RMSE/SSIM con la region | PET:174-175, :189-200, :236, :430; TM:102 | si (T04 de r12 aplicado) |
| :264 | Verdad de terreno; 33 = 19 (11 + 8) + 14; uno fuera por pixel de 1.62 mm; 13 | IMP #156; DEC 2026-10-09 (8) pto 3 | si (R12) |
| :266-272 | Anillos de 360 grados; guarda de un voxel; 12 mm; 8 mm; desviacion declarada; fraccion en el suelo; pose sin perturbar + `\GAPDEC`; 3.1/3.6/4.7 mm; sensibilidad con n = 10; todos los cortes de `G`; 51 frente a 25; uno de cada dos | DEC 2026-10-09 (4) pto 1 (:2292-2297); DEC 2026-10-09 (8) pto 4; DA0 | si (R12) |
| :276-280 | Reconstruccion en 19 (11 + 8); MAE en `G`, `M`, `B_delta`; integridades; salto; >= 500 mm3; 10 mm3; 24 cortes; > 15 h; enmienda con errata | DEC 2026-10-09 (8) pto 1-2, 6 (:2404-2409); DA0:71-100 | si (R12) |
| :284 | Primario unico; solo metricas; lecturas humanas del Obj 2; control visual + `\GAPDEC` | DEC D4 pto 1; DEC 2026-10-08 pto 9 | si (justificado) |
| :286 | Tres contrastes; equivalencia primaria; realismo; cordura | DEC 2026-10-05 (3) pto 5; DA0:58-64 | si (R12) |
| :290 | 5373 HU; 1 978 270 voxeles; 17 149 parches; 47 pacientes; CatSim/XCIST; AAPM | DEC 2026-10-09 (8) pto 5 | si (R12) |
| :292-300 | 2D y MAR; 1 fila, 900 columnas, 1 000 vistas; dispersion escalada a 64; FBP; 138 mm; fractales; fantoma fisico; tres materiales; $(\mathrm{HU}+1000)/1000$; cinco desviaciones; 459 mm; $[0.5, 3]$; `\GAPDEC` de #158; `4cf3544`, `4993e87`, BSD 3-Clause; parche de una linea; `\GAPLIT` | PET; SON:87-119; IMP #146, #158 ABIERTA | si (R12) |
| :302-306 | Sonda en un paciente de validacion sin metal (`0101`, grupo 3); 72 h; +/-20 HU; 2 %; triple; salidas; -2048 HU; +237/+276; camilla; -1000 HU; +3.9/+6.5; 72.8 veces (10 166 frente a 140); 114.7 h en la primera corrida; 108.9 h; ~54 h | SON:132 ("114.7 h > 72 h"), :140 (114.7 / 108.9 h), :143; DEC 2026-10-09 (2) pto 1 | si (E10 de r12 cotejado) |
| :308 | Fe y Ti; replicas A y B; uno de cada dos cortes; acero en implantes espinales de 2.5-10 mm; Fe preinscrito; 13; control sin metal; `\GAPDATO` | DEC 2026-10-09 (3) (:2269-2276); PET:68 | si (R12) |
| :310-314 | 815/1229, 5380/2205, 2051/1279 HU; regla sin el sintetizador; Ti 7 de 24, Fe 0 de 24 (por encima en las 24); Fe 9895 y Ti 5390 frente a 3092-3838 HU; 13 de 24 | A20:45-48; DEC 2026-10-09 (5) (:2314-2349); A21:5, :9; SON | si (R12) |
| :318 | Wilcoxon de una cola, 0.05, pareado; 13; `\GAPDEC` del tamano de efecto | DEC D4 pto 2; `a24_contrastes.py`:87-96 | si (R12) |
| :320 | TOST frente a Ti; `\GAPDEC` de #90; medianas; IC 90 % con *t*; 188.7 HU; `\GAPDEC` del supuesto *t* y de los desenlaces; sensibilidades | DEC 2026-10-09 (6) pto 2 (:2360-2363); IMP #90 ABIERTA | si (justificados) |
| :322 | Formula previa; $s_{\mathrm{sem}}$; $r_{\mathrm{rep}}$ con Fe; 2 receptores; tercer paciente sin osteosintesis con un accesorio, fuera por 1.6 mm; 188.7 y 23.2 HU; Ti 0.4 y 5.2 HU | DEC 2026-10-09 (4) pto 2-4 (:2298-2307); DEC :1386 (`0019`, accesorio); A20:18-34 | si (T02 de r12 aplicado) |
| :326-328 | Realismo con dos estadisticos; tornillos aislados de prueba; fraccion por paciente; desglose; regla escrita antes; incierto fuera; placas excluidas; `\GAPDATO` de la lista | DEC 2026-10-09 (7) (:2371-2396) | si (justificado) |
| :332 | Grado de cierre por objetivo; congela la evaluacion y no el modelo; remision a amenazas | DA0:14-19; DEC 2026-10-09 (6) pto 1 | si (T03 de r12 aplicado en `:354`) |
| Tabla `tab:diseno` | Filas 1-3 (2 x 3, 25 HU, 34, IC 95 %; 72 y 49; W1; IC no preinscrito; estratificacion; 13; 19; Ti/Fe; TOST 188.7; cascaras; Wilcoxon) | R12 fila de la tabla | si (R12) |
| :354 | Circularidad; limpieza, ocupacion y estratificacion post hoc; escala de lectura, sensibilidad sin 2 casos e intervalo por remuestreo, posteriores a los datos; 11 de 34 y 7 de 57; 91 | DEC 2026-10-08 pto 17, 18, 22 (:2129-2145); IMP #132, #136 | si (PAT-140 no reincide) |
| :356 | 10/15 y 10/15; 7 de 15 frente a 2 de 15; $p = 0.109$, Fisher bilateral | IMP #132 | si (R12) |
| :358 | Exploracion previa; 25 HU anterior; rediseno posterior; cota de Guo et al.; percentil 5, ancho de cascara y material sin pacientes de prueba; regla de realismo con 3 de 11 revisados y un tornillo aislado fuera de la lista previa | DEC 2026-10-05 pto 4; DEC 2026-10-09 pto 2, (5); DEC 2026-10-09 (7) (:2379-2380) | si (guia-3 de r12 aplicado) |
| :360 | Punto de control, material y $\Delta$ sobre los mismos dos receptores; los dos primeros con los dos tornillos de un unico paciente; el material acerco el protocolo fisico al sintetizador; el margen facilita la equivalencia; `\GAPDEC` del efecto conjunto | DEC 2026-10-08 (3) (:2193-2194); DEC 2026-10-09 (5) pto 2 y contexto (:2314-2325); DEC 2026-10-09 (4) pto 3 (:2304-2305) | si (guia-1 de r12; sentidos registrados, GAP justificado) |
| :362-368 | Protrusion; `\GAPDATO` del canal y los foramenes; `\GAPDATO` del techo de S1; 2 mm de tornillos pediculares; Tejwani et al. 2.5/5.0 mm, $p = 0.3$; S1 asumido; equiespaciado; $h = 2\sigma$; aleacion; truncamiento; Lin et al., Li et al.; "Este trabajo asume" | fichas `smith2006iliosacral`, `tejwani2014`, `lin2019`, `li2024` | si (E3 de r12 sin cambio de contenido) |
| :370 | Suelo con sesgo a la baja; una sola corrida; regla sin conversion fijada | DEC 2026-10-08 A.12; IMP #141 ABIERTA | si (R12) |
| :372 | Los dos materiales exageran; p95 bajo lo real; sentidos opuestos | DEC 2026-10-09 (3) pto 4 (:2277-2282) | si (R12) |
| :374-376 | Tile B y C; Reilly et al., 6 pelvis, 5-20 mm, 36-90 %; 20 de 30; fraccion local; TS sin exactitud para S1; protocolo 2D; tres desplazamientos; poses perturbadas fuera | ficha `reilly2003effect`; IMP #132; DA0:127 | si (R12) |
| :378 | 26 y 35 tornillos; W1 sin prueba; `\GAPDATO` del intervalo; multiplicidad; septimo candidato | PRE; DEC 2026-10-08 pto 18 | si (R12) |
| :380 | $\Delta$ sobre 2 pacientes; $s_{\mathrm{sem}}$ frente a la mediana de 5 semillas; tercer paciente fuera por 1.6 mm; tres angostos en prueba; sin regla comun; un receptor con objeto no ortopedico | DEC 2026-10-09 (4) pto 3-4; DEC :1386; DA0:43-44 | cifras si; "admite el tornillo" **(T01)** |
| :382 | Cortes distintos por brazo; 13 pacientes | DEC 2026-10-09 (3) pto 2; DEC 2026-10-09 (8) pto 3 | si |
| global | Ninguna cifra de la corrida final en prueba | busqueda en el `.tex`; `docs/ESTADO.md`:11-36 | si |
| global | Contenido retirado (Dice/HD95 como objetivo, difusion latente o ControlNet como metodo vigente, "31-60 %", BFC/ISC) | `CLAUDE.md` raiz; `docs/00-tesis.md` | ausente; solo aparece como exclusion (`:36`) o sustitucion (`:190`, figura) |
| global | Implicancias ABIERTAS afirmadas como hecho (#90, #141, #157, #158) | revision del texto | ninguna; todas con GAP o con decision en DEC |
| global | Claves `\cite` en `overleaf/referencias.bib` | mismas claves que r12 (sin claves nuevas) | si |
| global | Cita como sujeto (E-F3); apellido = primer autor | sin cambios en las citas desde r12 | si |
| global | Fabricantes y repositorios (P-EA1) | `:137`; repositorio AAPM sin cita y con GAP | si |
| global | Patrones VIGENTES de BITACORA §1 en mi dominio (PAT-11, 19, 20, 31, 39, 116, 120-123, 133, 134, 138, 139, 140) y PAT-13 (erradicado) | revision del texto | Reinciden PAT-19 (T01) y PAT-13 (T03). No reinciden PAT-11, 20 (lote aplicado), 31, 39, 116, 120-123, 133, 134 (semimaximo con GAP), 139 y 140. PAT-138 esta escalado y no se repite |
| global | Decisiones de BITACORA §2 respetadas | §2 2026-10-10 (describir lo corrido + `\GAPDEC`; "sin osteosintesis" con el objeto; amenaza con los sentidos registrados) | si |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP que declara no registrada una razon que una DEC si da, aunque sea en forma escueta, y que los datos del repositorio confirman | G-T4, OC-2 | "cuyo descarte no consta en las decisiones registradas" (DEC: "corredor viable") | PAT-19 |
| Criterio de seleccion parafraseado con una condicion mas debil que la registrada, que no separa a los incluidos de los excluidos | G-T4, E-P3 | "cuyo corredor admite el tornillo" (criterio: corredor viable, $D \geq 9$ mm) | nuevo |
| Etiqueta de grupo tomada de una DEC que contradice la clasificacion por grupos que usa el capitulo | G-T4, OC-5 | "sin ningún objeto metálico" (`0066`, grupo 2 en `grupos.csv`) | nuevo (sigue al patron "etiqueta de grupo" de r12) |
