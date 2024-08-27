#!/usr/bin/env python3
"""
This module defines a function
to measure the total runtime of wait_n and return
the average runtime per task.
"""
import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    for wait_n and returns the average time per task.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay in seconds.

    Returns:
        float: Average time per task.
    """
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    total_time = time.time() - start_time  # Calculate total time taken
    return total_time / n  # Return the average time per task
