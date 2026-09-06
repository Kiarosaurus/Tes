# 01 — Log de decisiones

> Solo lo escribe la autora. Formato: una entrada por decision, con fecha.
> Tres lineas bastan. Este archivo es la evidencia de que el trabajo avanzo.

---

## AAAA-MM-DD — Separacion en muestreador y renderizador

**Decision:** el pipeline se divide en dos componentes evaluados por separado.

**Alternativas descartadas:** un solo modelo end-to-end que coloque y renderice.

**Por que:** permite atribuir el error a geometria o a apariencia, y hace que el
muestreador sea defendible como contribucion independiente.

---
