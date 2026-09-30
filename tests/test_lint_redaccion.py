"""Tests del lint de redaccion: que detecte lo que ESTILO.md prohibe y no lo que permite."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("lint_redaccion", ROOT / "scripts" / "lint_redaccion.py")
lint = importlib.util.module_from_spec(_spec)
sys.modules["lint_redaccion"] = lint
_spec.loader.exec_module(lint)


def _revisar(tmp_path: Path, contenido: str, nombre: str = "capitulo1") -> list:
    """Escribe un .tex temporal dentro de ROOT y devuelve sus hallazgos."""
    ruta = ROOT / "redaccion" / ".build" / f"{nombre}.tex"
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")
    try:
        hallazgos, _ = lint.revisar_archivo(ruta, set(), {"liu2021ctpelvic1k"}, True)
    finally:
        ruta.unlink()
    return hallazgos


def _criterios(hallazgos: list) -> set[str]:
    return {h.criterio for h in hallazgos}


def test_detecta_muletilla_ia_con_y_sin_tilde(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "Cabe señalar que el método juega un papel crucial.\n")
    assert "E-IA" in _criterios(hs)


def test_detecta_primera_persona(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "Nuestro método se evaluó en la cohorte.\n")
    assert "E-INF" in _criterios(hs)


def test_texto_sobrio_pasa(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "La tomografía computarizada (TC) mide la atenuación \\cite{liu2021ctpelvic1k}.\n"
                            "La TC se reconstruye por cortes.\n")
    assert not [h for h in hs if h.severidad in ("alta", "media")]


def test_sigla_sin_definir(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "El SAP se calcula por paciente.\n")
    assert "E-T3" in _criterios(hs)


def test_cita_inexistente(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "Se reporta \\cite{clave_inventada}.\n")
    assert "G-T6" in _criterios(hs)


def test_resumen_sin_citas_ni_siglas(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "Se midió la TC \\cite{liu2021ctpelvic1k}.\n", nombre="resumen")
    assert [h.criterio for h in hs].count("P-R2") == 2


def test_oracion_larga(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, " ".join(["palabra"] * 45) + ".\n")
    assert "E-O1" in _criterios(hs)


def test_titulos_en_mayusculas_no_son_siglas(tmp_path: Path) -> None:
    hs = _revisar(tmp_path, "\\chapter{MARCO TEÓRICO}\n")
    assert "E-T3" not in _criterios(hs)
