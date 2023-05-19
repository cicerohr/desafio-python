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
from src.desafio_python.exercicio_01 import divisiveis_por_7


def test_quando_divisivel_7_nao_multiplo_5():
    assert divisiveis_por_7(7, 42) == [7, 14, 21, 28, 42]
