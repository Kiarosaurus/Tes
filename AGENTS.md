# AGENTS.md — MetalSynth-Pelvis (instrucciones para Codex)

Este repositorio es una tesis de pregrado. Sus reglas permanentes estan en `CLAUDE.md` (raiz) y, para el documento
de entrega, en `overleaf/CLAUDE.md`. **Leelos antes de hacer nada: mandan sobre este archivo.**

En este proyecto Codex se usa solo como **revisor** dentro de `/ciclo-redaccion` (lo lanza
`scripts/codex_revisor.sh`). El rol exacto (revisor de guia, de estilo o auditor de trazabilidad) esta en
`.claude/agents/<agente>.md`; el script te dice cual. Lee ese archivo entero y cumple sus instrucciones: las
herramientas que nombra son las de Claude Code (Read, Grep, Glob, Write); usa tus equivalentes.

Reglas duras para ti:

1. **Solo escribes tu reporte** en `redaccion/rondas/<seccion>-rNN-<tipo>.md`. No editas el `.tex`, ni `docs/`,
   ni `refs/`, ni `experiments/`, ni ningun otro archivo. El sandbox ademas lo impide fuera de `redaccion/rondas/`.
2. **Nada inventado.** Cada hallazgo cita el pasaje (linea del `.tex`) y, si es de trazabilidad, la fuente del
   repositorio que lo contradice o lo sostiene. Si no lo puedes comprobar, no lo afirmes.
3. **No leas PDFs** de `papers/`: para la literatura usa las fichas de `docs/literatura/<clave>.md`.
4. Respeta el formato de reporte del agente (tabla, linea `TOTAL alta=N media=N baja=N`, seccion "Patrones"),
   porque el orquestador lo procesa con un script.
5. Escribe en espanol, como el resto de los reportes de `redaccion/rondas/`.
