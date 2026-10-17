# introduccion — r09-puntual — respuesta del redactor

Correccion puntual sin ronda nueva (ENCARGO 2026-10-16, fila de introduccion). No hay reportes de revisores;
las filas son los tres `\GAPDATO` que el encargo manda cerrar. Formulacion tomada de `capitulo3.tex` (r27) para
G-B10.

| Hallazgo | Revisor | Decision | Detalle |
|---|---|---|---|
| `\GAPDATO` D9, §Justificacion (l. 68) | encargo | APLICADO | DEC 2026-10-16 (3) pto 1, #197 (DECIDIDA). "el analisis exploratorio que las generaria solo con el sintetizador se fijo y no se ejecuto, y queda como trabajo futuro (Seccion sec:ap-sintesis). Que la sintesis opere sobre una pose del muestreador es, asi, una propiedad del diseno y no un resultado evaluado." Igual que capitulo3 :359 y §Validez externa. Revisado el resto de la introduccion: ninguna oracion dice que el Obj 3 se evalua con poses del muestreador (l. 52 fija el eje sin perturbar; l. 66 y l. 98 describen el condicionamiento por la pose, no la evaluacion) |
| `\GAPDATO` segundo corredor bajo S1, §Alcance (l. 78) | encargo | APLICADO | DEC 2026-10-16 (3) pto 2. "Su eje esta medido en 69 de los 72 pacientes de la cohorte del Objetivo 2 y se reporta como dato de la geometria del corredor. El muestreo de poses en el no se preinscribio ni se ejecuto, y queda como trabajo futuro." Cifra copiada de capitulo3 :196 (alli "cohorte primaria"; la introduccion la nombra "cohorte del Objetivo 2", como en l. 92 y l. 94) |
| `\GAPDATO` envolvente/canal, §Alcance (l. 96) | encargo | APLICADO | DEC 2026-10-16 (2), #196 opcion (a); `experiments/registro/registro_2026-10-16.md` §2. Cifras copiadas de capitulo3 :529: 71 de 72 medidos (en el restante, `CLINIC_0044`, no se reprodujo la envolvente), hueco medial con HU de partes blandas o grasa, cierre lo ocupa solo en 14, tramos de hasta 6.4 mm en el eje craneocaudal; limites "no establece que ese hueco sea el canal, ni mide los foramenes o el efecto sobre la brecha de ninguna pose", con remision a sec:amenazas. Se omite el 6.3 mm AP para mantenerlo breve (el encargo pide "una sola vez, breve") |
| Parrafo de l. 96 a 8 oraciones (PAT-58) | redactor | APLICADO | Consecuencia de cerrar el GAP: el parrafo se parte en dos por funcion (etiqueta de S1 / envolvente osea), sin cambiar texto. La oracion inicial sigue anunciando las dos piezas |
| #138 y control visual E-A4 | encargo | sin cambio | La introduccion no menciona #138 ni E-A4; la oracion de la etiqueta de S1 (l. 96) no se toco |

Lint (`python scripts/lint_redaccion.py introduccion --compilar`): alta 0, media 1, baja 1; GAP lit 0, dato 0,
dec 0; FALLA solo por la oracion de 41 palabras de l. 7 (encabezado, DESFASADO por #126, fuera del encargo) y el
bajo de "robustos" en l. 7. Compila: 165 paginas.

## Decisiones de redaccion

- En la introduccion, la cohorte primaria del Objetivo 2 se nombra "cohorte del Objetivo 2" (72 pacientes), como
  en sus parrafos de limitaciones; el cap. 3 conserva "cohorte primaria".
- Cierre de un GAP con un calculo posterior en la introduccion: cifra con su n, limites como hecho ("no establece",
  "no mide") y remision a la seccion del cap. 3 que la discute; se omiten las cifras secundarias (6.3 mm AP).
