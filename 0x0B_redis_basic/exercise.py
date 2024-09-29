#!/usr/bin/env python3
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
        # Use __qualname__ to get the fully qualified name of the method as the key
        key = method.__qualname__
        # Increment the counter for this method in Redis
        self._redis.incr(key)  # Increment call count in Redis using __qualname__ as key
        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """
    Cache class for storing data in Redis and counting method calls.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client
        and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis using a random key and return the key.
        The method is decorated with count_calls to track invocations.
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
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.
        """
        return self.get(key, fn=lambda d: int(d))
