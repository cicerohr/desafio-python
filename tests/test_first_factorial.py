from src.coderbyte.first_factorial import first_factorial


def test_first_factorial_zero():
    assert first_factorial(0) == 1


def test_first_factorial_positivo():
    assert first_factorial(2) == 2


def test_first_factorial_negativo():
    assert first_factorial(-2) == 'Digite um número inteiro positivo!'


def test_first_factorial_strings():
    assert first_factorial('abc') == 'Digite um número inteiro positivo!'
