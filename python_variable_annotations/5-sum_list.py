#!/usr/bin/env python3
"""
Module for summing a list of floats with type annotations.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of float numbers and returns the total as a float.
    """
    return sum(input_list)
