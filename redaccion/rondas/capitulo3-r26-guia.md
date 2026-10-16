# Revision guia CS — capitulo3 — r26

Insumos: `capitulo3.tex` (estado previo al encargo), `ENCARGO_2026-10-15c.md`, `experiments/registro/registro_metodos_2026-10-15.md`
(§2-§5, §7-§9), `experiments/objetivo2/e15_w1_sensibilidad.md`, DEC 2026-10-15 (4) ptos 1-4, #195 (decision), respuesta r25.
Cruces leidos: `introduccion.tex:50-66` (G-C4, G-A7, G-T5). Ningun hallazgo RECHAZADO en r25 que reabrir.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | P-MM3, G-C2 | capitulo3.tex:85 | Patron PAT-19 reincide: el `\GAPDATO` del ajuste del decodificador declara ausentes parametros que el registro §2 ya documenta (L1, AdamW, lr 1e-4 con calentamiento de 500 pasos, lote 4, recorte 1.0, 30 000 pasos fijos sin eleccion de punto de control). Sin ellos la compuerta no es reproducible | Retirar la marca y dar en prosa parte ajustada (decodificador y `post_quant_conv`, codificador congelado), perdida, optimizador, lote y criterio de parada por numero fijo de pasos |
| guia-2 | media | P-MM3, G-C2 | capitulo3.tex:105 | Patron PAT-19 reincide: el algoritmo de busqueda del eje del corredor esta en el registro §3 (rejilla de centros, 81 direcciones de -20 a +20 grados, tramo oseo continuo con salida lateral, eje = maximo de $D$). Es la pieza que define la pose base del muestreador | Retirar la marca y describirlo en 3-4 oraciones; declarar como heuristica la separacion S1/S2 por picos de 12 mm |
| guia-3 | media | P-MM3 | capitulo3.tex:115 | Patron PAT-19 reincide: la heuristica de localizacion de referencias esta en el registro §4 (crestas, platillo de S1 por anchura sostenida, EIPS, legibilidad por esfera de 12 mm). Sostiene el analisis de aplicabilidad del marco con metal | Retirar la marca y describir la heuristica; decir que la legibilidad es una cota superior revisada por laminas (registro §4) |
| guia-4 | media | G-C8 | capitulo3.tex:262 | Patron PAT-19 reincide: el motivo de la marca ("solo consta en el codigo ... y no en un registro") ya no vale. El registro §5 fija el procedimiento del IC90 por anillo (remuestreo de pacientes, 2 000 remuestreos, percentiles 5 y 95), y de ese IC depende el alcance de 8-10 mm que justifica la banda | Retirar la marca y enunciar el procedimiento en la oracion que define el intervalo |
| guia-5 | media | G-C5, G-T4 | capitulo3.tex:218, :228 | Patron PAT-19 reincide en :218 (la razon del modelo evaluado es 0.638, 5 526 frente a 8 656, registro §7) y PAT-168 reincide en :228, que repite el hueco fuera de la marca ("0.62 frente a 1.40 ... la primera razon se midio en el conjunto anterior a los retiros"). El tercer desplazamiento de dominio se cuantifica con una cifra que no es la del modelo evaluado | Dar 0.638 en :218 sin marca y usarla en :228 frente a 1.40; quitar la salvedad del conjunto anterior a los retiros, o dejar 0.62 solo como dato previo |
| guia-6 | media | G-C7 | capitulo3.tex:111 | Patron PAT-122 reincide: el `\GAPDATO` de la sensibilidad sin los dos casos con error de segmentacion niega un analisis ya ejecutado (e15, registro §8). La amenaza de seleccion se declara, pero no se dice que su control se hizo | Retirar la marca: "se anade un analisis de sensibilidad sin ellos (capitulo de resultados)", sin cifra en el cap. 3 (BITACORA §2 2026-10-11) |
| guia-7 | media | G-C8, G-C7 | capitulo3.tex:531 | Patron PAT-122 reincide: el IC por remuestreo de pacientes de W1 ya existe (e15, 2 000 remuestreos, semilla 20261015). Validez de la conclusion se apoya en un intervalo que el texto marca como no calculado | Retirar la marca y describir el procedimiento (remuestreo de pacientes, IC95) con remision al cap. 4. Si el cap. 4 lo recoge, la consecuencia (los intervalos de las dos series se solapan) va alli |
| guia-8 | media | G-C1, G-C7 | capitulo3.tex:427, :533, :537 | #195 DECIDIDA (DEC 2026-10-15 (4) pto 3) sin aplicar. :427 presenta $\Delta = \max(s,r)$ solo como "formula decidida antes de ver ningun valor", sin decir que es una convencion propia ni de donde viene la idea. Las amenazas cubren 2 pacientes, la escala mediana frente a semillas sueltas y el incentivo al metodo mas ruidoso (:429), pero faltan dos limitaciones: que la regla no es la de `haber2008general` (promedio sin referencia) y que $s$ y $r$ son estimadores heterogeneos (rango frente a diferencia absoluta) | En :427, "convencion de este trabajo inspirada en la comparacion del desacuerdo entre metodos con el de replicas \cite{haber2008general}". En :533 o :537, declarar que el maximo no es la regla de la fuente y que $s$ y $r$ son estimadores heterogeneos, sin repetir lo ya dicho en :429 y :537 |
| guia-9 | media | G-C4, G-C8 | capitulo3.tex:423 | Patron PAT-116 reincide: la correspondencia con el caso B de Lakens queda en condicional ("solo si tambien el IC del 95 % excluye el cero") con `\GAPDATO` de implicancia abierta, pero #194 esta DECIDIDA y DEC (4) pto 1 fija que el IC95 de la version 1 excluye el cero. El lector no sabe a que categoria de la literatura corresponde el desenlace del contraste primario | Retirar la marca y decir que, en la version 1, el IC95 excluye el cero y la diferencia a la baja corresponde al caso B; la cifra va al cap. 4 (BITACORA §2 2026-10-14) o se da si la autora lo prefiere, porque la DEC la registra |
| guia-10 | media | G-C6, G-T4 | capitulo3.tex:291 | Patron PAT-122 reincide: el `\GAPDATO` de la reconstruccion de la version 2 remite a #184 como abierta, pero DEC (4) pto 2 la decide (lado a lado, exploratoria; la ventaja de uno de los modelos es de lectura y desaparece con el limite 0.030). El parrafo ya fija la repeticion con 0.030 "para separar el efecto del modelo del de la lectura", y su desenlace queda sin lectura | Retirar la marca; decir que esa lectura esta decidida, con remision al capitulo de resultados y sin cifras |

TOTAL alta=0 media=10 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple |
| G-T2 | cumple |
| G-T3 | cumple |
| G-T4 | no cumple (guia-5, guia-10) |
| G-T5 | cumple |
| G-T6 | cumple (`haber2008general` esta en `referencias.bib` y aun no se cita; ver guia-8) |
| G-C1 | no cumple (guia-8) |
| G-C2 | no cumple (guia-1, guia-2) |
| G-C3 | cumple |
| G-C4 | no cumple (guia-9); cumple frente a la introduccion :50-52 (mismos tres desenlaces y la lectura en dos niveles) |
| G-C5 | no cumple (guia-5) |
| G-C6 | cumple con GAP (realismo :38, :453; comparacion visual :291); ver guia-10 |
| G-C7 | no cumple (guia-6, guia-8); las cuatro validez estan, no pro forma |
| G-C8 | no cumple (guia-4, guia-7, guia-9) |
| G-C9 | cumple (protocolo fisico como contraste primario; copia y pegado como control de cordura) |
| G-A7 (cruce) | cumple |
| G-A8 (cruce) | cumple (:425 nombra el resultado que habria rechazado la hipotesis) |
| P-MM1 | cumple |
| P-MM2 | cumple (fig:pipeline) |
| P-MM3 | no cumple (guia-1, guia-2, guia-3) |

## Propuestas de criterio
Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| GAP cuyo motivo ("no consta en un registro") deja de valer cuando se crea el registro | G-T4, OC-2 | "solo consta en el codigo del experimento y no en un registro" | PAT-19 |
| GAP sobre un analisis ya ejecutado que sigue negandolo | OC-2, G-T4 | "analisis de sensibilidad del Objetivo 2 sin los dos casos" | PAT-122 |
| Al cerrar una cifra en la marca, la prosa vecina conserva la cifra vieja y su salvedad | G-T4 | "0.62 frente a 1.40 ... se midio en el conjunto anterior a los retiros" | PAT-168 |
| Condicional sobre una correspondencia que una decision ya resolvio | G-T4, E-M4 | "corresponde ... solo si tambien el IC del 95 % excluye el cero" | PAT-116 |
| Decision de la autora que cambia el estatus de un parametro (convencion, limitacion) no llega a la seccion que lo define | G-C1, OC-3 | "Se fijo con una formula decidida antes de ver ningun valor" | nuevo |
