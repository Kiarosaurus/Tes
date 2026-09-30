# Rubrica de revision del documento de tesis (overleaf/)

> Fuentes, y solo estas dos:
> - **G** = `overleaf/Guia general y recomendaciones para la redaccion de CS.pdf`
>   (Departamento de Computacion UTEC, 22-09-2026). Seccion de la guia entre parentesis.
> - **P** = pautas que traia la plantilla UTEC dentro de `secciones/*.tex`, conservadas aqui
>   al reemplazar el texto de relleno.
>
> Cada revisor cita el ID del criterio que falla. Un hallazgo sin ID de esta rubrica, de
> `ESTILO.md` (`E-*`) o de `overleaf/CLAUDE.md` (`OC-n` = su regla dura n) no es un hallazgo:
> es una opinion, y se descarta.
> No se agregan criterios que no esten en G o P. Si un revisor cree que falta uno, lo propone
> en su reporte bajo "Propuestas de criterio" y la autora decide.

## Transversales (G §1, §6)

| ID | Criterio | Aplica a |
|---|---|---|
| G-T1 | El documento es explicativo, autocontenido, replicable y verificable (G §1) | todo |
| G-T2 | **Precision terminologica**: cada termino tecnico se define la primera vez que se usa y se usa igual despues (G §6) | todo |
| G-T3 | **Notacion unica**: un simbolo no significa dos cosas en capitulos distintos (G §6) | todo |
| G-T4 | **Verificabilidad**: toda afirmacion cuantitativa se rastrea hasta un dato, una demostracion o una cita (G §6) | todo |
| G-T5 | **Progresion logica**: cada seccion puede justificar en una oracion por que va despues de la anterior y antes de la siguiente (G §6) | todo |
| G-T6 | Toda referencia citada esta en la bibliografia (G §7) | todo |

## Bloque (a) Introduccion — `introduccion.tex` (G §2)

| ID | Criterio |
|---|---|
| G-A1 | Estan los cuatro componentes de Creswell y se pueden senalar con el dedo: planteamiento del problema, revision preliminar que lo motiva, proposito del estudio, preguntas o hipotesis (G §2) |
| G-A2 | Se explica el dominio y se delimita el problema dentro de el (G §2.1) |
| G-A3 | El problema se formula como **tension no resuelta** (algo que deberia poder hacerse y no se puede, o no bien, o no de forma eficiente, correcta o segura). Esa tension es la brecha y **aparece aqui**, no recien en el estado del arte (G §2.1) |
| G-A4 | Se resaltan los desafios del problema (G §2.1) |
| G-A5 | **Error frecuente**: no se confunde el problema computacional con el objetivo de la tesis. El problema no es el metodo propuesto (G §2.1) |
| G-A6 | Los objetivos estan presentes y **resaltados**; nunca faltan (G §2.2) |
| G-A7 | Cada objetivo es verificable por el propio diseno de la contribucion: existe en el bloque (c) la evidencia que lo prueba (G §2.2) |
| G-A8 | **Error frecuente**: cada objetivo puede fallar. Existe evidencia posible que mostraria que la contribucion no funciona (falsable) (G §2.2) |
| G-A9 | Estructura de embudo: justificativa general (contexto, uso en la sociedad) -> contexto computacional -> justificativa (necesidad, literatura) -> problema computacional especifico -> hipotesis, preguntas, metodologia -> objetivos. La problematica se separa del problema computacional (G §2.2, fig. 2) |
| G-A10 | Se anticipa brevemente la contribucion sin desarrollarla, y sus limites deliberados: que se asume, que queda fuera de alcance y por que (G §2.3) |

## Bloque (b) Fundamentos — `capitulo1.tex` (G §3, §3.1) y plantilla

| ID | Criterio |
|---|---|
| G-B1 | Un lector competente en computacion pero no experto en el subtema entiende la contribucion sin salir del documento (G §3) |
| G-B2 | Se introduce el aparato conceptual minimo: definiciones, notacion, modelos, resultados previos usados como caja negra, marco estadistico para interpretar los experimentos (G §3.1) |
| G-B3 | Autocontencion exigible: tras este bloque, el lector verifica cada paso tecnico del bloque (c) sin fuentes externas para los conceptos **centrales**; los auxiliares se citan (G §3.1, recuadro) |
| G-B4 | Contribucion de modelado: se dan supuestos del modelo, variables y criterios de validez (G §3.1) |
| P-MT1 | Se describen en detalle los elementos de la teoria que se usaran directamente en el desarrollo (plantilla, Marco teorico) |
| P-MT2 | Diagrama de diseno teorico o de modulos del proyecto, con las definiciones necesarias (plantilla, Marco teorico) |

## Bloque (b) Estado del arte — `capitulo2.tex` (G §3.2, §3.3) y plantilla

| ID | Criterio |
|---|---|
| G-B5 | Los trabajos se **comparan criticamente** contra los objetivos del bloque (a), no se listan (G §3.2) |
| G-B6 | Disciplina de busqueda trazable: fuentes, criterios explicitos, cobertura representativa (G §3.2, Kitchenham) |
| G-B7 | Se atacan limitaciones concretas de soluciones concretas, no un vacio generico (G §3.2, Kuhn) |
| G-B8 | Tabla o taxonomia comparativa (enfoque, supuestos, resultados) con la **propia contribucion como fila adicional** (G §3.2, sugerencia) |
| G-B9 | **Error frecuente**: no es un estado del arte panoramico ni cronologico; cada trabajo se conecta con los objetivos (G §3.2) |
| G-B10 | **Bisagra**: la brecha de este capitulo coincide exactamente con la tension de G-A3. Si difieren, uno de los dos esta mal (G §3.3) |
| P-EA1 | Solo literatura primaria y secundaria; se evita literatura terciaria, gris y no cientifica (plantilla, Revision critica). Las fuentes de fabricante ya citadas en la tesis se senalan como tales, no se retiran sin decision de la autora |
| P-EA2 | Para las fuentes principales se analizan **los resultados obtenidos por los autores**, no solo su metodo (plantilla) |
| P-EA3 | Cierra con un resumen y el **aporte** de la tesis desde el punto de vista computacional (plantilla) |

## Bloque (c) Contribucion — `capitulo3.tex` (G §4.1, §4.2) y plantilla

| ID | Criterio |
|---|---|
| G-C1 | Modelo o arquitectura: descripcion formal, justificacion de cada supuesto y por que captura lo relevante del fenomeno (G §4.1) |
| G-C2 | Sistema o artefacto: arquitectura, decisiones de diseno y descripcion suficiente para que terceros lo reproduzcan (G §4.1) |
| G-C3 | Hay afirmaciones de desempeno o eficacia, asi que el diseno experimental es **obligatorio** (G §4.2, nota) |
| G-C4 | Objetivo experimental ligado a las preguntas del bloque (a) (G §4.2, 1) |
| G-C5 | Variables independientes y dependientes, con sus metricas concretas (G §4.2, 2) |
| G-C6 | Diseno: grupos de control, lineas base, aleatorizacion cuando aplique (G §4.2, 3) |
| G-C7 | **Amenazas a la validez** interna, externa, de constructo y de conclusion, explicitas y no pro forma (G §4.2, 4) |
| G-C8 | Analisis estadistico apropiado al tipo de dato (G §4.2, 5) |
| G-C9 | **Error frecuente**: la linea base es el mejor competidor razonable disponible, no una version debil ni solo una implementacion naive propia (G §4.2) |
| P-MM1 | Metodologia clara, en orden logico, relacionada con los objetivos y el marco teorico (plantilla) |
| P-MM2 | Diagrama del pipeline del proyecto (plantilla) |
| P-MM3 | Todo lo expresado puede ser reproducido por el lector (plantilla) |

## Bloque (c) Resultados — `capitulo4.tex` (G §4.3) y plantilla

| ID | Criterio |
|---|---|
| G-C10 | Datos primero (tablas, graficas, dispersion); interpretacion despues, en relacion con hipotesis u objetivos (G §4.3) |
| G-C11 | Nunca un numero unico sin variabilidad, condiciones de medicion ni supuestos (G §4.2, Jain) |
| G-C12 | Evidencia minima de un modelo/arquitectura: justificacion de supuestos + validacion; recomendada: validacion cuantitativa contra datos reales (G tabla 1) |
| P-RE1 | Los resultados cubren el objetivo general y cada objetivo especifico, alineados con lo prometido (plantilla) |
| P-RE2 | Casos positivos **y negativos**, para ver virtudes y falencias (plantilla) |
| P-RE3 | Termina con una discusion por objetivo (plantilla) |

## Bloque (d) Conclusion — `conclusiones.tex`, `trabajosFuturos.tex` (G §5) y plantilla

| ID | Criterio |
|---|---|
| G-D1 | Responde de forma explicita a **cada** objetivo o pregunta del inicio, incluso si la respuesta es negativa o parcial (G §5) |
| G-D2 | Sintesis en un parrafo: que se propuso, que se hizo, que se demostro. **Sin informacion nueva**. Cierra la promesa de G-A10 (G §5.1) |
| G-D3 | Limitaciones declaradas y **distinguidas** de trabajo futuro: limitacion = lo que este trabajo no cubre por diseno o restriccion; futuro = direccion posterior (G §5.2) |
| G-D4 | Trabajo futuro abierto por los resultados o las limitaciones; conecta de vuelta con la relevancia de la introduccion (G §5.3) |
| P-CO1 | No se mencionan conclusiones de otros autores; solo hallazgos propios (plantilla) |
| P-CO2 | Evalua hasta que punto se cumplieron los objetivos, con logros y limitaciones (plantilla) |

## Resumen y abstract — `resumen.tex`, `abstract.tex` (G §7) y plantilla

| ID | Criterio |
|---|---|
| G-R1 | Contiene problema, objetivos, contribucion y resultados (G §7) |
| P-R1 | Se entiende sin leer el documento (plantilla) |
| P-R2 | **Sin figuras, tablas, citas, referencias, abreviaturas ni siglas** (plantilla) |
| P-R3 | Estructura IMRyC: introduccion 2-3 oraciones; marco metodologico 3-4; resultados 4-6 **con numeros**; conclusiones 2-3 (plantilla) |
| P-R4 | El abstract es traduccion fiel del resumen, con titulo en ingles y keywords equivalentes (plantilla) |
