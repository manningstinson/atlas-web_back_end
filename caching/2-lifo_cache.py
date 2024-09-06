#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ LRUCache that uses the Least Recently Used caching algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys_order.remove(key)
            self.keys_order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                oldest_key = self.keys_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Get an item by key """
        if key in self.keys_order:
            self.keys_order.remove(key)
            self.keys_order.append(key)
        return self.cache_data.get(key, None)
