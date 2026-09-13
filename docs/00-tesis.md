# 00 — Definicion de la tesis

> Este archivo lo escribe la autora. Es la fuente de verdad del alcance.

## Titulo actual

MetalSynth-Pelvis: Conditioned synthesis of osteosynthesis implants and local metal
artifacts in pelvic CT scan volumes using Multi-Window Latent Diffusion.

## Pregunta de investigacion

<pegar del main.tex>

## Hipotesis

<pegar del main.tex>

## Alcance MINIMO VIABLE (lo que garantizo defender)

- Objetivo 1: validacion de la representacion multi-ventana (Go/No-Go, MAE < 25 HU en hueso)
- Objetivo 2: muestreador de colocacion quirurgicamente restringido, expresado en el
  marco de referencia de `kaiser2014dysmorphism` (reformateo por el eje sacro perpendicular
  al platillo superior de S1; angulo coronal contra la linea de crestas iliacas; angulo
  axial contra la linea de espinas iliacas posteriores; holgura cortical de 5 mm), con
  viabilidad de corredor segun `mclaren2021corridor` expresada como
  `Dmax >= d_implante + 2c` (#31, decision del 2026-09-11): `d_implante` del tornillo
  parametrico (6.5-8.0 mm) y holgura radial `c` de 1-2 mm por lado, derivada de Kaiser
- Metrica SAP + comparacion contra las DOS distribuciones ordinales de cuatro grados de
  `zwingmann2009navigated`, condicionadas por tecnica quirurgica **solo en S1**.
  S1/S2 se conserva como variable geometrica del muestreador; S2 se evalua
  descriptivamente (geometria y grados de brecha), sin prior ordinal clinico disponible.

Defendible por si solo como: "un muestreador de colocacion de implantes
quirurgicamente admisible, validado contra la distribucion clinica real de malposiciones".

## Alcance COMPLETO (si el tiempo alcanza)

- Objetivo 3: renderizador (LDM 2.5D + ControlNet + banda B_delta), demostrativo
- Objetivo 4: SAP como unica metrica propia, mas las metricas del protocolo adoptado
  (`peters2025hybrid`) con SUS nombres publicados
- Ablaciones por restriccion

## Fuera de alcance (explicito)

> Actualizado el 2026-09-08 por decision de la autora, aplicado tambien a `tesis/main.tex`.

1. **Evaluacion downstream de segmentacion (Dice, HD95). FUERA.** No por falta de tiempo:
   por dos condiciones auditables. Solo una minoria de los volumenes con metal tiene
   anotacion osea verificada (implicancia #13), y solo una parte de la coleccion publicada
   esta en disco (implicancia #18). Un resultado downstream se apoyaria en una cohorte
   demasiado pequena y demasiado parcialmente anotada. Se declara trabajo futuro.
2. **Metricas BFC e ISC como contribucion propia. RETIRADAS.** La apariencia se evalua
   con las metricas del protocolo adoptado bajo sus nombres publicados (bone integrity,
   metal integrity, streak amplitude). Renombrar medidas heredadas vaciaba el Objetivo 4.
   Cierra las implicancias #14 y #16. **SAP queda como unica metrica introducida por
   esta tesis.**
3. **Reimplementacion validada de XCIST como brazo de comparacion. FUERA.** Sustituida
   por la adopcion del protocolo de `peters2025hybrid` (implicancia #8, ya aplicada).
4. **Reclamo de novedad sobre la codificacion multi-ventana en si. RETIRADO.** El marco
   multi-ventana es de trabajo previo de MAR y `wang2025adaptiveweighting` lo atribuye a
   su vez a trabajo anterior (implicancia #24). La novedad reclamada es su uso **para
   sintesis** junto con B_delta.
5. **Rango unico de malposicion (31-60% o 2-15%). RETIRADO.** Ninguno resiste: el primero
   es derivacion propia sobre dos poblaciones distintas y el segundo es cita de tercera
   mano (implicancias #12 y #25). Se usan las distribuciones ordinales medidas.
6. **Zona segura sacroiliaca como geometria heredada. NO SE RECLAMA.** El marco de
   referencia se hereda de `kaiser2014dysmorphism` y el procedimiento de corredor de
   `mclaren2021corridor`. Lo que se reclama como propio es **la distribucion de poses**
   dentro de ese marco (implicancia #7).
7. **El umbral de 10 mm como estandar clinico validado. NO SE PRESENTA ASI.** Se usa como
   convencion de holgura geometrica, con la justificacion dimensional de Kaiser (1-2 mm
   alrededor de un tornillo de 6.3-8 mm). La cadena de citas tiene tres saltos
   (implicancia #25).
8. **Estratificacion por fenotipo sacro. FUERA POR COMPLETO** (2026-09-08). Ni los tres
   fenotipos, ni el score de dismorfismo, ni el corte `>70`. El efecto del fenotipo sobre
   el tamano de la zona segura **no es consistente entre estudios** (Carlson 2000, recogido
   en `gardner2010safezones`, no halla diferencia), y Kaiser y Gardner clasifican
   dismorfismo con criterios distintos. El muestreador **mide la geometria del corredor
   directamente sobre cada volumen**. Cierra la implicancia #27.
9. **Subir mas por la cadena de citas del umbral de 10 mm. FUERA.** Cuatro eslabones
   auditados, ninguno lo mide: es una convencion profesional derivada del calibre del
   tornillo, y las fuentes que la enuncian lo dicen en su texto (implicancia #25).

## Riesgos asumidos (2026-09-08)

> Se declaran aqui porque condicionan el Objetivo 2. Los dos estan en
> `04-implicancias.md` y en `01-decisiones.md`.

- **R1 — Los landmarks del marco de referencia pueden no sobrevivir al artefacto.**
  `kaiser2014dysmorphism` caracterizo su marco sobre pelvis **no lesionadas** y excluyo los
  CT con implantes que oscurecen la union lumbosacra, que es justo donde estan los tres
  landmarks y donde pega el streaking. **Se cierra midiendo en casa**, no leyendo:
  cuantificar en cuantos volumenes locales con metal se pueden ubicar los tres landmarks.
  **MEDIDO el 2026-09-11 y escrito en `main.tex`:** de 65 pacientes con material
  ortopedico, marco computable con S1 confirmado por revisor clinico en 49 y sin
  contaminacion en 30. La perdida la explican mas el FOV (7) y la localizacion que el
  artefacto. El tratamiento de los 7 con FOV cortado sigue sin decidir. Implicancia #26.
- **R2 — RESUELTO el 2026-09-08 por la via corta: no se avanza.** Se adopta de Kaiser solo
  lo operacional (marco de referencia, definiciones angulares, margen de 5 mm). El score,
  el `>70` y los fenotipos quedan fuera, asi que ya no hay nada que decidir. Las tres
  lecturas que iban a informar esta decision se hicieron: ninguna aporta un umbral medido
  y `gardner2010safezones` trajo ademas la objecion de Carlson 2000 a estratificar por
  fenotipo. Ver el punto 8 de `Fuera de alcance`.

## Pendiente de ejecucion (decidido, falta correrlo)

- ~~Tabla de sensibilidad del cribado (#22)~~ **HECHA** el 2026-09-09 (E1).
- ~~Cifra de R1 (#26)~~ **HECHA** el 2026-09-11 y escrita en `main.tex` (49 de 65 con
  marco computable y S1 confirmado por revisor clinico; 30 sin contaminacion).
- **Medicion del corredor por volumen (E9, #31).** Bloqueada por segmentacion: un umbral
  HU no representa el hueso esponjoso del sacro (implicancia #48).

## Pendiente de decision de la autora

- ~~Reparto del umbral en dos reglas (#22)~~ **DECIDIDO el 2026-09-11**: 2500 HU solo para
  cribado; metal integrity con la regla adaptativa por ROI de `peters2025hybrid`. Queda
  **propuesta** (no decidida) una tercera regla para extraer mascaras de implantes reales:
  umbral de semimaximo local (E8, #46).
- **`templeman1996proximity` sigue en `refs.bib` sin PDF.** Su prioridad bajo: su papel en
  la cadena del 2-15% ya no es decisivo.

## Eje S1/S2 y limite del benchmark (2026-09-08; implicancias #12 y #28)

`gardner2010safezones` aporta el respaldo **anatomico** del eje S1/S2: areas medias
minimas iliosacras de 346/109.3 mm2 en normales y 222/220.1 mm2 en dismorficos
(S1/S2; Results, p. 624 y Tabla 1, p. 627; evidencia textual en su ficha).
Las ultimas son aproximadamente iguales, no una inversion de las medias ni prueba
de igual seguridad clinica. Se evalua cada nivel midiendo su corredor en cada volumen,
sin imponer una jerarquia universal de amplitud ni reintroducir fenotipos o score.
Gardner mide el lado no lesionado y trayectorias centrales ideales: no aporta
frecuencias clinicas de grados de brecha ni calibra SAP en S2.

`vandenbosch2002` ya fue leido con `lector-papers`. Los 6/31 frente a 1/49
son **pacientes con quejas neurologicas por configuracion de tornillos**, no tornillos
malposicionados por nivel. Aporta respaldo clinico asociativo para distinguir S1/S2,
con sesgo temporal y de aprendizaje declarado. Su evaluacion de posicion es binaria
y no permite construir los cuatro grados de SAP en S2.

Se conserva el benchmark ordinal por tecnica de Zwingmann **en S1**; no se extrapola
a S2 ni se convierte lesion neurologica en brecha cortical. S2 conserva evaluacion
geometrica y descriptiva. #28 queda resuelta; #12 se cierra por delimitar el benchmark
al soporte disponible, no porque van den Bosch aporte el prior ordinal faltante.

## Fechas

| Hito | Fecha objetivo |
|---|---|
|  |  |
