#!/usr/bin/env python3
"""
This module contains a coroutine
that collects random numbers using asynchronous comprehension.
"""

from typing import List
from .async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from the async_generator using an asynchronous comprehension.
    Returns a list of these numbers.
    """
    return [number async for number in async_generator()]
