"""desafio-python/src/livro_nilo/capitulo_07_04.py | 2023-06-03.

    @author: Nilo Ney Coutinho Menezes
    @modified by: Cícero
    @link: https://python.nilo.pro.br/exercicios3/capitulo%2007/exercicio-07-04.html

Escreva um programa que leia uma string e imprima quantas vezes cada caractere
aparece nessa string.

    String: TTAAC
    Resultado:
    T: 2x
    A: 2x
    C: 1x
"""
from dataclasses import dataclass


@dataclass
class ContadorLetras:
    """Conta o número de vezes que um caractere aparece.

    Args:
        caracteres: string com caracteres a serem contados

    Examples:
        >>> entrada = ContadorLetras('sequencia')
        >>> entrada.contador_caracteres()
        {'s': 1, 'e': 2, 'q': 1, 'u': 1, 'n': 1, 'c': 1, 'i': 1, 'a': 1}
        >>> entrada = ContadorLetras(123)
        >>> entrada.contador_caracteres()
        'Erro: somente strings são válidas.'
    """

    caracteres: str

    def contador_caracteres(self) -> dict | str:
        """Conta quantas vezes cada caractere aparece.

        Returns:
            dicionário com o numero de vezes que cada caractere apareceu.
        """
        contador = {}
        if self.eh_valido():
            for caractere in self.caracteres:
                contador[caractere] = contador.get(caractere, 0) + 1
            return contador
        return 'Erro: somente strings são válidas.'

    def eh_valido(self):
        return isinstance(self.caracteres, str)


if __name__ == '__main__':  # pragma: no cover
    sequencia = input('Digite a string: ')
    conta = ContadorLetras(sequencia)
    print(conta)
    for chave, valor in conta.contador_caracteres().items():
        print(f'{chave}: {valor}x')
    conta2 = ContadorLetras(123)
    print(repr(conta2))
    print(str(conta2.contador_caracteres()))
