# v3 — borrador de plan (NO preinscrito, NO aprobado, nada lanzado). Fecha 2026-11-20
Estatus: propuesta de la sesión de investigación. Se vuelve preinscripción solo cuando la autora fije los `[POR FIJAR]` y lo copie a `experiments/objetivo3/` / `01-decisiones.md`.
Todo resultado = **post-hoc/exploratorio** (la prueba ya se vio con v1 y v2). v1 y v2 se reportan completas; v3 va al lado.

## Por qué v3 no repite v2
- v2 (run05a/b) cambió **dónde pesa la pérdida** (sobremuestreo de tornillos, peso 3 en 2–10 mm) → no mejoró.
- A28 (EVID): decodificar solo con LW mueve el p95 +3…+53 HU; 6/7 cáscaras siguen bajo la envolvente real → el defecto es del **modelo/muestreo**, no de la lectura.
- Código (EVID, `src/renderizador/difusion.py`): pérdida = MSE del objetivo v en espacio codificado [-1,1] de 3 canales a igual peso; muestreo = DDIM determinista `eta=0` con `x0` recortado a [-1,1] en cada paso. (EST, no probado) Ambos favorecen salidas "promediadas": rayas débiles y poca varianza entre pacientes (#188).

## Hipótesis (a verificar, no afirmadas)
H1 (muestreo): `eta>0` y/o más pasos recuperan amplitud de rayas sin reentrenar.
H2 (objetivo): una pérdida que penalice el error **en HU decodificados** (o ponderada por |HU|) recupera el p95 de 4–12 mm.

## Etapa 0 — solo inferencia, validación 0101/0102 (sin entrenar)
- Mismo `mejor.pt` de run04, delta 0.03. Variantes `[POR FIJAR]`: pasos ∈ {50, 100, 200}; eta ∈ {0, 0.3, 0.6}.
- **Requiere un parche:** `a15_cadena_completa.py` expone `--pasos` pero no `--eta` (`muestrea_ddim` ya lo tiene). Edición del repo → solo con orden explícita de la autora.
- Métrica y regla (copiadas de A28/a17, fijadas antes): nº de cáscaras de 1 mm con p95 dentro de la envolvente real (`metal_0039`), de 7 críticas. Éxito Etapa 0: ≥ 4/7 (umbral de A28). Salvaguarda de v1: no empeorar 0–2 mm (desv. ≤ tope 279.6 HU).
- Coste (EST): 2 pacientes × 5 semillas × ≤9 variantes; GPU corta (decenas de min por variante). Cabe en un job con `--time` ≤ 6 h.
- Decisión: si ≥1 variante pasa → se evalúa sobre los 13 de prueba **una sola vez** y no se entrena. Si ninguna → Etapa 1.

## Etapa 1 — entrenamiento v3 (solo si Etapa 0 falla)
- Cambio único: pérdida en espacio HU decodificado (o MSE de objetivo + término sobre `x0` predicho decodificado) `[POR FIJAR forma y peso]`. Mismos datos, manifiesto, semilla, lote, lr, 60 000 pasos que run04 (para atribuir el efecto).
- Coste (EST, INC): run04 ≈ 8 h en A6000; A100 entera estimada hoy 12:40→20:40 con 480 min asumidos. + cadena `a15` ≈ 3.5 h/shard (pedir ≥5 h) + `a20` 15–25 min.
- Corte duro: dom 22/11 12:00. Si el entrenamiento no termina antes del sáb 22:00, se aborta y se reporta como no concluido.

## Qué cambia en la tesis según el resultado
| Resultado | Texto |
|---|---|
| Etapa 0 pasa | "exploratorio: el muestreo `eta=…` recupera el p95" + limitación de post-hoc |
| Etapa 1 mejora | v3 junto a v1/v2, exploratorio, sin sustituir E-A2 |
| Nada mejora | limitación + trabajo futuro (#201); 3 intervenciones documentadas |

## Pendiente de la autora (fijar antes de correr)
1. Aprobar Etapa 0 y el parche `--eta`. 2. Fijar variantes y umbral. 3. Decidir si Etapa 1 existe. 4. Aprobar cada `sbatch` por job. 5. `git pull` (fast-forward) en Khipu.
