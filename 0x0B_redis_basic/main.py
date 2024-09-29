#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

# Store some data
cache.store("foo")
cache.store("bar")
cache.store(42)

# Replay the method call history
cache.replay(cache.store)
