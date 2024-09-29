#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis,
and decorators to count method calls and store call history.
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts the number of times a method is called.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The wrapped method with call count functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments the call count in Redis
        and then calls the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a function.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The wrapped method with history logging functionality.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that logs input arguments and output values
        in Redis, and then calls the original method.
        """
        # Generate Redis keys for input and output lists
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        # Store the input arguments as strings
        self._redis.rpush(input_key, str(args))

        # Call the original method and get its output
        result = method(self, *args, **kwargs)

        # Store the output
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    """
    Cache class for storing data in Redis, counting method calls,
    and tracking call history.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client
        and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The generated key for the stored data.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def replay(self, method: Callable):
        """
        Display the history of calls for a particular method.

        Args:
            method (Callable): The method to replay.
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        # Get the inputs and outputs from Redis
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        # Print the replay information
        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for inp, out in zip(inputs, outputs):
            print(
                f"{method.__qualname__}(*{inp.decode('utf-8')}) -> "
                f"{out.decode('utf-8')}"
            )
