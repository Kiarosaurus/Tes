# Revision guia CS — capitulo3 — r23

Entradas: `overleaf/secciones/capitulo3.tex` (estado tras r22), lint `capitulo3-r23-lint.md` (PASA; 24 E-P1 bajas
preexistentes), respuesta `capitulo3-r22-respuesta.md` (no hay hallazgos de guia RECHAZADOS; todos APLICADOS).
Cotejo con DEC 2026-10-15 (puntos 1-22) y 2026-10-15 (2), y con `experiments/objetivo3/EXPERIMENTOS.md` y
`resultados_dec_2026-10-15.md` (versionados desde r22). Cruces leidos: `introduccion.tex`:28-60 (objetivos y lectura
del Obj 3), `capitulo1.tex`:94-112 (`sec:mt-difusion`). Los 22 hallazgos de r22 estan atendidos. Lo nuevo viene casi
todo de que el encargo de r22 partia de "estas mediciones NO tienen resultado todavia", y desde entonces se corrieron
(EXPERIMENTOS: D4, D7, D8, variantes de v1, piso de ruido, v2 en prueba y E-A1 de v2 CORRIDOS).

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T4 | capitulo3.tex:248, :287, :509 | Patron PAT-122 reincide. El texto de tres pasajes niega mediciones que ya se corrieron: :248 dice "aun no medido" (D7 CORRIDO, veredicto por la regla en #191); el GAP de :287 dice que la prueba de equivalencia de v2 "no se ha ejecutado ... espera relanzarse" (Khipu 56857-56865 con rc=0, `resultados_dec`); :509 dice en prosa, fuera de la marca, que el piso de ruido del sintetizador "no se ha medido" (Khipu 56867, #188). | Mantener los resultados en `\GAPDATO` mientras sus implicancias (#188, #190, #191) sigan ABIERTAS (OC-3), pero redactar la marca como "medido; resultado en una implicancia abierta (#n)". En :509, quitar "no se ha medido" de la prosa y remitir a la marca de :421. |
| guia-2 | media | G-C7 | capitulo3.tex:509 (2.a asimetria) | La asimetria de ruido se da sin su efecto sobre el contraste primario (afin a PAT-38). El sintetizador regenera toda `G`, y su amplitud sin metal forma parte de la amplitud que se compara. Ni este parrafo ni la validez de constructo (:487) dicen en que sentido mueve eso la prueba. | Decir que la amplitud del sintetizador incluye la regeneracion de `G` sin metal y remitir a la marca con el piso medido. Si la autora no ha fijado el sentido del sesgo (#188 ABIERTA), abrir un `\GAPDEC` en una frase y no deducirlo. |
| guia-3 | media | G-C7 | capitulo3.tex:216, :473 | Patron PAT-140 reincide. Quitar la sensibilidad por semimaximo (prevista en la decision 2026-09-20) y reemplazarla por la diferencia de diametro se decidio el 15 de octubre, despues de ver la prueba de v1 (DEC pto 4). :216 no lo fecha y la lista de :473 no lo incluye. La misma lista omite la repeticion de E-A1 de v2 con 0.030, el margen comun y el protocolo de la comparacion a ciegas, que :287 fecha pero :473 no cuenta. | En :216, fechar el cambio ("el 15 de octubre, despues de ver la prueba de la version 1"). En :473, cerrar el recuento con esos cuatro elementos o remitir sin recuento a :287 y :216. |
| guia-4 | media | G-C4 | capitulo3.tex:411, :357 | Patron PAT-136 reincide. :411 define los tres desenlaces, y :357 dice que la decision del Obj 3 recae en la equivalencia, pero el capitulo no dice cual desenlace hace fallar el objetivo ni que significa "no concluyente" para el. La introduccion (:50) si lo dice: "no equivalencia, que haria fallar el objetivo". El objetivo experimental queda ligado al bloque (a) solo desde un lado. | Anadir en :411 una oracion con la lectura de cada desenlace para el Objetivo 3, con la misma formulacion de `introduccion.tex`:50. |
| guia-5 | media | P-MM3 | capitulo3.tex:363 | Con la descripcion no se puede reproducir el artefacto parametrico. DEC 2026-10-15 (2) fija su forma: medianas de D1 por anillo, interpoladas linealmente; en el plano perpendicular al eje, $A(r)/2\cdot\mathrm{signo}(\cos 2\theta)$, con dos lobulos claros y dos oscuros; $M$ a 5371 HU; fuera de la banda, la TC original. El texto dice "perfil radial medio", sin forma angular, y la DEC usa medianas, no medias. | Dar en :363 la forma angular, la interpolacion y el valor de $M$ citando la DEC (2), y escribir "mediana", no "medio". |
| guia-6 | media | G-T4 | capitulo3.tex:495 | Patron PAT-168 reincide. Para ordenar la gravedad del suelo entre los dos contrastes, el texto se apoya en "una sola ejecucion local del protocolo fisico, la de la verificacion de reproduccion". Pero el protocolo ya corrio sobre 2 receptores de validacion y 13 pacientes de prueba, y :335 y :421 definen la fraccion de su region bajo -1000 HU como medicion propia. La premisa quedo atras del diseno actual. | Remitir a la fraccion medida (:335, marca de :421) como evidencia de esa diferencia, o acotar la oracion a lo que esa medicion puede y no puede decir. |
| guia-7 | baja | G-T3 | capitulo3.tex:204, :302, :413 | Patron PAT-14 reincide. En el capitulo, la letra $s$ designa tres cosas: $s_n$, el coeficiente de la difusion (nuevo en r22 por el aviso de capitulo1-r09); $s$, la distancia con signo a la envolvente (Ec. de la brecha), y $s_{\mathrm{sem}}$, el rango entre semillas. | Cambiar el simbolo de la distancia con signo en la Ec. `eq:brecha` (p. ej., $\mathrm{dist}$ o $g$), que es local al capitulo; $s_n$ queda fijado por `sec:mt-difusion`. |
| guia-8 | baja | P-MM3 | capitulo3.tex:258 | No se dice con que procedimiento se calcula el "intervalo del 90 %" que decide hasta que anillo el artefacto real se separa del control nulo (remuestreo, *t*, otro). De ese intervalo depende el limite de 8-10 mm, que :489 usa en Amenazas. | Nombrar el procedimiento del intervalo en una frase, o `\GAPDATO` si solo consta en el codigo. |

TOTAL alta=0 media=6 baja=2

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple |
| G-T3 | cumple a medias (guia-7, baja) |
| G-T4 | no cumple (guia-1, guia-6) |
| G-T5 | cumple |
| G-T6 | cumple (lint PASA, sin referencias indefinidas) |
| G-C1 | cumple (desviacion de la cabeza y regla del suelo no aplicable, declaradas con motivo) |
| G-C2 | cumple (tabla `tab:desviaciones`, revisiones fijas, cita del repositorio) |
| G-C3 | cumple |
| G-C4 | no cumple (guia-4) |
| G-C5 | cumple con GAP |
| G-C6 | cumple (v2 posterior y exploratoria, margen comun, E-A1 con 0.030) |
| G-C7 | no cumple (guia-2, guia-3) |
| G-C8 | cumple con GAP (tres desenlaces, supuesto de *t* con IC exacto, degeneracion de Wilcoxon, `\GAPLIT` de Bland-Altman/Pitman-Morgan) |
| G-C9 | cumple (el protocolo fisico es la comparacion fuerte; copia y pegado declarada control de cordura) |
| P-MM1 | cumple |
| P-MM2 | cumple (`fig:pipeline`) |
| P-MM3 | no cumple (guia-5; guia-8 baja) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de resultado redactado como "no medido" o "no ejecutado" cuando la corrida ya termino | G-T4 | "desenlace del diagnostico del percentil 95, aun no medido" | PAT-122 |
| Cambio de diseno posterior sin fecha y fuera de la lista post hoc | G-C7 | "ese modelo no se entrena, por su costo de computo" | PAT-140 |
| Desenlaces de equivalencia definidos sin decir cual hace fallar el objetivo | G-C4 | "equivalencia ..., no equivalencia ..., y no concluyente ..." sin lectura para el Obj 3 | PAT-136 |
| Premisa que se apoya en una ejecucion previa cuando el diseno ya mide esa magnitud | G-T4 | "se apoya en una sola ejecucion local del protocolo fisico" | PAT-168 |
| Una letra reutilizada con subindices distintos para tres magnitudes del capitulo | G-T3 | $s$ (distancia con signo), $s_n$, $s_{\mathrm{sem}}$ | PAT-14 |
| Encargo escrito sobre un estado ("no tienen resultado") que las corridas del mismo dia dejan atras | G-T4 | "NO tienen resultado todavia: ... su resultado va como \GAPDATO" | PAT-176 |
