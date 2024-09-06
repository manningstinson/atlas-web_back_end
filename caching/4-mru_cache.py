#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that uses the Most Recently Used caching algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None  # Track the most recently used key

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

            # If we exceed MAX_ITEMS, discard the most recently used key
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            # Update the most recently used key
            self.last_key = key

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None

        if key in self.cache_data:
            # Update the most recently used key
            self.last_key = key
            return self.cache_data[key]

        return None
