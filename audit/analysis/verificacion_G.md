# Verificacion del orquestador sobre el informe G (informe original intacto: reports/G_reproducibility_codex.md)
Metodo: grep de cada cifra marcada "SIN ORIGEN EN EL MATERIAL" en review/results/ (el mismo snapshot que vio G).

| G | Cifra | Veredicto de G | Verificacion |
|---|---|---|---|
| G-009 | 61.72 HU, IC [55.12, 68.99], 34/34 | sin origen tabular | FALSO NEGATIVO: results/objetivo1/p1_compuerta.md:25 (y :38) |
| G-010 | subgrupos 53.72 / 46.99 / 76.03; sensibilidades 60.95 / 61.08 | sin origen | FALSO NEGATIVO: p1_compuerta.md:114-116; p1_sin_0072.md:20 (60.95 y 61.08 con IC [54.23, 68.57]); p1_sin_0053.md |
| G-014 | -301.0 HU, IC90 [-477.0, -124.9], Delta 196.3, n=13 | sin origen | FALSO NEGATIVO: results/objetivo3/resultados_prueba_v1.md:14 (tabla) y :36; ademas a24_contrastes.md/json/por_paciente.csv en outputs/obj3_pose/a24 (repo original) |
| G-015/016 | v2 -258.9/-264.3; +478.0/+411.7; -98.9 | sin origen | NO VERIFICADO aun: buscar en resultados_prueba_v2 / a24 de variantes |
| G-018/019 | p=0.000122; razones 1.92/6.71/4.08; CV 0.076/0.241 | parcial | NO VERIFICADO aun |
| G-024/025 | checkpoints y pesos no reproducibles | NO REPRODUCIBLE | Artefacto del snapshot: .pt y volumenes excluidos por diseno (viven en Khipu). No es hallazgo sobre la tesis; si pide archivar commit/hash de pesos (recomendacion valida) |
| G-002/003/022 | 178/179/168/166/159 y 64/66/69 | DIFIERE | VALIDO como hallazgo editorial (coincide con B): falta una tabla de flujo de cohortes con fecha de corte |
Conclusion: G (Codex, medium) cerro varias cifras como "sin origen" por busqueda superficial; la mayoria existen en results/. No usar G como lista de cifras sin respaldo sin esta verificacion. Valido: confusion de conteos de cohorte; no verificado: G-015/016/018/019.
