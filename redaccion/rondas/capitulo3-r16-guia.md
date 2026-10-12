# Revision guia CS — capitulo3 — r16

Entrada: `overleaf/secciones/capitulo3.tex` (estado tras la respuesta r15), lint `capitulo3-r16-lint.md`
(PASA, 14 E-P1 baja), respuesta `capitulo3-r15-respuesta.md` (todo APLICADO; nada RECHAZADO que reabrir).
Cotejado contra `docs/01-decisiones.md` 2026-10-09 (6)-(8) y 2026-10-11 (1)-(4), implicancias #166, #171 y #172,
`docs/02-datos.md` (actualizacion 2026-10-11), `experiments/objetivo3/EXPERIMENTOS.md`, `docs/ESTADO.md`:14 y
`introduccion.tex` (para G-C4). Los hallazgos guia-1 a guia-10 de r15 quedan resueltos en el texto actual.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7 | capitulo3.tex:52, 54, 77, 367 | La fuga `0003`/`0072` se declara solo para el Objetivo 3 (l. 54). #166 pto. 3 registra que tambien toca la compuerta: el decodificador adaptado se ajusto con entrenamiento, que incluia `0003`, y se evaluo en `0072`, que estaba entre los 34 de prueba. La sensibilidad sin `0072` sigue pendiente. La l. 77 afirma que el ajuste uso pacientes "separados de los de prueba", y la validez interna del Obj 1 (l. 367) no lo menciona. Para `0053` el capitulo si lo hace (l. 52). | Declararlo junto a `0053` en la l. 52 y en la l. 367, con su sentido: solo puede favorecer un aprobado, y el veredicto fue negativo. Marcar `\GAPDATO` para la sensibilidad sin `0072`. Acotar la l. 77. |
| guia-2 | media | G-C7, G-T4 | capitulo3.tex:198, 224, 329, 375 | Patron PAT-140 reincide. El limite 0.05 se esta recalibrando con el modelo evaluado (#172; `ESTADO.md`:14: si cambia, se rehacen el cotejo, $\Delta$ y la corrida final). Esa decision se tomo despues de ver la evaluacion de prueba con un modelo afectado. Aun asi, el cotejo (12 de 24) y $\Delta = 163.8$ HU se presentan como fijos, sin decir que se calcularon con 0.05 y dependen de el. La lista de decisiones posteriores de la l. 375 tampoco incluye la recalibracion. | En la l. 198, decir que cifras dependen del limite (el cotejo, $\Delta$ y la corrida final). En la l. 375, sumar la recalibracion a las decisiones posteriores a esa evaluacion, como una de las que aplican un criterio registrado antes. |
| guia-3 | media | G-T4 | capitulo3.tex:62 | Patron PAT-39 reincide. "El unico paciente adquirido dos veces sin cambios en el implante" lo contradice el mismo capitulo: la l. 52 describe otra adquisicion "con el mismo implante pelvico", y la l. 54 siete volumenes secundarios de pacientes adquiridos mas de una vez. `02-datos.md` da ademas `reproducibilidad` = 3 (`0003`, `0053`, `0065`). | Acotar la frase al par que se conserva como par de reproducibilidad, y decir que las demas adquisiciones repetidas salieron de las cohortes o quedan como secundarias (remision a las l. 52-54). |
| guia-4 | baja | G-T4 | capitulo3.tex:208 | "Ninguno de los resultados que este documento presenta proviene de un modelo afectado" es mas fuerte que lo que hace el capitulo: la l. 317 presenta como resultado lo que se observo con un modelo afectado ("quedaba mucho mas cerca del protocolo fisico con titanio"). | Acotar a cifras, con la formulacion de #171 ("ninguna cifra proviene de un modelo afectado"). |
| guia-5 | baja | G-T1 | capitulo3.tex:109 | "Los 64 pacientes con material ortopedico del recuento anterior a las auditorias del 11 de octubre" no se puede conciliar con el texto: el lector solo ha visto 65 (l. 48) y 59 volumenes (l. 54). El 64 resulta de retirar la adquisicion de la l. 52, y eso no se dice. | Remitir a la l. 52 ("tras retirar la adquisicion repetida descrita en la Seccion datos") o dar el 65 menos 1. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP, salvo guia-5 |
| G-T2 | cumple ("modelos afectados" se define en l. 208; los 17 se nombran ahora "candidatos solo por su forma") |
| G-T3 | cumple ($\Delta$ solo designa el margen; el 0.05 se llama "limite") |
| G-T4 | no cumple (guia-2, guia-3, guia-4) |
| G-T5 | cumple |
| G-T6 | cumple (el lint no reporta E-F) |
| G-C1 | cumple con GAP (cabeza de $M$, lotes, regla del suelo en HU) |
| G-C2 | cumple con GAP (algoritmo del eje, heuristica de referencias, prediccion $v$, repositorio AAPM) |
| G-C3 | cumple |
| G-C4 | cumple dentro del cap. 3. En el cruce con `introduccion.tex` siguen desfasadas la l. 48 ("un margen ... aun sin medir"; cap. 3: 163.8 HU) y la l. 56 ("el protocolo de Peters et al. sobre las poses del muestreador"; cap. 3, l. 277 y 393: eje sin perturbar). No se reportan como hallazgos de esta seccion: corresponden a la pasada `documento` o a la ronda de introduccion |
| G-C5 | cumple con GAP |
| G-C6 | cumple (copia y pegado como cordura, protocolo fisico como comparacion, sensibilidades declaradas) |
| G-C7 | no cumple (guia-1, guia-2) |
| G-C8 | cumple con GAP (supuesto de la *t*, desenlaces del TOST, tamano de efecto) |
| G-C9 | cumple (el protocolo fisico publicado es el competidor; la copia y pegado se declara cordura) |
| P-MM1 | cumple, salvo la promesa de la l. 341 frente a la lista de la l. 375 (guia-2) |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP |

## Propuestas de criterio
- Bloque (c): cuando una auditoria detecta una fuga entre particiones, el metodo debe declararla en **cada**
  objetivo que uso esa particion, no solo en el que motivo la auditoria. Hoy cabe en G-C7, pero la rubrica no
  lo nombra.
- Fuera de mi dominio, para `revisor-estilo` o el lint: en la l. 377 dice "da una emph{streak amplitude}", sin la
  barra invertida, y en el PDF saldra "emph" como texto.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Una fuga entre particiones se declara solo en el objetivo que la motivo, aunque otro objetivo uso la misma particion | G-C7 | fuga `0003`/`0072` declarada para el Obj 3; la compuerta evaluo `0072` sin mencion | nuevo |
| Cifras calculadas con un parametro en recalibracion se presentan sin esa condicion, y la recalibracion falta en la lista de decisiones posteriores | G-C7, G-T4 | "gana el punto de control del paso 16 500, con 12 de 24" | PAT-140 (y PAT-31) |
| Exclusividad ("el unico") que el mismo capitulo contradice | G-T4, E-P3 | "el unico paciente adquirido dos veces sin cambios en el implante" | PAT-39 |
