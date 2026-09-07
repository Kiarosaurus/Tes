# zhang2026pediclescrew — STADW-M: CT sintetico desde CBCT para planificacion de tornillo pedicular

**Profundidad: solo abstract.** Ficha generada el 2026-09-06 a partir del abstract
aportado por la autora en chat. No se leyo el cuerpo. Ninguna cifra esta verificada
contra el texto completo, y por la regla dura de accesibilidad de `_index.md` ninguna
cifra de esta fuente puede citarse en la tesis mientras siga en ABSTRACT.

- **DOI / URL:** NO ENCONTRADO EN EL PDF (no hay PDF; el abstract no lo trae)
- **Nivel de lectura:** 1 (PROPUESTO por Claude, pendiente de confirmacion de la
  autora). Razon de proponer nivel 1: es el trabajo mas cercano al mio que ha
  aparecido hasta ahora, y ademas usa una escala de brecha cortical.
- **Leido a fondo por la autora:** no
- **PDF:** NO DISPONIBLE. La autora lo esta consiguiendo.

## Que hace (3 lineas maximo)

Propone STADW-M, un modelo de difusion que genera CT sintetico (sCT) a partir de CBCT
intraoperatorio, para mejorar la planificacion de tornillos pediculares. Combina un
modulo de difusion adaptativo consciente de artefactos, un modulo de consistencia
estructural con doble guia, y una estrategia de "CBCT Warm-Start". Valida con metricas
de imagen y con planificacion automatica de tornillos sobre los sCT generados.

## Restriccion o supuesto clave

Es **traduccion de dominio con datos pareados**: CBCT de entrada, CT de referencia.
El modelo mejora la calidad de una adquisicion que ya contiene la anatomia y el
artefacto reales. No inserta estructuras que no existen en la entrada.

Frase que lo delata:

> "generate high-quality synthetic CT (sCT) images from CBCT data"

Y sobre el tratamiento del artefacto:

> "an Artifact-Aware Adaptive Diffusion Module to mitigate localized artifact
> distributions"

**Mitigate**, no generate. Igual que `wang2025adaptiveweighting`: el artefacto es lo
que se quita, no lo que se fabrica. Ver implicancia #2 en `docs/04-implicancias.md`.

## Que toco de aqui

- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

Matices, porque las dos marcas necesitan explicacion:

- **"numero que cito"** queda marcado en *intencion*, no en acto. El abstract trae la
  escala de brecha cortical (Grade A, erosion menor a 2 mm) que roza directamente mi
  metrica BFC. Es exactamente el tipo de cifra que querria citar. Pero no puedo:
  fuente en ABSTRACT. Marcado para no perderlo de vista cuando llegue el PDF.
- **No es baseline mio.** Traduce CBCT a CT; yo inserto implantes en CT. Tareas
  distintas, entradas distintas. Compararme contra el seria comparar peras con
  manzanas.

## Numeros que cito de este paper

| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| (ninguna) | — | — |

Tabla vacia a proposito: fuente en ABSTRACT.

Cifras que aparecen en el abstract y que **NO se pueden citar todavia**, anotadas solo
para saber que buscar cuando llegue el PDF:
RMSE 890.1 a 152.9 HU; MAE 859.7 a 102.6 HU; PSNR 13.6 a 27.9 dB; 100% Grade A;
94.7% sin brecha cortical; 5.3% con erosion menor a 2 mm.
Ninguna verificada. Ninguna va a la tesis en este estado.

## Donde entra en mi tesis

Tres frentes, en orden de importancia:

1. **Related Work, y posiblemente mi reclamo de novedad.** Titulo y encuadre
   ("Diffusion-Based Synthetic CT" + planificacion de tornillos) colisionan de frente
   con como presento mi trabajo, aunque la tarea tecnica sea otra. Ver implicancia #3.
2. **Definicion de mi metrica BFC.** Usa una graduacion de brecha cortical con umbral
   explicito de 2 mm. Mi BFC se apoya hoy en `smith2006iliosacral`. Ver implicancia #4.
3. **Metodo del renderizador.** El "Warm-Start" y las perdidas compuestas para
   fidelidad textural podrian ser utiles para mi renderizador. Nivel 2 como mucho, y
   solo cuando tenga el texto completo.

## Dudas para el asesor

- Este paper y el mio comparten titular ("difusion" + "CT sintetico" + "tornillos")
  pero no tarea: el traduce CBCT a CT, yo inserto implantes que no estan en la imagen
  de entrada. Basta con explicitar esa diferencia en Related Work, o el parecido
  superficial es suficiente para que un revisor me pida comparacion cuantitativa?
- El abstract dice "100% Grade A" sin nombrar la escala. Si resulta ser una escala
  estandar de tornillo pedicular, aplica a tornillo iliosacral en pelvis, o son
  escalas distintas y no debo mezclarlas con `smith2006iliosacral`?
- Su 5.3% de brecha menor conversa con el 31-60% de malposicion de
  `zwingmann2009navigated`? Sospecho que no son comparables (planificacion sobre
  imagen sintetica vs colocacion real, columna vs pelvis), pero quiero confirmarlo
  antes de que alguien me lo pregunte en la sustentacion.
