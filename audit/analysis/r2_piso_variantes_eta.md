# R-2 (C): piso de ruido (G sin M, --sin-metal) de las variantes de eta. Khipu job 65097 (A100), val 0101/0102, 5 semillas, run04_mejor.
Comparador: khipu/comparar_perfiles.py (perfil por anillo de 1 mm, media sobre 2 casos x 5 semillas). Exploratorio: n = 2 pacientes.

p95 medio por anillo (HU), sin metal: 50:0 ~475-541; 50:0.3 ~522-585; 100:0.3 ~533-608 (el p95 incluye anatomia, no solo ruido).
Diferencia frente a 50:0 (p05 / p50 / p95), anillos de 1 mm:
- 50:0.3: p95 +16 a +61 HU (maximo +60.6 a 4-5 mm; +47 a 0-1 mm); p05 -23 a 0; p50 ~0 a +7.
- 100:0.3: p95 +23 a +75 HU (maximo +74.6 a 3-4 mm); p05 -27 a -5; p50 ~0.
SD entre semillas del p95 por anillo (media): 38.8 (50:0), 52.5 (50:0.3), 53.0 (100:0.3) -> +35 %.
Lectura: sin ningun metal, eta > 0 ensancha las colas en todos los anillos (p95 sube 30-75 HU entre 1 y 10 mm; p05 baja) y aumenta la variabilidad entre semillas. Parte de cualquier subida de p95 de 100:0.3 con metal puede ser varianza inyectada por eta y no artefacto (apoya C-02/E-07). NO se comparo con la magnitud de la mejora de p95 reportada en la tesis (no extraida); n = 2; ring p95 absoluto incluye anatomia.
