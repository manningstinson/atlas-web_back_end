#!/usr/bin/env python3
"""
Module for calculating element lengths in an iterable with type annotations.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from the
    iterable and its length.
    """
    return [(i, len(i)) for i in lst]
