# Revision guia CS — capitulo3 — r17

Entrada: `overleaf/secciones/capitulo3.tex` (estado tras la respuesta r16), lint `capitulo3-r17-lint.md`
(PASA, 12 E-P1 baja), respuesta `capitulo3-r16-respuesta.md` (nada RECHAZADO que reabrir; T02 y T03 escalados,
con sus `\GAPDEC` en l. 66 y l. 381). Cotejado contra `docs/04-implicancias.md` #163, #166, #171 y #172 (con la
adenda y la recalibracion del 2026-10-11), `docs/01-decisiones.md` 2026-10-11 (1)-(4),
`experiments/objetivo3/diseno_A.md` (seccion 0 y ENMIENDA 2026-10-11), `docs/02-datos.md`:146,
`docs/ESTADO.md`:14 e `introduccion.tex` (para G-C4). Los hallazgos guia-1 a guia-5 de r16 estan resueltos en el
texto actual.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7, G-T4 | capitulo3.tex:202, 212, 381 | Patron PAT-11 reincide (y PAT-122). El `\GAPDATO` dice que la calibracion del limite con el modelo evaluado "esta en curso", y la l. 212 dice "hoy en recalibracion". La adenda de #172 (2026-10-11) registra que la recalibracion ya se hizo y que no confirma 0.05 para el punto de control elegido; para el estado final si lo confirma. Segun #172, "como el cotejo elige el punto de control, la eleccion misma podria cambiar". La amenaza de la l. 381 sobre las tres elecciones no lo menciona. | Cambiar el `\GAPDATO` por un `\GAPDEC`: la recalibracion con el modelo evaluado esta hecha, no confirma el limite para el elegido y falta decidir como aplicarla (implicancia 172). Por OC-3, el valor de una implicancia ABIERTA no va en la prosa como hecho. En la l. 381, decir que la eleccion del punto de control depende de ese limite. Corregir "hoy en recalibracion" en la l. 212. |
| guia-2 | media | G-C7, G-T4 | capitulo3.tex:48, 54, 206 | No se dice hasta donde llegan las auditorias de identidad de paciente, y la l. 206 afirma sin acotar que "la regla de aislamiento estricto se mantiene". Segun #163, el barrido por firma metalica "NO es exhaustivo" y no cubre "casos sin metal" ni "vinculos entre datasets sin metal comun". Justo ese tipo de par cruzo particiones: el `0003`/`0072`, antes y despues de la cirugia, lo hallo la autora a ojo. Si queda un par sin detectar, en el Obj 1 favorece un aprobado, en el Obj 3 favorece al sintetizador y en el Obj 2 se cuenta como dos pacientes independientes. | En sec:datos, decir que cubren las auditorias y que no. En amenazas, dar el sentido de un par no detectado en cada objetivo. Acotar la l. 206 a "segun las auditorias de identidad de paciente". |
| guia-3 | baja | G-T5, P-MM1 | capitulo3.tex:56 | Cifra de veredicto del Obj 1 en el capitulo de metodo: "la mejor combinacion da 61.08 HU, con un intervalo ... de 54.23 a 68.57 HU". BITACORA §2 (2026-09-29) manda los veredictos al cap. 4, y la l. 87 dice que el veredicto "se presenta en el capitulo de resultados". El lector recibe la cifra de sensibilidad antes que la principal, que el cap. 3 no da. | Dejar en el cap. 3 "sin ninguno de los dos pacientes, con 32, el veredicto negativo no cambia" y llevar la cifra con su IC al cap. 4, junto a la principal. |
| guia-4 | baja | G-C7 | capitulo3.tex:212, 379 | Patron PAT-140 reincide. La l. 212 enumera lo que se repitio tras el reentrenamiento: el punto de control, $\Delta$ y "el valor de la insercion por copia y pegado". La lista de la l. 379 ("seis decisiones" fijadas con el resultado de prueba ya visto) omite el valor de copia y pegado (5371 HU, DEC 2026-10-11 (3).5). | Sumarlo a la lista, entre las que aplican una regla previa (la mediana del metal de entrenamiento), o decir por que no cuenta como decision. |
| guia-5 | baja | G-T1 | capitulo3.tex:377 | "3 de los 11 pacientes de prueba que entonces se contaban con material" no se concilia con el texto. El lector solo ha visto 9 con material ortopedico en prueba (l. 58, l. 275), y la unica salida explicada (l. 52) daria 10. `diseno_A.md` da 11 + 8 = 19 antes del recuento y 9 + 10 despues: dos pacientes cambiaron de grupo sin que el capitulo lo diga. | Remitir al recuento del 11 de octubre (sec:datos) y decir en una clausula que dos pacientes pasaron de material ortopedico a objetos no ortopedicos, o dar el 11 como "antes de ese recuento". |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP, salvo guia-5 |
| G-T2 | cumple ("auditorias de identidad de paciente" y "modelos afectados" se definen una vez y se retoman igual) |
| G-T3 | cumple ($\Delta$ designa solo el margen; 0.01 y 0.05 se llaman "limite") |
| G-T4 | no cumple (guia-1, guia-2) |
| G-T5 | cumple, salvo guia-3 |
| G-T6 | cumple (el lint no reporta E-F) |
| G-C1 | cumple con GAP (cabeza de $M$, lotes, regla del suelo en HU) |
| G-C2 | cumple con GAP (algoritmo del eje, heuristica de referencias, prediccion $v$, repositorio AAPM) |
| G-C3 | cumple |
| G-C4 | cumple dentro del cap. 3. En el cruce con `introduccion.tex` siguen desfasadas la l. 48 ("un margen ... aun sin medir"; cap. 3: 163.8 HU) y la l. 56 ("el protocolo de Peters et al. sobre las poses del muestreador"; cap. 3, l. 281 y 399: eje sin perturbar). No se reportan como hallazgos de esta seccion: corresponden a la ronda de introduccion o a la pasada `documento` |
| G-C5 | cumple con GAP |
| G-C6 | cumple (copia y pegado como cordura, protocolo fisico como comparacion, sensibilidades declaradas) |
| G-C7 | no cumple (guia-1, guia-2; guia-4 menor). La fuga `0003`/`0072` ya esta declarada en los Obj 1 y 3 con su sentido |
| G-C8 | cumple con GAP (supuesto de la *t*, desenlaces del TOST, tamano de efecto) |
| G-C9 | cumple (el protocolo fisico publicado es el competidor; la copia y pegado se declara cordura) |
| P-MM1 | cumple, salvo guia-3 |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP |

## Propuestas de criterio
- Bloque (c): cuando el aislamiento entre particiones se sostiene con una auditoria, el metodo debe decir la
  cobertura de esa auditoria, no solo su resultado. Hoy cabe en G-C7, pero la rubrica no lo nombra.
- Fuera de mi dominio, para `revisor-estilo`: en la l. 56, "Como con el paciente del parrafo anterior" apunta a la
  l. 54, que trata del mismo paciente compartido; el otro caso esta en la l. 52, que ademas no dice que esa fuga
  favorezca un aprobado (PAT-34). En la l. 66, "(Seccion~\ref{sec:datos})" remite a la seccion en que ya se esta.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP de un paso en curso que envejece cuando la implicancia registra su resultado | G-T4, G-C7 | "Su calibracion con el modelo evaluado esta en curso" | PAT-11 (y PAT-122) |
| Aislamiento entre particiones afirmado sin acotarlo a la cobertura de la auditoria que lo verifica | G-C7, G-T4 | "la regla de aislamiento estricto ... se mantiene" | nuevo (afin a PAT-13) |
| Cifra de veredicto que entra al capitulo de metodo por una sensibilidad, mientras la principal queda en resultados | G-T5, P-MM1 | "la mejor combinacion da 61.08 HU, con un intervalo" | nuevo |
| Lista de decisiones posteriores que omite un elemento que otro parrafo enumera como rehecho | G-C7 | "se fijaron seis decisiones" sin el valor de copia y pegado | PAT-140 |
