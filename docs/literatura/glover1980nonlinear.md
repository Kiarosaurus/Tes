# glover1980nonlinear — Artefactos no lineales de volumen parcial en CT

- **DOI / URL:** https://doi.org/10.1118/1.594678 (`refs/raw/glover1980nonlinear.nbib`)
- **Nivel de lectura:** 2 (metodo)
- **Leido a fondo por la autora:** no
- **PDF:** papers/glover1980nonlinear.pdf (12 paginas; articulo escaneado en pp. 238-248)

## Que hace (3 lineas maximo)

Deriva como la integracion del flujo y su logaritmo vuelven no lineal la medicion cuando la atenuacion varia axialmente dentro del haz. Simula errores locales y streaks entre estructuras, prueba dos correcciones con cortes vecinos y las contrasta con CT craneal clinica.

## Restriccion o supuesto clave

El analisis idealiza una fuente monocromatica puntual, ignora scatter, divergencia axial y variaciones transversales rapidas, y simula la geometria de un GE CT/T 8800 de 1980 (Sec. II.A, p. 242 / PDF p. 6). Estudia huesos petrosos, no metal: implante, aleacion, pelvis, tornillo y mascara `M` son **NO ENCONTRADO EN EL PDF**. El propio trabajo indica que el acoplamiento entre volumen parcial y beam hardening “is not known in detail” (Sec. IV, p. 247 / PDF p. 11), de modo que no separa mecanismos en un artefacto metalico moderno.

No es sintesis generativa y no define un soporte espacial finito. `B_delta`, 12 mm, difusion, U-Net y condicionamiento por mascara: **NO ENCONTRADO EN EL PDF**.

## Que toco de aqui
- [ ] metodo que reimplemento
- [x] numero que cito
- [ ] baseline de comparacion
- [x] solo contexto

## Numeros que cito de este paper
| Cifra | Frase original (corta) | Seccion / pagina |
|---|---|---|
| Reduccion clinica de espesor: 5 a 1.5 mm | “slice thickness has been reduced from 5 to 1.5 mm” | Sec. I, p. 239 / PDF p. 3 |
| Simulacion: 576 vistas en 360 grados | “using 576 views in 360°” | Sec. II.A, p. 242 / PDF p. 6 |
| Reconstruccion simulada: pixeles de 0.8 mm, matriz 320 x 320 | “0.8 mm pixels on a 320 x 320 matrix” | Sec. II.A, p. 242 / PDF p. 6 |
| Dos discontinuidades: error de proyeccion 4 veces mayor que una | “error in the projection measurement is 4 times larger” | Sec. II.A, p. 242 / PDF p. 6 |
| Correccion discreta: umbral de similitud de 200 HU | “a threshold of 200 HU was used” | Sec. III, p. 244 / PDF p. 8 |

## Donde entra en mi tesis

Es fundamento fisico para que el artefacto no sea una textura exclusiva de `M`. Una sola discontinuidad produce principalmente error local, mientras dos o mas pueden generar streaks de largo alcance que conectan estructuras (Sec. II, pp. 240-243). Esto apoya la direccion de generar fuera del implante, pero no calibra `B_delta`: distancia radial, decaimiento en mm y ancho de 12 mm son **NO ENCONTRADO EN EL PDF**. De hecho, los streaks conectores muestran que una banda local trunca por diseno un efecto potencialmente no local.

La dependencia axial es especialmente relevante para el modelo 2.5D de tres cortes: aporta contexto entre cortes, pero no reproduce la integracion continua dentro del espesor del detector ni convierte el modelo en un simulador fisico. Para E-A1 y E-A2, streak amplitude puede detectar la apariencia resultante, pero no atribuirla a volumen parcial frente a beam hardening, scatter o photon starvation. Para E-A3, RMSE/SSIM iguales a cero fuera de `G` deben reportarse solo como garantia de composicion; no como exito fisico, porque el paper describe streaks de largo alcance. Para E-A4 conviene inspeccionar continuidad entre cortes y streaks que conectan estructuras, no solo el borde de `B_delta`.

Las correcciones propuestas funcionan cuando la geometria simulada coincide con el modelo, pero fallan en casos clinicos por informacion axial insuficiente (Secs. III-IV, pp. 246-247). Esto refuerza que tres cortes no bastan para reclamar causalidad fisica, aunque puedan bastar empiricamente para realismo local.

## Dudas para el asesor

- ¿Citarlo para declarar que E-A3 verifica preservacion por construccion y no fidelidad del campo completo de artefacto?
- ¿Anadir a E-A4 una lamina o perfil entre cortes que pueda revelar discontinuidades axiales del resultado 2.5D?
