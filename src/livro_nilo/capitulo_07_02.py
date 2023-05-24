"""desafio-python/src/livro_nilo/capitulo_07_02.py | 2023-05-23.

Gere uma string com os caracteres em comum de duas outras strings

    @author: Nilo Ney Coutinho Menezes
    @modified by: Cícero
    @link: https://python.nilo.pro.br/exercicios3/capitulo%2007/exercicio-07-02.html

Escreva um programa que leia duas strings e gere uma terceira com os caracteres
comuns às duas strings lidas.

    1ª string: AAACTBF
    2ª string: CBT
    Resultado: CBT

A ordem dos caracteres da string gerada não é importante, mas deve conter todas
as letras comuns a ambas.
"""
from dataclasses import dataclass


@dataclass
class InterseccaoConjunto:
    """Realiza a intersecção entre duas strings e a retornando em uma
    terceira string.

    Args:
        a: string a
        b: string b

    Examples:
        >>> ab = InterseccaoConjunto('AAACTBF', 'CBT')
        >>> ab.interseccao()
        'BCT'
        >>> ab = InterseccaoConjunto('aaactbf', 'CBT')
        >>> ab.interseccao()
        ''
        >>> ab = InterseccaoConjunto(123, 'CBT')
        >>> ab.interseccao()
        "Erro: 'int' object is not iterable"
        >>> ab = InterseccaoConjunto('AAACTBF', 3.21)
        >>> ab.interseccao()
        "Erro: 'float' object is not iterable"
    """

    a: str
    b: str

    def interseccao(self) -> str:
        """Intersecção entre a e b (a ∩ b).

        Returns:
            intersecção das strings a e b (a ∩ b).
        """

        try:
            ab = set(self.a) & set(self.b)
        except Exception as e:
            return f'Erro: {e}'
        c = ''
        for item in sorted(ab):
            c += item
        return c


if __name__ == '__main__':  # pragma: no cover
    primeira = input('Digite a primeira string: ')
    segunda = input('Digite a segunda string: ')
    conjunto = InterseccaoConjunto(primeira, segunda)
    print(conjunto.interseccao())
    print(conjunto)
