# resumen-r01 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/resumen.tex`. Pedido de la autora: DEC 2026-10-16 (7), incluido el pto 6
(titulo ajustado). Reportes leidos: `resumen-r01-lint.md` (PASA), `-guia.md`, `-estilo.md`, `-trazabilidad.md`.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (alta, P-R4) | guia | FUERA DE SECCION | Toca `abstract.tex`, no `resumen.tex`. El orquestador lanza abstract r00 despues; no se edito aqui |
| guia-2 (media, G-R1) | guia | APLICADO | Objetivo 4 integrado sin oracion nueva ni sigla: en el metodo, "la admisibilidad quirurgica de la colocacion, propuesta aqui, califica cada pose por viabilidad del corredor y grado de brecha cortical" (`introduccion.tex`:43); en resultados, "La admisibilidad quirurgica paso sus controles" (`conclusiones.tex`:22: controles de identidad, monotonia y resolucion) |
| guia-3 (media, G-T2, P-R1) | guia | APLICADO | Autoencoder glosado como "la red que comprime la imagen y la reconstruye" (`introduccion.tex`:37); *streak amplitude* glosada como lo que "mide la intensidad de las rayas respecto de la imagen sin metal" (`capitulo3.tex`:345) |
| ES-01 (media, E-T1, E-R5) | estilo | APLICADO (por el orquestador) | Titulo cambiado en `overleaf/main.tex` a "...difusion con codificacion multiventana en el dominio de imagen"; el redactor no toco `main.tex` |
| ES-02 (media, E-M8) | estilo | APLICADO | Primera oracion abre con los artefactos y la escasez de volumenes con implantes y anotacion osea, y nombra lo que se sintetiza: "el implante y su artefacto". Se mantiene en una oracion (P-R3: introduccion en 3) |
| ES-03 (media, E-T1, E-R5) | estilo | APLICADO | "con codificacion multiventana de los valores en unidades Hounsfield" (termino fijo) |
| ES-04 (media, E-M4, E-M8, E-P3) | estilo | APLICADO | El sujeto pasa a ser "La *streak amplitude*"; desaparece el "Su apariencia" ambiguo |
| ES-06 (media, E-P3, E-R5) | estilo | APLICADO | "la equivalencia de la *streak amplitude* con la del protocolo fisico no se establecio" |
| ES-07 (media, E-M8) | estilo | APLICADO | "...porque la autora lo juzgo insuficiente; ella y su asesor decidieron no redisenar el sintetizador, y su salida no reproduce la caida de la amplitud con la distancia al metal". Se separa la decision del defecto sin agregar oracion (P-R3: conclusiones en 3) |
| T01 / ES-05 (baja) | trazab. / estilo | APLICADO | "la mejor dio 61.72 unidades Hounsfield" (`experiments/objetivo1/p1_compuerta.md`:18-25) |

## Ajustes colaterales

- Al integrar el Objetivo 4 y las glosas, seis oraciones pasaron de 40 palabras (E-O1, lint). Para no exceder los
  limites de P-R3 (3/4/6/3) se compactaron: "Antes de la cadena" pasa a "Una compuerta previa"; se omiten "medido en cada
  volumen" (corredor), "publicadas" en las series clinicas y el detalle de "identidad, monotonia y resolucion" de los
  controles; la comparacion con las series pasa del metodo al resultado ("disto 0.206 grados, en distancia de
  Wasserstein-1, de una serie clinica con navegacion y 0.230 de otra sin ella"). Ninguna cifra cambio.
- Estructura final: introduccion 3, metodo 4, resultados 6, conclusiones 3 oraciones.

## Lint

`python scripts/lint_redaccion.py resumen --compilar`: PASA, alta=0, media=0, baja=2 (E-P1, cifras sin `\ref`;
inevitables por P-R2). Compila.

## GAP

Abiertos: ninguno. Cerrados: ninguno.

## Decisiones de redaccion

- En resumen y abstract, el Objetivo 4 se nombra por el termino fijo sin sigla ("admisibilidad quirurgica de la
  colocacion") y se integra en las oraciones del muestreador, no en una oracion propia.
- Glosas de una clausula para el resumen: autoencoder = "la red que comprime la imagen y la reconstruye";
  *streak amplitude* = "mide la intensidad de las rayas respecto de la imagen sin metal". El abstract deberia usar
  las equivalentes en ingles.
