"""desafio-python/src/livro_nilo/capitulo_07_01.py | 2023-05-23.

Procurando strings dentro de strings

    @author: Nilo Ney Coutinho Menezes
    @modified by: Cícero
    @link: https://python.nilo.pro.br/exercicios3/capitulo%2007/exercicio-07-01.html

Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro
da primeira e imprima a posição de início.

    1ª string: AABBEFAATT
    2ª string: BE
    Resultado: BE encontrado na posição 3 de AABBEFAATT
"""
from dataclasses import dataclass


@dataclass
class BuscaString:
    """Busca sequência de caracteres em uma string e retorna o índice quando
    encontrado.

    Examples:
        >>> buscar = BuscaString('Palavra', 'P')
        >>> buscar.procurar()
        0
        >>> buscar = BuscaString('palavra', 'P')
        >>> buscar.procurar()
        -1
        >>> buscar = BuscaString('palaVra', 'V')
        >>> buscar.procurar()
        4
        >>> buscar = BuscaString('palaVra', 'Vra')
        >>> buscar.procurar()
        4
        >>> buscar = BuscaString('palaVra', 'Vxx')
        >>> buscar.procurar()
        -1
        >>> buscar = BuscaString('Palavra', 0)
        >>> buscar.procurar()
        Erro: must be str, not int
        >>> buscar = BuscaString(1, 0)
        >>> buscar.procurar()
        Erro: 'int' object has no attribute 'find'

    Args:
        alvo: texto para pesquisa
        busca: caracteres a serem buscados no alvo
    """

    alvo: str
    busca: str

    def procurar(self) -> int:
        """Busca a string na sting alvo.

        Returns:
            índice do primeiro símbolo encontrado; -1 caso contrário.
        """
        try:
            return self.alvo.find(self.busca)
        except Exception as e:
            print(f'Erro: {e}')


if __name__ == '__main__':  # pragma: no cover
    busca = BuscaString('palavra', 'vra')
    print(
        f'"{busca.busca}" está no índice {busca.procurar()} '
        f'da string "{busca.alvo}".\n'
    )
    print(busca)
