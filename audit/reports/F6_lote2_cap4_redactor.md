# F6 lote 2 - capitulo4.tex (modo CORREGIR, B2-027 y B2-028)

Archivo editado: overleaf/secciones/capitulo4.tex (CRLF conservado, 268 lineas, 268 CR). Lint: PASA (alta=0, media=0, baja=0); compila (206 paginas).

## (a) Hallazgos

| Hallazgo | Estado | Detalle |
|---|---|---|
| B2-027 (c4:45, detalle de inspeccion de codigo de MAISI) | APLICADO | Se quitaron el nombre del paquete, la utilidad de descarga y el guion; se conserva la procedencia ("se tomo del codigo distribuido del modelo") y el rango de -1000 a 1000 HU. La parte "REUBICAR a cap3:93" NO se hizo, por instruccion: cap3 no se tocó. Hoy el nombre del paquete/guion no consta en ningun lugar del documento hasta que el orquestador decida. Se conservan 42.24 HU, mediana, rango y 11/34. |
| B2-028 / A-013 (c4 §Compuerta) | APLICADO | Se quito el inventario de cifras (55.12 HU; 0.00 y 13.71 HU) y la repeticion de la lista de variantes evaluadas. Se conserva: veredicto negativo no marginal (ahora con \ref a tab:res-compuerta), consecuencia para el Objetivo 3 (rediseño en dominio de imagen), la distincion difusion latente / codificacion multiventana (ahora cualitativa y con \ref a sec:res-obj1), el argumento de multiplicidad (con la regla de cap3:89 "aprueba si lo hace alguna") y el limite de alcance ("no establece que ningun espacio latente..."). Las cifras 0.00/13.71 HU siguen en la prosa de c4:41. |
| B2-028 / A-014 (c4 §Muestreador y Objetivo 4) | APLICADO | Se quitaron 64.2 %, 69 %, 3.3 %, 0.186, 0.299, 0.203, 0.237 y 0.395 de la discusion (todos en tab:res-sap; 0.395 tambien en c4:80). Se conserva "15 de los 72" (caso negativo, P-RE2, dato de la tabla y pedido en NO TOCAR de B2) y "20 de los 30" (solo en cap3:66, confusion con fractura). Se añadio la frase de A-014 "el agregado mezcla corredores de viabilidad distinta", que reformula c4:86 sin dato nuevo. Del parrafo del Objetivo 4 se quitó la lista de controles (identidad, monotonia, resolucion), sustituida por un \ref a sec:res-obj2, donde se informan. |
| Voz impersonal | APLICADO | Unico sujeto personal en lo editado: "La inspeccion del codigo hecha en este trabajo lo encontro" (c4:45), reescrito con "se tomó". |

Sin cambios de estatus ni de sentido. No se tocaron Limitaciones, Sintetizador, v2, tablas, captions, \label, \cite ni marcas GAP.

## (b) Palabras (texcount -brief -inc -q)

Antes 4709 -> despues 4676 en el cuerpo (-33). Es menos que el ahorro estimado de B2-028 (-108) y A-013/A-014 (-300): para no perder la consecuencia ni el limite de alcance, se dejó cualitativa la parte de la discusion que ya no recita cifras, y no se fusionaron los parrafos. Si se quiere mas ahorro, la candidata es el parrafo de la banda $B_{\delta}$/ida y vuelta (c4:238), ya cubierto en c4:41.

## (c) Cifras que quedaron solo en prosa en lo editado

- c4:45: 42.24 HU (media), 18.24 HU (mediana), rango 6.96 a 231.43 HU, 11 de los 34 pacientes por encima de 25 HU, rango de saturacion de -1000 a 1000 HU. No estan en tabla.
- c4:41 (no editado, pero ahora es el unico sitio): 0.00, 21.80, 13.71 y 15.25 HU de la ida y vuelta sin autoencoder.
- Discusion: "20 de los 30" (solo en cap3:66, no en tabla de cap4). "15 de los 72" esta en tab:res-sap.

## (d) Texto literal quitado de MAISI (c4:45)

> La inspección del código hecha en este trabajo lo encontró en el paquete distribuido \texttt{maisi\_ct\_generative}, descargado con la utilidad \texttt{monai.bundle}: su guion \texttt{scripts/sample.py} fija la salida del modelo entre $-1000$ y 1000~HU.

Reemplazo: "El artículo no publica el rango de intensidades, que se tomó del código distribuido del modelo: su salida queda fijada entre $-1000$ y 1000~HU."

## (e) Oraciones con sujeto personal fuera de lo editado (sin cambiar)

- c4:76 (nota de la tabla tab:res-sap): "La distancia entre las dos series la calcula este trabajo con la Ecuación~\eqref{eq:w1}." (tabla; fuera de alcance).
- c4:260 (Limitaciones): "La autora juzgó insuficiente el resultado visual del modelo evaluado y, con su asesor, decidió no rediseñar ni reentrenar el sintetizador (Sección~\ref{sec:amenazas})."
- c4:264 (Limitaciones): "Por decisión de la autora, la envolvente y las cifras del Objetivo~2 se mantienen (Sección~\ref{sec:amenazas})."
- No hay otras con "este trabajo", "la tesis", "los autores" ni primera persona en cap4 (grep).
