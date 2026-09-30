# Respuesta del redactor — capitulo3 — r03

Insumos: `capitulo3-r03-lint.md` (PASA, 0/0/5), `-guia.md`, `-estilo.md`, `-traza.md`. Se aplica el criterio
de r02: una cifra congelada en `docs/01-decisiones.md` (DEC) entra como hecho. Ningun hallazgo se saco por
oscilacion. Siglas de fuente: las de `capitulo3-r03-traza.md` (TM, PRE, DAT, DEC, IMP, RES, E12, R1).

## Hallazgos de severidad alta y media

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-1 (recorte sin definir, l.85) | guia | APLICADO | Se define en la primera aparicion: el recorte es un modelo previo de menor resolucion que delimita la region de interes; por defecto 6 mm, alternativo 3 mm (`--robust_crop`). Fuente: DEC 2026-09-14 (4) (:763-765, 6 mm / 3 mm); IMP #49 hallazgo 3 (:3938-3940, descripcion del codigo). De #49 (ABIERTA) solo se toma la descripcion de la herramienta; la eleccion del recorte ya la fijo DEC |
| guia-2 (69 "sin objeto metalico" frente a 66 del grupo 3) | guia | APLICADO | Junto con T01. l.95: "69 pacientes de `dataset6` que la revision tridimensional clasifico sin objeto" y una oracion que dice que ese conjunto no coincide con el grupo 3 (66). Fuente: R1:4 (69); DAT:127 (69 pacientes) y DAT:137 (grupo 3 = 66). No se afirma cronologia ni cuantos pasaron al grupo 2, porque ninguna fuente leida da ese numero |
| guia-3 (supuesto mascara-artefacto sin justificar ni en amenazas) | guia | APLICADO | l.180: se dice que el supuesto no se verifico y se da el dato que motivo no filtrar (5 de 40 componentes revisados eran tornillos). Fuente: DEC 2026-09-21 "Lo que se descarto" (:1301-1303). Se anade a validez de constructo como supuesto no verificado, con remision a la seccion |
| S01 ("mas del doble", l.101) | estilo | APLICADO | Se retira el factor; queda "mas seccion de metal que el cuerpo de 4.91 mm de la Tabla". El factor viene de TM:117 ("more than a factor of two"), pero no vale en todo el rango y la decision de §2 excluye factores calculados. Se deja nota para la autora (abajo) |
| S02 (isotropia, l.158) | estilo | APLICADO | Reformulado sin anadir argumento: "Fijarla a juicio anadiria un parametro sin dato que lo sostenga, el mismo defecto que tendria tomarlo de la referencia clinica". Fuente: PRE §3.2 ("ponerlo a ojo seria el mismo defecto que calibrar contra el benchmark"). No se adopta la variante del revisor ("el unico criterio disponible seria la referencia clinica") porque PRE no lo dice |
| S03 (parrafo de dos oraciones, l.176) | estilo | APLICADO | Unido al final del parrafo de l.174 sin cambiar el texto |
| S04 (oracion final suelta, l.209) | estilo | APLICADO | "se considero y se rechazo por dos razones. La primera ... La segunda, que Zwingmann et al. tampoco reportan haber excluido a sus pacientes de corredor estrecho". Fuente: TM:109 ("the reference series did not exclude its own narrow-corridor patients either"). No se adopta la consecuencia propuesta ("dejaria de ser comparable"), que TM no enuncia |
| S05 (parrafo de validez interna demasiado largo, l.251) | estilo | APLICADO | Partido en dos: Objetivo 2 (circularidad, decisiones post hoc, control de nivel, fractura) y Objetivo 1/3 (exploracion previa, rediseno, extension a Guo et al.) |
| S06 ("envolvente" para el calibre nominal) | estilo | APLICADO | Tabla: fila "Calibre nominal"; l.101: "El calibre nominal solo se usa para la viabilidad"; GAPDEC de l.189: "fija el calibre nominal". "Envolvente" queda solo para la envolvente osea. MAPA actualizado |
| S07 ("distribuciones clinicas" junto a "referencia clinica") | estilo | APLICADO | Figura, l.127, l.185, l.196 ("series clinicas" del denominador) y l.257 pasan a "referencia clinica". Se mantiene "dos series clinicas pequenas" en l.207, que describe la referencia y no la nombra de otro modo. En l.251 se quito ademas la repeticion "contra la referencia clinica" dos veces en la misma oracion |
| T01 (69 "sin objeto metalico") | traza | APLICADO | Ver guia-2 |
| T02 (fractura confirmada omitida, l.251) | traza | APLICADO | "Al menos un paciente de la cohorte primaria, con un corredor mas estrecho que el calibre de 7.0 mm, tiene una fractura confirmada por un medico sin especialidad." Fuente: IMP #125 (:8697-8700, confirmacion 2026-09-23 con la salvedad obligatoria; :8702-8704, `D_TS_max` = 6.2 mm, dentro de los 15 estrechos). #125 sigue ABIERTA: no se elige ninguna de sus opciones y se mantiene el `\GAPDATO` del cribado en l.52 |

## Hallazgos de severidad baja

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| guia-4 | guia | APLICADO | Una oracion en validez externa que remite a los tres desplazamientos de dominio |
| guia-5 | guia | APLICADO | l.223 dice ahora que mide Delta (semillas del sintetizador sobre un mismo caso, mas prueba y reprueba del protocolo fisico) y sobre cuantos pacientes (3 con implante real tras el criterio de inclusion). Fuente: DEC 2026-09-21 (2) (:1394-1400). En l.259 queda solo la amenaza |
| guia-6 | guia | APLICADO (variante) | No se escribe $h = 2\sigma_t$: segun PRE §3.1 la misma convencion fija tambien $\sigma_a = \arctan(h/(L/2))/2$. l.158 dice ahora que vale "en distancia para $\sigma_t$ y en el angulo que produce para $\sigma_a$" |
| guia-7 | guia | APLICADO | La referencia clinica se define en su primera aparicion (l.79, en negrita) como las dos series de Zwingmann et al. |
| guia-8 | guia | APLICADO | Los 8 mm son el mismo recorte de extremos de la medicion del corredor; "su razon es clinica y no numerica". Fuente: DEC D-O2.3 pto 4 (:1457-1460); `e9_corredor.py:77` |
| guia-9 | guia | NO APLICADO | Ninguna fuente leida da el motivo de restringir la sensibilidad al grupo 3 (DEC D-O2.2 :1438-1439 y PRE §1 solo la definen). Escribirlo seria completar con conocimiento propio (regla 1 de `overleaf/CLAUDE.md`). Pregunta para la autora abajo |
| S08 | estilo | APLICADO | "Zwingmann et al. reportan distribuciones de malposicion distintas para una serie operada con navegacion y otra con tecnica convencional" |
| S09 | estilo | APLICADO (variante) | "coincide" pasa a "esta proxima a", con ambas cifras visibles (4.91 y 4.8 mm). No se escribe la diferencia de 0.11 mm: es un calculo propio (§2: sin factores calculados) |
| S10 | estilo | APLICADO | "la unica medicion de las fuentes revisadas" |
| S11 | estilo | APLICADO | "sin que la colocacion mejorara" |
| S12 | estilo | APLICADO | Se elimina "se reporta tal como se mide" |
| S13 | estilo | APLICADO | Negrita movida de l.217 a l.185, primera aparicion en el texto corrido |
| S14 | estilo | APLICADO | Tabla: "Mascara del implante $M$" |
| S15 | estilo | APLICADO | "brazo fisico" pasa a "protocolo fisico" en l.221, l.225, l.259 y en los dos GAP de l.221. MAPA actualizado |
| S16 | estilo | APLICADO (parcial) | GAPDATO de l.164: "69 de los 72 pacientes de la cohorte primaria". Se mantiene "18 volumenes" en la submuestra: TM:78 la da en volumenes ("subsample of 18 volumes from the cohort") |
| S17 | estilo | APLICADO | "57 tenian las cinco referencias localizadas y dentro del campo de vision. De los 8 restantes, 7 tenian las crestas iliacas truncadas". Fuente: R1:42 y R1:57-88 (verificado por el auditor) |
| S18 | estilo | APLICADO | "A esos parches se anaden todos los parches disponibles que solo contienen banda, que estan en razon de 0.62" |
| S19 | estilo | APLICADO | El argumento de multiplicidad queda solo en validez de la conclusion |
| S20 | estilo | APLICADO | "La composicion de la cohorte primaria difiere, por eso, de la del conjunto de partida". No se dan porcentajes (serian calculados) ni se afirma si afecta al diametro |
| T03 | traza | APLICADO | l.185 y l.198: uno sobre un fantasma de geometria conocida y cinco sobre el eje del corredor de dos volumenes reales; la resolucion de 0.083 mm "en el fantasma". Fuente: E12:3-89, :96 |
| T04 | traza | APLICADO | l.95 "reviso el nivel S1"; l.97 "computable con el nivel S1 correcto segun el revisor clinico en 48". Fuente: R1:45-46 |
| T05 | traza | APLICADO | "Este trabajo lee ese margen ... como una distancia radial ... Con esa lectura, $h$ equivale al radio del corredor de 10 mm". Fuente: DEC 2026-09-11 (2) |
| T06 | traza | APLICADO | "numero de semillas por caso" se anade al `\GAPDEC` de l.170; en l.223 "el numero de semillas por caso no esta fijado". Se retira "varias semillas". MAPA actualizado |

Cambios adicionales para cerrar el lint: al aplicar T05, guia-1, S01, S09, guia-6, T03 y T02 quedaron nueve
oraciones de mas de 40 palabras (E-O1, media). Se partieron sin cambiar su contenido. Lint final: PASA,
alta 0, media 0, baja 4 (E-P1, mismas lineas de cifras con fuente en DEC que en r02).

## Escalados

Ninguno nuevo en esta ronda. Los `\GAPDEC` de r01-r02 siguen como estaban (implicancia #127).

## Notas para la autora (no son GAP nuevos)

1. **guia-9.** Por que la cohorte de sensibilidad del Objetivo 2 son solo los pacientes del grupo 3 (sin objeto)?
   El revisor pide una oracion con la hipotesis que pone a prueba; ninguna fuente del repositorio la da.
2. **S01.** `tesis/main.tex:117` dice que un cilindro de 6.5-8.0 mm "would overstate the metal cross-section ...
   by more than a factor of two" (tambien DEC :1193). El factor no se cumple en el extremo inferior del rango
   frente a un cuerpo de 4.8-4.91 mm. El capitulo ya no lo afirma; `main.tex` sigue diciendolo.

## Decisiones de redaccion

- "Referencia clinica" se define en su primera aparicion (en negrita) como las series navegada y convencional
  de Zwingmann et al., y es el unico nombre en todo el documento: ni "distribuciones clinicas" ni "series
  clinicas" como nombre (si como descripcion: "dos series clinicas pequenas").
- "Envolvente" solo para la envolvente osea. El rango 6.5-8.0 mm es el "calibre nominal"; hay tres geometrias:
  calibre nominal, mascara del implante $M$ y calibre de medicion.
- "Protocolo fisico" (de Peters et al.) tambien para el brazo de comparacion, incluidos los textos de GAP;
  "brazo" solo en plural generico ("tres brazos").
- Recorte de TotalSegmentator: "recorte por defecto" (modelo de 6 mm) y "recorte alternativo" (3 mm,
  `--robust_crop`), definidos en la primera aparicion.
- Controles de SAP: "seis controles, uno sobre un fantasma de geometria conocida y cinco sobre volumenes reales";
  nunca "seis controles sobre geometria conocida".
- Una lectura operativa propia de una fuente se introduce como "este trabajo lee ... como ...", no como
  propiedad del marco citado.
- Cercania entre cifras: "esta proxima a" con ambas cifras visibles, sin diferencia ni factor calculado.
- Revisor clinico de S1: "reviso", no "confirmo" (su revision dio S1 correcto en 51 de 65).
