# AUDIT_STATE
Fase actual: F0.5 completada. Esperando aprobacion de F1.
Prioridad (autora): primero secciones estables, intro->cap3 sin relacion con T/P/A. Despues sec:v2, apendices de realismo/metricas, amenazas, cap4 sec:res-obj3 (PROVISIONAL, esperan experimentos activos).
Alcance (autora, 2026-11-24): se promete prueba de Turing visual (aun no escrita en 01-decisiones.md); se investiga con experimentos post-hoc. Revisores E y F evaluan diseno prospectivo.
Requisito nuevo: maximizar diagramas/graficos/SVG para digestibilidad. Hoy: 2 \begin{figure} en cap1-4, 0 includegraphics/tikz.
Herramientas: tools/inventario_tex.py -> state/inventory.{json,md} (50 unidades).
Modelos efectivos: orquestador Sonnet 5.5; Codex gpt-6-luna medium (config); sin subagentes lanzados aun.

## Actualizacion 2026-11-24 (F4)
Informes A-G completos y versionados en rama audit/auditoria-independiente. Consolidacion: CONSOLIDACION.md, PRIORITIZED_ACTION_PLAN.md, FINDINGS.json (extraccion mecanica, estado REPORTADO). Verificados por el orquestador: C-01, C-03, C-02 (formula), F-H1, C-04; G descartado en sus "sin origen". Khipu: R-11 completo; R-2 (65097), R-9 (65092), R-4 (65098) en curso/cola.
Modelos efectivos: Codex gpt-6-luna (high: A,D,F; medium: G); Claude Sonnet 5.5 (B, F1, extraccion JSON); Claude Opus high (C, E).

## Fase 6 (autorizada por la autora 2026-11-24)
Lote 1 — capitulo4.tex: recorte de prosa que recita tablas (B2-029, 030, 034, 035 aplicados; B2-026, 031, 032 parciales; sin tocar tablas ni marcas). texcount cuerpo 5004 -> 4709 (-295, -5.9 %). Compilacion: sin referencias indefinidas; PDF 207 pag. (sin cambio medible en paginas). Lint: 0 hallazgos en capitulo4; el unico "alta" es anexos.tex:5 (relleno de plantilla, ajeno a este lote). Cifras: ninguna perdida (+0.283/+1.683 estan en tabla como 0.283/1.683). Pendiente de la autora: cap4:136 dice que los analisis de asimetria "acercan la diferencia a cero" pero uno (-329.3 HU) queda mas lejos que -301.0 HU.
Lote 2 — capitulo4.tex: B2-027 (detalle de inspeccion de MAISI) y B2-028 (discusion sin recitar cifras de tablas); texcount cuerpo 4709 -> 4676 (-33); acumulado -328 (-6.6 %). Compila sin referencias indefinidas; PDF 207 -> 206 pag. Ninguna cifra perdida. Voz impersonal estricta aplicada en lo editado. Regla de voz agregada a .claude/agents/redactor-tesis.md (pedido de la autora).
Pendiente de la autora: (1) destino del texto quitado de MAISI (nombre del paquete monai.bundle y el guion scripts/sample.py quedaron sin lugar en el documento; ver reports/F6_lote2_cap4_redactor.md (d)); (2) oraciones con sujeto personal fuera de lo editado: cap4:76 ("la calcula este trabajo"), 260 ("La autora juzgo..."), 264 ("Por decision de la autora...").
