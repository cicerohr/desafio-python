"""desafio-python/src/livro_nilo/capitulo_07_03.py | 2023-06-03.

    @author: Nilo Ney Coutinho Menezes
    @modified by: Cícero
    @link: https://python.nilo.pro.br/exercicios3/capitulo%2007/exercicio-07-03.html

Escreva um programa que leia duas strings e gere uma terceira apenas com os
caracteres que aparecem em uma delas.

    1ª string: CTA
    2ª string: ABC
    3ª string: BT

A ordem dos caracteres da terceira string não é importante.
"""
from dataclasses import dataclass


@dataclass
class DiferencaSimetricaConjunto:
    """Retorna os caracteres que não são comuns entre as strings.

    Tip:
        A diferença simétrica é a união tirando a interseção entre dois
        conjuntos.

    Args:
        a: string a
        b: string b

    Examples:
        >>> ab = DiferencaSimetricaConjunto('CTA', 'ABC')
        >>> ab.diferenca_simetrica()
        'BT'
        >>> ab = DiferencaSimetricaConjunto('CTA', 'CTA')
        >>> ab.diferenca_simetrica()
        ''
        >>> ab = DiferencaSimetricaConjunto(123, 'CBT')
        >>> ab.diferenca_simetrica()
        "Erro: 'int' object is not iterable"
        >>> ab = DiferencaSimetricaConjunto('AAACTBF', 3.21)
        >>> ab.diferenca_simetrica()
        "Erro: 'float' object is not iterable"
    """

    a: str
    b: str

    def diferenca_simetrica(self) -> str:
        """Diferenca simétrica entre a e b (A Δ B).

        Returns:
            diferenca simétrica entre as strings a e b (a Δ b).
        """

        try:
            ab = set(self.a) ^ set(self.b)
        except Exception as e:
            return f'Erro: {e}'

        c = ''
        for item in sorted(ab):
            c += item
        return c


if __name__ == '__main__':  # pragma: no cover
    primeira = input('Digite a primeira string: ')
    segunda = input('Digite a segunda string: ')
    conjunto = DiferencaSimetricaConjunto(primeira, segunda)
    print(conjunto.diferenca_simetrica())
    print(conjunto)
