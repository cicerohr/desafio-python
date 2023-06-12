def exchange_money(budget: float, exchange_rate: float) -> float:
    """Estimate value after exchange.

    This function should return the value of the exchanged currency.

    Args:
        budget: amount of money you are planning to exchange
        exchange_rate: unit value of the foreign currency.

    Returns:
        exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculate currency left after an exchange.

    This function should return the amount of money that is left from the
    budget.

    Args:
        budget: amount of money you are planning to exchange.
        exchanging_value: unit value of the foreign currency.

    Returns:
        exchanged value of the foreign currency you can receive.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calculate value of bills.

    This exchanging booth only deals in cash of certain increments. The total
    you receive must be divisible by the value of one "bill" or unit, which can
    leave behind a fraction or remainder. Your function should return only the
    total value of the bills (excluding fractional amounts) the booth would
    give back. Unfortunately, the booth gets to keep the remainder/change as an
    added bonus.

    Args:
        denomination: the value of a bill.
        number_of_bills: amount of bills you received.

    Returns:
        total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """Calculate number of bills.

    This function should return the number of currency bills that you can
    receive within the given budget. In other words: How many whole bills of
    currency fit into the amount of currency you have in your budget?
    Remember -- you can only receive whole bills, not fractions of bills, so
    remember to divide accordingly. Effectively, you are rounding down to the
    nearest whole bill/denomination.

    Args:
        budget: the amount of money you are planning to exchange.
        denomination: the value of a single bill.

    Returns:
        number of bills after exchanging all your money.
    """
    return int(budget // denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Calculate leftover after exchanging into bills.

    This function should return the leftover amount that cannot be exchanged
    from your budget given the denomination of bills. It is very important to
    know exactly how much the booth gets to keep.

    Args:
        budget: the amount of money you are planning to exchange.
        denomination: the value of a single bill.

    Returns:
        the leftover amount that cannot be exchanged given the current
        denomination.
    """
    return budget % denomination


def exchangeable_value(
    budget: float, exchange_rate: float, spread: int, denomination: int
) -> int:
    """Calculate value after exchange.

    This function should return the maximum value of the new currency after
    calculating the exchange rate plus the spread. Remember that the currency
    denomination is a whole number, and cannot be sub-divided.

    Args:
        budget: the amount of your money you are planning to exchange.
        exchange_rate: the unit value of the foreign currency.
        spread: percentage that is taken as an exchange fee.
        denomination: the value of a single bill.

    Returns:
        maximum value you can get.
    """
    new_rate = exchange_rate + (exchange_rate * (spread / 100))
    new_currency = exchange_money(budget, new_rate)
    number_of_bills = get_number_of_bills(new_currency, denomination)
    return get_value_of_bills(denomination, number_of_bills)
