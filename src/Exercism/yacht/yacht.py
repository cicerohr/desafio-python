"""Yacht

The dice game Yacht is from the same family as Poker Dice, Generala and
particularly Yahtzee, of which it is a precursor. In the game, five dice are
rolled and the result can be entered in any of twelve categories. The score of
a throw of the dice depends on category chosen.

See also:
    https://en.wikipedia.org/wiki/Yacht_(dice_game)
"""

# Score categories.
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
CHOICE = 'CHOICE'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
YACHT = 'YACHT'


def score(dice: list, category: str) -> int:
    """Score a given dice.

    Given a list of values for five dice and a category, your solution should
    return the score of the dice for that category. If the dice do not satisfy
    the requirements of the category your solution should return 0. You can
    assume that five values will always be presented, and the value of each
    will be between one and six inclusively. You should not assume that the
    dice are ordered.

    Args:
        dice:  list of values for five dice.
        category: a constant category.

    Returns:
        data score for this category, zero otherwise.
    """
    match category:
        case 'ONES':
            return sum(i for i in dice if i == 1)
        case 'TWOS':
            return sum(i for i in dice if i == 2)
        case 'THREES':
            return sum(i for i in dice if i == 3)
        case 'FOURS':
            return sum(i for i in dice if i == 4)
        case 'FIVES':
            return sum(i for i in dice if i == 5)
        case 'SIXES':
            return sum(i for i in dice if i == 6)
        case 'FULL_HOUSE':
            visited = []
            dup = [visited.append(x) for x in dice if dice.count(x) > 1]
            return (
                sum(i for i in dice if dice.count(i) > 1)
                if len(set(dice)) == 2 and len(set(visited)) == 2
                else 0
            )
        case 'FOUR_OF_A_KIND':
            return (
                sum(i for i in dice if dice.count(i) > 3)
                if len(set(dice)) > 1
                else dice[0] * 4
            )
        case 'CHOICE':
            return sum(dice)
        case 'LITTLE_STRAIGHT':
            little_straight = [1, 2, 3, 4, 5]
            return 30 if little_straight == sorted(dice) else 0
        case 'BIG_STRAIGHT':
            big_straight = [2, 3, 4, 5, 6]
            return 30 if big_straight == sorted(dice) else 0
        case 'YACHT':
            return 50 if len(set(dice)) == 1 else 0


# # Alternativa
# YACHT = lambda d: 50 if len(set(d)) == 1 else 0
# ONES = lambda d: sum(x for x in d if x == 1)
# TWOS = lambda d: sum(x for x in d if x == 2)
# THREES = lambda d: sum(x for x in d if x == 3)
# FOURS = lambda d: sum(x for x in d if x == 4)
# FIVES = lambda d: sum(x for x in d if x == 5)
# SIXES = lambda d: sum(x for x in d if x == 6)
# FULL_HOUSE = (
#     lambda d: sum(d)
#     if len(set(d)) == 2 and any(d.count(x) == 3 for x in set(d))
#     else 0
# )
# FOUR_OF_A_KIND = lambda d: sum(x * 4 for x in set(d) if d.count(x) > 3)
# LITTLE_STRAIGHT = lambda d: 30 if list(set(d)) == [1, 2, 3, 4, 5] else 0
# BIG_STRAIGHT = lambda d: 30 if list(set(d)) == [2, 3, 4, 5, 6] else 0
# CHOICE = lambda d: sum(x for x in d)
#
#
# def score(dice, category):
#     return category(dice)
