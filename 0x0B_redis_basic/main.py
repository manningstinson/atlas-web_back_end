#!/usr/bin/env python3
"""
Main file for testing Cache class and decorators.
"""

from exercise import Cache

cache = Cache()

# Test storing data
s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

# Fetch input and output history from Redis
inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

print(f"inputs: {inputs}")
print(f"outputs: {outputs}")
