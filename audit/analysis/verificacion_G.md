# Verificacion del orquestador sobre el informe G (informe original intacto: reports/G_reproducibility_codex.md)
Metodo: grep de cada cifra marcada "SIN ORIGEN EN EL MATERIAL" en review/results/ (el mismo snapshot que vio G).

| G | Cifra | Veredicto de G | Verificacion |
|---|---|---|---|
| G-009 | 61.72 HU, IC [55.12, 68.99], 34/34 | sin origen tabular | FALSO NEGATIVO: results/objetivo1/p1_compuerta.md:25 (y :38) |
| G-010 | subgrupos 53.72 / 46.99 / 76.03; sensibilidades 60.95 / 61.08 | sin origen | FALSO NEGATIVO: p1_compuerta.md:114-116; p1_sin_0072.md:20 (60.95 y 61.08 con IC [54.23, 68.57]); p1_sin_0053.md |
| G-014 | -301.0 HU, IC90 [-477.0, -124.9], Delta 196.3, n=13 | sin origen | FALSO NEGATIVO: results/objetivo3/resultados_prueba_v1.md:14 (tabla) y :36; ademas a24_contrastes.md/json/por_paciente.csv en outputs/obj3_pose/a24 (repo original) |
| G-015/016 | v2 -258.9/-264.3; +478.0/+411.7; -98.9 | sin origen | FALSO NEGATIVO: objetivo3/resultados_dec_2026-10-15.md (todas), a26_log/v2_base/a26_lecturas.md, d1/d1_por_paciente.csv |
| G-018/019 | p=0.000122; razones 1.92/6.71/4.08; CV 0.076/0.241 | parcial | FALSO NEGATIVO: p en resultados_prueba_v1.md y a24_contrastes.md; razones y CV en resultados_dec_2026-10-15.md y a20_pareado_r02_04.csv |
| G-024/025 | checkpoints y pesos no reproducibles | NO REPRODUCIBLE | Artefacto del snapshot: .pt y volumenes excluidos por diseno (viven en Khipu). No es hallazgo sobre la tesis; si pide archivar commit/hash de pesos (recomendacion valida) |
| G-002/003/022 | 178/179/168/166/159 y 64/66/69 | DIFIERE | VALIDO como hallazgo editorial (coincide con B): falta una tabla de flujo de cohortes con fecha de corte |
Conclusion: G (Codex, medium) cerro varias cifras como "sin origen" por busqueda superficial; la mayoria existen en results/. No usar G como lista de cifras sin respaldo sin esta verificacion. Todas las cifras de resultados que G marco sin origen (G-009, 010, 014-019) existen en results/. Valido solo: confusion de conteos de cohorte (G-002/003/022) y archivar hashes/comandos (G-024/025).
