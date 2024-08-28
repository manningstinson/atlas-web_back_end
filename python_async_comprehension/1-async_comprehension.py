#!/usr/bin/env python3
"""
This module contains a coroutine that
collects random numbers using
asynchronous comprehension.
"""

from typing import List

# Using __import__ to dynamically import the module with a name starting with a digit
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from the 
    async_generator using an asynchronous comprehension.
    Returns a list of these numbers.
    """
    return [number async for number in async_generator()]
