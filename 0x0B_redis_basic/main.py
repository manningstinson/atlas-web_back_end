#!/usr/bin/env python3
"""
Main file for testing the Cache class.
"""

from exercise import Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(f"Generated key: {key}")

local_redis = cache._redis
retrieved_data = local_redis.get(key)
print(f"Retrieved data: {retrieved_data}")
