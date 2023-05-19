"""
Metodologias de teste.

(GWT Test)
- Given -> dado
- When -> quando
- Then -> então

(AAA Test)
- Arrange -> arranjar
- Act -> agir
- Assert -> afirmar
"""
from src.desafio_python.exercicio_02 import fatorial


def test_quando_igual_zero():
    assert fatorial(0) == 1


def test_quando_igual_um():
    assert fatorial(1) == 1


def test_quando_igual_tres():
    assert fatorial(3) == 6
