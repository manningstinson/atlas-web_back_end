#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))  # Should print the number of times store() has been called, starting with '1'

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))  # Should print '3' after the third call
