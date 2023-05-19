"""desafio-python in: 2023-05-18.

Exercícios Python - #01

Escreva um programa que encontre todos os números divisíveis por 7, mas que não
sejam múltiplos de 5, entre 2000 e 3200 (ambos inclusos). Os números obtidos
devem ser impressos em sequência separada por vírgula em uma única linha.
"""


def divisiveis_por_7(inicio: int, fim: int) -> list:
    """Verfica se os números, de uma faixa, são divisíveis por 7, mas não é
    múltiplo de 5.

    Examples:
        >>> divisiveis_por_7(7, 77)
        [7, 14, 21, 28, 42, 49, 56, 63, 77]
        >>> divisiveis_por_7(50, 77)
        [56, 63, 77]

    Args:
        inicio: número inicial da faixa
        fim: número final da faixa

    Returns:
        lista com o resultado dos números

    """
    return [n for n in range(inicio, fim + 1) if n % 7 == 0 and n % 5 != 0]


def main():
    """Função principal."""
    print(divisiveis_por_7(2000, 3200))


if __name__ == '__main__':
    main()
