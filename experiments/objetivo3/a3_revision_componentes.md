# Revision de laminas de componentes metalicos (autora) — #104

Planilla: `a3_revision_componentes.csv` (**40 filas**, ordenadas por volumen ascendente). Solo la llena la
autora; `veredicto` y `nota` empiezan vacias. Laminas en `outputs/a3/laminas/` (fuera de git).
Se generan con `python a3_laminas_componentes.py --out outputs/a3` (semilla 20260920, reproducible).

## Que se decide con esto, y que NO

**Se valida un CRITERIO, no 40 componentes.** A1b partio el metal de la cohorte en **363 componentes**, y cada
uno es una unidad de entrenamiento del renderizador (decision D2, #102). #104 mostro que son en buena parte
fragmentos: volumen mediano **458 mm3** frente a los ~1450 mm3 de un tornillo de 4.8 x 80 mm, con el **52%**
por debajo de 500 mm3. Hay que fijar un **umbral declarado** de que cuenta como implante, y la propuesta sobre
la mesa es **200 mm3**.

Esta revision contesta una sola pregunta: **¿el filtro automatico acierta?** Si acierta, el umbral queda
justificado con evidencia propia y se preinscribe. Si falla, se recalibra **antes** de entrenar.

**No es un juicio clinico.** Distinguir "objeto alargado y fino" de "placa, protesis o fragmento" es geometria,
no diagnostico. No hay que decidir si la cirugia fue correcta, ni en que vertebra esta, ni si hay lesion: eso
si requeriria un medico, y por eso #53 fue a un revisor clinico y esto no.

## La muestra

Estratificada por volumen en escala logaritmica, con **sobremuestreo deliberado de la franja 100-500 mm3**,
que es donde cae el umbral en discusion y donde la decision se juega. Cubre de **11 mm3 a 15 530 mm3**.
La columna `propuesta_auto` trae lo que dice hoy el filtro: **17 `fragmento`, 17 `otro implante`, 6 `tornillo`**.

## Vista 3D interactiva (A4), para decidir "dentro o fuera del cuerpo"

Las laminas sirven para juzgar **forma**, pero no **donde esta** el objeto. Esa pregunta aparecio sola al
revisar (#105): hay metal que no esta dentro del paciente —electrodos, cursores de cremallera, botones—
y en una proyeccion recortada eso no se distingue de un implante.

`python a4_html_componentes.py --out outputs/a3` escribe **un HTML por caso** en `outputs/a3/html/`, en el
mismo formato que los de `exploration-3d/outputs/` (plotly, offline, se abre en el navegador). Trae:

- **silueta del paciente** a 300 HU, marfil y casi transparente: la referencia de dentro o fuera;
- **hueso** a 1500 HU, apagado por defecto (se enciende desde la leyenda);
- cada componente muestreado, **coloreado por lo que propone el filtro**: **verde = tornillo**,
  naranja = otro implante, gris = fragmento.

**El color es la hipotesis, no la verdad.** Es lo que hay que contrastar: si algo **verde** aparece
flotando **fuera de la piel**, el filtro se equivoco, y ese es exactamente el dato que esta revision busca.
Cada componente es una entrada de la leyenda, asi que se pueden encender y apagar uno por uno.

## Que muestra cada lamina

Cuatro paneles, todos recortados a la caja del componente:

1. **`proyeccion axial`** — silueta vista por el eje de los cortes.
2. **`proyeccion 1`** y **`proyeccion 2`** — las otras dos vistas. **Aqui se juzga la forma**: un tornillo se ve
   alargado y fino, con un extremo mas ancho (la cabeza); una placa se ve plana y ancha; un fragmento se ve como
   una mancha sin eje.
3. **`CT, corte N`** — el TAC real en ventana osea con el componente contorneado en rojo, para ver **donde esta**
   y si lo que el umbral capturo coincide con el objeto que se ve.

El encabezado trae volumen, largo y anchos por **eje principal** (PCA, la misma medida de E11 — no la caja
alineada a los ejes, que exagera los objetos oblicuos), numero de parches que aporta, y la referencia de
~1450 mm3 para comparar.

## Como llenar `veredicto`

| Valor | Cuando |
|---|---|
| `tornillo` | objeto alargado y fino, con eje claro; puede tener un extremo mas ancho |
| `otro implante` | metal deliberado **dentro del cuerpo**: placa, protesis, clavo grande, cerclaje |
| `externo` | **metal que no es un implante**: electrodo de ECG, cursor de cremallera, boton, broche o accesorio de ropa, borde de mesa. Tipicamente **fuera del cuerpo** o pegado a la piel |
| `diu` | dispositivo intrauterino: es interno y deliberado, pero **no es osteosintesis** y no toca hueso |
| `fragmento` | trozo suelto, sin eje, o parte evidente de un objeto mayor que el umbral partio |
| `no es metal` | el umbral capturo algo que no es un objeto (artefacto puro, contraste) |
| `dudoso` | no se puede juzgar con estos paneles |

**`externo` y `diu` se anadieron el 2026-09-20**, a raiz de la observacion de la autora al mirar las primeras
laminas: aparecen objetos que ni siquiera estan dentro del cuerpo. El esquema original no los contemplaba y los
habria forzado a `otro implante`, que es justo el error que contamina el entrenamiento. Ver **#105**.

**Como distinguirlos en la lamina:** en el panel del CT, un `externo` aparece **en el borde o fuera de la
silueta del paciente**, a menudo sobre la piel o en el aire; un electrodo se ve como un disco o boton pequeno
pegado a la superficie, y un cursor de cremallera como una pieza compacta con forma de herraje. Un implante
osteosintetico esta **dentro del hueso** y se ve continuo con la cortical.

En `nota`, que se ve y en que panel. **Las laminas son proyecciones y un corte: no demuestran ausencia de
error** (#19, #21). Un `dudoso` no se fuerza, se deja como `dudoso`.

## Que se hace despues con los resultados

1. **Se mide el acuerdo** entre `propuesta_auto` y `veredicto`, y se reporta la tabla de confusion completa, no
   solo el porcentaje. Interesa sobre todo el tipo de error:
   - **`fragmento` automatico que resulta `tornillo`** -> el umbral de 200 mm3 esta **alto** y descarta implantes
     reales. Es el error caro: quita datos buenos.
   - **`tornillo`/`otro implante` automatico que resulta `fragmento` o `no es metal`** -> el umbral esta **bajo**
     y mete ruido de entrenamiento. Es el error que #104 sospecha.
2. **Si el acuerdo es alto**, el umbral se preinscribe tal cual, citando esta revision como su justificacion.
3. **Si aparece un patron de error**, se recalibra el umbral (o se anade el criterio de elongacion por PCA) y se
   vuelve a mirar **la misma muestra**, sin generar una nueva: cambiar de muestra tras ver el resultado seria
   seleccionar el dato que conviene.
4. En los dos casos, la decision se escribe en **`docs/01-decisiones.md`** y se cierra **#104** en
   `docs/04-implicancias.md`.

**Nada de esto se entrena antes de que la politica este escrita.** Es la condicion que #104 pone y la que
distingue un criterio preinscrito de uno elegido a posteriori.

## Donde queda el registro

| Que | Donde | Quien |
|---|---|---|
| Los veredictos | `experiments/objetivo3/a3_revision_componentes.csv` (versionado) | **la autora** |
| Las laminas | `experiments/objetivo3/outputs/a3/laminas/` (fuera de git, regenerables) | el script |
| El acuerdo medido y la tabla de confusion | `a3_revision_componentes.md`, seccion nueva al final | el asistente |
| La politica de muestreo ya decidida | `docs/01-decisiones.md` | **la autora** (o el asistente por orden suya) |
| El cierre del hallazgo | `docs/04-implicancias.md`, #104 | el asistente |
