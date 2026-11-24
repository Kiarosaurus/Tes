# CONSOLIDACION (F4) — contraste de A..G sin votacion; los informes originales no se modifican
Fecha: 2026-11-24. Cada afirmacion grave se contrasto con el material (review/ y repo original). "VERIFICADO" = comprobado por el orquestador en archivo:linea.

## 1. Coincidencias entre revisores independientes
| Tema | Revisores | Verificacion |
|---|---|---|
| Duplicacion argumentativa intro/cap1/cap2/cap3 (brecha, contribucion, banda 12 mm, escala Smith, difusion); intro y cap3 contienen resultados y cronologia | A, B | Texto leido por ambos; reubicacion a cap4/anexos |
| Falta de diagramas (2 figure en cap1-4; 0 includegraphics/tikz) y figuras propuestas casi identicas (pipeline, compuerta, corredor, SAP, difusion/inpainting, streaks) | A, B, D | VERIFICADO (inventory) |
| La particion de prueba/validacion ya no es independiente; ocho decisiones sobre 0101/0102 y los 13 de prueba | C (C-04), F (H1), E (E-02), D (MED-08) | VERIFICADO: cap3:602-604 admite que el diseno de ajuste fino y la metrica angular se decidieron conociendo la prueba; Delta=196.3 = media de 291.6 y 100.9 (resultados_validacion_pose.md:51) |
| El criterio visual (c) no es prueba de Turing: lectora unica, 6 paneles/brazo, sin anclas | C, D (MED-06), E (E-05), F (H2) | Puntajes reproducidos exactamente con la clave (ver verificacion de la clave de c2b) |
| Delta/margen de equivalencia endogeno (crece con la variabilidad del modelo) | C, E (E-07), F (H3) | cap3/cap4 lo reconocen; |
| Perdidas T/P/A: no hay base para esperar mejora perceptual; no gastar GPU antes de diagnosticos baratos | C, D, E, F | sin resultados T/P/A en el material |
| Control de ajuste fino confundido por hardware/continuacion | C (C-06/R-4), F (H4) | R-4 en cola en Khipu |
| Protocolo fisico = comparador, no verdad de terreno | D (MED-05), F (H6) | cap3 lo declara |
| Superar Turing no implica utilidad diagnostica ni coherencia fisica | C, D, E, F | — |

## 2. Hallazgos de un solo revisor VERIFICADOS por el orquestador
- **C-01** (alta): el sintetizador no recibe la anatomia de G (los cortes vecinos llevan G borrada: a15_cadena_completa.py cond_de, `hu_v[g_v] = -1000.0`; entradas = 2 contextos + M + G). VERIFICADO en codigo. La interpretacion (explica piso de ruido y perfil plano) es hipotesis.
- **C-03** (alta): la perdida de validacion que elige `mejor.pt` usa 256 de 896 parches, todos de metal_0011. VERIFICADO: `--lote 16 --lotes-val 16` (a7_run04.sbatch:65,70), validacion sin barajar (entrenar.py:271), y las primeras 538 filas del manifiesto son metal_0011. El texto dice "896 parches de 3 casos" (cap3:230).
- **C-02** (alta, parcial): `sigma = eta * sb_s` (difusion.py:192) no es la sigma de DDIM de Song et al. VERIFICADO que la formula difiere; la razon 1.0-2.9x NO se recalculo.
- **F-H1** VERIFICADO (cap3:602-604). **E-02** candidato de validacion intacta: se calcularon 27 candidatos (analysis/r3_candidatos.csv) frente a los "30" de C.
- **G**: ver analysis/verificacion_G.md. Las cifras de resultados que marco "sin origen" (G-009, 010, 014-019) EXISTEN en results/ (falsos negativos). Vale solo: conteos de cohorte (178/179/168/166/159; 64/66/69; coincide con B) y archivar hashes/comandos de corridas (G-024/025).

## 3. Discrepancias (no resueltas por votacion)
| Punto | A | B | Resolucion propuesta (requiere decision de la autora) |
|---|---|---|---|
| Reduccion de palabras | -13 920 (50 % del alcance) | -8 974 bruto; -6 200 neto esperado | **CERRADA (autora, 2026-11-24):** meta = rango de B; A = cota optimista. Conteo unico con texcount |
| Cap. 2 | 7 072 -> 2 750 | 6 575 -> 4 675 | **CERRADA (autora, 2026-11-24):** meta = rango de B (~4 700 palabras, conteo con texcount); A (~2 750) es solo cota optimista; la guia manda (G-B8, G-B10, P-EA3): comprimir con tabla comparativa y recortar narracion repetida, sin eliminar la comparacion critica ni la brecha |
| Paginas | ~50 | 16-19 esperado | No verificado con el PDF; medir tras la primera tanda de cambios |
| Fusionar secciones cap2 | si (A-018) | no | Decidir con la guia |
| C vs F: como lograr independencia | "validacion 2" de 12-15 pelvis sin metal de train | cohorte independiente nueva | Compatibles si H5 (identidad de volumenes sin metal) sale limpia; primero H5 |
| G vs resto | cifras "sin origen" | — | G descartado en esos puntos (falsos negativos) |

## 4. Resultados de analisis propios (CPU/Khipu)
R-5 (sd entre semillas de eta2: 0.08-0.09 en run04_mejor); F-H5 (0 grupos en >1 particion segun grupos.csv; limite: no detecta duplicados no vinculados); R-8 NO interpretable (metal en G); R-11 (W1 solo bajo 0.395 para ambas referencias con sigma x1; x0.5 y x2 no); R-2, R-9, R-4 pendientes en Khipu.

## 5. Estado de cobertura
Informes A..G completos sobre: intro, cap1, cap2, cap3 (A,B: hasta poses y SAP; C,D,E,F,G: completo), cap4, conclusiones. NO cubierto aun: el 75 % de cap3 desde el punto de vista editorial (A,B no revisaron sintetizador v2, protocolo de apariencia ni amenazas), cap4 editorialmente, trabajosFuturos, anexos, resumen/abstract editorialmente.

## 6. Ronda editorial 2 (2026-11-24): cap3 367-525/546-565 y cap4 1-223/234-247 (A2 Codex high; B2 Sonnet high; a ciegas)
Coincidencias (A2, B2): la prosa de cap4 recita cifras que ya estan en las tablas (tab:res-sap, res-tost, res-anillos, res-integridad, res-ea1); la regla de los tres desenlaces/TOST esta definida en cap3 (496-500) y re-explicada en cap4 (94, 128-130); resultados dentro de metodologia: cap3:389-410 (tab:c4-eta, eta2_exc) y cap3:482-488 (amplitudes de validacion y eleccion de material) deben ir a cap4/anexo; la discusion (cap4 234-247) repite resultados; historia de decisiones y enmiendas dispersa en cap3 (registro/anexo unico).
Magnitud: A2 -5 700 palabras (13 800 -> 8 100; ~20 pag.); B2 -3 700 neto (12 460 -> ~8 760; rango 2 400-4 500; 8-11 pag., 5-7 conservador). Regla de la autora (2026-11-24): meta = rango de B2; A2 = cota optimista.
Figuras/tablas propuestas por B2: tabla de sonda de viabilidad (B2-016), regla del material (B2-017), flujo de cohortes 33->19/14->13->10 (B2-007), forest plot con banda +-196.3 HU (B2-031), perfil por anillos (B2-032), cronologia de decisiones en tabla (B2-024).
Fuera de alcance de esta ronda y pendiente: cap3:526-545 (contraste de realismo, ~1 275 palabras con resultados dentro de metodologia). Cifras de palabras de ambos informes: conteos aproximados, no verificados con texcount.
