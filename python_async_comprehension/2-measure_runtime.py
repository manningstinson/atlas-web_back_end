#!/usr/bin/env python3
"""
This module contains a coroutine that
measures the runtime of parallel asynchronous comprehensions.
"""

import asyncio
import time
from .async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times in parallel.
    Returns the total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
