"""desafio-python > exercicio_03.py | 2023-05-20.

Exercícios Python - #03

Escreva um programa que aceite uma sequência de números separados por vírgulas
do console e gere uma lista e uma tupla que contenha todos os números.

Suponha que a seguinte entrada seja fornecida ao programa: 34,67,55,33,12.

Então, a saída deve ser:
['34', '67', '55', '33', '12'] ('34', '67', '55', '33', '12')

Notes: Dica

    No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir
    que é uma entrada do console.

    O método tuple() pode converter uma lista em tupla.
"""


def gerar_colecoes(valores: str) -> print:
    """Gerador de coleções.

    Args: Parâmetro:
        valores (str): Sequência de números separados por vírgulas.

    Returns:
        print: Lista e Tupla da sequência de números.

    Examples: Exemplo:
        >>> gerar_colecoes('34,67,55,33,12')
        ['34', '67', '55', '33', '12'] ('34', '67', '55', '33', '12')
    """
    lista = valores.split(',')
    tupla = tuple(lista)
    return print(lista, tupla)


if __name__ == '__main__':  # pragma: no cover
    sequencia = input(
        'Digite uma sequência de números separados por vírgulas: '
    )
    gerar_colecoes(sequencia)
