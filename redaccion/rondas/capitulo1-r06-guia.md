# Revision guia CS — capitulo1 — r06

Leidos: `redaccion/RUBRICA.md`, `overleaf/CLAUDE.md`, `redaccion/BITACORA.md` (§1 patrones VIGENTES y §2
decisiones, incluidas las cuatro del 2026-10-05), `overleaf/secciones/capitulo1.tex`, y como secciones
cruzadas `capitulo3.tex` (§Obj 1, §Geometria del implante, §SAP, §Amenazas) y `redaccion/MAPA.md`
(filas 44, 79-85). Respuesta previa: `capitulo1-r05-respuesta.md` (sin hallazgos RECHAZADOS: todos
APLICADOS, 0 escalados). Material nuevo cotejado: `docs/04-implicancias.md` #130 (decidida 2026-10-04,
aplicada a `main.tex`), #141 (ABIERTA, 2026-10-05), #140 y `redaccion/rondas/paridad-r01-trazabilidad.md`
(M-02). Lint r06: PASA.

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | alta | OC-2, G-T4 | capitulo1.tex:72 | El `\GAPDEC` pregunta "que tornillo representa el corredor que mide este trabajo" y si es del mismo tipo que los de la referencia clinica: #130 lo decidio el 2026-10-04 y esta aplicado a `main.tex`:117. Patron PAT-11 y PAT-19 reinciden | Escribir como hecho lo decidido: la trayectoria medida va de la cortical externa de un ilion, cruzando ambas articulaciones sacroiliacas, a la contralateral, luego es un tornillo transiliaco-transsacro, y las tolerancias angulares de `mclaren2021corridor` le aplican por ser del mismo corredor; `zwingmann2009navigated` queda como referencia de distribuciones de grado y no de equivalencia geometrica (#130.3). Dejar en el `\GAPDEC` **solo** lo que #130 no decidio: si le aplican el umbral de 10 mm y la holgura radial de Kaiser et al. Actualizar la fila 85 de `MAPA.md` |
| guia-2 | alta | G-B3, G-T1 | capitulo1.tex:72 | "La Seccion~\ref{sec:sap}, sin embargo, trata el tornillo de este trabajo como uno que entra y sale por la cortical del ilion" presenta como discrepancia sin resolver lo que `capitulo3.tex`:206 y :109 ya afirman (tornillo transiliaco-transsacro, entra y sale por la cortical del ilion por diseno). El marco teorico contradice al capitulo cuya terminologia debe fijar. Patron PAT-113 reincide | Sustituir el "sin embargo" por la afirmacion directa: el tornillo de este trabajo entra y sale por la cortical del ilion, que es el rasgo del tipo transiliaco-transsacro, y por eso §SAP excluye los extremos. La remision a `sec:sap` se conserva, sin oposicion |
| guia-3 | media | G-T2 | capitulo1.tex:72 | El capitulo define el tipo solo como "transiliosacro", mientras `capitulo3.tex`:103, :109, :127 y :206 usan la forma acentuada "transiliaco-transsacro" fijada en BITACORA §2 (2026-10-05). El termino se define en este capitulo y se usa con otro nombre en el de la contribucion | En la primera aparicion, "\textbf{tornillo transiliaco-transsacro} (transiliosacro)" con la tilde (transil\'iaco), y despues solo la forma acentuada. **No** tocar las menciones que describen fuentes ajenas: el "tornillo iliosacro" de `smith2006iliosacral` (:72 y :82) y el umbral de 10 mm de `kaiser2014dysmorphism` (:78) siguen diciendo iliosacro |
| guia-4 | alta | G-T4, G-B4 | capitulo1.tex:44 | "La codificacion multiventana usa varias ventanas a la vez ... y evita asi elegir entre conservar el rango y separar los contrastes": la frase insinua que la codificacion conserva el rango de HU, y hoy se sabe que para el rango negativo no es cierto (#141, ABIERTA: suelo en $-1000$~HU por construccion). Ademas choca con la inanicion de fotones que el propio capitulo define en :56 | Acotar la propiedad al extremo que las codificaciones varian: las tres comparten $w_{\min} = -1000$~HU, de modo que la codificacion multiventana extiende el rango solo hacia arriba y lo que cae bajo ese suelo satura (:42). Como #141 esta ABIERTA, no dar cifras: anadir `\GAPDEC` sobre si el suelo de $-1000$~HU se declara como limite de alcance o se cambia la representacion. Patron PAT-123 reincide |
| guia-5 | media | G-B3, G-B4 | capitulo1.tex:46 | El parrafo presenta el techo como la unica variable entre las tres codificaciones ("cuyo techo de 2000~HU queda bajo el umbral de 2500~HU", "eleva ese techo a 20 000~HU") y dice que la compuerta mide el error "dentro del hueso" sin decir que ese criterio no cubre nada. El lector no puede verificar que la compuerta no evalua el rango negativo del artefacto. Patron PAT-52 reincide | Decir que las tres codificaciones comparten el suelo de $-1000$~HU y que un error de ida y vuelta medido dentro del hueso no dice si la representacion conserva los valores saturados bajo ese suelo, con el mismo molde que `capitulo3.tex`:75 usa para $B_{\delta}$ ("un error restringido al hueso no muestra si el autoencoder las conserva"), y remitir a `sec:amenazas` |
| guia-6 | media | G-T1 | capitulo1.tex:21 | La fila 3 de `fig:mt-conceptos` da como concepto de §1.3 "Tornillo iliosacro" y lo liga al muestreador (Objetivo~2) y a SAP (Objetivo~4), pero el implante que esas dos piezas colocan y miden es el transiliaco-transsacro (#130; `capitulo3.tex`:109, :206). Patron PAT-117 reincide | En esa fila, nombrar el tipo que usan las piezas: "tornillo transiliaco-transsacro (y el tornillo iliosacro como antecedente)", o dejar solo el primero y que §1.3 sostenga la distincion |
| guia-7 | media | G-B2 | capitulo1.tex:118 | El marco estadistico enumera tres tipos de analisis (umbral, Wasserstein-1, pruebas pareadas) y el remuestreo, pero `capitulo3.tex`:265 sostiene una amenaza de validez interna con un valor $p$ de una tabla $2\times2$ (7 de 15 frente a 2 de 15, $p = 0.109$) cuya prueba el capitulo no introduce. El lector no puede verificar ese paso sin fuente externa | Anadir una oracion en §1.5 con la prueba exacta sobre una tabla $2\times2$ y lo que su valor $p$ permite concluir con 15 casos por grupo, incluida en el `\GAPLIT` de pruebas estadisticas (`MAPA.md`:81). Escalar al cap. 3 que la prueba debe nombrarse en :265, donde hoy solo aparece el valor $p$ |
| guia-8 | baja | G-T2, G-T3 | capitulo1.tex:116 | "Marco estadistico de la evaluacion" usa "marco" para un segundo sentido: :80 lo reserva al marco de referencia anatomico de Kaiser et al., y BITACORA §2 (2026-09-30) lo restringe a ese. Escalado de r01 sin resolver. Patron PAT-14 reincide | Decision de la autora: dejar el titulo con `\GAPDEC` sobre si §1.5 se renombra ("Analisis estadistico de la evaluacion") o si "marco" deja de estar reservado. No cambiar el titulo sin su visto bueno |
| guia-9 | baja | G-T2 | capitulo1.tex:35 | "umbral con que este trabajo criba la cohorte" nombra el procedimiento sin calificarlo, mientras el cap. 3 distingue tres (cribado por HU, cribado ciego de fractura, censo morfologico del metal) por la decision de BITACORA §2 del 2026-10-05 | "umbral del cribado por HU con que este trabajo delimita el metal clinico de sus volumenes", para que no se confunda con los otros dos cribados del documento |

Nota: las otras dos decisiones de `capitulo3`-r06 no tienen objeto aqui. No hay ninguna lectura o juicio
humano en el capitulo (nada que reemplazar por "un medico recien egresado y sin especialidad"), y ninguna
cifra propia va en porcentaje: la unica es la fraccion 0.42 de :35, con cohorte, recorte y "en la mediana".

## Cobertura

| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-2, guia-6) |
| G-T2 | no cumple (guia-3, guia-9; guia-8 pendiente de la autora) |
| G-T3 | cumple ($\xi$, $\bar{\gamma}_n$ y $[w_{\min}, w_{\max}]$ declarados en :97 y :284 de BITACORA; $\Delta$ es el mismo que `capitulo3.tex`:235) |
| G-T4 | no cumple (guia-1, guia-4) |
| G-T5 | cumple (:11 y :13 justifican el orden de las cinco secciones y la cadena fisica -> cirugia -> generativo -> estadistica) |
| G-T6 | cumple (lint PASA, sin citas indefinidas) |
| G-B1 | cumple con GAP (`\GAPLIT` de anatomia pelvica en :72 y de fisica de TC en :35) |
| G-B2 | no cumple (guia-7); el resto, cumple con GAP (`\GAPLIT` de Wasserstein-1 en :120 y de Wilcoxon, TOST y remuestreo en :126) |
| G-B3 | no cumple (guia-2, guia-5) |
| G-B4 | no cumple (guia-4, guia-5); los supuestos de dominio de imagen (:62), convencion de $B_{\delta}$ (:62) y escala ordinal (:86) si estan |
| P-MT1 | cumple con GAP (`\GAPDATO` de la compresion arcoseno hiperbolico en :46; `\GAPDEC` de 2.5D en :114 y de muestreo en :112) |
| P-MT2 | cumple (`fig:mt-conceptos` liga conceptos y piezas y remite a `fig:pipeline`), con la fila corregida por guia-6 |

## Propuestas de criterio

Ninguna. Los nueve hallazgos caen en criterios existentes de `RUBRICA.md` o en reglas duras de
`overleaf/CLAUDE.md`.

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una propiedad de una representacion se enuncia por el extremo que el experimento vario y se generaliza al rango completo | G-T4, G-B4 | "evita asi elegir entre conservar el rango y separar los contrastes" | nuevo |
| Un valor $p$ o una prueba que otro capitulo usa para sostener una amenaza no tiene su prueba en el marco estadistico | G-B2 | "7 de 15 frente a 2 de 15, con $p = 0.109$" sin prueba introducida | nuevo |
| Un `\GAPDEC` sobrevive a la decision de la autora que lo responde y sigue preguntando lo ya decidido | OC-2, G-T4 | `\GAPDEC{que tornillo representa el corredor ...}` con #130 decidida | PAT-11, PAT-19 |
| El marco teorico plantea como discrepancia abierta ("sin embargo") lo que el capitulo de la contribucion ya afirma | G-B3 | "La Seccion SAP, sin embargo, trata el tornillo ... como uno que ..." | PAT-113 |
| El mapa concepto-pieza nombra el objeto con el tipo que una decision posterior sustituyo | G-T1 | fila "Tornillo iliosacro" ligada al muestreador y a SAP | PAT-117 |
| Una implicancia ABIERTA que pide declarar un limite de alcance no deja marca en la seccion que lo sufre | OC-2 | parrafo de la codificacion multiventana sin `\GAPDEC` del suelo | PAT-123 |
| Una palabra reservada a un concepto reaparece como titulo de seccion con otro sentido | G-T2, G-T3 | "Marco estadistico" frente al marco de referencia de Kaiser et al. | PAT-14 |
