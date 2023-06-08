"""desafio-python/src/coderbyte/first_factorial.py | 2023-06-08.

Have the function FirstFactorial(num) take the num parameter being passed and
return the factorial of it. For example: if num = 4, then your program should
return (4 * 3 * 2 * 1) = 24.

For the test cases, the range will be between 1 and 18 and the input will
always be an integer.

Examples:
    Input: 4

    Output: 24

    Input: 8

    Output: 40320
"""


def first_factorial(num: int) -> int | str:
    """Retorna o fatorial de um número de forma recursiva.

    tips:
        0! = 1

        1! = 1

    Examples:
        >>> first_factorial(0)
        1
        >>> first_factorial(1)
        1
        >>> first_factorial(4)
        24
        >>> first_factorial(8)
        40320
        >>> first_factorial(-4)
        'Digite um número inteiro positivo!'
        >>> first_factorial('a')
        'Digite um número inteiro positivo!'

    Args:
        num: inteiro positivo a ser fatorado.

    Returns:
        fatorial do número 'num'.
    """
    if not isinstance(num, int) or num < 0:
        return 'Digite um número inteiro positivo!'
    elif num == 0 or num == 1:
        return 1
    else:
        return num * first_factorial(num - 1)


if __name__ == '__main__':  # pragma: no cover
    print(first_factorial(int(input('Digite um número: '))))
