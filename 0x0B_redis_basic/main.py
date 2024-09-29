#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

# Store data
cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Should print b'1'

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))  # Should print b'3'
