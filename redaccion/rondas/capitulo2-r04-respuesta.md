# capitulo2 — r04 — respuesta del redactor

Modo: corregir. Archivo: `overleaf/secciones/capitulo2.tex`. Se leyeron los cuatro reportes de la ronda.
No se abrio ningun PDF. Fuentes consultadas: fichas `karageorgos2024ddpm` (Tabla I p. 28, filas DDPM y NMAR;
Tabla III), `yun2026simulationdriven` (Tabla 1 p. 10, datos sinteticos), `peters2025hybrid` (2.5 p. 5, escala
calibrada con NMAR = 2); `capitulo3.tex` (ll. 60-72, 125-134, 164); `introduccion.tex` (ll. 58-60).
Criterio de desplazamiento minimo: solo se movieron dos oraciones del parrafo del aporte (ES-03) y una de Wang
(ES-02); la oracion de orden de 2.3 se reordeno y describe el orden real (planificacion, l. 54-56; mascaras de
lesion, l. 58; series clinicas, l. 60-66; corredor, l. 68; carencias del Obj 2, l. 70; Obj 4, l. 72-74).

## Hallazgos altos y medios

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 = ES-01 | guia, estilo | APLICADO | l. 122: "el esquema multiventana sirve para quitar el artefacto y no para generarlo" (BITACORA §2, capitulo2-r03, decision 2). Ya no niega el tercer elemento del aporte |
| guia-2 | guia | APLICADO | Ultima oracion del aporte: "Como declara la justificacion de la introduccion, ningun objetivo aisla la geometria parametrica, y tampoco la codificacion ni la banda, porque el Objetivo 3 evalua el sintetizador completo" (= `introduccion.tex`:60) |
| guia-3 | guia | APLICADO | Parrafo nuevo tras el de Rombach/Chen/Guo (su funcion es la compuerta del Obj 1, E-M1). Abre con "El criterio de fallo de esa compuerta tampoco tiene un umbral publicado"; presenta los errores de MAR sobre datos simulados con su condicion: Karageorgos et al. RMSE 12.3 (DDPM) y 20.2 (NMAR, el algoritmo con que Peters et al. calibran su escala) (ficha Tabla I p. 28; `peters2025hybrid` 2.5 p. 5); Yun et al. 12.74 (ficha Tabla 1 p. 10). Remite a `sec:obj1` y no duplica el cap. 3. Sin unidad, por la decision §2 capitulo2-r03 (4): las fichas no dan la unidad del RMSE. La sigla RMSE se define aqui (primera aparicion en el orden del documento) y la l. 92 pasa a usarla sin definir |
| ES-02 | estilo | APLICADO | l. 80: la oracion de CLINIC-metal va tras la de metricas; el parrafo cierra con la lectura propia |
| ES-03 | estilo | APLICADO con variante | Las dos oraciones salen del parrafo del aporte, que queda en cinco. Ambas (medicion sin autoencoder + `\GAPDEC`) van al final de la l. 82 y no se reparten entre l. 82 y l. 84: la medicion es sin autoencoder y sigue a "las variantes de techo que describe la Seccion obj1", mientras que la l. 84 trata el paso por el autoencoder y recibe ya el criterio de guia-3. "Fuera de la regla de su compuerta" se conserva porque es la condicion de la medicion (`p1_compuerta.md`:5) y la frase ahora sigue a la descripcion de la compuerta en el mismo apartado. Texto del `\GAPDEC` sin cambios. La remision al capitulo de resultados queda en texto plano (T03) |
| ES-04 | estilo | APLICADO | l. 92: "Para decidir si la generacion debe exceder la mascara del implante, el diseno se apoya en un experimento de MAR de Karageorgos et al."; lectura propia marcada: "Este trabajo lee en esos valores una asimetria: una mascara menor que la traza eleva el RMSE mucho mas que una mayor, y de ahi toma la decision de generar mas alla de la mascara del implante". "Experimento de reduccion" pasa a "experimento de MAR" (tambien atiende guia-5) |
| ES-05 = guia-4 | estilo, guia | APLICADO | l. 52: planificacion; colocacion de mascaras de lesion; series clinicas; geometria del corredor |
| ES-06 | estilo | APLICADO | l. 66: datos primero (36.5/14.8 %, p = 0.035, ningun tornillo del todo fuera del hueso), despues las tres consecuencias; la lectura propia dice en que importa el nivel: "la comparacion depende del nivel sacro de la referencia clinica". Incluye T04 |
| ES-07 | estilo | APLICADO | l. 74: sujeto "la Seccion sec:poses cita como motivacion"; consecuencia explicita: "de ese modelo no pueden tomarse limites en HU para una zona de densidad" (ficha: HU y calibracion NO ENCONTRADO). Se escribio "limites en HU" y no "los limites de una zona de densidad" para no afirmar mas de lo que se sigue de la ausencia de HU |
| T01 | traza | APLICADO | Tabla: "aceptacion de 86.7 % en 12 casos, segun tres cirujanos". Cuerpo l. 54: "y, en una encuesta sobre 12 de esos casos, una tasa de aceptacion clinica del 86.7 %" (`liu2025pipeline.md`:96, 98) |

## Hallazgos bajos

Aplicados: guia-5 ("reduccion de la fractura" en l. 54 y en la tabla; "experimento de MAR" en l. 92), guia-6
("Las fuentes que segmentan el metal clinico de forma automatica usan un umbral de HU"), guia-7 (la oracion ya no
remite a `sec:obj1` como lugar de la medicion; depende de alinear `capitulo3.tex`:172 e `introduccion.tex`:46,
ver pendientes), guia-8 = ES-10 (l. 126: "perturba el eje del corredor medido en cada volumen segun una distribucion
preinscrita", `capitulo3.tex`:125-134; celda: "Distribucion de poses preinscrita alrededor del corredor medido en
cada volumen"), ES-08 (una sola oracion de carencia para los dos grupos; partida en dos por el lint E-O1), ES-09
("fijado"), ES-11, ES-12, ES-13, T02 ("en uno de los experimentos" en la celda de Peters), T03 (remision en texto
plano, anotada en la fila de MAPA l. 40), T04 ("distribucion ordinal clinica por debajo de S1", =
`capitulo3.tex`:164), T05 (celda propia: "SAP frente a la referencia clinica, ya ejecutado; sin resultado del
sintetizador, que se comparara por *streak amplitude* con la insercion por copia y pegado y, segun el plazo, con el
protocolo fisico").

No aplicado: guia-9 (glosa de "zona segura"). La primera aparicion esta en `introduccion.tex`:75, fuera de mi
seccion, y ni `docs/03-glosario.md` ni el cap. 3 dan una definicion que copiar; glosarla aqui seria completar.

## GAP tras la ronda

Lint: lit = 1, dato = 2, dec = 9 (sin cambio). Ninguno abierto ni cerrado. Movido: el `\GAPDEC` de codificacion
y precision del sintetizador pasa de §Comparacion critica y brecha a §Representacion multiventana (fila de MAPA
l. 40 anotada, con la nota de T03). `_candidatos.md` no cambia.

## Pendientes fuera de mi alcance

1. Siguen: `introduccion.tex`:46 y `capitulo3.tex`:172 dan como no verificada la ida y vuelta sin autoencoder que
   el cap. 2 da por medida (PAT-19); `capitulo3.tex` `sec:obj1` no describe esa medicion (guia-7).
2. `capitulo4.tex` sin `\label`: cuando se redacte, poner `\label{cap:resultados}` y cambiar en el cap. 2 "en el
   capitulo de resultados" por `Capitulo~\ref{cap:resultados}` (T03).
3. `capitulo3.tex`:67 da en HU los RMSE de Karageorgos (20.2, 12.3) y de Yun (12.74); las fichas no traen la unidad.
   El cap. 2 los da sin unidad. Verificar con `lector-papers`.
4. "Zona segura" sin definicion en su primera aparicion (`introduccion.tex`:75) (guia-9).
5. Relecturas previas: `ramzan2026claim` Sec. 3.5, `herman2016` p. 8, `hu2023` Fig. 3.

## Lint

`python scripts/lint_redaccion.py capitulo2 --compilar`: PASA, alta = 0, media = 0, baja = 0; compila, 89 paginas.

## Decisiones de redaccion

1. Cuando el umbral de fallo de un objetivo no viene de la literatura, el estado del arte lo dice y presenta las
   cifras publicadas que le dan escala, con su condicion, y remite al capitulo de metodo sin repetir su argumento.
2. Una sigla que el capitulo necesita antes de su definicion actual se define en la nueva primera aparicion y la
   definicion posterior se reduce a la sigla (RMSE: ahora en el parrafo de la compuerta del Obj 1).
3. "Reduccion" sola se reserva a la MAR; la clinica se escribe "reduccion de la fractura".
