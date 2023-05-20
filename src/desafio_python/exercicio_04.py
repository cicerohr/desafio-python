"""desafio-python in: 2023-05-20.

Exercícios Python - #04

Defina uma classe que tenha pelo menos dois métodos:

get_string(): obtém uma string do console

print_string: imprime a string em maiúscula

Também inclua uma função de teste simples para testar os métodos de classe.

Notes: Dica:

    Use o método `__init__` para construir alguns parâmetros.
"""


class ImprimeStringMaiusculas:
    """Imprime os caracteres, de uma string, em caixa-alta.

    Methods: Métodos
        __init__(): inicializa o objeto ImprimeStringMaiusculas

        get_string(): obtém uma string do console

        print_string(): imprime a string em caixa-alta

    Examples: Exemplo:
        >>> imprimir = ImprimeStringMaiusculas()
        >>> imprimir.string = 'teste'
        >>> imprimir.print_string()
        TESTE
    """

    def __init__(self):
        """Inicializador do objeto ImprimeStringMaiusculas."""
        self.string = ''

    def get_string(self):
        """Através do console obtém a string do usuário."""
        self.string = input('Digite uma string: ')

    def print_string(self):
        """Imprime, no console, a string em caixa-alta."""
        print(self.string.upper())


if __name__ == '__main__':
    imprime = ImprimeStringMaiusculas()
    imprime.get_string()
    imprime.print_string()
