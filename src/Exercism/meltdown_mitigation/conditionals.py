"""Functions to prevent a nuclear meltdown.

In this exercise, we'll develop a simple control system for a nuclear reactor.

For a reactor to produce the power it must be in a state of criticality. If the
reactor is in a state less than criticality, it can become damaged. If the
reactor state goes beyond criticality, it can overload and result in a
meltdown. We want to mitigate the chances of meltdown and correctly manage
reactor state.
"""


def is_criticality_balanced(
    temperature: int | float,
    neutrons_emitted: int | float,
) -> bool:
    """Verify criticality is balanced.

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800° K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than
    500000.

    Args:
        temperature: temperature value in kelvin.
        neutrons_emitted: number of neutrons emitted per second.

    Returns:
        is criticality balanced?
    """
    temperature_neutrons = temperature * neutrons_emitted
    if (
        temperature < 800
        and neutrons_emitted > 500
        and temperature_neutrons < 500_000
    ):
        return True
    return False


def reactor_efficiency(
    voltage: int | float,
    current: int | float,
    theoretical_max_power: int | float,
) -> str:
    """Assess reactor efficiency zone.

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black -> less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current

    Args:
        voltage: voltage value.
        current: current value.
        theoretical_max_power: power that corresponds to a 100% efficiency.

    Returns:
        one of ('green', 'orange', 'red', or 'black').
    """
    generated_power = voltage * current
    percentage = (generated_power / theoretical_max_power) * 100
    if percentage < 30:
        return 'black'
    if 60 > percentage >= 30:
        return 'red'
    if 60 <= percentage < 80:
        return 'orange'
    return 'green'


def fail_safe(
    temperature: int | float,
    neutrons_produced_per_second: int | float,
    threshold: int | float,
) -> str:
    """Assess and return status code for the reactor.

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the
    above-stated ranges


    Args:
        temperature: value of the temperature in kelvin.
        neutrons_produced_per_second: neutron flux.
        threshold: threshold for category.

    Returns:
        one of ('LOW', 'NORMAL', 'DANGER').
    """
    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * 0.9):
        return 'LOW'
    if (threshold * 0.9) < criticality < (threshold * 1.1):
        return 'NORMAL'
    return 'DANGER'
