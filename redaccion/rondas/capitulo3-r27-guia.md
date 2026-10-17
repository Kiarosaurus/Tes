# Revision guia CS — capitulo3 — r27

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T1, G-C4, P-MM1 | capitulo3.tex:31, :38, :369, :455, :474 | Patron PAT-200 reincide: el contraste de realismo, que la introduccion identifica como disenado y no ejecutado (`introduccion.tex:41`), aparece en la figura y en el orden de contrastes como parte de la evaluacion, mientras :38 lo deja pendiente. No queda un estado experimental unico que el lector pueda seguir. | Retirarlo de la caja de evaluacion ejecutada y presentar en :38, :369, :455 y la tabla un solo estado: diseno no ejecutado, conservado como trabajo futuro; mantener su procedimiento en pasado para documentar la desviacion. |
| guia-2 | media | G-T1, G-C4, P-MM1 | capitulo3.tex:349, :533 | El analisis exploratorio con poses del muestreador tiene un resultado marcado como faltante en :349, pero :533 afirma que esas poses «se examinan». Asi, no se distingue una propiedad del diseno —el sintetizador acepta una pose— de evidencia experimental sobre las poses producidas por el muestreador. | Indicar en ambos pasajes que el analisis se fijo pero no se ejecuto y que queda como trabajo futuro; aclarar que la evaluacion del Objetivo 3 uso el eje sin perturbar. |

TOTAL alta=0 media=2 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | no cumple (guia-1, guia-2) |
| G-T2 | cumple |
| G-T3 | cumple |
| G-T4 | cumple |
| G-T5 | no evaluable: `capitulo4.tex` sigue como esqueleto |
| G-T6 | cumple |
| G-C1 | cumple con GAP (efecto del canal en secciones estrictamente convexas) |
| G-C2 | cumple con GAP (constancia de revision multiplanar) |
| G-C3 | cumple |
| G-C4 | no cumple (guia-1, guia-2); los tres objetivos experimentales principales si se enlazan con la introduccion |
| G-C5 | cumple |
| G-C6 | cumple con GAP (contraste de realismo y comparacion visual no ejecutados) |
| G-C7 | cumple con GAP (envolvente/canal, techo de S1 y estructura direccional); las cuatro clases de validez son explicitas y sustantivas |
| G-C8 | cumple |
| G-C9 | cumple: el protocolo fisico es el contraste primario y la copia y pegado se limita a control de cordura |
| G-A7 (cruce) | cumple con GAP |
| G-A8 (cruce) | cumple |
| P-MM1 | no cumple (guia-1, guia-2) |
| P-MM2 | cumple (`fig:pipeline`) |
| P-MM3 | cumple con GAP |

## Propuestas de criterio

Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un ensayo disenado y no ejecutado aparece tambien como comparacion existente | G-T1, G-C4 | «y realismo frente a tornillos reales» | PAT-200 |
| Un analisis sin ejecutar conserva verbos que afirman que produjo evidencia | G-T1, G-C4 | «Las poses perturbadas [...] se examinan» | nuevo |
