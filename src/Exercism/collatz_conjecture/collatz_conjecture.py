"""The Collatz Conjecture or 3x+1 problem.

The Collatz Conjecture or 3x+1 problem can be summarized as follows:

Take any positive integer n. If n is even, divide n by 2 to get n / 2.
If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process
indefinitely. The conjecture states that no matter which number you start
with, you will always reach 1 eventually.

    Given a number n, return the number of steps required to reach 1.
"""


def steps(number: int) -> int:
    """The Collatz Conjecture

    Return the number of steps required to reach 1.

    Args:
        number: takes a positive number.

    Returns:
        number of steps to get to 1.
    """
    if number < 1:
        raise ValueError('Only positive integers are allowed')

    if number == 1:
        return 0

    return 1 + (
        steps(number // 2) if number % 2 == 0 else steps(3 * number + 1)
    )
