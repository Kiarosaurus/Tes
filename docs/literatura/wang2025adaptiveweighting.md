# wang2025adaptiveweighting — AdaW: pesado adaptativo para MAR multi-ventana

**Profundidad: solo abstract.** Ficha generada el 2026-09-06 a partir del abstract
aportado por la autora en chat. No se leyo el cuerpo del articulo. Ninguna cifra del
cuerpo esta verificada, y por la regla dura de accesibilidad de `_index.md` no se
puede citar ninguna cifra de esta fuente en la tesis mientras siga en ABSTRACT.

- **DOI / URL:** NO ENCONTRADO EN EL PDF (no hay PDF; el abstract no lo trae)
- **Codigo:** https://github.com/hongwang01/AdaW — segun el abstract, "We will
  release the code at". No verificado que exista ni que este publicado.
- **Nivel de lectura:** 1 (profunda)
- **Leido a fondo por la autora:** no
- **PDF:** NO DISPONIBLE. Pendiente de conseguir.

## Que hace (3 lineas maximo)

Propone AdaW, un algoritmo de pesado adaptativo para reduccion de artefactos
metalicos (MAR) entrenada bajo multiples ventanas HU a la vez. Formula el problema
multi-ventana como optimizacion bi-nivel y aprende el peso de cada ventana con un
esquema learning-to-learn, en vez de pesarlas por igual. Es agnostico al backbone:
se enchufa sobre distintas redes de MAR.

## Restriccion o supuesto clave

Es un metodo de **remocion** de artefactos, no de sintesis. Todo el aparato asume que
existe una imagen limpia de referencia a la cual reconstruir, y optimiza contra ella.
Nada en el abstract sugiere que el metodo pueda generar el artefacto.

Frase que sostiene la motivacion multi-ventana:

> "The methods trained on a fixed single window would lead to insufficient removal
> of metal artifacts when being transferred to deal with other windows."

Y sobre el estado del arte multi-ventana:

> "few works have proposed to reconstruct the CT images under multiple-window
> configurations"

Ambas del abstract. No verificadas contra el cuerpo.

## Que toco de aqui

- [ ] metodo que reimplemento
- [ ] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

Justificacion de por que solo contexto: mi C3 usa codificacion multi-ventana en HU
como **entrada de condicionamiento de un renderizador generativo**. AdaW usa
multi-ventana como **objetivo de supervision de una red de remocion**. Comparten la
premisa (una sola ventana HU pierde informacion diagnostica relevante) pero no el
uso. No es baseline mio: no sintetiza nada.

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| (ninguna) | — | — |

No se llena esta tabla: fuente en ABSTRACT. El abstract menciona "five datasets with
different body sites", pero por la regla dura de accesibilidad esa cifra no puede ir
a la tesis hasta tener el texto completo.

## Donde entra en mi tesis

Related Work y justificacion de C3 (codificacion multi-ventana en HU). Sirve como
respaldo **cualitativo** de que fijar una sola ventana HU degrada el desempeno al
transferir a otras ventanas. Nada mas que eso mientras siga en ABSTRACT.

## Dudas para el asesor

- AdaW pesa ventanas para *remover* artefactos. Yo codifico ventanas para
  *generarlos*. Vale citarlo como motivacion de C3, o el asesor lo va a leer como
  que estoy forzando una analogia entre tareas distintas?
- El abstract dice que hay pocos trabajos multi-ventana, y todos en remocion.
  Refuerza que multi-ventana para sintesis de artefacto metalico es terreno libre?
