from src.livro_nilo.capitulo_07_02 import InterseccaoConjunto


def test_interseccao_existe():
    ab = InterseccaoConjunto('AAACTBF', 'CBT')
    assert ab.interseccao() == 'BCT'


def test_interseccao_nao_existe():
    ab = InterseccaoConjunto('AAACTBF', 'cbt')
    assert ab.interseccao() == ''


def test_interseccao_tipo_diferente():
    ab = InterseccaoConjunto('AAACTBF', 321)
    assert ab.interseccao() == "Erro: 'int' object is not iterable"


def test_interseccao_tipo_diferente_pf():
    ab = InterseccaoConjunto('AAACTBF', 3.21)
    assert ab.interseccao() == "Erro: 'float' object is not iterable"
