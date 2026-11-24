# C2 — D3 a ciegas / prueba de Turing (protocolo declarado ANTES de generar o mirar imágenes)
Fecha: 2026-11-20. Estatus: **exploratorio / post-hoc**. No sustituye a E-A2 (−301.0 HU, p_TOST 0.845). No se usa para elegir modelo ni para reescribir hipótesis.

## Qué mide
Cuánto confunde cada brazo a la autora frente a artefacto real: % de paneles juzgados "real" por brazo, con IC de Wilson 95 %. Descriptivo; N pequeño → no hay prueba de hipótesis.

## Brazos y datos (todo local, solo lectura)
| Brazo | Fuente | Nota |
|---|---|---|
| run04_mejor | `outputs/obj3_pose/delta/run04_mejor` semilla s0 | |
| run05a | `.../delta/run05a_mejor` s0 | |
| run05b | `.../delta/run05b_mejor` s0 | |
| Peters Ti | `outputs/obj3_pose/peters_val/a19_*.npz`, `Ti_A` | recon XCIST; misma pose y `M` |
| Real | `data/dataset7/..._metal_0039_data.nii.gz`, 2 tornillos aislados (>2500 HU, conectividad 6, ≥500 mm³) | **otro paciente/anatomía**; única referencia real validada (a17) |
Pacientes sintéticos: `0101`, `0102` (**validación**, no prueba). Limitación: run05a/b no tienen volúmenes de los 13 de prueba en local (solo CSV); eso queda INC hasta ver Khipu.

## Selección de cortes (regla fija)
Cortes axiales con `M`>0 que también estén en `ks` de Peters; 3 por paciente en las posiciones 1/6, 3/6, 5/6 de la lista ordenada. Real: 3 cortes por tornillo en 1/6, 3/6, 5/6 de su extensión axial. Total: 2×3×4 = 24 sintéticos/Peters + 6 reales = 30 paneles.

## Presentación
Recorte 160×160 px centrado en el centroide de `M` (o del componente real) en ese corte, **misma ventana fija [-500, 1300] HU**, sin etiquetas, sin escala de color, orden aleatorio, ids opacos. Clave en `c2/clave_NO_ABRIR.csv` (no abrir hasta puntuar). Respuesta: real/sintético + confianza 1–5.

## Sesgos conocidos (se reportan, no se corrigen)
- Real = otra anatomía y escáner: puede delatarse por contexto, no por el artefacto.
- Peters/real pueden diferir en recorte de rango (clip de CT real); la ventana de 1300 HU lo atenúa.
- Tú conoces los modelos y sus defectos (rayas débiles): el cegamiento es imperfecto. Hacerlo en una sola sesión, sin consultar `clave`.
- Pacientes 0101/0102 intervinieron en calibración (delta, a21): no son datos limpios para confirmar nada.
- Seeds fija s0: no mide variabilidad entre semillas.
## Qué NO se concluirá
Nada confirmatorio; nada sobre "equivalencia" con Peters. Resultado se informa completo (todos los brazos, también los desfavorables).
