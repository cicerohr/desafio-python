"""desafio-python/src/coderbyte/codeland_username_validation.py | 2023-06-08.

Have the function CodelandUsernameValidation(str) take the str parameter being
passed and determine if the string is a valid username according to the
following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true,
otherwise return the string false.

Examples:
    Input: "aa_"

    Output: false

    Input: "u__hello_world123"

    Output: true
"""
from dataclasses import dataclass


@dataclass
class CodelandUsernameValidation:
    """Validador de nome de usuário.

    Regras:
        1. O nome de usuário tem entre 4 e 25 caracteres.
        2. Deve começar com uma letra.
        3. Ele só pode conter letras, números e o caractere sublinhado.
        4. Não pode terminar com um caractere sublinhado.

    Examples:
        >>> CodelandUsernameValidation('a234').validador()
        False
        >>> CodelandUsernameValidation('a234567890123456789012345').validador()
        False
        >>> CodelandUsernameValidation('1aa').validador()
        False
        >>> CodelandUsernameValidation('aa_').validador()
        False
        >>> CodelandUsernameValidation('u__hello_world123').validador()
        True

    Args:
        sequencia: string com o nome do usuário a ser validado.
        MIN_CARACTERES: número de caracteres mínimo.
        MAX_CARACTERES: número de caracteres máximo.
    """

    sequencia: str
    MIN_CARACTERES: int = 4
    MAX_CARACTERES: int = 25

    def validador(self) -> bool:
        """Valida a entrada do usuário.

        Returns:
            True se é válido, false caso contrário.
        """
        if (
            self.MIN_CARACTERES < len(self.sequencia) < self.MAX_CARACTERES
            and self.sequencia[0].isalpha()
            and self.sequencia[-1] != '_'
            and [
                c
                for c in self.sequencia
                if self.sequencia.isalnum() or c == '_'
            ]
            != []
        ):
            return True
        return False


if __name__ == '__main__':  # pragma: no cover
    validada = CodelandUsernameValidation('u__hello_world123')
    print(validada.validador())
