# EVIDENCE_MANIFEST (F0.5, 2026-11-24)
Snapshot: git HEAD 9bee18d4b58ce6306752d4000fd14e9b61e345f3 (rama exp/textura-percep-adv) + working tree sucio (ver state/dirty_count.txt; SHA-256 de .tex en state/tex_sha256.txt).
Copia, no symlinks: review/ es inmutable y no cambia si la autora sigue trabajando.

## Incluido (review/)
| Ruta | Contenido | Motivo |
|---|---|---|
| thesis/ | main.tex, secciones/, encabezados/, .cls, .bst, referencias.bib | objeto de auditoria |
| code/ | src/, tests/, lint_redaccion.py | implementacion para G (reproducibilidad) |
| results/ | .py .sbatch .sh .csv .json .md .log .txt de experiments/ (<2 MB, sin png) | configuraciones y resultados originales, incl. negativos |
| docs/ | RUBRICA.md, 02-datos.md, 03-glosario.md, Guia CS (pdf) | requisitos oficiales, dataset, definiciones |
| refs/ | refs.bib | bibliografia |

## Excluido
CLAUDE.md, AGENTS.md, overleaf/CLAUDE.md, .claude/ (agentes/skills con decisiones previas); docs/00, 01, 04, 05, ESTADO, SITUACION_ACTUAL, literatura/ (interpretaciones e historia); redaccion/ salvo RUBRICA (rondas, BITACORA, MAPA, ESTILO); experiments/*/EXPERIMENTOS.md, KHIPU.md, README.md (justificaciones); experiments/obsoletos/ (archivado; vuelve en ronda 2 si hace falta); data/, papers/, repos/, tar.gz (pesados / sin PHI innecesaria); tesis/main.tex (boceto historico); PNG de experiments (laminas de pacientes, 1 415 archivos).
## Fugas conocidas (menores, se aceptan)
- thesis/main.tex l.41: comentario cita overleaf/CLAUDE.md. - results/objetivo3/c4_resultado.md y objetivo2/ts_cohorte.md citan docs/01-decisiones.md o CLAUDE.md por nombre; docs/RUBRICA.md cita ESTILO.md. Ninguna transmite conclusiones.
## Pendiente
Ronda 2 (verificacion): agregar 01-decisiones, EXPERIMENTOS.md, obsoletos. Sin PHI: no se copiaron imagenes ni NIfTI.

## Correccion del snapshot (2026-11-24)
Agregado: results/obsoletos_citados/objetivo1/p1_maisi{.py,.sbatch,_cota.csv} (evidencia de la cifra 42.24 HU citada en la tesis; verificada: media de 'hueso mae' en 34 casos = 42.24).
Agregado: results/objetivo3/c2b_respuestas_2026-11-21.csv (48 puntajes del criterio visual (c)). La clave ID->brazo, c2b_ciego.py y c2b_puntuar.py NO se encontraron (ni en repo, ni en D:, ni en Downloads/pesados, ni en ramas git); probablemente en Khipu.
