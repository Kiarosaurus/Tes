# Revision guia CS — trabajosFuturos — r01

## Hallazgos
| ID | Sev | Criterio | Ubicacion | Problema | Correccion propuesta |
|---|---|---|---|---|---|
| guia-1 | media | G-T2 | trabajosFuturos.tex:29 | Patron PAT-3 reincide: «formulacion residual» aparece por primera y unica vez como variante de un sintetizador futuro, pero no se define que residuo modelaria. El lector no puede distinguirla de las otras dos variantes enumeradas. | Precisar en una frase, con respaldo del repositorio, cual seria la entrada, la referencia y el residuo predicho; si ese contenido no esta documentado, retirar esta variante y conservar solo las direcciones que si pueden explicarse. |

TOTAL alta=0 media=1 baja=0

## Cobertura
| Criterio | Estado |
|---|---|
| G-T1 | cumple: cada direccion identifica el resultado o la limitacion que la abre, la medicion pendiente y su alcance; las remisiones permiten recuperar el diseno previo |
| G-T2 | no cumple (guia-1): «formulacion residual» se introduce sin definicion |
| G-T3 | cumple: conserva los significados de $M$, $G$ y de las metricas ya fijadas en el documento |
| G-T4 | cumple: las afirmaciones cuantitativas remiten a resultados, discusion o secciones metodologicas; la comprobacion material de cada cifra corresponde al auditor de trazabilidad |
| G-T5 | cumple: sigue a las conclusiones, ordena las direcciones por objetivo y cierra con la aplicacion que motiva la introduccion |
| G-T6 | cumple: `guo2025maisi` y `liu2021ctpelvic1k` estan en `refs.bib` |
| G-D1 | cumple: en el bloque conjunto, `conclusiones.tex:12-24` responde el objetivo general, los cuatro objetivos especificos y la pregunta; esta seccion conserva esa misma organizacion |
| G-D2 | cumple: la sintesis de propuesta, ejecucion y demostracion esta en `conclusiones.tex:8`; esta seccion separa de ella las acciones posteriores y no las presenta como resultados |
| G-D3 | cumple: distingue de forma explicita lo no ejecutado o no medido en este trabajo de la accion futura formulada en condicional |
| G-D4 | cumple: las direcciones nacen de resultados o limitaciones identificables y `trabajosFuturos.tex:37-39` vuelve a la motivacion de segmentacion de `introduccion.tex:58-60` |
| P-CO1 | cumple: no atribuye al trabajo conclusiones de otros autores; las fuentes externas solo delimitan referencias o datos disponibles |
| P-CO2 | cumple: `conclusiones.tex:12-32` evalua logros y limites por objetivo, y esta seccion deriva de ellos las direcciones posteriores |

## Propuestas de criterio

Ninguna.

## Patrones
| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Termino tecnico usado antes de su definicion formal | G-T2 | «con una formulacion residual» | PAT-3 |
