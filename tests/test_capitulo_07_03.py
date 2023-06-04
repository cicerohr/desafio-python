from src.livro_nilo.capitulo_07_03 import DiferencaSimetricaConjunto


def test_diferenca_simetrica_existe():
    ab = DiferencaSimetricaConjunto('AAACTBF', 'CBT')
    assert ab.diferenca_simetrica() == 'AF'


def test_diferenca_simetrica_nao_existe():
    ab = DiferencaSimetricaConjunto('AAACTBF', 'AAACTBF')
    assert ab.diferenca_simetrica() == ''


def test_diferenca_simetrica_tipo_diferente():
    ab = DiferencaSimetricaConjunto('AAACTBF', 321)
    assert ab.diferenca_simetrica() == "Erro: 'int' object is not iterable"


def test_diferenca_simetrica_tipo_diferente_pf():
    ab = DiferencaSimetricaConjunto('AAACTBF', 3.21)
    assert ab.diferenca_simetrica() == "Erro: 'float' object is not iterable"
