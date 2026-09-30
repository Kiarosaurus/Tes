#!/usr/bin/env python3
"""Concatena refs/clean/*.bib en refs.bib.

refs/raw/ es la fuente descargada del editor y no se toca nunca.
refs/clean/ es la version normalizada a mano, una entrada por archivo.
refs.bib es el producto: no se edita a mano, se regenera con este script.
overleaf/referencias.bib es una copia identica para el documento de la universidad
(Overleaf solo ve archivos dentro de su carpeta); tampoco se edita a mano.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLEAN = ROOT / "refs" / "clean"
OUT = ROOT / "refs.bib"
OUT_OVERLEAF = ROOT / "overleaf" / "referencias.bib"

HEADER = """% refs.bib — MetalSynth-Pelvis
% GENERADO. No editar a mano: se reconstruye con `python scripts/build_refs.py`.
% Fuente: refs/clean/*.bib, uno por entrada, normalizado a mano desde refs/raw/.
% refs/raw/ guarda el archivo tal como lo entrego el editor y no se modifica.
% Manda el raw: ningun campo sin respaldo en refs/raw/ sobrevive aqui, y ningun
% campo se completo con conocimiento del asistente. Procedencia: refs/MAPEO.md.
"""


def main() -> int:
    """Escribe refs.bib con las entradas de refs/clean ordenadas por clave."""
    files = sorted(CLEAN.glob("*.bib"), key=lambda p: p.stem.lower())
    if not files:
        print(f"sin entradas en {CLEAN}", file=sys.stderr)
        return 1
    parts = [HEADER]
    for path in files:
        parts.append(path.read_text(encoding="utf-8").strip() + "\n")
    texto = "\n".join(parts)
    OUT.write_text(texto, encoding="utf-8")
    print(f"{len(files)} entradas -> {OUT.relative_to(ROOT)}")
    if OUT_OVERLEAF.parent.is_dir():
        OUT_OVERLEAF.write_text(texto, encoding="utf-8")
        print(f"{len(files)} entradas -> {OUT_OVERLEAF.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
