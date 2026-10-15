# Auditoria de trazabilidad — capitulo1 — r07

Archivo: `overleaf/secciones/capitulo1.tex` (134 lineas). Respuesta revisada: `capitulo1-r07-respuesta.md`; no contiene hallazgos rechazados. Se auditaron de nuevo todas las unidades verificables, con prioridad en las ocho fuentes incorporadas en esta ronda. No se abrieron PDF.

Todas las claves citadas existen en `overleaf/referencias.bib`; los apellidos nombrados coinciden con el primer autor y ninguna cita aparece sola como sujeto gramatical. No aparecen como vigentes Dice/HD95, BFC/ISC, el rango 31--60 %, difusión latente ni ControlNet. Las fuentes nuevas de Kak, Standring, Vallender, Wilcoxon, Schuirmann y Efron sostienen lo que se les atribuye en las filas de evidencia de sus fichas. La GAPLIT bilateral de Fisher está justificada, pero la ficha tampoco deja trazable la distribución hipergeométrica que la prosa ya atribuye al artículo.

**Conteo: alta=4 media=0 baja=0**

## Hallazgos

| ID | Sev | Criterio | Ubicacion | Afirmacion (max 15 palabras) | Fuente buscada | Problema | Correccion |
|---|---|---|---|---|---|---|---|
| T01 | alta | G-T4, OC-2 | `capitulo1.tex:48` | “margen de equivalencia [...] aún no medido” | `experiments/objetivo3/resultados_validacion_pose.md`:51; `EXPERIMENTOS.md`:63; `capitulo3.tex`:381, :433 | Patrón PAT-122 reincide. El margen ya se midió: 196.3 HU para el modelo principal. El GAP sigue siendo necesario para el desenlace de la regla del suelo, pero su motivo quedó falso. | Decir que el margen ya está fijado y estrechar el GAP a la comparación no registrada entre la pérdida, aún sin conversión a HU, y ese margen. |
| T02 | alta | G-T4 | `capitulo1.tex:122` | “pruebas pareadas [...] 14 valores” | `capitulo3.tex`:321, :365, :381, :463; `EXPERIMENTOS.md`:63, :81 | La cifra no coincide con el diseño vigente: hay 14 pacientes sin metal, pero uno carece de eje; el contraste usa 13. | Sustituir “14 valores” por “13 valores” y, si se conserva el 14, explicar la exclusión del caso sin eje. |
| T03 | alta | G-T4, OC-2, OC-3 | `capitulo1.tex:128` | “comparación [...] aún sin preinscribir” | `capitulo3.tex`:38, :343, :365, :381; `docs/04-implicancias.md`:8143-8146 | Patrón PAT-11/PAT-122 reincide. La comparación fue preinscrita, ejecutada como contraste primario y evaluada. #90 sigue formalmente abierta, pero ya no permite decidir entre ejecutarla o pasarla a futuro. | Declarar la comparación preinscrita y ejecutada; conservar un `\GAPDEC` solo para el cierre formal de la contingencia #90. |
| T04 | alta | E-R6, G-T4 | `capitulo1.tex:130` | “evalúa [...] mediante una distribución hipergeométrica” | `docs/literatura/fisher1935logic.md`, tabla “Evidencia textual” | La ficha respalda márgenes fijos, tablas compatibles y el conteo exacto, pero no contiene una fila textual que nombre o formule la distribución hipergeométrica. La cita no es auditable con la ficha disponible. | Relectura con `lector-papers` para añadir a la ficha la evidencia exacta de la hipergeométrica, o retirar esa atribución y describir solo lo que las filas actuales sostienen. |

## Inventario

| Ubicacion | Unidad verificable | Fuente (ruta:linea o clave + fila de evidencia) | OK |
|---|---|---|---|
| :11-13, Fig. `fig:mt-conceptos` | Función, orden y relación de conceptos con los objetivos | `capitulo3.tex`:11-38, :72, :93, :194, :279 | si |
| :31 | Coeficiente de atenuación, Beer--Lambert, integral de línea y supuesto monoenergético | `kak2001book`, evidencia “Atenuación exponencial”, “Logaritmo medido”, “Condición monoenergética” | si |
| :31 | Fuentes médicas policromáticas y endurecimiento del haz | `kak2001book`, evidencia “Fuente médica real” y “Definición de beam hardening” | si |
| :31 | Sinograma y modelo espectral de CatSim | `deman2007catsim`, Sec. 2.1 | si |
| :31 | DukeSim usa Beer--Lambert; Wang la discretiza en cinco energías | fichas `abadi2019`, `wang2019cochlear` | si |
| :33 | Dos pasos de retroproyección filtrada | `kak2001book`, evidencia “Dos pasos de FBP”, “Paso de filtrado”, “Paso de retroproyección” | si |
| :33 | De Man, CatSim y Karageorgos emplean FBP; Radon monocromático | fichas `deman1999`, `deman2007catsim`, `karageorgos2024ddpm`, `park2015ct` | si |
| :33 | Dominios de proyección e imagen; cohorte ya reconstruida; protocolo físico por proyecciones | `docs/02-datos.md`; `capitulo3.tex`:42-70, :347-365 | si |
| :35 | Fórmula HU, agua 0 y aire ideal -1000 HU | `kak2001book`, evidencia “Fórmula HU”, “Agua”, “Aire”; `wu2022xcist` | si |
| :35 | Conversión dependiente de energía en Wang | `wang2019cochlear`, Sec. 2.1 | si |
| :35 | Hueso >150 HU; metal 2500 HU; umbrales operativos | fichas `peters2025hybrid`, `wang2025adaptiveweighting`, `li2024` | si |
| :35 | Mediana 0.42 dentro de máscaras sacras y consecuencia para el corredor | `tesis/main.tex`:123; `experiments/objetivo2/maintex_cifras.md`:4, :17 | si |
| :37-42 | Ventana, saturación y canje rango/contraste | `wang2025adaptiveweighting`, Ec. 2; derivación de `eq:ventana` | si |
| :44-46 | Codificación multiventana; tres ventanas; techos 2000/20000 HU; asinh | `wang2025adaptiveweighting`; `tesis/main.tex`:77; `capitulo3.tex`:72-91 | si |
| :46 | GAP de forma y parámetros de asinh | `experiments/objetivo1/e6c_techo_lw.py`:61-69; ausencia en registros | si (GAP justificado) |
| :48 | Suelo -1000 HU, regla y margen aún no medido | `capitulo3.tex`:198, :381; `resultados_validacion_pose.md`:51 | **no (T01)** |
| :52-60 | Definición y mecanismos del artefacto: endurecimiento, dispersión, ruido, inanición y borde | fichas `selles2024marreview`, `deman1999`, `park2015ct` | si |
| :56 | Razón dispersa/primaria 0.0001 y condición de simulación 2D | `deman1999`, evidencia Sec. III-C | si |
| :62 | Volumen parcial axial, una o varias discontinuidades y alcance idealizado | `glover1980nonlinear`; `deman1999` | si |
| :64 | Rayas fuera del implante, banda propia y supuesto de síntesis en imagen | `deman1999`, `park2015ct`; `capitulo3.tex`:194-228 | si |
| :66 | CatSim/XCIST y mecanismos simulados; comparación física | fichas `wu2022xcist`, `deman2007catsim`; `capitulo3.tex`:347-365 | si |
| :68 | Tres métricas de Peters y su lectura para síntesis | `peters2025hybrid`; `capitulo3.tex`:315-343 | si |
| :72 | Tile B/C, vía percutánea y referencia clínica externa | `zwingmann2009navigated` | si |
| :74 | Tres corticales y dirección caudal | fichas `smith2006iliosacral`, `routt1997` | si |
| :74 | Hueso compacto sacro, ala, forámenes, platillos y articulación SI | `standring2020grays`, filas homónimas de evidencia | si |
| :76 | Superficie glútea, articulaciones SI y cortical lateral | `standring2020grays`, evidencia “Superficie externa del ilion”; `mclaren2021corridor`; decisión #130 | si |
| :76-84 | Umbral 10 mm, holgura, corredor, zona segura y marco anatómico | fichas `mclaren2021corridor`, `kaiser2014dysmorphism`, `routt1997`, `gardner2010safezones` | si |
| :82 | TotalSegmentator y medición sobre máscaras | `wasserthal2023`; `capitulo3.tex`:97-113 | si |
| :84 | Techo de S1 frente al platillo, diferencia no medida | `capitulo3.tex`:437; implicancia #138 | si |
| :86-90 | Posición ideal y grados 0-3; anchuras 2/4 mm; convención equiespaciada | `smith2006iliosacral`; `capitulo3.tex`:287-303 | si |
| :88 | Zwingmann usa escala de perforación; Hinsche, definición binaria | fichas `zwingmann2009navigated`, `hinsche2002fluoroscopy` | si |
| :92 | SAP sin densidad; ala con menor gris; trabajo futuro | `arand2019pelvicring`; `capitulo3.tex`:190 | si |
| :96-108 | Proceso de difusión, 1000 pasos, ecuación directa, calendario, pérdida y U-Net | fichas `ho2020denoising`, `dorjsembe2024`, `zhang2025diffboost`, `nichol2021improved`, `rombach2022latentdiffusion`, `ronnenberger2015unet` | si |
| :110 | DDIM determinista, 10-50 veces y dominio de imágenes naturales | `song2021ddim`; fichas `ho2020denoising`, `nichol2021improved` | si |
| :112-118 | Condicionamiento, ControlNet descartado, difusión latente, inpainting y 2.5D | fichas `rombach2022latentdiffusion`, `dorjsembe2024`, `zhang2023controlnet`, `lugmayr2022repaint`, `zhang2025lefusion`; `capitulo3.tex`:194-204 | si |
| :122 | Tipos de resultados y unidades de análisis | `capitulo3.tex`:72-91, :298-343 | parcial |
| :122 | Contraste del Obj. 3 sobre 14 pacientes | `capitulo3.tex`:321, :365, :381, :463; `EXPERIMENTOS.md`:81 | **no (T02)** |
| :124 | Fórmula 1D de Wasserstein-1 | `vallender1974wasserstein`, evidencia “Caso unidimensional”, “Wasserstein-1 en la recta”, “F y G son CDF” | si |
| :124 | Reducción discreta, unidad grado y máximos 1/3 | derivación de la fórmula de Vallender sobre soporte `{0,1,2,3}`; `capitulo3.tex`:298-303 | si |
| :126 | TOST, dos nulas, IC 90 % con alpha=0.05 y margen externo | `schuirmann1987comparison`, evidencia “Rechazar ambas nulas”, “IC equivalente”, “90 %” | si |
| :128 | Algoritmo de rangos con signo | `wilcoxon1945rankingmethods`, evidencia “Orden por magnitud”, “Restitución del signo”, “Menor suma” | si |
| :128 | Estado de preinscripción y contingencia de la equivalencia | `capitulo3.tex`:38, :343, :365, :381; implicancia #90 | **no (T03)** |
| :130 | Bootstrap: mismo tamaño, reemplazo, recalcular estadístico y percentiles | `efron1992bootstrap`, evidencia “Tamaño de réplica”, “Con reemplazo”, “Método percentil” | si |
| :130 | Paciente como unidad del bootstrap del Obj. 1 | `capitulo3.tex`:72-91; `efron1992bootstrap`, ejemplo por sujetos | si |
| :130 | Fisher: márgenes fijos y tablas compatibles | `fisher1935logic`, evidencia “Márgenes”, “Márgenes fijos”, “13 tablas posibles” | si |
| :130 | Fisher mediante distribución hipergeométrica | ficha `fisher1935logic`, sin fila textual correspondiente | **no (T04)** |
| :130 | GAP de convención bilateral | `fisher1935logic`, evidencia “Prueba bilateral 2x2 explícita: NO ENCONTRADO” | si (GAP justificado) |
| :132 | Cronología, multiplicidad de seis/siete y veredicto negativo | `capitulo3.tex`:72-91, :409-463; implicancias #91, #93 | si |
| :134 | MAE, RMSE y desigualdad RMSE >= MAE | `capitulo3.tex`:79-83; derivación algebraica | si |
| global | Claves nuevas y autores: Kak, Standring, Vallender, Wilcoxon, Schuirmann, Efron, Fisher | `overleaf/referencias.bib`:229, :264, :556, :1002, :1083, :1179, :1282 | si |
| global | Contenido retirado | `docs/00-tesis.md`; búsqueda en el `.tex` | si (ausente o explícitamente descartado) |

## Patrones

| Patron (una linea, generalizable a otras secciones) | Criterio | Ejemplo antes (max 15 palabras) | Ya en bitacora (PAT-n o "nuevo") |
|---|---|---|---|
| Un GAP de resultado propio conserva el estado anterior después de medirse o ejecutarse | G-T4, OC-2 | “margen de equivalencia [...] aún no medido” | PAT-122 |
| Una cifra de cohorte conserva el total elegible y no el n final analizado | G-T4 | “pruebas pareadas [...] 14 valores” | PAT-31 / PAT-155 |
| Una ficha resume un método, pero su tabla no incluye la evidencia textual atribuida | E-R6, G-T4 | “mediante una distribución hipergeométrica” | nuevo |
