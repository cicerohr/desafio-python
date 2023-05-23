from src.livro_nilo.capitulo_07_01 import BuscaString


def test_letra_maiuscula_e_encontra():
    buscar = BuscaString('Palavra', 'P')
    assert buscar.procurar() == 0


def test_letra_minuscula_n_encontra():
    buscar = BuscaString('Palavra', 'p')
    assert buscar.procurar() == -1


def test_sequencia_caracteres():
    buscar = BuscaString('Palavra', 'vra')
    assert buscar.procurar() == 4


def test_sequencia_caracteres_n_existe():
    buscar = BuscaString('Palavra', 'vrx')
    assert buscar.procurar() == -1


def test_type_errado_alvo():
    buscar = BuscaString(0, 'vra')
    assert buscar.procurar() is None


def test_type_errado_busca():
    buscar = BuscaString('Palavra', 0)
    assert buscar.procurar() is None


def test_type_errado_ambos():
    buscar = BuscaString(0, 0)
    assert buscar.procurar() is None
