# Estadistico vs geometria de medicion (plano axial, 13 pacientes de prueba) — verificacion propia, exploratoria
Script: estadistico_vs_geometria.py. run04_mejor (semillas 0-1) y Peters Ti (cond. A), referencia exacta sin metal, hasta 8 cortes por paciente con M, anillos de 2 mm en el plano axial. No es el procedimiento exacto de A20 (ROIs en planos perpendiculares a u): solo sirve para comparar ORDENES DE MAGNITUD y tendencias.
(a) exceso D1 = amplitud(img) - amplitud(ref); (b) amplitud de Delta = amplitud(img - ref) (la definicion de A20, aqui en anillos axiales).

| anillo mm | modelo (a) exceso | modelo (b) amp Delta | Peters Ti (a) | Peters Ti (b) | tab:res-anillos (perp. a u, amp Delta): modelo / Peters Ti |
|---|---|---|---|---|---|
| 0-2 | 1672 | 2558 | 5004 | 5935 | 1828 / 3864 |
| 2-4 | 786 | 1630 | 2558 | 3110 | 1234 / 1808 |
| 4-6 | 396 | 1337 | 1931 | 2323 | 949 / 894 |
| 6-8 | 175 | 1227 | 1404 | 1743 | 946 / 613 |
| 8-10 | 107 | 1035 | 1054 | 1391 | 919 / 448 |
| 10-12 | 35 | 887 | 829 | 1204 | 727 / 338 |

Lecturas: (1) El ESTADISTICO importa mucho para el modelo: su amplitud de Delta (b) tiene un piso de ~900-1200 HU a 6-12 mm (regeneracion sin metal) que el exceso (a) casi anula (175-35 HU). Para Peters (a) y (b) difieren 15-45 %. (2) La GEOMETRIA importa: con anillos axiales, (b) da valores 1.4x (modelo) y 1.5-3.6x (Peters Ti) mayores que tab:res-anillos. (3) La lectura cualitativa del campo lejano cambia: en tab:res-anillos el modelo supera a Peters Ti desde 4 mm (949 vs 894; 946 vs 613; 919 vs 448); en anillos axiales con la misma definicion (b) queda por debajo en todos los anillos (1337 vs 2323; 1227 vs 1743; 1035 vs 1391). (4) El umbral de 'perfil plano' (razon 0-2 / 6-8 < 2): 1.92 en tab:res-anillos; con (b) axial 2558/1227 = 2.08, con (a) axial 9.6. Es decir, la conclusion 'perfil plano' depende de estadistico y geometria.
Limites: ~8 cortes por paciente y 2 semillas; muestreo de cortes distinto al de A20; no se reprodujo la tabla de la tesis; exploratorio.
