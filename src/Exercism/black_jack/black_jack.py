"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/

"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.

    Examples:
        >>> value_of_card('K')
        10
        >>> value_of_card('4')
        4
        >>> value_of_card('A')
        1

    Args:
        card: given card.

    Returns:
        value of a given card.  See above for values.
    """
    cards = {
        'A': 1,
        'J': 10,
        'Q': 10,
        'K': 10,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
    }
    if card in cards:
        return cards[card]
    return 0


def higher_card(card_one: str, card_two: str) -> str | tuple:
    """Determine which card has a higher value in the hand.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.

    Examples:
        >>> higher_card('K', '10')
        ('K', '10')
        >>> higher_card('4', '6')
        '6'
        >>> higher_card('K', 'A')
        'K'

    Args:
        card_one: cards dealt in hand.  See above for values.
        card_two: cards dealt in hand.  See above for values.

    Returns:
        resulting Tuple contains both cards if they are of equal value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.

    Notes:
        if we already have an ace in hand then its value would be 11.

    Examples:
        >>> value_of_ace('6', 'K')
        1
        >>> value_of_ace('7', '3')
        11

    Args:
        card_one: card dealt. See above for values.
        card_two: card dealt. See above for values.

    Returns:
        either 1 or 11 value of the upcoming ace card.
    """
    sum_cards = value_of_card(card_one) + value_of_card(card_two)
    if sum_cards <= 10 and 'A' not in (card_one, card_two):
        return 11
    if sum_cards > 10 or 'A' in (card_one, card_two):
        return 1
    return 0


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.

    Notes:
        The score calculation can be done in many ways. But if possible,
        we'd like you to check if there is an ace and a ten-card in the hand
        (or at a certain position), as opposed to summing the hand values.

    Examples:
        >>> is_blackjack('A', 'K')
        True
        >>> is_blackjack('10', '9')
        False

    Args:
        card_one: card dealt. See above for values.
        card_two: card dealt. See above for values.

    Returns:
        is the hand is a blackjack (two cards worth 21).
    """
    if 'A' in (card_one, card_two) and 10 in (
        value_of_card(card_one),
        value_of_card(card_two),
    ):
        return True
    return False


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    Examples:
        >>> can_split_pairs('Q', 'K')
        True
        >>> can_split_pairs('10', 'A')
        False

    Args:
        card_one: cards dealt.
        card_two: cards dealt.

    Returns:
        can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    Examples:
        >>> can_double_down('A', '9')
        True
        >>> can_double_down('10', '2')
        False

    Args:
        card_one: first cards in hand.
        card_two: second cards in hand.

    Returns:
        can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    sum_cards = value_of_card(card_one) + value_of_card(card_two)
    doubling_down = (9, 10, 11)
    if sum_cards in doubling_down:
        return True
    return False
