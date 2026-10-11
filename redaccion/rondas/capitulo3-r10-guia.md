# Revision guia CS — capitulo3 — r10

Leidos: `RUBRICA.md`, `overleaf/CLAUDE.md`, `BITACORA.md` (§1 y §2), `capitulo3-r09-respuesta.md`, `ENCARGO_2026-10-10.md`,
`capitulo3-r10-lint.md`; para cruces, `introduccion.tex` (objetivos, l. 21-64) y grep en `capitulo1.tex`/`capitulo2.tex`.
Cotejo de diseno contra `experiments/objetivo3/diseno_A.md` §0, `a20_resultados.md`, `a15_cadena_completa.py` y
`01-decisiones.md` 2026-10-05 (#141) y 2026-10-09 (3)-(8). r09 no tuvo revisores, asi que no hay RECHAZADOS que respetar.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C6, G-C4, P-MM2 | capitulo3.tex:252 (y :15, :27, :194) | La sintesis sobre pelvis sin metal usa el eje del corredor sin perturbar, pero nada dice por que ni que se pierde con eso. La l. 194 y la Figura 3.1 dicen que la sintesis usa "una pose muestreada", y ninguna amenaza recoge que el sintetizador nunca se evalua sobre las poses que produce el muestreador (salvo los 3 corredores angostos). `diseno_A.md` §0 solo lo pone en "Lo que NO entra", sin razon. | Dar la razon con su fuente o abrir un `\GAPDEC`. Distinguir en l. 194 y en la figura la sintesis en general de la pose de la evaluacion. Anadir la consecuencia en validez externa. Cruce para la autora: `introduccion.tex:56` y `capitulo2.tex:106` dicen "sobre las poses del muestreador" (contradiccion 2 de r09) |
| guia-2 | media | G-C2, P-MM3 | capitulo3.tex:109, :121 (Tabla 3.1), :129 | El capitulo describe $M$ como "cilindro uniforme de 4.91 mm" y la cabeza como variante de sensibilidad. La corrida congelada rasteriza con cabeza: `diseno_A.md` §0 dice "cilindro de 4.91 mm con cabeza" y `a15_cadena_completa.py:298-299` pasa `con_cabeza=True`. Un tercero que siga el capitulo no reproduce la $M$ evaluada (contradiccion 3 de r09). | Describir la $M$ que se corrio: cuerpo de 4.91 mm mas cabeza de 8.0 x 4.5 mm. Si la autora no lo ratifica, `\GAPDEC` con lo que difiere entre decision D3 y corrida (decision §2 del 2026-09-29: "si decision y codigo difieren, el metodo describe lo que se corrio") |
| guia-3 | media | G-C5, P-MM3 | capitulo3.tex:129, :133 | Se anuncian como analisis de la evaluacion "la cabeza y la rosca entran como variantes de sensibilidad" y "se evalua el tornillo macizo frente al hueco". El diseno congelado los excluye: "variantes de rosca, arandela o canulacion (D3, sensibilidad no programada)" (`diseno_A.md` §0, l. 126). Son variables independientes prometidas que no estan en la Tabla 3.3 ni en el diseno. | Decir que esas variantes no estan programadas en la corrida final y pasarlas a trabajo futuro o a un `\GAPDATO` |
| guia-4 | media | G-C5, G-C7 | capitulo3.tex:198, :256 | La l. 198 dice que el segundo desplazamiento de dominio (rayas lejanas en el contexto de entrenamiento, ausentes en los receptores sin metal) "se mide con el salto ... para los dos brazos que generan artefacto". El diseno congelado solo mide la costura en la reconstruccion de implantes reales (l. 256; `diseno_A.md` §0, l. 97), donde el contexto si trae metal real. Ahi no se observa el desplazamiento que se dice cuantificar (contradiccion 6 de r09). | Alinear la l. 198 con el diseno congelado. Si el salto no se mide en la sintesis sobre pelvis sin metal, el segundo desplazamiento queda sin medicion y pasa a amenaza abierta, o va a `\GAPDEC` |
| guia-5 | media | G-A8, G-C4 | capitulo3.tex:268, :296, :346 | Se dice que "la decision del Objetivo 3 recae en la comparacion de equivalencia", pero no que significa para el objetivo cada desenlace del TOST. Son tres: IC dentro del margen, IC entero fuera del margen o IC que cruza el margen. La l. 346 admite que puede no concluirse "ni equivalencia ni diferencia", pero no dice cual de los tres desenlaces cuenta como fallo del sintetizador y cual como no concluyente. | Una oracion por desenlace con su lectura para el Objetivo 3, sin anticipar resultados. Debe decir cual es evidencia en contra (falsabilidad del lado del bloque c) |
| guia-6 | media | G-C6, G-A7 | capitulo3.tex:296 | Patron PAT-11 reincide. El `\GAPDEC` pregunta "si el brazo de equivalencia ... se mantiene o pasa a trabajo futuro" (#90, 2026-09-21). El diseno congelado (DEC 2026-10-09 (6), pto 2) fija ese TOST como contraste primario, y la corrida final ya lanzo el brazo (ESTADO, job 55453). Tal como esta, el capitulo deja en duda que el Objetivo 3 tenga contraste decisorio. | Reformular el GAP con el estado vigente: el congelamiento lo mantiene como primario y queda pendiente que la autora cierre #90. O retirarlo si ella lo confirma |
| guia-7 | media | G-C1, G-C8 | capitulo3.tex:298, :188 | Se da la formula de $\Delta$ sin su justificacion. `tesis/main.tex:98` la tiene: el margen sale de "the method's own variability under conditions that should not change the result". Tampoco se trata un desajuste de escala: $s$ es el rango entre semillas sueltas, mientras que el TOST compara la mediana de 5 semillas por paciente (l. 296), que varia menos. | Anadir la razon del margen con su fuente y una oracion que reconozca que $\Delta$ se mide sobre semillas sueltas y se aplica a medianas. Si hace falta, llevarlo a validez de la conclusion |
| guia-8 | media | G-C1, G-C5 | capitulo3.tex:184, :338 | Patron PAT-116 reincide. (a) La regla del suelo compara "que parte" del vano se pierde, una fraccion sin unidad (1 - 0.914 en DEC 2026-10-05, pto 2), con $\Delta$ en HU. Como esta escrita, no se puede evaluar. (b) La rama "si es mayor, se cambia la representacion" ya no puede ocurrir: el diseno se congelo (DEC 2026-10-09 (6)) y la corrida final ya uso esa representacion. | (a) `\GAPDEC` sobre como se lleva la fraccion a HU para compararla con $\Delta$. (b) Decir que el congelamiento deja la representacion fija y que el desenlace adverso solo puede declararse como limitacion |
| guia-9 | media | G-C4 | capitulo3.tex:256-258, :317 | La reconstruccion de implantes reales entra en la tabla de diseno, pero no se liga a ninguna pregunta ni objetivo del bloque (a): el Objetivo 3 de la introduccion (l. 41) no la nombra. Ademas, la l. 200 argumenta que esa tarea "premia memorizar ... y no es la de este trabajo". Queda sin decir que informa su resultado. | Una oracion que diga que mide y para que sirve, por ejemplo la transferencia fuera de distribucion de los 8 objetos o la costura. Si ningun objetivo la usa, declararla analisis descriptivo adicional (cruce con la introduccion) |
| guia-10 | media | G-T3 | capitulo3.tex:220-223 frente a :298; :296 | Patron PAT-14 reincide. En el mismo capitulo, $s$ es la distancia con signo a la envolvente (Ec. 3.3) y tambien el rango entre semillas, y $r$ es el radio del calibre de medicion y tambien la diferencia entre replicas. Ademas, $t$ es el parametro del eje en la Ec. 3.3 y "$t$ de Student" en la l. 296. | Renombrar los terminos de $\Delta$ con simbolos libres (p. ej. $s_{\mathrm{sem}}$, $r_{\mathrm{rep}}$, o letras no usadas) y cotejar con la notacion del cap. 1 (decision §2 del 2026-10-03) |
| guia-11 | media | P-MM1, G-T5 | capitulo3.tex:240-300 | La subseccion de coherencia de apariencia tiene unos 27 parrafos sin subestructura. Mezcla metricas, poblaciones, regiones, reconstruccion de implantes reales, realismo, brazos, verificacion del protocolo, sonda, material y analisis estadistico. $\Delta$ se usa en la l. 254 y se define en la l. 298, y el TOST llega despues de 14 parrafos sobre el brazo fisico. | Partir en subsubsecciones por funcion: metricas e inversion; poblaciones y regiones; brazos (copia y pegado, protocolo fisico, sonda, material); analisis (Wilcoxon, TOST, $\Delta$); realismo. Definir $\Delta$ antes de su primer uso |
| guia-12 | media | P-MM3, G-C2 | capitulo3.tex:194, :200 | La l. 194 sigue diciendo "el entrenamiento se fija en 30 000 pasos" con su justificacion por meseta ("Dos corridas ..."). El modelo evaluado es el punto de control de ~37 000 pasos de un segundo entrenamiento cuya duracion total no se da, y la l. 200 admite que la cifra "deja de describir el modelo usado". Ademas, las "dos corridas" no son independientes (misma semilla y datos, #148 ABIERTA). | Describir el entrenamiento que produjo el modelo evaluado (segundo entrenamiento, duracion, punto de control). Dejar los 30 000 pasos como antecedente o retirarlos, y no presentar las dos corridas como corroboracion |
| guia-13 | baja | G-T2 | capitulo3.tex:204, :262, :290 | "Envolvente real" (el rango de los perfiles reales) convive con "envolvente osea" (l. 91), y la decision §2 del 2026-09-29 reserva "envolvente" para la osea. | Otro nombre para el rango real, p. ej. "rango real" o "banda min-max de lo real", sin usar "banda" (reservada a $B_\delta$) |
| guia-14 | baja | G-C8 | capitulo3.tex:328 | Se da "$p = 0.109$" sin nombrar la prueba. La decision §2 del 2026-10-05 fija "prueba exacta de Fisher, bilateral" (escalado previo, aun pendiente). | Nombrar la prueba en la oracion |
| guia-15 | baja | G-C8 | capitulo3.tex:296, :298 | El IC con $t$ supone diferencias aproximadamente normales con n = 13, y no se dice. Falta tambien decir que con titanio $r$ no cambia $\Delta$ (\|A-B\| Ti de 0.4 y 5.2 HU, `a20_resultados.md` l. 18-19). | Una oracion para cada punto, con su fuente |
| guia-16 | baja | G-C6 | capitulo3.tex:304 | El resumen de lo fijado de antemano para el Objetivo 3 no remite a los cambios posteriores a ver validacion (ancho de cascara, material) ni a la enmienda de la reconstruccion de implantes reales (decision §2 del 2026-10-03). | Anadir la remision a `sec:amenazas` |
| guia-17 | baja | P-MM3 | capitulo3.tex:266 | "una muestra fija de casos sintetizados" no tiene tamano ni regla de seleccion. | Dar tamano y regla, o un `\GAPDEC` |
| guia-18 | baja | G-T4, OC-2 | capitulo3.tex:278 | Patron PAT-122 reincide. El `\GAPDATO` dice que faltan los "resultados del protocolo fisico ... sobre la anatomia y las poses de este trabajo", pero las l. 284-292 ya dan resultados de la sonda y de validacion. | Acotar el GAP a la particion de prueba |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | no cumple (guia-13) |
| G-T3 | no cumple (guia-10) |
| G-T4 | no cumple (guia-18; el resto, para auditor-trazabilidad) |
| G-T5 | no cumple (guia-11) |
| G-T6 | cumple (lint sin citas indefinidas) |
| G-A7 (cruce) | no cumple (guia-6, guia-9) |
| G-A8 (cruce, lado del bloque c) | no cumple (guia-5) |
| G-C1 | no cumple (guia-7, guia-8) |
| G-C2 | no cumple (guia-2, guia-12) |
| G-C3 | cumple |
| G-C4 | no cumple (guia-1, guia-5, guia-9). Cruce: `introduccion.tex:48` dice que $\Delta$ esta "aun sin medir", `capitulo1.tex:122` da n = 14 y `introduccion.tex:56` / `capitulo2.tex:106` hablan de "poses del muestreador". Se reportan en sus secciones |
| G-C5 | no cumple (guia-3, guia-4, guia-8) |
| G-C6 | no cumple (guia-1, guia-6, guia-16) |
| G-C7 | cumple: cuatro tipos explicitos y no pro forma, con constructo nuevo para los dos brazos desplazados; falta la amenaza de guia-1 |
| G-C8 | no cumple (guia-7, guia-14, guia-15) |
| G-C9 | cumple: el protocolo fisico es la linea base fuerte; la copia y pegado es control de cordura declarado |
| P-MM1 | no cumple (guia-11) |
| P-MM2 | no cumple (guia-1: la figura no refleja la pose de la evaluacion) |
| P-MM3 | no cumple (guia-2, guia-3, guia-12, guia-17) |

## Propuestas de criterio
- Coherencia entre el diseno descrito y el registro congelado (`diseno_A.md` §0) cuando ese registro existe: hoy solo cae bajo P-MM3 y G-T4. Seria un criterio del bloque (c): "lo que el capitulo describe como evaluado coincide con lo congelado; lo que no se corre se marca".

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| El metodo describe la geometria o variante decidida y no la que corrio la corrida congelada | G-C2, P-MM3 | "Cilindro uniforme de 4.91 mm" (la corrida usa cabeza) | PAT-20 |
| Analisis de sensibilidad prometido que el diseno congelado excluye, sin marca | G-C5, P-MM3 | "la cabeza y la rosca entran como variantes de sensibilidad" | nuevo |
| Regla preinscrita que compara magnitudes en unidades distintas | G-C1, G-C5 | "que parte ... pierde ... Si es menor que el margen $\Delta$" | nuevo |
| Evaluacion anadida por enmienda sin decir que pregunta u objetivo responde | G-C4 | reconstruccion de implantes reales en la tabla, sin objetivo que la nombre | PAT-57 |
| El mismo simbolo con dos sentidos en el capitulo | G-T3 | $s$ distancia con signo / $s$ rango entre semillas | PAT-14 |
| GAP sobre una contingencia que el congelamiento posterior ya resolvio | G-C6, G-T4 | "si el brazo de equivalencia se mantiene o pasa a trabajo futuro" | PAT-11 |
| Condicional preinscrito cuya rama ya no puede ocurrir tras el congelamiento | G-T4, G-C1 | "si es mayor, se cambia la representacion" | PAT-116 |
| Desenlaces de una prueba de equivalencia sin su lectura para el objetivo | G-A8, G-C4 | "puede no alcanzar a concluir equivalencia ni diferencia" | nuevo |
