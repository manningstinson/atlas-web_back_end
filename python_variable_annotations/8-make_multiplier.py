#!/usr/bin/env python3
"""
Module for returning a function that multiplies a float by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.
    """
    return lambda x: x * multiplier
