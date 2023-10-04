"""Main module."""

import math


def degree(time: float, acc: float, rad: float, vel: float = 0) -> float:
    """Calc angle of deflection.

    Args:
        time (float): time
        acc (float): acceleration
        rad (float): radius
        vel (float): velocity. Defaults to 0.

    Returns:
        float: angle of deflection
    """
    #lenght of circle
    circle = 360

    # Calculating the angular displacement
    way = vel * time + (acc * time ** 2) / 2

    # Calculate the circumference using the formula C = 2*pi*r
    lenght = 2 * math.pi * rad

    # Calculate the angle in radians
    radians = way / lenght

    # Convert the angle from radians to degrees
    degrees = circle * abs(math.floor(radians) - radians)

    return round(degrees, 2)
