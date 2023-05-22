"""desafio-python > exercicio_07.py | 2023-05-21.

Exercícios Python - #07

Escreva um programa que aceite uma sequência de linhas como entrada e imprima
as linhas após colocar todos os caracteres da frase em maiúsculos.

Suponha que a seguinte entrada seja fornecida ao programa:
`Ola Mundo pratica chega a perfeicao`
A saída do programa deverá ser:
`OLA MUNDO PRATICA CHEGA A PERFEICAO`

Tip: Dica
    No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir
    que é uma entrada do console.
"""
from dataclasses import dataclass, field


@dataclass
class FraseEmMaiuscula:
    """Transforma os caracteres de uma frase de minúsculos para maiúsculos.

    Attributes: Atributo:
        linhas (list): linhas a serem transformadas
    """

    linhas: list = field(default_factory=list)

    def __post_init__(self):
        """Processamento pós-inicialização."""
        self.le_entrada()
        self.imprime_saida()
        print()

    def le_entrada(self):
        """Armazena as entradas do usuário."""
        while True:
            linha = input('Digite uma frase: ')
            if not linha:
                break
            self.linhas.append(linha.upper())

    def imprime_saida(self):
        """Imprime as linhas transformadas."""
        for linha in self.linhas:
            print(linha)


if __name__ == '__main__':
    f = FraseEmMaiuscula()
    print(f)
