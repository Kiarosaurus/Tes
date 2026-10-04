# Revision de estilo — capitulo1 — r04

Lint de la ronda: PASA, sin hallazgos. Respuesta previa: r03, 0 RECHAZADOS; guia-1 NO APLICADO (no es
de este revisor). Vara de tono: ESTILO §1.1 (E-M1 a E-M8); `muestras_autora.md` sigue vacio. Fichas
cotejadas: `deman1999` (l.52 "todas las causas": respaldado, Conclusiones p. 695; l.56: la ficha no
nombra la inanicion), `arand2019pelvicring` (l.88: patron cualitativo, sin cifras; no hay PAT-8).
Cap. 3 cotejado: l.85 (0.42), l.172 (*inpainting* condicionado), l.215 (inversion de metricas).
No se re-abre "escala de perforacion" (l.84): la propuso este revisor en r02 (S15) y distingue la
dimension de perforacion de la angular de Smith et al.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S01 | media | E-O2, E-P3 | l.35, oraciones 7-8 | "En la cohorte local, por ejemplo, la mediana ... fue 0.42" / "Un hueso definido por ese umbral dejaria fuera esa fraccion" | El parrafo tiene 8 oraciones (la correccion S01 de r03 lo hizo crecer, cf. PAT-58), y la ultima es casi tautologica y pierde el "en la mediana" del cap. 3 l.85 (Patron PAT-31 reincide). Fundir en una: "En la cohorte local, a lo largo del eje del corredor mas ancho, la mediana de la fraccion de voxeles sacros a 150~HU o menos fue 0.42, fraccion que un hueso definido por ese umbral dejaria fuera en la mediana (Seccion~\ref{sec:corredor})." |
| S02 | media | E-R2, E-P3 | l.66, ultima oracion | "su uso para evaluar sintesis exige invertirlas (Seccion~\ref{sec:apariencia})" | "Invertir una metrica" suena preciso y no dice que se invierte; ademas oculta que el cap. 3 (l.215) deja esa definicion en `\GAPDEC`. "Las tres se disenaron para evaluar MAR, y su uso para evaluar sintesis exige invertirlas, con una definicion operativa que aun esta pendiente (Seccion~\ref{sec:apariencia}); el Objetivo~3 toma la \emph{streak amplitude} como su unico criterio primario." |
| S03 | media | E-M1, E-O3 | l.80, oraciones 5-6 | "Kaiser et al. justifican, por su parte, su umbral de 10~mm" | El parrafo trata del marco de referencia para expresar la pose; la justificacion del umbral de 10 mm interrumpe y repite un tema del parrafo anterior (l.78, tercera mencion del umbral de Kaiser et al. en la seccion), y "por su parte" es conector de relleno. Llevarla a l.78, tras "Los tres lo toman de trabajos anteriores ...": "Kaiser et al. lo justifican como una holgura de 1 a 2~mm alrededor de un tornillo de 6.3 a 8~mm, que la Seccion~\ref{sec:corredor} lee como holgura radial por lado." En l.80 queda: "El marco incluye ademas una regla de longitud util, que exige al menos 5~mm hasta la cortical a cada lado del eje y que la Seccion~\ref{sec:corredor} lee como margen cortical." (l.78 queda en 7 oraciones; l.80, en 5) |
| S04 | media | E-R4, E-M4 | l.114, ultima oracion | "Glover y Pelc derivan el volumen parcial no lineal de la integracion" | Patron PAT-102 reincide: la caracterizacion de Glover y Pelc ya esta en l.60. Ademas el lector tiene que adivinar que se sigue para el sintetizador. "Como el volumen parcial no lineal nace de integrar la atenuacion dentro del espesor del haz (Seccion~\ref{sec:mt-artefactos}), este trabajo lee que unos pocos cortes vecinos aportan informacion axial pero no reproducen esa integracion, de modo que el sintetizador no contiene ese mecanismo y solo puede aprender la apariencia que deja en los cortes." |
| S05 | media | E-M4 | l.126, oraciones 5-6 | "lo que eleva a siete las combinaciones que pueden aprobar. El veredicto ..." | Patron PAT-52 reincide: la oracion anterior concluye que la multiplicidad "no compromete" el veredicto porque fue negativo, y la extension deja sin decir si eso vale para el septimo candidato. "... con la misma regla y los mismos pacientes de prueba, lo que eleva a siete las combinaciones que pueden aprobar. El veredicto de esa extension se presenta en el capitulo de resultados; si fuera aprobatorio, esa multiplicidad si lo favoreceria (Seccion~\ref{sec:amenazas})." |
| S06 | media | E-R1 | l.64, l.124, l.128 (aperturas); cf. l.35, l.54, l.62, l.118, l.122 | "Dos familias de metodos ..." / "Tres procedimientos de inferencia ..." / "Dos errores por voxel ..." | Once parrafos u oraciones tematicas anuncian un recuento ("dos dominios", "dos umbrales", "dos consecuencias", "tres tipos", "dos preguntas"...); leido seguido, el recuento anunciado es el tic que mas delata el texto generado. Conservarlo donde el parrafo enumera de verdad (l.62, l.118) y abrir los otros por su contenido. l.64: "La MAR elimina el artefacto de una TC ya adquirida, y la simulacion fisica lo produce reproduciendo la adquisicion; este trabajo no hace ni lo uno ni lo otro." (y se elimina la oracion siguiente, que lo repetia). l.124: eliminar "Tres procedimientos de inferencia completan el marco." y abrir con "Para la superioridad, el diseno usa ...". l.128: "El error absoluto medio y la raiz del error cuadratico medio, los dos errores por voxel del documento, no son intercambiables." |
| S07 | baja | E-M4 | l.56, 2a oracion | "De Man et al. no nombran la inanicion de fotones; describen como artefacto" | La yuxtaposicion sugiere que el artefacto de ruido es el analogo de la inanicion, pero el lector tiene que adivinarlo. Decir la relacion como lectura propia: "De Man et al. no nombran la inanicion de fotones; este trabajo lee como su analogo el artefacto de ruido que describen, lineas finas ..., cuya intensidad depende de la atenuacion total integrada a lo largo del rayo \cite{deman1999}." |
| S08 | baja | E-R2 | l.44, ultima oracion | "su error mide cuanto valor de TC pierde la representacion" | "Cuanto valor de TC pierde" no dice que se compara. "El paso de ida y vuelta lleva los HU a la representacion y de vuelta a HU, y su error es la diferencia, en HU, entre el valor original de cada voxel y el recuperado." |
| S09 | baja | E-M4 | l.106, 5a oracion | "Las tres fuentes evaluan imagenes naturales, y ninguna trabaja con TC" | Hecho sin consecuencia para el parrafo, que trata del costo de muestrear. "Las tres fuentes evaluan imagenes naturales y ninguna trabaja con TC ni con metal \cite{...}, de modo que la aceleracion que reportan Song et al. no esta medida sobre TC." |

## Impresion general
Leido seguido, el capitulo suena a tesis: define por contraste, acota a las fuentes revisadas y dice
que hace cada concepto en la propuesta. El patron dominante es ya de ritmo: aperturas con recuento
anunciado ("Dos ...", "Tres ...") y parrafos que crecen con cada correccion (S01, S03).

TOTAL alta=0 media=6 baja=3

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Oracion tematica que anuncia un recuento ("Dos X ...", "Tres Y ...") como apertura habitual de parrafo | E-R1 | "Tres procedimientos de inferencia completan el marco." | nuevo |
| Cifra copiada de otro capitulo pierde su calificador ("en la mediana") en la oracion de consecuencia | E-P3 | "Un hueso definido por ese umbral dejaria fuera esa fraccion" | PAT-31 |
| La misma caracterizacion de una fuente se repite en dos secciones del capitulo | E-R4 | "Glover y Pelc derivan el volumen parcial no lineal de la integracion" | PAT-102 |
| Hecho anadido que deja sin revisar una conclusion previa del mismo parrafo | E-M4 | "lo que eleva a siete las combinaciones que pueden aprobar" | PAT-52 |
| Termino que suena operativo ("invertir la metrica") mientras su definicion esta en GAP en otro capitulo, sin decirlo | E-R2, E-P3 | "su uso para evaluar sintesis exige invertirlas" | nuevo |
| Correccion de una ronda que lleva el parrafo por encima de siete oraciones | E-O2 | l.35 pasa a 8 oraciones tras anadir la cifra 0.42 | PAT-58 |
