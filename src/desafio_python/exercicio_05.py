"""desafio-python > exercicio_05.py | 2023-05-20.

Exercícios Python - #05

Escreva um programa que calcule e imprima o valor de acordo coma fórmula dada:
Q = √ (2 . C. D) / H, onde C=50 e H=30. D é a variável cujos valores devem ser
inseridos em seu programa em uma sequência separada por vírgulas.

Ex.: vamos supor que a seguinte sequência de entrada, separada por vírgula,
seja fornecida. 100, 150, 180. A saída do programa deve ser 18, 22, 24.

Tip: Dica
    Se a saída recebida estiver na forma decimal, deve ser arredondado para o
    valor mais próximo (ex.: 26,0 -> 26).
"""
from math import sqrt


class CalculaSequenciaNumerica:
    """Calcula uma sequência numérica usando a fórmula Q = √ (2 . C. D) / H.

    Methods: Métodos
        * __init__ ⇨ Inicializa o objeto CalculaSequenciaNumerica
        * __repr__ ⇨ Representação do objeto
        * __str__ ⇨ Retorna a sequência numérica calculada
        * calcular_sequencia ⇨ Calcula a sequência numérica
        * obter_dados ⇨ Obtém dados do console
        * tratar_dados ⇨ Verifica se os dados obtidos são válidos

    Examples: Exemplos:
        >>> s = CalculaSequenciaNumerica()
        >>> s.d = ['100', '150', '180']
        >>> s.calcular_sequencia()
        ['18', '22', '24']
        >>> s.d = [100, 150, 180]
        >>> s.calcular_sequencia()
        ['18', '22', '24']
    """

    def __init__(self):
        """Inicializa o objeto CalculaSequenciaNumerica."""
        self.c: int = 50
        self.h: int = 30
        self.d: list[str] = []

    def obter_dados(self):
        """Obtém os dados da sequência numérica do console."""
        try:
            self.d = [
                dado for dado in input('Digite os valores de D: ').split(',')
            ]
        except ValueError:
            print('Dados inválidos.')

        self.tratar_dados()

    def tratar_dados(self):
        """Verifica se os dados obtidos são válidos."""
        if len(self.d) == 0 or self.d == ['']:
            print()
            print(' Dados inválidos! Tente novamente. '.center(40, '='))
            print('Ex.: 100,200,300\n')
            self.__init__()
            self.obter_dados()

    def calcular_sequencia(self) -> list:
        """Calcula a sequência numérica.

        Returns:
            list: sequência numérica calculada.
        """
        return [
            str(round(sqrt(2 * self.c * float(d) / self.h))) for d in self.d
        ]

    def __str__(self) -> str:
        """Retorna a sequência numérica calculada.

        Returns:
            str: sequência numérica calculada.
        """
        return ','.join(self.calcular_sequencia())

    def __repr__(self) -> str:
        """Representação do objeto.

        Returns:
            str: representação do objeto.
        """
        return (
            f'{self.__class__.__name__}()\n'
            f'{self.__class__.__doc__}\n'
            f'{self.__class__.__module__} {self.__dict__}\n'
        )


if __name__ == '__main__':
    c = CalculaSequenciaNumerica()
    c.obter_dados()
    print(c)
    print(repr(c))
