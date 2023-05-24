"""desafio-python > exercicio_08.py | 2023-05-21.

Exercícios Python - #08

Escreva um programa que aceite uma sequência de palavras separadas por espaços
em branco como entrada e imprima as palavras após remover todas as palavras
duplicadas e classificá-las de forma alfanumerica.

Suponha que a seguinte entrada seja fornecida ao programa:

`ola mundo a pratica faz bem ola mundo denovo`

Então, a saída deve ser:

`a bem denovo faz mundo ola pratica`

Tip: Dica
    No caso de dados de entrada serem fornecidos à pergunta, deve-se presumir
    que é uma entrada do console. Usamos `set` _container_ para remover dados
    duplicados automaticamente e então usamos `sorted()` para classificar
    dados.
"""
from dataclasses import dataclass, field


@dataclass
class ClassificaPalavras:
    """Classifica as palavras de uma frase, e retiras as repetidas,
    em ordem alfanumérica.

    Args: Argumento:
        palavras: frase a ser classificada

    Examples: Exemplo:
        >>> p = ['ola','mundo', 'a', 'pratica', 'faz', 'bem', 'ola','mundo']
        >>> ab = ClassificaPalavras(p)
        >>> ab.palavras
        ['a', 'bem', 'faz', 'mundo', 'ola', 'pratica']
    """

    palavras: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Processamento pós-inicialização."""
        self.palavras = list(set(self.palavras))
        self.palavras.sort()

    def __str__(self) -> str:
        """Retorna uma string apropriada para ser exibida ao usuário final.

        Returns:
            string para ser exibida ao usuário.
        """
        return ' '.join(self.palavras)


if __name__ == '__main__':  # pragma: no cover
    frase = input(
        'Digite uma sequência de palavras separadas por espaços em branco: '
    ).split()
    print(frase)
    print(ClassificaPalavras(frase))
