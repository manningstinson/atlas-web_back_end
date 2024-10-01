#!/usr/bin/env python3
"""
Main script to run the Cache and replay functionalities.
"""

from exercise import Cache

def main():
    # Create a cache instance
    cache = Cache()

    # Store some data
    cache.store("foo")
    cache.store("bar")
    cache.store("egg")
    cache.store("eggsperiment")

    # Replay the calls to the store method
    cache.replay(cache.store)

if __name__ == "__main__":
    main()
