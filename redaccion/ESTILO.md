# Guia de estilo del documento de tesis (overleaf/)

> Define el registro. Lo usan `redactor-tesis`, `revisor-estilo` y `scripts/lint_redaccion.py`.
> IDs `E-*`: un hallazgo de estilo cita uno de estos IDs o no cuenta.
> Lo que esta en **lista negra** lo detecta el lint; lo demas lo juzga el revisor.
> La autora puede editar este archivo. Si lo hace, el lint se actualiza en el mismo commit.

## 1. Registro buscado

Academico, sobrio y verificable. El texto suena a alguien que midio algo y cuenta exactamente que
midio, con que limites. **No** suena a divulgacion, ni a propuesta comercial, ni a resumen generado.
El modelo de voz es `tesis/main.tex` traducido al espanol: afirma lo medido, acota lo no medido y
distingue lo que **se midio**, lo que **se declara** (convencion propia) y lo que **se asume**.

### 1.1 Modelo de prosa: la guia del departamento (eleccion de la autora, 2026-09-29)

La autora eligio como modelo la redaccion de `overleaf/Guia general y recomendaciones para la
redaccion de CS.pdf`. Rasgos que se imitan:

| ID | Rasgo de la guia | Ejemplo de la guia (menos de 15 palabras) |
|---|---|---|
| E-M1 | El parrafo abre con su funcion o su tesis, y el resto la desarrolla | "La primera funcion de la tesis es situar al lector" (§2) |
| E-M2 | Se define por contraste: se niega la lectura ingenua y se afirma la correcta | "El cierre de la tesis no es un resumen mecanico: es..." (§5) |
| E-M3 | La autoridad se cita con nombre, cita y un verbo preciso de lo que hace | "Booth et al. (2016, cap. 2) recomienda formular el problema..." (§2.1) |
| E-M4 | La consecuencia se dice explicita, con su alcance practico | "Esta coherencia es, en la practica, el criterio mas comun de rechazo" (§3.3) |
| E-M5 | Negrita solo en el concepto clave, en su primera aparicion | "**brecha** (*gap*)", "**autocontenida**" (§2.1, §3) |
| E-M6 | Dos puntos para desarrollar una definicion o una consecuencia, nunca para crear suspenso | "construir un argumento verificable: cada afirmacion debe apoyarse en evidencia" (§1) |
| E-M7 | Listas solo para elementos paralelos, cada uno abierto por su termino en negrita | lista de "Precision terminologica", "Notacion unica"... (§6) |
| E-M8 | Oraciones de 20 a 35 palabras con subordinadas, pero una sola idea cada una | — |

Rasgos de la guia que **no** se imitan: la falta de tildes (defecto de la fuente); los recuadros
"Error frecuente" y los imperativos al lector ("Evite", "organice"), porque una tesis informa
y no instruye; y "Note que", que es propio de un documento didactico.

Si existen muestras en `redaccion/muestras_autora.md`, **se suman** a este modelo: el redactor
imita su vocabulario, y el revisor compara contra ambos. Si chocan, manda la muestra de la autora.

## 2. Reglas positivas

| ID | Regla |
|---|---|
| E-V1 | **Voz impersonal con "se"**: "se propone", "se midio", "se declara". Nada de primera persona ("propongo", "proponemos", "nuestro metodo"). Se dice "el metodo propuesto", "este trabajo" |
| E-V2 | Pasiva perifrastica solo si el agente importa ("fue revisado por un medico"); si no, pasiva refleja ("se reviso") |
| E-O1 | Oracion media de 20 a 30 palabras. **Mas de 40 es hallazgo** (lint). Una idea por oracion |
| E-O2 | Parrafo de 3 a 7 oraciones, con la primera como oracion tematica. Un parrafo de una sola oracion es hallazgo, salvo la formulacion del problema |
| E-O3 | Conectores solo cuando hay relacion logica real (causa, contraste, consecuencia). No se abre cada parrafo con un conector |
| E-P1 | Una cifra lleva unidad, n y fuente: cita, `\ref` a tabla propia o `\GAPDATO`. Nunca una cifra "suelta" |
| E-P2 | Toda afirmacion de mejora o diferencia lleva su medida y su prueba ("p = 0.035", "IC 95 %"). Sin prueba, no se dice "significativo" |
| E-P3 | Se calibra la certeza con el verbo: "muestra" (medido aqui), "reportan" (otros), "sugiere" (indicio), "se asume" (supuesto declarado). No se sube la certeza de una fuente al citarla |
| E-P4 | Adjetivos valorativos solo con dato al lado. "Mejor", "mayor", "menor" siempre con contra que y cuanto |
| E-T1 | Un termino por concepto en todo el documento (G-T2). Glosario de referencia: `docs/03-glosario.md` y la tabla de terminos de `overleaf/CLAUDE.md` |
| E-T2 | Termino en ingles: la primera vez, termino en espanol + ingles en cursiva entre parentesis: "franja de generacion (*generation band*)". Despues, solo espanol. Si no hay traduccion establecida, se usa el ingles en cursiva siempre igual |
| E-T3 | Sigla: se define en su primera aparicion, "tomografia computarizada (TC)", y despues se usa sola. Sigla en espanol si existe (TC, no CT); en ingles si es nombre propio de metrica o metodo (SAP, MAE, HU) |
| E-T4 | Nombres de metodos, datasets y herramientas se escriben como en su fuente: CTPelvic1K, TotalSegmentator, nnU-Net, XCIST/CatSim |
| E-F1 | Enfasis tipografico (negrita, cursiva) solo en objetivos (G-A6), terminos definidos por primera vez y marcas GAP. No en texto corrido para "subrayar" |
| E-F2 | Listas con vinetas solo para enumeraciones reales (objetivos, criterios). La argumentacion va en prosa |
| E-F3 | Citas numericas IEEE (`\cite`). La cita no es sujeto gramatical sin nombre: "Zwingmann et al. \cite{...} reportan", nunca "\cite{...} reporta" |

## 3. Lista negra: marcadores de texto generado (lint)

Aparecen en texto generado por IA muy por encima de su frecuencia en tesis humanas. Cada uno es
hallazgo **E-IA**. La correccion no es un sinonimo: es quitar la muletilla y decir el contenido.

**Muletillas de relleno**: "cabe destacar", "cabe senalar", "cabe mencionar", "cabe resaltar",
"es importante destacar/senalar/mencionar/resaltar/notar", "vale la pena", "es fundamental",
"es crucial", "es esencial", "en este sentido", "en este orden de ideas", "dicho esto", "dicho lo
anterior", "en la actualidad", "hoy en dia", "en el panorama actual", "en el ambito de".

**Inflacion**: "juega un papel", "desempena un papel", "papel crucial/fundamental/clave",
"crucial", "vital", "innovador", "novedoso", "revolucionar", "sin precedentes", "de vanguardia",
"transformador", "holistico", "sinergia", "potenciar", "aprovechar", "robusto/robustez" (salvo
definido operacionalmente), "una amplia gama", "un amplio abanico", "multiples/diversos" sin
enumerar, "significativamente" sin prueba estadistica (E-P2).

**Verbos de relleno**: "profundizar", "adentrarse", "sumergirse", "explorar" (cuando no hay
exploracion), "abordar" repetido, "arrojar luz", "allanar el camino", "sentar las bases".

**Estructuras**: "no solo ... sino (tambien)"; tríadas por reflejo ("rapido, preciso y
robusto"); cierres "En resumen," / "En conclusion," / "En definitiva," dentro de un capitulo;
guion largo (`---`, `—`) como inciso; dos puntos para anunciar lo obvio ("La razon es simple:");
preguntas retoricas (la unica pregunta admitida es la formulacion del problema).

**Calcos**: "en base a" (-> "con base en", "a partir de"), "a nivel de" (-> "en"), "jugar un rol",
"hacer sentido", "en orden a", "remarcar".

## 4. Lista negra: registro informal (lint)

Hallazgo **E-INF**: "super", "bastante", "un monton", "cosa/cosas", "basicamente",
"obviamente", "claramente", "evidentemente", "por supuesto", "realmente", "increible",
"etc.", signos de exclamacion, "yo", "nosotros", "nuestro/nuestra/nuestros" (E-V1).

## 5. Lo que el lint no ve y el revisor si

| ID | Patron |
|---|---|
| E-R1 | Parrafos que empiezan igual o con la misma estructura sintactica tres veces seguidas |
| E-R2 | Frase que suena bien y no dice nada verificable ("esto abre nuevas posibilidades") |
| E-R3 | Equilibrio artificial: cada ventaja seguida de "sin embargo" por reflejo |
| E-R4 | Resumen de lo que se acaba de decir al final del parrafo |
| E-R5 | Sinonimia elegante: el mismo concepto con tres nombres para "no repetir" (viola E-T1) |
| E-R6 | Afirmacion mas fuerte que su fuente (viola E-P3); se contrasta con la ficha en `docs/literatura/` |
