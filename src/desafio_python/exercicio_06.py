"""desafio-python > exercicio_06.py | 2023-05-21.

Exercícios Python - #06

Escreva um programa que aceite uma sequência de palavras separadas por vírgulas
como entrada e imprima as palavras em uma sequência separada por vírgulas
após classificá-las em ordem alfabética.

Suponha que a seguinte entrada seja fornecida ao programa:
__rota,olá,saco,mundo__. Então, a saída deverá ser __mundo,olá,rota,saco__.
"""
from dataclasses import dataclass, field


@dataclass
class OrdenaSequencia:
    """Ordena sequência de palavras de forma alfabética.

    Args: Parâmetros:
        palavras (str): sequência de palavras separadas por vírgulas
        lista_palavras (list): lista com as palavras do usuário
        lista_ordenada (list): lista coa as palavras ordenadas

    Examples: Exemplos:
        >>> x = OrdenaSequencia('rota,olá,saco,mundo')
        >>> print(x.lista_ordenada)
        ['mundo', 'olá', 'rota', 'saco']
        >>> print(x.__str__())
        mundo, olá, rota, saco
        >>> print(x.__repr__())
        OrdenaSequencia(palavras='rota,olá,saco,mundo', lista_palavras=['rota', 'olá', 'saco', 'mundo'], lista_ordenada=['mundo', 'olá', 'rota', 'saco'])
    """

    palavras: str
    lista_palavras: list = field(default_factory=list)
    lista_ordenada: list = field(default_factory=list)

    def __post_init__(self):
        """Processamento pós-inicialização."""
        self.lista_palavras = self.palavras.split(',')
        self.lista_ordenada = sorted(self.lista_palavras)

    def __str__(self) -> str:
        """Retorna uma string apropriada para ser exibida ao usuário final.

        Returns:
            str: string para ser exibida ao usuário.
        """
        return ', '.join(self.lista_ordenada)


if __name__ == '__main__':
    palavras = input(
        'Digite uma sequência de palavras separadas por vírgulas: '
    )
    s = OrdenaSequencia(palavras=palavras)
    print(s)
