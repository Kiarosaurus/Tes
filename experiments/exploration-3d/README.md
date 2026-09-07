# Exploración 3D

Un script, **un CSV editable** (`revision.csv`) y un resumen regenerable (`resumen.md`).
No modifica `experiments/exploration` ni los NIfTI. Cada imagen significa un volumen CT.

**Ya ejecutado al 2026-09-07:** 178 CT, sin errores; 38 candidatos HU en dataset6 y
75 en dataset7. Seis grupos duplicados, 172 contenidos únicos. El CSV está listo
para llenar: no necesitas repetir `inventario` para comenzar la revisión.

Desde la raíz del repositorio:

```powershell
python -m pip install -r experiments/exploration-3d/requirements.txt
python experiments/exploration-3d/explorar.py inventario
python experiments/exploration-3d/explorar.py ver dataset7_CLINIC_metal_0002_data
python experiments/exploration-3d/explorar.py vistas
python experiments/exploration-3d/explorar.py cortes dataset7_CLINIC_metal_0002_data
python experiments/exploration-3d/explorar.py resumen
```

`ver` genera HTML autónomos en `outputs/`: abrir el archivo sin sufijo para rotar,
acercar y ocultar superficies haciendo clic en su leyenda. No necesita conexión.
El HTML `_cortes` solo muestra tres cortes por el máximo HU, para orientación rápida.
`cortes` abre un visor local con deslizadores para recorrer **todo** el volumen y
ventanas de hueso, tejido y metal. Cerrar la ventana termina ese comando.
Los ejes de las superficies son coordenadas físicas RAS en mm. El visor de cortes
reorienta a RAS y mantiene la proporción del spacing; no es convención radiológica.

`vistas` corre `ver` sobre todos los candidatos HU de `revision.csv` y **no rehace**
las que ya existen. Diferencias con `ver` de un caso: comparte un `plotly.min.js` en
`outputs/` en vez de incrustarlo en cada archivo (sigue funcionando sin conexión) y
omite el HTML de cortes, que pesa ~8 MB por caso y ya está cubierto por las láminas
PNG. `--todos` incluye los no candidatos, `--con-cortes` recupera el HTML de cortes,
`--rehacer` regenera y `--parte 2/3` reparte el trabajo entre procesos paralelos.
Las superficies son idénticas a las de `ver`: 300, 1500, 2500 y 3500 HU.

## Cómo llenar la tabla

Las primeras ocho columnas conservan el orden y nombres de `Tabla compañera.jpeg`:
Caso, Tipo de estructura observada, Cantidad aprox., Ubicación anatómica,
Lateralidad, Artefactos, Severidad, Confianza. Una fila por volumen; si hay varios
tipos, separarlos con `;` y describir cantidades y ubicaciones en el mismo orden.
No interpretar número de componentes conectados como número de implantes.

1. Ordenar `Candidato HU` = `sí` primero; revisar también los `no`, incluidos dataset6.
2. Rotar el 3D, ocultar hueso y comparar superficies de 1500, 2500 y 3500 HU.
   Son superficies de intensidad, no máscaras diagnósticas: hueso, contraste y
   otros objetos pueden aparecer. El hueso se simplifica con paso 4; las superficies
   altas usan paso 1 para no omitir objetos pequeños por submuestreo.
3. Recorrer los tres planos con `cortes`; inspeccionar el cuerpo completo, no solo
   pelvis o el máximo HU. El 3D ayuda con geometría; los cortes con artefactos,
   límites y objetos que el umbral no muestra. Ajustar también en el visor habitual
   si las ventanas disponibles no permiten resolver un caso.
4. Llenar `Metal` y `Objeto extraño` con `sí`, `no` o `incierto`.
   `Objeto extraño` incluye implantes, DIU, clips y objetos externos, aun sin metal.
   Tipo, lateralidad o severidad desconocidos: `por determinar`; no forzarlos.
   Severidad/confianza son cualitativas, no una escala clínica validada.
5. Solo al terminar ambos modos escribir `completa` en `Revisión 3D y cortes`,
   junto con Revisor y Fecha (AAAA-MM-DD). En `Grupo paciente` usar identidad
   anonimizada verificada; no asumir que el nombre del archivo identifica al paciente.
6. `Ejemplo`: ruta local del HTML o captura elegida; `Notas`: evidencia, índices
   de cortes y dudas. Las filas metal_0002 y metal_0003 de la foto se conservan en
   `Antecedente 2D`, junto con las observaciones de los CSV anteriores y su origen,
   no como clasificación validada.
7. Guardar/cerrar CSV y ejecutar `resumen`. Excel: importar como UTF-8, separador coma.

## Filtro y trazabilidad

El filtro de trabajo es **al menos un vóxel >2500 HU**, configurable con
`inventario --hu 2000`. Es una heurística sensible de priorización, no una regla
de Peters ni evidencia de ausencia/presencia de metal. No filtra por tamaño mínimo
ni elimina objetos externos: ambos podrían importar para excluir entrenamiento.
Se usan HU escalados por NIfTI (slope/intercept), sin clipping. Debe confirmarse
que la exportación original conservó la calibración HU; el header no lo demuestra.
`Antecedente 2D` preserva notas históricas sin trasladar la decisión a las columnas nuevas.
Reejecutar inventario conserva campos manuales por Caso y recalcula datos automáticos;
se niega a sobrescribir si desaparecen casos del inventario anterior.

SHA256 se calcula sobre forma y vóxeles escalados float32 en orden nativo.
Detecta copias exactas aun con distinta compresión; no detecta reorientaciones,
recortes o estudios repetidos del mismo paciente. Todos los duplicados quedan
bloqueados hasta elegir un representante, verificar geometría y resolver su identidad.
La carpeta local solo aporta CT: una máscara ausente no se infiere a partir del paper.

## Entrenamiento y prueba

`Cohorte propuesta` se recalcula: pendientes/incertidumbre nunca ingresan a entrenamiento.
Entrenamiento candidato exige revisión completa, metal=no, objeto extraño=no,
revisor/fecha e identidad agrupable. Metal confirmado propone prueba metal;
no implica osteosíntesis pélvica ni disponibilidad de ground truth.
Duplicados y grupos de paciente repetidos requieren resolver el conjunto entero.
No hay split final automático ni porcentajes inventados: falta revisión y decidir
validación, representantes y subconjunto de osteosíntesis con el asesor.
No usar pacientes o geometrías de prueba para entrenamiento ni ajuste de parámetros.

## Qué puede hacer el asistente

Puede inventariar, priorizar, generar vistas y proponer una clasificación visual
preliminar de ejemplos. No puede certificar ausencia de objetos a partir de un
umbral o de unas capturas. La revisión completa y la confirmación anatómica deben
quedar a cargo de la autora/lector competente; las dudas se conservan como tales.
En esta ejecución se inspeccionaron dos ángulos 3D y tres cortes por el máximo HU
de los ejemplos siguientes. Se dejaron anotaciones **parciales**, no revisiones completas.

| Caso | Observación preliminar | Abrir vista |
|---|---|---|
| dataset7 metal_0002 | Varias estructuras de fijación; barra curva con elementos de anclaje y estructura alargada posterior. El antecedente «1 dominante» no es exhaustivo | [3D](outputs/dataset7_CLINIC_metal_0002_data.html) / [cortes](outputs/dataset7_CLINIC_metal_0002_data_cortes.png) |
| dataset7 metal_0003 | Estructuras compatibles con placas y múltiples tornillos en región ilíaca; estrías visibles en cortes | [3D](outputs/dataset7_CLINIC_metal_0003_data.html) / [cortes](outputs/dataset7_CLINIC_metal_0003_data_cortes.png) |
| dataset6 CLINIC_0017 | Pequeña estructura hiperdensa pélvica, compatible con antecedente de DIU; otra señal periférica requiere inspección | [3D](outputs/dataset6_CLINIC_0017_data.html) / [cortes](outputs/dataset6_CLINIC_0017_data_cortes.png) |

La anatomía exacta, recuento, lateralidad y severidad deben confirmarse recorriendo
el volumen. Las superficies no establecen composición química ni modelo del dispositivo.

Los HTML contienen geometría derivada de CT y quedan en `outputs/`, excluido de git.
El CSV y las estadísticas sí son resultados tabulares reproducibles.

## Láminas PNG y propuesta asistida

`laminas.py` genera vistas deterministas sin GUI para revisar en lote o para que el
subagente `clasificador-metal` proponga una clasificación preliminar:

```powershell
python experiments/exploration-3d/laminas.py dataset7_CLINIC_metal_0003_data
python experiments/exploration-3d/laminas.py dataset6_CLINIC_0017_data --hu 1500
```

Escribe en `outputs/laminas/<caso>/`: `proyecciones.png` (MIP en los tres ejes en
ventana de metal, más el acumulado de vóxeles sobre umbral), `ortogonales.png` (los
tres planos por el centroide del umbral, en ventana de hueso y de metal, con el umbral
superpuesto), `axiales.png` (16 axiales que cubren la extensión del umbral) y
`hallazgos.json` (por componente conexo: vóxeles, volumen mm³, HU máximo, centroide en
índices y en RAS mm, bbox en mm, rango de cortes axiales, lado geométrico por el signo
de x en RAS y si toca el borde del FOV). Los ejes de las figuras están en índices de
vóxel RAS base 0, los mismos que muestra el visor `cortes`.

16 axiales no son todo el CT y un componente conexo no es un implante: el artefacto
funde piezas vecinas y parte otras. Las láminas sirven para priorizar y para describir,
no para cerrar un caso.

El subagente `clasificador-metal` (`.claude/agents/clasificador-metal.md`) lee esas
láminas y escribe filas en `propuesta_clasificacion.csv`, con las mismas ocho columnas
de la compañera más evidencia trazable (índices de corte y componente). **No escribe en
`revision.csv`**: la autora valida y recién entonces traslada la fila. El agente tiene
prohibido marcar `completa`, proponer cohortes, afirmar ausencia de objetos y nombrar
material o modelo del dispositivo; ante duda escribe `incierto`.

El estado del encargo del asesor, sub-tarea por sub-tarea, está en
[`cumplimiento-encargo.md`](cumplimiento-encargo.md).
