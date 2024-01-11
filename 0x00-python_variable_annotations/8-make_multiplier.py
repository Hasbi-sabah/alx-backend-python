#!/usr/bin/env python3
""" Module for the function make_multiplier """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier
    """

    def multiply(floaty: float) -> float:
        """
        type-annotated function that takes a float multiplier returns
        multiplier * multiplier
        """
        return float(floaty * multiplier)

    return multiply
