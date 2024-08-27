#!/usr/bin/env python3
"""
Module for converting a string and a number to a tuple with type annotations.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of the int/float value.
    """
    return (k, float(v ** 2))
