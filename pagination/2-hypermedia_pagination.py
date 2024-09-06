#!/usr/bin/env python3
"""
Hypermedia pagination for the baby names dataset.
This module implements a Server class to paginate a CSV dataset of popular
baby names and provides hypermedia pagination with metadata such as
page size, current page, next page, previous page, and total pages.
"""

import csv  # Import the csv module for reading CSV files
import math  # Import math for rounding calculations
from typing import Dict, List

# Dynamically import the function from the module with a leading number
index_range = __import__('0_simple_helper_function').index_range


class Server:
    """
    Server class to paginate a dataset of popular baby names.

    Attributes:
        DATA_FILE (str): The name of the CSV file containing the dataset.
        __dataset (List[List]): Cached version of the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.
        The dataset is initially set to None to indicate that it hasn't been
        loaded yet.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file if it hasn't been loaded
        already.

        Returns:
            List[List]: A list of lists where each list contains data for a
                        single row in the CSV file, excluding the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of data from the dataset.

        Args:
            page (int): The page number to return (1-indexed).
                        Defaults to 1.
            page_size (int): The number of rows per page. Defaults to 10.

        Returns:
            List[List]: A list of rows for the specified page, or an empty
                        list if the page is out of range.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return paginated data along with meta-information.

        Args:
            page (int): The page number to return (1-indexed).
                        Defaults to 1.
            page_size (int): The number of rows per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing the following keys:
                - page_size (int): The number of rows in the current page.
                - page (int): The current page number.
                - data (List[List]): The list of rows for the current page.
                - next_page (int, None): The next page number, or None if
                                         there is no next page.
                - prev_page (int, None): The previous page number, or None if
                                         there is no previous page.
                - total_pages (int): The total number of pages in the dataset.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
