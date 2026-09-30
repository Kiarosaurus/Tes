---
name: ciclo-redaccion
description: Redacta y revisa en bucle una seccion del documento de tesis UTEC (overleaf/secciones/<seccion>.tex), o hace la pasada global con "documento", hasta que el lint pase y los tres revisores (guia CS, estilo, trazabilidad) no dejen hallazgos altos ni medios, con tope de rondas y deteccion de oscilacion. Usar cuando la autora pida redactar, corregir o revisar el documento de overleaf.
argument-hint: <seccion|documento> [rondas=5]
---

# /ciclo-redaccion

Orquestas; no redactas ni revisas tu mismo. Las tareas van a los subagentes `redactor-tesis`,
`revisor-guia-cs`, `revisor-estilo` y `auditor-trazabilidad`. Tu trabajo es correr el bucle, decidir
cuando parar y reportar a la autora.

Argumentos: `$ARGUMENTS`. Primer argumento: nombre del `.tex` sin extension (`introduccion`,
`capitulo1` ... `capitulo4`, `conclusiones`, `trabajosFuturos`, `resumen`, `abstract`) o
`documento`. Segundo, opcional: tope de rondas (por defecto **5**).

## 0. Preparacion

1. Lee `overleaf/CLAUDE.md`, `redaccion/MAPA.md` y `redaccion/BITACORA.md`.
2. Si la seccion es `resumen` o `abstract` y algun capitulo sigue en esqueleto o DESFASADO segun
   `MAPA.md`, **para** y dile a la autora que el resumen se escribe al final (regla 7).
3. El modelo de prosa es la guia del departamento (`ESTILO.md` §1.1). `muestras_autora.md` es
   opcional y se suma si tiene texto; si esta vacio, no hace falta avisar.
4. Numero de ronda: mira `redaccion/rondas/<seccion>-r*-lint.md`; la primera ronda nueva es la
   siguiente a la ultima que exista. Guarda `r0` = esa primera ronda.

## 1. Redaccion inicial (solo si hace falta)

Si `MAPA.md` marca la seccion como esqueleto, plantilla o DESFASADO, lanza `redactor-tesis` en modo
`redactar` con la seccion. Espera su respuesta y **cierra la etapa `r00`** (paso 2g). En `documento`
no se redacta: se salta este paso.

## 2. Bucle, para r = r0 ... r0 + tope - 1

a. **Lint**:
   `python scripts/lint_redaccion.py <seccion> --compilar > redaccion/rondas/<seccion>-rNN-lint.md`
   (en `documento`, sin argumento de seccion). Guarda el total y si dice PASA o FALLA.

b. **Revision en paralelo**: lanza en **un solo mensaje** tres llamadas Agent, a
   `revisor-guia-cs`, `revisor-estilo` y `auditor-trazabilidad`. A cada una le pasas:
   seccion, `rNN`, ruta del lint de esta ronda y, si r > r0 o existe una ronda previa, la ruta de
   `redaccion/rondas/<seccion>-r(NN-1)-respuesta.md`. Cada revisor arranca sin contexto de rondas
   anteriores, salvo esa respuesta; eso es a proposito, para que no se autoconvenza.

c. **Criterio de parada por convergencia**: si el lint dice PASA **y** los tres revisores devuelven
   `alta=0 media=0`, **para: CONVERGIO**.

d. **Deteccion de oscilacion**: lee los tres reportes y compara con la ronda anterior. Un hallazgo
   oscila si, con el mismo criterio y sobre el mismo pasaje:
   - fue APLICADO en la ronda anterior y ahora se pide lo contrario, o
   - fue RECHAZADO con motivo y reaparece sin "Re-apertura:" con argumento nuevo.

   Los hallazgos que oscilan se sacan del bucle y se listan para la autora. Si **todos** los altos y
   medios restantes oscilan o estan ESCALADOS, **para: SOLO QUEDAN DECISIONES DE LA AUTORA**.

e. **Correccion**: lanza `redactor-tesis` en modo `corregir` con la seccion y `rNN`. Dile que
   hallazgos sacaste por oscilacion, para que no los toque. En `documento`, el redactor se lanza una
   vez **por cada seccion** con hallazgos, en serie (no en paralelo: comparten siglas y terminos).

f. **Cierre de etapa** (paso g), siempre, antes de seguir o de parar.

g. **Cierre de etapa `rNN`** — obligatorio tras cada redaccion inicial y cada correccion:
   1. Compila: `python scripts/lint_redaccion.py --compilar` (documento entero, para que las siglas
      y referencias cruzadas se evaluen en el orden real). Si la compilacion falla, la etapa **no
      se cierra**: se relanza `redactor-tesis` solo para arreglar la compilacion.
   2. Guarda una copia del PDF: `redaccion/.build/etapas/<seccion>-rNN.pdf` (crea la carpeta si
      falta). Asi la autora puede comparar etapas.
   3. Actualiza `redaccion/BITACORA.md`:
      - §3: una fila con fecha, seccion, etapa, que cambio en una linea, conteos del lint y de los
        revisores, GAP por tipo (del recuadro BORRADOR o del total del lint), paginas y ruta del PDF;
      - §1: consolida la seccion "Patrones" de los tres reportes de la ronda. Patron ya listado:
        suma 1 a Veces y agrega la seccion a "Visto en". Patron nuevo: fila VIGENTE. Patron VIGENTE
        que ningun revisor vio en esta etapa ni en la anterior, en ninguna seccion: ERRADICADO;
      - §2: las decisiones de redaccion que el redactor declaro en su respuesta.
   4. Dile a la autora, en una linea, que la etapa cerro y donde esta el PDF.

h. Si llegaste al tope, **para: TOPE DE RONDAS**, aunque queden hallazgos.

## 3. Cierre

0. La ultima etapa ya quedo compilada y registrada en el paso 2g; no se compila de nuevo.
1. Actualiza la fila de la seccion en `redaccion/MAPA.md`: Estado (`en revision`, `convergido` o
   `con decisiones pendientes`) y Ultima ronda.
2. Reporta a la autora, en este orden y sin adornos:
   - motivo de parada y numero de rondas;
   - evolucion `alta/media` por ronda y revisor, en una tabla corta;
   - GAP abiertos por tipo, con el texto de cada `\GAPDEC` (esos son suyos);
   - hallazgos escalados u oscilantes, uno por linea, con la pregunta concreta que tiene que
     responder;
   - que leer primero en el PDF (`redaccion/.build/main.pdf`; las etapas en
     `redaccion/.build/etapas/`);
   - patrones VIGENTES nuevos de la bitacora (ver §1 de `BITACORA.md`).
3. Regla 13 raiz: evalua si algo de lo redactado obliga a ajustar alcance, supuesto, baseline o abre
   un gap. Si si, registralo en `docs/04-implicancias.md` como ABIERTA. Si no, dilo: "sin
   implicancias sobre la tesis".
4. Actualiza `docs/ESTADO.md` (regla 12 raiz), en tres o cuatro lineas.

## Advertencia que hay que decirle a la autora la primera vez

"Cero hallazgos" de un revisor LLM no prueba que el texto este bien, igual que un `ok` del revisor
de laminas no prueba ausencia de error (#19, #21). Convergencia quiere decir que tres lecturas
independientes con criterios explicitos ya no encuentran nada que citar. La lectura final es suya y
del asesor (la guia exige su visto bueno).
