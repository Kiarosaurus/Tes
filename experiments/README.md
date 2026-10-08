# experiments/

Todo lo ejecutable que produce evidencia para la tesis. El codigo reutilizable vive en `src/`.

## Mapa

| Carpeta | Que contiene | Indice de artefactos |
|---|---|---|
| `exploration-3d/` | cohorte por paciente: `revision.csv`, `grupos.csv`, exclusiones, cribado HU, clasificacion visual | `exploration-3d/EXPERIMENTOS.md` (uso: `README.md`) |
| `objetivo1/` | representacion multi-ventana y compuerta Go/No-Go del VAE (E6a, E6c, E6b, P1) | `objetivo1/EXPERIMENTOS.md` |
| `objetivo2/` | muestreador: landmarks (R1), TotalSegmentator, corredor (E9-TS), SAP y muestreo (E12-E14) | `objetivo2/EXPERIMENTOS.md` |
| `objetivo3/` | renderizador (Diseno A): parches, entrenamiento, cadena completa, brazo fisico | `objetivo3/EXPERIMENTOS.md` (diseno: `diseno_A.md`) |
| `obsoletos/` | pruebas, pilotos y versiones superadas que **nadie importa**; no alimentan la ruta principal | `obsoletos/README.md` |
| `KHIPU.md` | manual del cluster para los tres objetivos: acceso, entorno, colas, lecciones y recetas | — |

## Convenciones

- **Un `EXPERIMENTOS.md` por carpeta**: que es cada artefacto, quien lo produjo (`script`, `Khipu`,
  `autora`, `revisor clinico`, `agente`) y su estado (VIGENTE, SUPERADO, ABIERTO, CERRADO). Los agentes de
  redaccion (`redactor-tesis`, `auditor-trazabilidad`) leen `experiments/*/EXPERIMENTOS.md`: mantener el nombre.
- **Las notas de resultado** van junto a su script con el mismo prefijo (`e13_sap.md`, `p1_compuerta.md`).
- **`outputs/` no se versiona** (pesado y regenerable). Los `.sbatch` buscan las salidas ahi.
- **Un solo `KHIPU.md`**, en esta raiz: el cluster y sus lecciones son los mismos para todos los objetivos.
  Las recetas de un job concreto pueden ir tambien en la cabecera del `.sbatch`.
- **No se borra evidencia.** Lo superado se marca en su indice; si ademas nadie lo importa ni lo lee, se
  mueve con `git mv` a `obsoletos/<carpeta>/` y se anota en `obsoletos/README.md` con su ruta anterior.
- El estado del proyecto ("por donde voy") esta en `docs/ESTADO.md`; los hallazgos que tocan el argumento,
  en `docs/04-implicancias.md`. Estos indices no los sustituyen.
