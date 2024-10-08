#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List

# Dynamically import the function from the module with a leading number
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class with deletion-resilient hypermedia pagination."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return data with deletion-resilient pagination."""
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "Invalid index"
        assert isinstance(page_size, int) and page_size > 0, \
            "Invalid page size"

        indexed_data = self.indexed_dataset()
        data = []
        next_index = index

        for i in range(page_size):
            while next_index not in indexed_data:
                next_index += 1
            data.append(indexed_data[next_index])
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
