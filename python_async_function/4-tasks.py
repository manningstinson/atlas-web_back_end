#!/usr/bin/env python3
"""
This module defines a
task-based version of wait_n using task_wait_random.
"""
import asyncio
from typing import List

# Importing task_wait_random from 3-tasks.py
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random
    n times with the specified max_delay using asyncio.Task.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create tasks
    delays = await asyncio.gather(*tasks)  # Gather all results
    return sorted(delays)  # Return sorted list of delays
