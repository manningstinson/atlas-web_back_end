#!/usr/bin/env python3
"""
This module demonstrates the usage of the Cache class and its replay method.
"""

from exercise import Cache

if __name__ == "__main__":
    cache = Cache()
    
    # Store some values
    cache.store("foo")
    cache.store("bar")
    cache.store("egg")
    cache.store("eggsperiment")

    # Replay the calls to the store method
    cache.replay(cache.store)
