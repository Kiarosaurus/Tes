# Revision de estilo — capitulo3 — r27

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Texto actual (max 15 palabras) | Propuesta |
|---|---|---|---|---|---|
| S1 | media | E-P3 | `overleaf/secciones/capitulo3.tex:345` | "el 5\,% superior y el 5\,% inferior encuentran las rayas" | La frase atribuye estructura de raya a un estadistico que solo detecta extremos; el propio capitulo reconoce ese limite en la linea 519. Propuesta: "Un estadístico de colas no exige orientar el anillo: toma los extremos de HU sin atribuirles estructura de raya." |
| S2 | media | E-R2 | `overleaf/secciones/capitulo3.tex:206` | "La regla se declaró no aplicable" | Patron PAT-5 reincide: la oracion anuncia una declaracion en vez de decir qué ocurrió. Propuesta: "La regla no se aplicó porque su desenlace dependía del percentil elegido después de ver la distribución." |
| S3 | media | E-O2, E-M1 | `overleaf/secciones/capitulo3.tex:109` | "La búsqueda recorre centros candidatos" | Patron PAT-58 reincide: el parrafo acumula ocho oraciones sobre rejilla, trayectorias, seleccion, heuristica y ocupacion. Dividir antes de "El eje del caso es la trayectoria de mayor diámetro"; esa oración ya funciona como apertura temática del segundo párrafo. |
| S4 | media | E-O2, E-M1 | `overleaf/secciones/capitulo3.tex:224` | "La inclusión en el conjunto de entrenamiento se rige" | Patrones PAT-58 y PAT-33 reinciden: nueve oraciones mezclan reglas de inclusion, razon de parches, supuesto de forma y version 2. Dividir antes de "En la versión~1, el tamaño y la forma del componente se reportan y no se filtran". |
| S5 | media | E-O2, E-M1 | `overleaf/secciones/capitulo3.tex:268` | "El diagnóstico compara, anillo por anillo" | Patron PAT-58 reincide: el parrafo reúne definicion, referencias, cohorte, regla de alcance, agregacion e intervalo en nueve oraciones. Dividir antes de "Lo real se midió en 18 pacientes de entrenamiento y validación". |
| S6 | media | E-M1, E-M4, E-O2 | `overleaf/secciones/capitulo3.tex:297` | "se completó ese procedimiento" | Patrones PAT-34 y PAT-58 reinciden: el parrafo abre con una anafora al anterior y acumula ocho oraciones. Propuesta de apertura: "El 15 de octubre, antes de probar la versión~2, se completó su procedimiento de evaluación exploratoria." Dividir antes de "La evaluación exploratoria ya se ejecutó en prueba". |
| S7 | media | E-O2, E-M1 | `overleaf/secciones/capitulo3.tex:431` | "El margen $\Delta$ mide la variabilidad propia del método" | Patron PAT-58 reincide: ocho oraciones juntan definicion conceptual, formula, procedencia, estimacion y valores. Dividir antes de "Cada término se calcula por paciente y se promedia sobre los dos receptores de validación". |
| S8 | media | E-O2 | `overleaf/secciones/capitulo3.tex:505` | "Las primeras fijaron la lectura de los desenlaces" | Re-apertura: la respuesta r26 afirma que S12 dejó este párrafo en cuatro oraciones, pero el texto vigente conserva ocho; ahora viola E-O2 y reincide PAT-58. Dividir antes de "Las últimas fijaron qué significa un desenlace no concluyente para el Objetivo~3". |
| S9 | media | E-O2, E-M1 | `overleaf/secciones/capitulo3.tex:541` | "El margen $\Delta$ descansa en solo 2 pacientes" | Patrones PAT-58 y PAT-33 reinciden: diez oraciones mezclan estimadores, relación con Haber y Barnhart, elegibilidad y el objeto metálico de un receptor. Dividir antes de "El margen se midió solo en receptores con corredor viable"; el primer párrafo trata la construcción del margen y el segundo, la población en que se estimó. |
| S10 | baja | E-R5, E-T1 | `overleaf/secciones/capitulo3.tex:159` | "de ese mismo tramo sale la longitud del implante" | Patron PAT-126 reincide: "salir" vuelve como verbo comodín de procedencia. Propuesta: "Para cada caso, la pose base es el eje del corredor medido, anclado en el punto medio de su tramo; ese mismo tramo determina la longitud del implante." |

TOTAL alta=0 media=9 baja=1

## Impresion general
Leído de corrido, el capítulo mantiene un registro sobrio y una certeza bien calibrada frente a las fuentes consultadas. La dificultad dominante es la densidad: varios párrafos acumulan reglas, salvedades y cronología hasta perder una función única. También reaparecen una metadeclaración y una atribución de estructura de raya que la propia sección desmiente después.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un párrafo crece con reglas, cifras y salvedades hasta superar siete oraciones | E-O2, E-M1 | "La inclusión en el conjunto de entrenamiento se rige" | PAT-58 |
| Un párrafo reúne procedimientos o limitaciones de funciones distintas sin una tesis única | E-M1 | "El margen $\Delta$ descansa en solo 2 pacientes" | PAT-33 |
| Un párrafo abre con una anáfora cuyo antecedente queda en el párrafo anterior | E-M1, E-M4 | "se completó ese procedimiento" | PAT-34 |
| Se anuncia que una regla fue declarada en vez de decir que no se aplicó | E-R2 | "La regla se declaró no aplicable" | PAT-5 |
| Una métrica de extremos recibe el nombre del mecanismo que no distingue | E-P3 | "encuentran las rayas claras y las oscuras" | nuevo |
| "Salir" sustituye al verbo preciso de procedencia o determinación | E-R5, E-T1 | "de ese mismo tramo sale la longitud" | PAT-126 |
