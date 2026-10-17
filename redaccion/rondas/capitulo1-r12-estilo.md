# Revision de estilo — capitulo1 — r12

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| ES-1 | baja | E-V2 | l.11, oracion 2 | "Esta escrito para un lector de computacion que no conoce la fisica" | "El capitulo se dirige a un lector de computacion que no conoce la fisica de la tomografia ni la cirugia de la pelvis." |
| ES-2 | baja | E-M8 | l.13, oracion 4 | "De la fijacion iliosacra salen el corredor oseo, la escala" | "En la Seccion~\ref{sec:mt-iliosacra} se definen el corredor oseo, la escala de brecha cortical y la referencia clinica del Objetivo~2." |
| ES-3 | media | E-R5, E-T1 | l.53, oracion 3 | "resuelve con finura... y con poca resolucion los del rango alto" | "A diferencia de la ventana, la pendiente de la compresion es mayor cerca de 0~HU y menor en el rango alto, donde se ubica el metal." |
| ES-4 | media | E-M8 | l.147, oracion 5 | "SciPy, cuya convencion es la \emph{minlike}" | "El recalculo con \texttt{scipy.stats.fisher\_exact} bilateral (SciPy 1.15.3), que aplica la convencion \emph{minlike}, reproduce los valores de las cuatro tablas." |
| ES-5 | media | E-R4 | l.151, oracion 3 | "esa multiplicidad solo puede favorecer un veredicto aprobatorio" | eliminar. La misma consecuencia ya cierra el parrafo de la l.149. Patron PAT-98 reincide |

TOTAL alta=0 media=3 baja=2

## Impresion general
Leido seguido, el capitulo conserva un registro sobrio, preciso y calibrado; no suena informal ni afirma realismo visual.
Los defectos restantes son locales: dos giros menos precisos que el resto de la prosa y una repeticion conclusiva al final del marco estadistico.
No reaparecen las metadeclaraciones ni los parrafos con funciones acumuladas corregidos en r11.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| La consecuencia de una regla se repite al presentar su extension en el parrafo siguiente | E-R4 | "esa multiplicidad solo puede favorecer un veredicto aprobatorio" | PAT-98 |
