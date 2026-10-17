# conclusiones — r01 (modo corregir) — respuesta del redactor

Encargo: `redaccion/ENCARGO_2026-10-16.md` (modo una ronda). Reportes leidos: `-lint` (PASA, 0 GAP), `-guia`
(guia-1, guia-2), `-estilo` (ES-01..ES-11), `-trazabilidad` (T01..T03). Sin reporte de asesor (sin GAP).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| T01 (alta) | trazabilidad | APLICADO | l. 12: el autoencoder de Guo et al. "no llego a correrse"; se da la cota por saturacion (42.24 HU, cap. 4 l. 45) y el cierre dice "solo se evaluaron esas dos variantes y, en el de Guo et al., la cota por saturacion". Las seis combinaciones se nombran como "las dos variantes del autoencoder de Stable Diffusion 1.5 y tres codificaciones" (cap. 4 l. 236). l. 36 (antes l. 34): "ninguna de las dos variantes evaluadas del autoencoder de Stable Diffusion 1.5 conserva..." + "En el generador de Guo et al., la sola saturacion a su rango de salida ya supera esa tolerancia". Ya no aparece "dos autoencoders examinados" ni que se comprobo que el de Guo no conserva HU (DEC 2026-10-16 (6)) |
| T02 (alta) | trazabilidad | ESCALADO | Contradiccion entre `CLAUDE.md` raiz (muestrea de las distribuciones de Zwingmann) y la preinscripcion / `docs/00-tesis.md` (Zwingmann solo para comparar). Registrada como implicancia #199; la resuelve la autora. Por indicacion del orquestador el texto no se cambia: "Ningun parametro del muestreador se tomo de la referencia clinica" coincide con `experiments/objetivo2/preinscripcion_muestreador.md` l. 52-75 y `docs/00-tesis.md` l. 61-78. No se puso `\GAPDEC` en la seccion porque el orquestador pidio no tocar ese pasaje; si la autora alinea `CLAUDE.md` con la preinscripcion, no hay nada que cambiar aqui |
| T03 (alta) | trazabilidad | APLICADO | l. 36: "El perfil por anillos y la variabilidad entre pacientes agregan dos dimensiones que la comparacion de medias no recoge. El sintetizador no reproduce la caida de la amplitud con la distancia al metal, y varia menos de un paciente a otro que el protocolo fisico." Ya no se afirma que la media no separara los brazos (-301.0 HU, IC excluye cero). Mismas palabras que cap. 4 l. 252-254 |
| guia-1 (media) | guia | APLICADO | Nuevo primer parrafo de la subseccion de respuesta: el objetivo general "se cumplio como objetivo de diseno, implementacion y evaluacion"; la cadena se implemento, con el sintetizador en el dominio de imagen, y sus dos componentes se evaluaron por separado; la coherencia quirurgica tiene lectura descriptiva sin regla de decision y la coherencia fisica con el protocolo fisico no se establecio. Responde a `introduccion.tex` l. 32 sin endurecer las formulas por objetivo (Obj 2 sin "se cumple"; Obj 3 con la formula del cap. 4 l. 250) |
| guia-2 (media) | guia | APLICADO | Mismo pasaje que T03 |
| ES-01 (alta) | estilo | APLICADO | Resuelto con T01, coherente con cap. 4 l. 45: "El articulo no publica su rango de salida, y la saturacion al rango que fija el guion de su paquete distribuido..." sin `\cite` nuevo ni nombre de archivo (el cap. 4 ya da paquete y guion) |
| ES-02 (media) | estilo | APLICADO | l. 20: "la supera junto al borde de $G$, en $+478.0$ y $+411.7$~HU en los anillos de 8 a 10 y de 10 a 12~mm (Tabla~\ref{tab:res-tost})". La banda completa ya tiene su -301.0 HU en el parrafo anterior; no se repite |
| ES-03 (media) | estilo | APLICADO | "sus valores se leen respecto del protocolo fisico, que es una referencia de comparacion y no una verdad fisica" |
| ES-04 (media) | estilo | APLICADO | "Frente a la insercion por copia y pegado, que no produce rayas, la diferencia solo confirma que el sintetizador genera artefacto y no cuenta a favor de su coherencia con el protocolo fisico" (cap. 4 l. 132: control de cordura) |
| ES-06 (media) | estilo | APLICADO | "Las cifras del Objetivo~2 se calcularon con esa envolvente y no se corrigieron por ese efecto" (DEC 2026-10-16 (2)) |
| ES-07 (media) | estilo | APLICADO | "No se establecio que estrecha los 15 corredores ..., y la fractura, confirmada en 20 de los 30 casos de un cribado, es un factor de confusion de esa causa". No se tomo la propuesta literal ("confunde la atribucion ... a una causa anatomica concreta") porque agrega una lectura que el cap. 4 l. 244 no hace |
| ES-08 (media) | estilo | APLICADO | "Del segundo corredor bajo S1 solo se midio el eje, en 69 de los 72 pacientes, sin poses ni grados de brecha" (DEC 2026-10-16 (3) pto 2) |
| ES-09 (media) | estilo | APLICADO | Mismo pasaje que T03 |
| ES-10 (media) | estilo | APLICADO | Eliminada "Lo que el trabajo aporta a esa aplicacion es una condicion previa..." |
| ES-05 (baja) | estilo | APLICADO | "su criterio no cambio despues" |
| ES-11 (baja) | estilo | APLICADO | "porque el realismo visual de su apariencia no se reclama" (formula de DEC 2026-10-16 / #193; no "no se establecio", que diria otra cosa) |

Arreglos colaterales: al insertar la frase de Guo entre la compuerta y "Ese veredicto...", el referente quedaba ambiguo;
se cambio a "El veredicto de la compuerta es un hallazgo propio" y "Lo que la compuerta no establece". El lint marco
dos oraciones largas (E-O1) en el parrafo de implicancias tras la correccion; se partieron.

## Fuente de cada cifra nueva

| Cifra | Fuente en el documento | Fuente primaria |
|---|---|---|
| 42.24 HU (media del error con solo saturacion, Guo) | cap. 4 l. 45 | #93; DEC 2026-10-16 (6) |
| +478.0 y +411.7 HU (anillos 8-10 y 10-12 mm) | cap. 4 `tab:res-tost` l. 112-113; l. 138 | `experiments/objetivo3/resultados_dec_2026-10-15.md` |

Las demas cifras no cambiaron (ver `conclusiones-r00-respuesta.md`). Lint `conclusiones --compilar`: PASA (0/0/0; 189 paginas).

## Decisiones de redaccion

- **Autoencoder de Guo et al.:** fuera del cap. 4 se dice que "no llego a correrse" y que se calculo la cota por
  saturacion; nunca "se examinaron dos autoencoders" ni que se comprobo que no conserva HU. Los autoencoders
  evaluados son "las dos variantes del autoencoder de Stable Diffusion 1.5" (PAT-201). Nota: el propio cap. 4 l. 236
  y l. 238 todavia dice "Se examinaron dos autoencoders" / "solo se examinaron dos autoencoders"; queda para la
  ronda del cap. 4.
- **Objetivo general en conclusiones:** se responde con la formula "se cumplio como objetivo de diseno,
  implementacion y evaluacion", separada del resultado sobre la coherencia, que se da por componente.
- **Perfil y variabilidad frente a la media:** se escriben como "dimensiones que la comparacion de medias no
  recoge", nunca como si separaran donde la media no lo hizo (la media si separo: -301.0 HU, IC excluye cero).
