# F6 figura 1 (pipeline TikZ)

Aplicado:
- overleaf/main.tex: `\usepackage{tikz}` y `\usetikzlibrary{arrows.meta,positioning}` tras el comentario de paquetes adicionales. Nada más.
- overleaf/secciones/capitulo3.tex, sección "Visión general": el entorno figure con \fbox y flechas se reemplazó por el contenido de pipeline_tikz.tex (etiqueta fig:pipeline, texto de cajas y pie sin cambios). Nada más.
- Ajuste permitido: solo los text width (caja 0.50 a 0.64 \linewidth; lado 0.28 a 0.24). Con 0.50 había partes de palabra feas ("Total-Segmentator", "alrede-dor") y la compuerta quedaba estrecha.

Compilación (python3 scripts/lint_redaccion.py --compilar; `python` no existe en el entorno):
- main.log: sin errores "!", sin "undefined", sin Overfull. Sin Underfull en la figura (los Underfull que hay son preexistentes y de otras líneas).
- El lint global marca FALLA por 1 alta preexistente (anexos.tex:5, relleno de plantilla), ajena a la figura.
- Páginas del PDF: 205 antes, 205 después. La figura está en la pág. PDF 72 (impresa 63), igual que antes.

PNG: /tmp/fig_pipeline-072.png

Lo que se ve: seis cajas apiladas con flechas rectas entre ellas, centradas en la columna. Las dos cajas clave (Muestreador, Sintetizador) tienen borde grueso y fondo gris. A la derecha, caja punteada de la compuerta (Objetivo 1) con flecha punteada que sube de su base y entra por el lado derecho del Sintetizador. Pie debajo; la figura cabe en la página y queda cerca del párrafo que la cita.

Problemas menores: persisten cortes de palabra en "distribu-ciones", "ne-gativo" e "in-painting"/"do-minio" por los \\ forzados dentro de cajas de ancho fijo. Es cosmético; no se tocó texto. Si se quiere eliminarlo habría que reflujar los saltos de línea (cambia el texto de las cajas, fuera del encargo). En la caja de $G = M \cup B_\delta$ el espacio alrededor del "=" se ve algo ancho; viene del contenido original.
