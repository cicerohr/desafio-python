"""desafio-python > exercicio_09.py | 2023-05-21.

Exercícios Python - #09

Este programa aceita uma sequência de números binários de 4 digitos separados
por vírgulas com entrada e verifique se eles são divisíveis por 5 ou não. Os
números divisíveis por 5 são impressos em uma sequência separada por vírgulas.

Example: Exemplo
    Entrada ⇨ 0100,0011,1010,1001,00010100

    Saída ⇨ 1010,10100

Tip: Dica
    Com base no resultado abaixo, demonstre ou crie pelo menos mais duas
    maneiras de resolver o mesmo exercício.

    Nota: você pode usar o mesmo código e apenas fazer alterações.

    ```python
    valor = []
    itens = [x for x in input().split(',')]
    for p in itens:
        intp = int(p, 2)
        if not intp % 5:
            valor.append(p)

    print(','.join(valor))
    ```
Examples:
    >>> sequencia = ['0100', '0011', '1010', '1001', '00010100']
    >>> verifica = DivisivelPorCinco(sequencia)
    >>> print(verifica)
    1010,10100
"""
from dataclasses import dataclass, field


@dataclass
class DivisivelPorCinco:
    """Verifica se uma sequência de binários são divisíveis por cinco.

    Args:
        binarios: sequência de binários da entrada
        divisiveis_por_cinco: lista de binários divisíveis por cinco
    """

    binarios: list = field(default_factory=list)
    divisiveis_por_cinco: list = field(default_factory=list)

    def __post_init__(self):
        """Processamento pós-inicialização.

        Transforma cada binário para inteiro.
        """
        self.binarios = [int(x, 2) for x in self.binarios]

    def verificar(self) -> list:
        """Verifica se o binário, convertido para inteiro, é divisível por
        cinco.

        Returns:
            lista com binários divisíveis por cinco
        """
        for x in self.binarios:
            if x % 5 == 0:
                self.divisiveis_por_cinco.append(bin(x).replace('0b', ''))

        return self.divisiveis_por_cinco

    def __str__(self) -> str:
        """Retorna os binários divisíveis por cinco.

        Returns:
            string para ser exibida ao usuário
        """
        self.verificar()
        return ','.join(map(str, self.divisiveis_por_cinco))


if __name__ == '__main__':  # pragma: no cover
    entrada = input(
        'Digite a sequência de binário separados por vírgulas: '
    ).split(',')
    por_cinco = DivisivelPorCinco(entrada)
    print(por_cinco)
    print(repr(por_cinco))
