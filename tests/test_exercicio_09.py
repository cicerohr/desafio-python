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
from src.desafio_python.exercicio_09 import DivisivelPorCinco


def test_divisivel_por_cinco():
    entrada = ['00010100', '1010', '0001']
    assert DivisivelPorCinco(entrada).__str__() == '10100,1010'
