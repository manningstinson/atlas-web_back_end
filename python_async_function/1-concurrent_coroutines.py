#!/usr/bin/env python3
"""
This module defines an async routine
that spawns multiple wait_random coroutines
and returns the list of all the delays in ascending order.
"""
import asyncio
from typing import List

# Importing wait_random from 0-basic_async_syntax.py
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay concurrently.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
