# R1 — auditoria visual del nivel de S1 (2026-09-10)

**Procedencia: `agente-laminas` (Claude, sesion del 2026-09-10). NO es validacion de la
autora.** Mosaicos en `outputs/r1_mosaico/mosaico_evaluacion_0[1-4].png`
(`r1_mosaico.py`). Por teja: la cruz roja (S1 sagital) esta en el platillo superior de S1,
un nivel arriba, en otro sitio, o no se puede decidir. Tabla por volumen en
`r1_auditoria_s1_agente.csv`.

Auditados primero los 69 volumenes de la cohorte por volumen (antes de #45); luego se anadio
la union `metal_0059u0071` (`ok`). **Recuento por paciente (65, `grupo 1` de
`grupos.csv`), que es el vigente:** ok 53, un nivel arriba 4, grosero 2, ambiguo 2, no
hallado 4. La tabla de abajo es la de los 69 volumenes.

| Juicio | n | Casos |
|---|---|---|
| ok | 55 | resto |
| un nivel arriba (L5) | 5 | `0010`, `0011`, `0014`, `0034`, `0067` |
| error grosero | 3 | `0015` (teja sin cuerpo vertebral), `0058` (arco posterior), `0068` (dos niveles) |
| ambiguo | 2 | `0003`, `0038` |
| no hallado | 4 | `0016`, `0022`, `0023`, `0053` |

- Los 8 errores salen con `S1_estado = limpio`: el punto equivocado cae lejos del metal, asi
  que **el error de nivel sesga la cifra de contaminacion hacia "limpio"**.
- En los 5 "un nivel arriba" y en `0068`, el metodo del ala da un z **menor** (discrepancia
  de -18 a -51 mm) y en las tejas parece caer en el sacro. En `0005` y `0059` el ala da un z
  mayor y el sagital acierta. Regla candidata: **ante discrepancia > 10 mm, tomar el z
  menor**. Esta derivada **de los mismos casos que se auditaron** (circular): es hipotesis,
  no correccion, y falla por construccion en una lumbarizacion de S1.
- Sospecha lateral: `metal_0065` y `metal_0066` se ven anatomicamente identicos en la teja
  (mismo tornillo, misma forma) con distinto spacing (0.835 vs 0.770 mm), cortes (332 vs
  344) y HU maximo. Posibles dos reconstrucciones del mismo estudio; el hash por corte de
  #45 no puede verlo. **No verificado.**

## Revision clinica (2026-09-11)

`r1_auditoria_s1_clinico.csv` lo lleno un **medico cirujano otorrinolaringologo** (revisor
clinico externo), a ciegas de esta auditoria. Es la **referencia** vigente: ok 53, +1 6,
otro 2, no hallado 4. Acuerdo con este documento: 92.3% exacto, kappa 0.80 (ok / no-ok).
Detalle en `r1_landmarks.md` y en #26 de `docs/04-implicancias.md`.

**Correccion de transcripcion (2026-09-14, informada por la autora):** `metal_0012` es `+1`, no `ok`;
`metal_0015` es `?` (el revisor dudo, "tirando a otro"). Referencia vigente: ok 51, +1 7, otro 2,
no hallado 4, ? 1. Acuerdo con este documento: 90.8% exacto; ok/no-ok 93.8%, kappa 0.81. Marco
computable con S1 correcto: 48 de 65; ademas sin contaminacion: 29 (#51 cerrada).
