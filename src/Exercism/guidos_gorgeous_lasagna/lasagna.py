"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.

    Args:
        elapsed_bake_time: baking time already elapsed.

    Returns:
        remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculates the preparation time for a given number of layers.

    Function that returns the total time of preparation of the lasagna taking
    into account the number of layers.

    Args:
        number_of_layers: number of layers to calculate the preparation.

    Returns:
        time of preparation in minutes.
    """
    preparation_time = 2

    return preparation_time * number_of_layers


def elapsed_time_in_minutes(n_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculates elapsed time in minutes.

    Args:
        n_of_layers: number of layers to calculate the preparation time.
        elapsed_bake_time: bake time elapsed in minutes.

    Returns:
        elapsed time in minutes.
    """
    return preparation_time_in_minutes(n_of_layers) + elapsed_bake_time
