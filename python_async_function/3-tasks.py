#!/usr/bin/env python3
"""
This module defines a function
that returns an asyncio.Task for the wait_random coroutine.
"""
import asyncio
from typing import Union

# Importing wait_random from 0-basic_async_syntax.py using __import__()
wait_random = __import__('2_basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task
        object that runs the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
