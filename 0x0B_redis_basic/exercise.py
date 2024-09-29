#!/usr/bin/env python3
"""
This module provides a Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class for storing data in Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client
        and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): Data to be stored in Redis.

        Returns:
            str: The generated random key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and apply an optional conversion function.

        Args:
            key (str): The Redis key.
            fn (Optional[Callable]): Optional function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The data after applying the conversion function, or None if key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[str]: The data as a UTF-8 decoded string, or None if key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key (str): The Redis key.

        Returns:
            Optional[int]: The data as an integer, or None if key does not exist.
        """
        return self.get(key, fn=int)
