#!/usr/bin/env python3
"""
This module contains a coroutine
that generates random numbers asynchronously.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates 10 random numbers 
    between 0 and 10.
    Waits 1 second between each generation.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
