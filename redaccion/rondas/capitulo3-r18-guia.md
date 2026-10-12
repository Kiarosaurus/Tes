# Revision guia CS — capitulo3 — r18

Entrada: `overleaf/secciones/capitulo3.tex` (estado tras la respuesta r17), lint `capitulo3-r18-lint.md` (PASA, 11 E-P1
baja), respuesta `capitulo3-r17-respuesta.md` (nada RECHAZADO que reabrir; guia-1 a guia-5 de r17 resueltos en el
texto). Cotejado con `redaccion/ENCARGO_2026-10-12.md` (P1-P6), `docs/04-implicancias.md` #172, #173, #174 y #175,
`experiments/objetivo3/resultados_validacion_pose.md` y `docs/ESTADO.md`:32-42.

Nota de alcance: el texto revisado es anterior a la correccion de la pose (#173). Lo que el encargo ya pide en
P1-P6 (cifras del cotejo en :232 y :234, material en :327 y :329, sonda en :319-321, $\Delta$ en :337, :339 y :385,
GAPDATO de :206, "en curso" de :216 y la declaracion del error de pose en amenazas) **no se repite como hallazgo**.
Los hallazgos de abajo son lo que el encargo no cubre, o la consecuencia argumentativa que deja abierta.

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-C7 | capitulo3.tex:38 | Patron PAT-13 reincide (afin a PAT-150). Dice que el diseno se enmendo el 11 de octubre "antes de procesar con él la partición de prueba" y que la corrida final es "la única que procesa la partición de prueba con el modelo evaluado". Segun `ESTADO.md`:32 y :38 y #172-#173, el modelo evaluado ya proceso la particion de prueba con la pose equivocada y la lectura de 0.05 (job 55859, cortado), y el estado final completo los 13 pacientes (55911). El encargo P1 solo pide mencionarlo en amenazas, y la definicion de :38 seguiria siendo falsa. | Redefinir la corrida final como la que procesa la particion de prueba con la pose corregida y la lectura calibrada. Decir en :38 que hubo generaciones previas sobre la particion de prueba con el modelo evaluado y la pose equivocada, que no se evaluaron, y remitir a amenazas. Si "no evaluadas" no puede verificarse en el registro, va como `\GAPDATO` (encargo P1). |
| guia-2 | media | G-T4 | capitulo3.tex:38 | Patron PAT-122 reincide. El `\GAPDATO` de la vision general dice que el cotejo "se rehace con el límite de lectura de HU recalibrado" y que no hay resultados sobre la particion de prueba. Segun #174, el cotejo ya se rehizo con 0.030 y la pose corregida, y segun el encargo P6 la corrida final de los dos brazos y la de E-A1 ya se ejecutaron. El encargo solo nombra :206 y :216, asi que este GAP quedaria envejecido. | Reescribir el `\GAPDATO`: la cadena se ejecuto sobre dos pacientes de validacion con la pose corregida; la corrida final de los dos brazos y la reconstruccion de implantes reales ya se ejecutaron; falta su evaluacion. |
| guia-3 | media | G-T4, G-C7 | capitulo3.tex:236 | Este parrafo sostiene que la sensibilidad con el estado final es "la lectura conservadora", pero sus cifras son de la pose espejada: 749/1076 frente a 977/1238 HU, y titanio 2051/1279 HU. El encargo P5 corrige las de :325 y no nombra :236. Con la pose corregida (`resultados_validacion_pose.md` §3) son 1164/1163 (estado final) frente a 1248/1182 (elegido), y titanio 1881/1287. El sentido del argumento se mantiene, pero no se puede verificar con las cifras impresas. | Sustituir las tres parejas de cifras por las de la pose corregida, o remitir a :325 sin repetirlas. El argumento de la lectura conservadora no cambia. |
| guia-4 | media | G-C7 | capitulo3.tex:377-383 | Patron PAT-140 reincide. A la lista de decisiones del Obj 3 tomadas despues de ver datos le faltan tres que #173-#174 registran: (1) el control de pose, criterio de cordura no preinscrito, fijado tras ver las colocaciones (#173 "Aplicado"); (2) no rehacer la sonda y conservar su veredicto, tomado con la pose equivocada (#174 (c)); (3) mantener el titanio, que gana por 2 de 24 cascaras, con la lectura "el menos alejado" (#174 (b)). El encargo P1 pide declarar el error de pose, pero no pide sumar estas decisiones a la lista. | Sumar las tres a la enumeracion de :377-379, cada una con la regla previa que aplica o sin ella, y con su sentido si esta registrado. Si el parrafo de :383 pasa de siete oraciones, partirlo (PAT-58). |
| guia-5 | media | G-C7, G-A8 | capitulo3.tex:401 | Afin a PAT-52: la debilidad se nombra con su consecuencia en un solo sentido. :401 dice que "la equivalencia con el protocolo físico no implica cercanía a las observaciones reales". No dice lo simetrico: el protocolo con titanio queda por encima de lo real en 22 de 24 cascaras (#174) y el p95 sintetico queda por debajo, asi que un intervalo entero por debajo de $-\Delta$ tampoco mostraria que el sintetizador se aleja de lo real. Ese es el desenlace que el `\GAPDEC` de :335 deja sin lectura. | Agregar en :401 una oracion con la consecuencia en el otro sentido: un resultado de no equivalencia no se atribuye por si solo al sintetizador. Remitir al `\GAPDEC` de :335. Sin citar la diferencia de validacion como conclusion (encargo P5). |
| guia-6 | baja | G-C7 | capitulo3.tex:377 | "Esa segunda corrida mantuvo la comparación de equivalencia como contraste primario". Segun #174 (c), la sonda se corrio con la pose equivocada, y quien confirma su veredicto es el protocolo completo en validacion, a posteriori y sin aplicar el tercer criterio escrito (amplitud con hierro de al menos el triple del ruido). El encargo P4 pide la frase de confirmacion en :321, pero en amenazas el lector no veria que el contraste primario se sostiene en una confirmacion posterior. | En :377, una clausula: el veredicto que mantuvo el contraste primario se tomo con la pose equivocada, y despues se confirmo con el protocolo completo en validacion, sin el criterio escrito de la sonda. |
| guia-7 | baja | P-MM3 | capitulo3.tex:321 | Riesgo al aplicar el encargo P4, que retira todas las cifras de la sonda: :321 es el unico sitio que justifica simular "un corte de cada dos". Ese submuestreo condiciona :287 y la amenaza de :411. Si sale el costo de 108.9 h frente al limite de 72 h, el lector deja de poder reconstruir por que se submuestrea. | Mantener sin cifras que el costo fue el unico criterio que fallo y que por eso se aplico la salida fijada de un corte de cada dos. Que el costo dependa de la pose lo decide el redactor con el registro. |

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple con GAP |
| G-T2 | cumple ("modelos afectados", "auditorias de identidad de paciente", "punto de control" y "corrida final" definidos una vez; la definicion de "corrida final" queda falsa, ver guia-1) |
| G-T3 | cumple ($\Delta$ solo para el margen; "limite" para 0.01/0.05/0.030) |
| G-T4 | no cumple (guia-2, guia-3; las demas cifras desfasadas las cubre el encargo P2-P6) |
| G-T5 | cumple |
| G-T6 | cumple (el lint no reporta E-F) |
| G-C1 | cumple con GAP (cabeza de $M$, lotes, regla del suelo en HU) |
| G-C2 | cumple con GAP (algoritmo del eje, heuristica de referencias, prediccion $v$, repositorio AAPM). La conversion de la pose al marco del volumen y el control de pose faltan en el texto, pero los pide el encargo P1 |
| G-C3 | cumple |
| G-C4 | cumple dentro del cap. 3 (el cruce con la introduccion sigue desfasado, como en r17; no evaluable aqui) |
| G-C5 | cumple con GAP |
| G-C6 | cumple (copia y pegado como cordura, protocolo fisico como comparacion, sensibilidades declaradas) |
| G-C7 | no cumple (guia-1, guia-4, guia-5; guia-6 menor; el error de pose lo cubre el encargo P1) |
| G-C8 | cumple con GAP (supuesto de la *t*, desenlaces del TOST, tamano de efecto) |
| G-C9 | cumple (el protocolo fisico publicado es el competidor; que "ningun material reproduce lo real" lo cubren :329 (encargo P3) y :401) |
| P-MM1 | cumple |
| P-MM2 | cumple (Figura `fig:pipeline`) |
| P-MM3 | cumple con GAP (riesgo de guia-7 al aplicar P4) |

## Propuestas de criterio
- Bloque (c): si una correccion de implementacion obliga a rehacer mediciones, el metodo debe listar que se rehizo y
  que no, y cada parrafo que cita la medicion vieja debe quedar cubierto. Hoy cabe en G-T4 y G-C7, pero la rubrica
  no lo nombra.
- Fuera de mi dominio, para `revisor-estilo`: :383 (7 oraciones) y :385 (9 oraciones) estan al limite de E-O2 o lo
  pasan, y los encargos P1 y P5 les agregan texto.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Al rehacer una medicion, la lista de pasajes que la citan omite uno, que conserva la cifra vieja | G-T4 | :236 "medianas entre semillas de 749 y 1076 HU frente a 977 y 1238" | nuevo (afin a PAT-11/PAT-122) |
| Integridad del congelamiento ("la unica corrida que procesa prueba") que una corrida descartada posterior desmiente | G-C7 | "la corrida final, la única que procesa la partición de prueba" | PAT-13 (afin a PAT-150) |
| Lista de decisiones post hoc que no incorpora los criterios agregados al corregir un error de implementacion | G-C7 | control de pose no preinscrito ausente de la lista de :377-383 | PAT-140 |
| Debilidad del comparador con su consecuencia en un solo sentido del desenlace | G-C7, G-A8 | "la equivalencia ... no implica cercanía" sin el caso de no equivalencia | PAT-52 (afin) |

alta=0 media=5 baja=2
