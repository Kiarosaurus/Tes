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
- Objetivo 2: muestreador de colocacion quirurgicamente restringido
- Metrica SAP + comparacion de distribuciones contra la tasa clinica real

Defendible por si solo como: "un muestreador de colocacion de implantes
quirurgicamente admisible, validado contra la distribucion clinica real de malposiciones".

## Alcance COMPLETO (si el tiempo alcanza)

- Objetivo 3: renderizador (LDM 2.5D + ControlNet + banda B_delta)
- Objetivo 4: metricas BFC e ISC
- Objetivo 5: evaluacion downstream (Dice, HD95) + ablaciones
- Reimplementacion validada de XCIST como brazo de comparacion

## Fuera de alcance (explicito)

<que decides NO hacer, para poder decirlo en la sustentacion>

## Fechas

| Hito | Fecha objetivo |
|---|---|
|  |  |
