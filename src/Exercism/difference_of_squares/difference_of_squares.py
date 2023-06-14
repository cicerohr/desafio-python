"""Difference of Squares.

Find the difference between the square of the sum and the sum of the squares of
the first N natural numbers.

The square of the sum of the first ten natural numbers is
(1 + 2 + ... + 10)² = 55² = 3025.

The sum of the squares of the first ten natural numbers is
1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural
numbers and the sum of the squares of the first ten natural numbers
is 3025 - 385 = 2640.
"""


def square_of_sum(number: int) -> int:
    """The square of the sum.

    Args:
        number: first n natural numbers.

    Returns:
        the square of the sum of the first n natural numbers.
    """
    return sum(n for n in range(number + 1)) ** 2


def sum_of_squares(number: int) -> int:
    """The sum of the squares.

    Args:
        number: first n natural numbers.

    Returns:
        the sum of the squares of the first n natural numbers.
    """
    return sum(n * n for n in range(number + 1))


def difference_of_squares(number: int) -> int:
    """The difference between the square of the sum and the sum of the squares.

    Args:
        number: first n natural numbers.

    Returns:
        the difference between the square of the sum and the sum of the squares of the first n natural numbers.
    """
    return square_of_sum(number) - sum_of_squares(number)
