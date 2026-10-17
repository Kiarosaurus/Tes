# Respuesta del redactor — capitulo1 — r12

Archivo: `overleaf/secciones/capitulo1.tex`. Encargo: `redaccion/ENCARGO_2026-10-16.md`. Trazabilidad sin hallazgos.
Ningun cambio deshace algo APLICADO en r11: ES-4 conserva la clausula de la convencion *minlike* y el verbo
"reproduce" que pidio r11 (ES-6). No se toco `capitulo3.tex`.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 | guia | APLICADO | Antes de la mediana 0.42 (:37) se define el termino solo con `capitulo3.tex`:105: "Las mascaras oseas de este trabajo provienen de TotalSegmentator \cite{wasserthal2023}, que antes de segmentar delimita la region de interes con un modelo de recorte de menor resolucion; el **recorte por defecto** es el que usa un modelo de 6~mm (Seccion~\ref{sec:corredor})." El recorte alternativo de 3 mm y la sensibilidad quedan en el metodo. |
| ES-3 | estilo | APLICADO | "A diferencia de la ventana, la pendiente de la compresion es mayor cerca de 0~HU que en el rango alto, donde cae el metal. Por eso separa mas los valores proximos a 0~HU que los del metal." Partida en dos oraciones porque la primera version marco E-O1 (41 palabras). Fuente sin cambio: `registro_metodos_2026-10-15.md`:13. |
| ES-4 | estilo | APLICADO | "...en la version 1.15.3 de SciPy, que aplica la convencion *minlike*, reproduce los valores de las cuatro tablas." Solo cambia el relativo ("cuya convencion es" podia leerse referido a SciPy y no a la funcion); se mantiene lo de r11 (sujeto "El recalculo", verbo "reproduce", version y convencion). |
| ES-5 | estilo | APLICADO | Eliminada la oracion final de :151 ("Como en la regla original, esa multiplicidad solo puede favorecer..."); "eleva a siete las combinaciones que pueden aprobar" ya lleva la idea y la consecuencia esta en :149 (PAT-98). |

Bajos: ES-1 APLICADO como "Se dirige a un lector de computacion..." (sin "El capitulo", para no repetir el sujeto de la
oracion anterior, "Este capitulo reune"). ES-2 no aplicado: la propuesta vuelve a abrir con "En la Seccion~\ref{...}",
que r11 (ES-1, PAT-119) retiro para no encadenar aperturas iguales en :13. Lint E-P1 en :53: falso positivo, igual que
en r10 y r11 (definicion propia de la compresion; fuente `experiments/registro/registro_metodos_2026-10-15.md`:7-16).

Lint: `python scripts/lint_redaccion.py capitulo1 --compilar` PASA (alta 0, media 0, baja 1; GAP 0/0/0; 165 paginas).
GAP abiertos: ninguno. GAP cerrados: ninguno. Sin cambios de titulos.

## Decisiones de redaccion

- Un termino operativo que el marco teorico usa antes que el metodo (aqui "recorte por defecto") se define en su
  primera aparicion con una oracion copiada en contenido del metodo y una remision `\ref` al detalle; las variantes y
  analisis de sensibilidad se quedan en el metodo (PAT-3).
- Para atribuir una convencion a una funcion de software se usa "que aplica la convencion X", no "cuya convencion es X",
  que puede leerse referido al paquete.
