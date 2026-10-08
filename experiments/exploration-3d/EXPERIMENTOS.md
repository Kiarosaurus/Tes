# Indice de artefactos de la exploracion 3D

> **Para que existe.** Procedencia de artefactos, con el formato de `experiments/objetivo2/EXPERIMENTOS.md`.
> Como se usa cada script (comandos, columnas, limitaciones): `README.md`. Data card: `docs/02-datos.md`.
>
> **Esta carpeta es la base de los tres objetivos:** define la cohorte por paciente (`revision.csv`,
> `grupos.csv`, `exclusiones.csv`). No es exploracion descartable. La exploracion 2D que la precedio esta
> archivada en `experiments/obsoletos/exploration-2d/`.

## 1. Tabla de revision y cohorte

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `explorar.py` (`inventario`, `ver`, `vistas`, `cortes`, `resumen`) | inventario, superficies 3D, visor de cortes | script | **VIGENTE** |
| `revision.csv` | una fila por volumen, 178 filas; columnas de `Tabla compañera.jpeg` | autora + script | **VIGENTE — tabla maestra.** Solo se toca con scripts que verifican y respaldan |
| `Tabla compañera.jpeg` | plantilla de columnas de `revision.csv` | autora | **VIGENTE** (antes en `experiments/`) |
| `procedencia.py`, `correcciones_autora.py`, `grupo_paciente.py` | procedencia por campo (#37), correcciones confirmadas, grupo paciente (#20, #45) | script | **VIGENTES** |
| `revision.csv.bak`, `revision.pre-correcciones.csv`, `revision.pre-paciente.csv`, `revision.previo-merge.csv` | respaldos automaticos de esos scripts | script | **RESPALDOS.** No mover: los scripts los crean "una sola vez" en esta carpeta |
| `grupos.py` / `grupos.csv` | grupo por objetivo (1 con material = 65, 2 = 37, 3 limpio = 66) | script | **VIGENTE** |
| `exclusiones.py` / `exclusiones.csv` | 11 volumenes fuera de uso (ninguno borrado) | script | **VIGENTE** |
| `duplicados_parciales.py` / `.csv` | volumenes con cortes compartidos (#20) | script | **VIGENTE** |
| `union_0059_0071.py` / `.md` | union sin perdida de `metal_0059` + `metal_0071` (#45) | script | **VIGENTE** |
| `resumen.md` | resumen regenerable de la cohorte | script | **VIGENTE** |

## 2. Cribado HU

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `sensibilidad_hu.py` / `.csv` / `.md` / `.log` | sensibilidad del cribado a 1500 / 2500 / 3500 HU (#22) | script | **VIGENTE**: 2500 HU, 0 falsos negativos |
| `candidatos.txt` | 113 candidatos HU | script | **VIGENTE** |

## 3. Clasificacion visual asistida (agente `clasificador-metal`)

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `laminas.py` | laminas PNG deterministas por caso (`outputs/laminas/`) | script | **VIGENTE** |
| `propuesta_clasificacion.csv` | propuesta consolidada, 113 filas | agente | **PROPUESTA**: no sustituye a `revision.csv` |
| `propuesta_lote-01` ... `-12.csv` | lotes de la propuesta anterior | agente | **VIGENTES** como procedencia |
| `propuesta_lote-tipo-ref.csv` | tipo de implante de `metal_0011/0039/0056` (#154) | agente | **ABIERTO**: validacion de la autora |
| `propuesta_lote-tornillos-{A,B,C,D}.csv`, `tornillos_candidatos.md` | censo visual de tornillos IS/TS en 65 pacientes (#154, #155) | agente | **ABIERTO**: propuesta sin validar |

## 4. Auditoria

| Artefacto | Que es | Origen | Estado |
|---|---|---|---|
| `cumplimiento-encargo.md` | auditoria del encargo del asesor sobre esta carpeta (2026-09-07) | asistente | **HISTORICO**, citado en `docs/05-asesor.md` |
| `inventario.log`, `laminas.log`, `laminas.err`, `sensibilidad_hu.log` | registros de corrida | script | registros |
