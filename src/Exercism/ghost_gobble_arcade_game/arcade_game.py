"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verify that Pac-Man can eat a ghost if he is empowered by a power
    pellet.

    Args:
        power_pellet_active: does the player have an active power pellet?
        touching_ghost: is the player touching a ghost?

    Returns:
        can the ghost be eaten?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verify that Pac-Man has scored when a power pellet or dot has been
    eaten.

    Args:
        touching_power_pellet: is the player touching a power pellet?
        touching_dot: is the player touching a dot?

    Returns:
        has the player scored or not?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost
    without his power pellet.

    Args:
        power_pellet_active: does the player have an active power pellet?
        touching_ghost: is the player touching a ghost?

    Returns:
        has the player lost the game?
    """
    return not power_pellet_active and touching_ghost


def win(
    has_eaten_all_dots: bool,
    power_pellet_active: bool,
    touching_ghost: bool,
) -> bool:
    """Trigger the victory event when all dots have been eaten.

    Args:
        has_eaten_all_dots: has the player "eaten" all the dots?
        power_pellet_active: does the player have an active power pellet?
        touching_ghost: is the player touching a ghost?

    Returns:
        has the player won the game?
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
