"""desafio-python > exercicio_02.py | 2023-05-19.

Exercícios Python - #02

Escreva um programa que possa calcular o fatorial de um dado número.
Os resultados devem ser impressos em uma sequência separada por vírgulas em
uma única linha. Suponha que a seguinte entrada seja fornecida ao programa:
8 então, a saída deve ser: 40320

Notes: Definição:
    Na matemática, o fatorial (AO 1945: factorial) de um número natural 'n',
    representado por 'n!', é o produto de todos os inteiros positivos menores
    ou iguais a n. A notação 'n!' foi introduzida por Christian Kramp em 1808.

        0! = 1
        1! = 1
"""


def fatorial(n: int) -> int:
    """Calcula o fatorial de um número de forma recursiva.

    Examples: Exemplos:
        >>> fatorial(0)
        1
        >>> fatorial(1)
        1
        >>> fatorial(2)
        2
        >>> fatorial(3)
        6

    Args: Parâmetro:
        n: número

    Raises:
        ValueError: se o número for negativo

    Returns:
        fatorial
    """

    if n < 0:
        raise ValueError('n precisa ser positivo')
    if n == 0:
        return 1
    return n * fatorial(n - 1)


def main():
    """Função principal."""
    n = int(input('Digite um número: '))
    print(fatorial(n))


if __name__ == '__main__':  # pragma: no cover
    main()
