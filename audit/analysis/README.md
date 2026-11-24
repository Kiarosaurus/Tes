# Analisis CPU de la auditoria (solo lectura sobre resultados existentes; no se modifico codigo ni resultados del repo)
Entorno: ~/.venvs/audit (numpy, pandas, scipy, nibabel). Cada script escribe su CSV aqui.

| Script | Origen | Resultado |
|---|---|---|
| r5_eta2_semillas.py -> r5_eta2_semillas.csv | C R-5 | SD entre semillas de eta2_exc por celda (paciente x corte x K): run04_mejor_test 0.08-0.09 (rango medio 0.20-0.21); run04_60k_test 0.047-0.049 (rango 0.12). Cualquier diferencia entre brazos de eta2 < ~0.1 queda dentro del ruido de semilla en una celda. Falta el SD de la media por paciente (n=13) para decidir umbrales. |
| h5_particiones.py, h5_obj3.py | F H5 | Segun grupos.csv: 0 grupos de paciente en mas de una particion (p1_particion, n=166); train/val/test de run04 (39/3/13) sin casos ni grupos comunes. LIMITE: solo prueba la consistencia del agrupamiento ya registrado; no detecta pacientes sin metal duplicados que grupos.csv no vincule (cap3:600). |
| r8_gradiente_axial.py -> r8_gradiente_axial.csv | C R-8 | Media |dI/dz| en G: sintetico/original = 4.06 (min 2.75, max 6.73; 13 casos x 5 semillas). NO INTERPRETABLE como discontinuidad axial: el sintetico contiene el metal M (HU>2500) y sus rayas, el original es pelvis sin metal. Hace falta excluir M y comparar con Peters o con el real. |
| (no ejecutado) R-11 | C R-11 | Necesita mascaras TotalSegmentator de la cohorte (ts_total, solo en Khipu); en local solo hay 2 pilotos. CPU en Khipu. |
