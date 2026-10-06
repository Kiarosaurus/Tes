# capitulo3 — r07 — respuesta del redactor

Ronda **acotada**: no hubo reportes de `revisor-guia-cs`, `revisor-estilo` ni `auditor-trazabilidad`.
Las filas de la tabla son los puntos del encargo del orquestador (A1-A6, B7-B9, C10, D11) mas los
hallazgos del lint `capitulo3-r07-lint.md`. Fuente de autoridad: `docs/01-decisiones.md`, entradas
**2026-10-05 (2), (3), (4) y (5)**, que entran como hechos (regla 3 de `overleaf/CLAUDE.md`).

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| A1. La `streak amplitude` se mide solo en los pacientes de prueba sin metal; en los que tienen implante real se mide discrepancia | orquestador (encargo) | APLICADO | Parrafo nuevo en §Apariencia: verdad de terreno = TC original sin metal del mismo paciente; la particion de prueba reune 34 pacientes (20 con implante real, 14 sin metal); la amplitud solo se mide en los 14; en los 20 restantes se mide discrepancia frente a la TC real con el MAE en HU dentro de `G`, como medida descriptiva. Cifras de DEC 2026-10-05 (3) §1 |
| A2. Campo de desviacion: diferencia entre la imagen sintetica y la original sin metal, en HU | orquestador (encargo) | APLICADO | Segunda oracion del mismo parrafo. No se escribe la formula para no abrir notacion nueva en una subseccion de protocolo |
| A3. ROIs derivadas de la pose: anillos de 360 grados, de un voxel de guarda a 12 mm, cortes con `M` menos 8 mm por extremo; desviacion declarada que no hereda la validacion del protocolo publicado | orquestador (encargo) | APLICADO con una precision | Parrafo nuevo "Las regiones de medicion se derivan de la pose...", con los cuatro parametros de DEC 2026-10-05 (4) y remision a §SAP por la exclusion de extremos. **Precision:** no se escribe que la colocacion de Peters et al. sea *manual*. La ficha `peters2025hybrid.md` solo acredita "perpendicular to strong streak artifacts in the uncorrected images" (2.5, p. 5) y, como limitacion, "ROI for noise and streak amplitude were placed in regions without or with artifacts, based on the images without MAR" (4, p. 10); "manual" en esa ficha califica la colocacion del **metal**, no la de las ROIs (4, p. 9). El texto dice lo que la ficha sostiene y anade que aqui las regiones no dependen de un lector (E-R6, regla 4 de `overleaf/CLAUDE.md`) |
| A4. La guarda esta al minimo a proposito: una mayor sesgaria la medida a la baja | orquestador (encargo) | APLICADO | Parrafo propio: volumen parcial y artefacto de campo cercano son la misma senal, separarlos exigiria una imagen sin metal del mismo paciente, una guarda mayor descartaria senal y sesgaria a la baja, y por eso se fija en un voxel en plano. Se anade la fraccion de voxeles en el suelo de $-1000$~HU como cifra reportada junto a la amplitud, con su lectura de cota inferior (DEC 2026-10-05 (3) §3) |
| A5. Unidad de agregacion: el paciente; mediana sobre regiones y cortes; pruebas pareadas sobre los 14 | orquestador (encargo) | APLICADO | En el parrafo de Wilcoxon, en lugar del `\GAPDEC` que preguntaba por la agregacion (cerrado por DEC 2026-10-05 (3) §4) |
| A6. Jerarquia de contrastes: equivalencia primaria, realismo, y superioridad como control de cordura y no evidencia de calidad | orquestador (encargo) | APLICADO | Parrafo nuevo con los tres contrastes. La superioridad frente a copia y pegado se declara "control de cordura y no evidencia de calidad", "una debilidad reconocida del diseno y no una victoria del metodo", y se dice la consecuencia: ningun resultado de ese contraste cuenta a favor del sintetizador y la decision del Objetivo 3 recae en la equivalencia (G-C9, PAT-16, PAT-52). Para no duplicar, se quita del parrafo anterior la clausula "y la unica que la insercion por copia y pegado no puede producir" |
| B7. Paciente y metal se proyectan juntos por desplazamiento de material; la frase pasa de promesa a hecho | orquestador (encargo) | APLICADO | Parrafo nuevo "Reproducir ese protocolo no es validar el simulador": volumen de tres materiales (agua con el paciente, agua con la mascara del metal en signo negativo, aleacion con esa misma mascara), desplazamiento antes de proyectar y no pegado en el dominio de imagen, y eso es lo que hace hibrido al protocolo. Se retira "algo que se verificara en el codigo del simulador antes de reproducirlo" |
| B8. Revision de codigo y condiciones de acceso: licencia, dos revisiones, script que no corre tal como viene | orquestador (encargo) | APLICADO con `\GAPLIT` | Parrafo nuevo con las revisiones `4cf3544` y `4993e87`, la licencia de tres clausulas (BSD 3-Clause), el aborto al serializar la configuracion, el parche de una linea y que se aplico en copia local y no en el clon revisado. **No se invento clave bibliografica** (regla 9 raiz): los datos van en prosa y la referencia del software queda en `\GAPLIT` nuevo, con candidato PENDIENTE en `docs/literatura/_candidatos.md` |
| B9. Dos precisiones que refuerzan la brecha: metal fractal aleatorio, y geometria de una sola fila de detector | orquestador (encargo) | APLICADO con cita al articulo | Las dos constan en la ficha con evidencia textual, asi que se citan con `\cite{peters2025hybrid}` y no al repositorio: "random fractal shapes ... inserted in random soft tissue or bone positions" (2.3, p. 4) y "1 detector row with 900 columns ... 1000 views" mas la dispersion escalada a 64 filas (2.1, p. 3); la reconstruccion FDK con "water beam hardening correction" tambien es de la ficha (2.1, p. 3), y se escribe "retroproyeccion filtrada con correccion de agua" sin sigla. **La cuantificacion del salto no usa los "unos 150 mm" del encargo**, que no constan en el documento: se usa la longitud mediana del corredor, 138~mm, de la Tabla de preinscripcion, que es cifra propia ya publicada en el capitulo |
| C10. Asimetria del suelo de $-1000$~HU, cualitativa, con `\GAPDEC` sobre contra cual contraste se evalua la regla | orquestador (encargo) | APLICADO | Parrafo nuevo en §Amenazas, validez de constructo: el sesgo es siempre a la baja, apenas pesa frente al protocolo fisico porque su salida reconstruida baja poco por debajo del suelo, y pesa mucho mas frente a la distribucion de las observaciones reales, que alcanza valores de TC muy inferiores. Se anade que la diferencia se apoya en una sola corrida local, de modo que ordena la gravedad y no fija una cota. **Sin ninguna cifra de #141, #144, #145 ni #146**. El `\GAPDEC` del suelo que puso r06 sigue en §Sintetizador, con su pregunta original; el nuevo no la duplica |
| D11. Los 30 000 pasos, con la salvedad en la misma oracion | orquestador (encargo) | APLICADO | En §Sintetizador, parrafo de los pares de entrenamiento: "El entrenamiento se fija en 30 000 pasos, una eleccion de hiperparametro hecha sobre el conjunto de validacion y no fijada de antemano", mas la meseta de la curva y que ningun paciente de prueba intervino, de modo que la regla de aislamiento estricto se mantiene. El `\GAPDEC` de congelar el diseno pasa a decir "los demas parametros de entrenamiento" (PAT-19). **No se escribe el numero de pacientes de validacion**: DEC 2026-10-05 (1) y (2) dicen 5, y el capitulo declara 8 casos de validacion y 3 pacientes con implante real tras el criterio de inclusion; la cifra se omite para no fijar una discrepancia (vease abajo) |
| Lint, 4 hallazgos de severidad baja (E-P1, lineas 73, 190, 208 y 281) | lint r07 | NO APLICADO | Los cuatro son anteriores a esta ronda y estan fuera del encargo acotado: ninguna de las lineas se toco. Siguen identicos tras los cambios (la 267 es ahora la 281 por el desplazamiento de lineas) |

Efecto colateral que se corrigio al minimo, y se declara: la fila 3 de la tabla de diseno
experimental listaba como comparacion "Copia y pegado; protocolo fisico" y como analisis
"Wilcoxon; TOST", lo que contradecia la jerarquia recien escrita en el cuerpo (PAT-67, G-T1). La
celda pasa a nombrar los tres contrastes en su orden, con el papel de cada uno. Por la misma razon,
§Resumen del diseno dice ahora que del Objetivo 3 se fijaron el criterio primario, su definicion
operativa y el orden de los contrastes, y que el margen $\Delta$ sigue pendiente.

## GAP cerrados, estrechados y abiertos

| Marca | Que | Estado |
|---|---|---|
| `\GAPDEC` ubicacion de las regiones de medicion respecto de `B_delta` | DEC 2026-10-05 (4) fija los cuatro parametros | **CERRADO** |
| `\GAPDEC` agregacion por paciente antes de Wilcoxon y TOST | DEC 2026-10-05 (3) §4 | **CERRADO** en `capitulo3`; sigue en `capitulo1` §Marco estadistico, no tocado |
| `\GAPDEC` que resultado de la superioridad contaria como fallo, o si la decisiva es la equivalencia | DEC 2026-10-05 (3) §5 | **CERRADO** en `capitulo3`; sigue en `introduccion` §Objetivos, no tocada |
| `\GAPDEC` inversion de cada metrica de Peters et al. | queda solo `bone integrity` y `metal integrity` | **ESTRECHADO**; pendiente de estrechar igual en `introduccion` y `capitulo2` |
| `\GAPDEC` metrica y analisis del realismo | el contraste esta fijado; falta la distancia y su analisis | **ESTRECHADO**; pendiente igual en `introduccion` §Objetivos |
| `\GAPDATO` protocolo fisico | ya no dice "implementacion y resultados": el protocolo se corrio en local y su codigo se reviso; faltan los resultados sobre esta anatomia y estas poses | **REFORMULADO** |
| `\GAPLIT` referencia del software del protocolo fisico | nueva | **ABIERTO**, con candidato PENDIENTE |
| `\GAPDEC` contra cual contraste se evalua la regla del suelo | nueva | **ABIERTO** |

Totales del lint: `alta=0 media=0 baja=4`, `GAP lit=1 dato=9 dec=23` (antes `lit=0 dato=9 dec=25`).
Compila: 114 paginas, sin citas indefinidas ni avisos de referencia.

## Pendientes para la autora (no se resolvieron aqui)

1. **Numero de pacientes de validacion.** DEC 2026-10-05 (1) y (2) hablan de "los 5 pacientes de
   validacion"; el capitulo declara 8 casos de validacion en la particion y 3 pacientes con implante
   real tras el criterio de inclusion. El texto de los 30 000 pasos se escribio sin esa cifra. Si la
   autora confirma cual es la unidad de cada numero, entra sin marca; si no, hace falta un `\GAPDEC`.
2. **Tamano del brazo fisico.** DEC 2026-10-05 (3) §4 fija las pruebas pareadas sobre n = 14,
   mientras §Apariencia mantiene el `\GAPDEC` del "subconjunto reducido de pacientes" del protocolo
   fisico. Las dos cosas conviven en el texto; si el brazo fisico corre sobre los 14, ese `\GAPDEC`
   se cierra solo.
3. **#145 esta ABIERTA y su confirmacion esta corriendo.** El capitulo no dice nada del rendimiento
   del renderizador ni de que punto de control es mejor, tal como pedia el limite 1 del encargo.

## Decisiones de redaccion

| Decision | Por que | Donde debe aplicarse igual |
|---|---|---|
| La verdad de terreno de la `streak amplitude` para sintesis se nombra "la TC original sin metal del mismo paciente", y lo que se mide donde hay implante real se llama **discrepancia**, nunca amplitud | DEC 2026-10-05 (3) §1 separa las dos magnitudes; usar un solo nombre para las dos haria pasar por endpoint lo que no lo es | `introduccion` §Objetivos (Obj 3), `capitulo4` |
| Las ROIs del endpoint son **anillos completos** en planos perpendiculares al eje, y se llaman "regiones de medicion" (decision de capitulo1-r06, S10). "Anillo" y "banda" no se intercambian: "banda" sigue reservada a `B_delta` (PAT-14) | evita competir con la region de generacion `G` y con la banda | `capitulo1`, `capitulo4` |
| Un contraste que no puede fallar se declara con esas palabras: "control de cordura y no evidencia de calidad", "una debilidad reconocida del diseno y no una victoria del metodo", seguido de la consecuencia (ningun resultado cuenta a favor) | G-C9 y PAT-52 piden la consecuencia, no solo la salvedad | `introduccion` §Objetivos, `capitulo4` |
| Reproducir un protocolo publicado se llama **verificacion de reproduccion**, nunca validacion; y se dice en la misma oracion que validar exigiria fantoma con material conocido y un tomografo real | DEC 2026-10-05 (5) §1 y el limite de #8; "validar" en este contexto afirma lo que la tesis no puede sostener | `capitulo2`, `capitulo4`, `conclusiones` |
| Un hecho observado en el codigo o en los archivos de un repositorio publicado entra como hecho, con los identificadores en prosa (revision, licencia) y un solo `\GAPLIT` por la referencia del software. No se inventa clave bibliografica ni se cita el articulo por lo que solo esta en el codigo | regla 9 raiz y regla 4 de `overleaf/CLAUDE.md` | todo el documento |
| Cuando una ficha sostiene un hecho que una decision tambien afirma, se cita la ficha y se escribe lo que la ficha dice, no la version mas fuerte de la decision (caso de la colocacion "manual" de las ROIs de Peters et al.) | E-R6; la autoridad de DEC decide **que** se afirma, la ficha decide **con que palabras** se le atribuye a la fuente | todo el documento |
| Una cifra que el encargo da de memoria se sustituye por la cifra equivalente que ya existe en el documento (138~mm de longitud mediana del corredor en lugar de "unos 150 mm") | regla 5 de `overleaf/CLAUDE.md`: las cifras propias se copian de `tesis/main.tex` o de `experiments/` | todo el documento |
