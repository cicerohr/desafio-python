"""desafio-python/src/livro_nilo/capitulo_07_05.py | 2023-06-05.

    @author: Nilo Ney Coutinho Menezes
    @modified by: Cícero
    @link: https://python.nilo.pro.br/exercicios3/capitulo%2007/exercicio-07-05.html

Escreva um programa que leia duas strings e gere uma terceira, na qual os
caracteres da segunda foram retirados da primeira.
    1ª string: AATTGGAA
    2ª string: TG
    3ª string: AAAA
"""
from dataclasses import dataclass


@dataclass
class DiferencaConjuntos:
    """Busca elementos que estão no conjunto A e não estão em B

    Args:
        a: string de comparação a
        b: string de comparação b
    """

    a: str
    b: str

    def diferenca_conjunto(self) -> str:
        return str(set(self.a) - set(self.b))


if __name__ == '__main__':  # pragma: no cover
    primeira = input('Digite a primeira string: ')
    segunda = input('Digite a segunda string: ')

    terceira = DiferencaConjuntos(primeira, segunda)
    print(terceira)
    print(terceira.diferenca_conjunto())
