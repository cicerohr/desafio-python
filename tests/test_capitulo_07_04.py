from src.livro_nilo.capitulo_07_04 import ContadorLetras


def test_entrada_correta():
    entrada = ContadorLetras('abbccc')
    assert entrada.contador_caracteres() == {'a': 1, 'b': 2, 'c': 3}


def test_entrada_incorreta():
    entrada = ContadorLetras(123)
    assert (
        entrada.contador_caracteres() == 'Erro: somente strings são '
        'válidas.'
    )
