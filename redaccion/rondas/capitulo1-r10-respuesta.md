# Respuesta del redactor — capitulo1 — r10 (UNICA, encargo 2026-10-15c)

Archivo: `overleaf/secciones/capitulo1.tex`. Encargo: `redaccion/ENCARGO_2026-10-15c.md` (capitulo1). Fuentes nuevas:
`experiments/registro/registro_metodos_2026-10-15.md` §1 y §6, `experiments/registro/r_fisher_amenazas.py`,
`experiments/objetivo2/e15_w1_sensibilidad.md`, DEC 2026-10-15 (4) ptos 1 y 4, fichas `walker2011understanding` y
`lakens2017equivalence`. No se toco ningun `\REVVISUAL` (el capitulo no tiene, y el texto nuevo no trata del
realismo visual). No se saco ningun hallazgo por oscilacion.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 / T01 | guia, trazabilidad | APLICADO | `\GAPDATO` de asinh retirado. Ecuacion nueva `eq:asinh` (registro §1:11-13): saturacion en [-1000, 20 000] HU, escala 500 HU, extremos asinh(-2) y asinh(40), salida en [0, 1], inversa dentro del intervalo; "fina cerca de 0 HU y gruesa en el rango alto" (registro §1:13). Se escribe con los numeros y sin simbolos $s$, $a$, $b$, porque $s_n$ ya nombra un coeficiente de la difusion y $s_{\mathrm{sem}}$ el del cap. 3 (G-T3). Sin el MAE de 61.84 HU (encargo). |
| guia-2 / T02 / ES-11 | guia, trazabilidad, estilo | APLICADO | Oracion "El repositorio no registra..." y su `\GAPDATO` sustituidas: el programa original no consta; recalculados con `scipy.stats.fisher_exact` bilateral, SciPy 1.15.3, cuya convencion es la *minlike*, se obtienen los mismos valores en las cuatro tablas (registro §6:71-74). "Coinciden", no "se calcularon con" (T04). La conducta de scipy se apoya en el registro, sin `\cite{fay2010two}` (PAT-166). Apertura reescrita: "En la Seccion amenazas se comparan proporciones..." (ES-11). |
| guia-3 / T03 | guia, trazabilidad | APLICADO | Parrafo nuevo tras los tres desenlaces (DEC 2026-10-15 (4) pto 1): "no concluyente" es nombre de este trabajo; Walker y Nowacki rotulan "equivalencia no establecida" el IC que cruza un limite (Fig. 1, p. 193) y dicen que la no equivalencia no puede descartarse (p. 192); Lakens decide la diferencia frente a cero con el IC95 y llama diferente-no-equivalente o indeterminado al intervalo que cruza un limite segun el IC95 (p. 356). La direccion de este trabajo se lee con el IC90 y solo corresponde al escenario B si tambien el IC95 excluye el 0. Sin rotulo atribuido a las fuentes, sin la Fig. 2 de Walker, sin la palabra "a la baja" atribuida, sin la cifra del IC95 (va al cap. 3). Aviso para capitulo3: :421-423 repite ahora el mapeo; guia-3 pide dejar alli solo la lectura con remision (PAT-102). No se toca otra seccion. |
| ES-1 | estilo | APLICADO | "Peters et al., cuyas metricas adopta este trabajo (Seccion mt-artefactos), definen el hueso..." |
| ES-2 | estilo | APLICADO | Definicion general sin la promesa: "...para separar los contrastes del tejido; que conserve o no el techo del metal depende del techo de su ventana mas ancha". La decision de BITACORA 2026-10-05 ("separa contrastes sin perder el techo del metal") se refiere a la representacion propia, no a la definicion general; con la ventana de Wang et al. el capitulo dice que el metal satura. |
| ES-3 | estilo | APLICADO | "...no puede expresar los valores de TC que este mecanismo deje por debajo de ese suelo". |
| ES-4 | estilo | APLICADO | Salvedad definida una vez (:55): "Ese analisis se añadio despues de conocer el resultado de la primera version del sintetizador en la particion de prueba" (oracion aparte, sin relativo ambiguo, PAT-161). En :135 "añadida tambien despues de conocer el resultado de la primera version"; en :151 "despues de conocer su resultado" (el de la prueba del modelo principal, nombrada en la oracion anterior). |
| ES-5 | estilo | APLICADO | "La inversion de la streak amplitude se define con la sintesis sobre pelvis sin metal (sec:ap-sintesis); las otras dos ... (sec:ap-reconstruccion)", como `capitulo3.tex`:331. |
| ES-6 | estilo | APLICADO | Justificaciones de McLaren y Kaiser fundidas en una oracion tras la del traslado; eliminada la oracion final que las repetia. Kaiser "lo emplean" (no "eligen"): BITACORA 2026-09-29, Kaiser no es origen del 10 mm. |
| ES-7 | estilo | APLICADO | "...solo el umbral de 10 mm, que usa como convencion de comparacion, y la holgura radial" (BITACORA 2026-09-29). |
| ES-8 | estilo | APLICADO | "...porque SAP y Zwingmann et al. graduan la brecha con la misma escala de perforacion." Oracion partida en dos por E-O1 (41 palabras en el lint). |
| ES-9 | estilo | APLICADO | Orden nuevo: definicion de superioridad/equivalencia y TOST (:135); contraste primario y tres desenlaces (:137); mapeo a la literatura (:139); Wilcoxon al final, nombrando lo que compara (copia y pegado, `capitulo3.tex`:415) y por que es pareada (:415). |
| ES-10 | estilo | APLICADO | "Como en la regla original, esa multiplicidad solo puede favorecer un veredicto aprobatorio (Seccion amenazas)." |
| ES-11 | estilo | APLICADO | Ver guia-2. |

Bajos: guia-4 APLICADO (oracion en :143: en el Obj 2 se remuestrean pacientes con todas sus poses, como bloques, e intervalo descriptivo; `e15_w1_sensibilidad.md`: "se remuestrean casos con reemplazo y se juntan sus poses"; sin cifras). guia-5 APLICADO por la salida (b): :11 dice ahora "conceptos centrales" y que las herramientas descriptivas auxiliares se presentan donde se usan (G-B3). T04 APLICADO en lo obligatorio (version y "coinciden"); la oracion opcional sobre la convencion central no se agrega: la simetria con 15/15 es un recalculo del auditor, no consta en el repositorio. ES-12 APLICADO en :63 ("y por eso"), :131 ("Por eso,") y :153; quedan cinco "de modo que", con relacion de consecuencia. ES-13, ES-14, ES-15, ES-16 APLICADOS (ida y vuelta pasa a abrir el parrafo de la compuerta, :53).

Cifras nuevas y su fuente: 500 HU, [-1000, 20 000] HU, asinh(-2), asinh(40), [0, 1] — registro §1:11-13. SciPy 1.15.3 y coincidencia de los cuatro valores — registro §6:71-74. Ninguna cifra recalculada.

Lint: `python scripts/lint_redaccion.py capitulo1 --compilar` PASA (alta 0, media 0, baja 1; GAP 0/0/0; 163 paginas). La baja (E-P1 en :51, "500 HU" en la ecuacion) es un falso positivo: es la definicion propia de la compresion, cuya fuente (registro §1) va en este reporte (OC-5); no se esquiva con un `\ref` artificial.

## Decisiones de redaccion

- Una formula propia cuyos parametros solo constan en un registro de metodos se escribe con los valores numericos y sin simbolos nuevos cuando las letras naturales ($s$, $a$, $b$) ya tienen otro uso en el documento; la fuente va en el reporte de ronda.
- Reproduccion de una cifra con un programa distinto del original: "El programa con que se calcularon originalmente ... no consta. Recalculados con <programa, version> ..., se obtienen los mismos valores"; nunca "se calcularon con" la convencion del programa nuevo.
- Mapeo de un rotulo propio a una taxonomia publicada: se dice que el nombre es de este trabajo, se da el rotulo de cada fuente con su condicion (Lakens: IC95 para la diferencia frente a cero) y se declara la condicion bajo la cual la regla propia (IC90) coincide con la fuente.
- Salvedad temporal de la version 1 en el cap. 1: "despues de conocer el resultado de la primera version del sintetizador en la particion de prueba", completa una vez; despues "tambien despues de conocer el resultado de la primera version" o "despues de conocer su resultado" con antecedente explicito.
