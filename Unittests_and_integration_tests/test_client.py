#!/usr/bin/env python3
"""Test cases for client.py"""

import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Unit-test GithubOrgClient.public_repos"""
        # Mocking the value of _public_repos_url
        mock_repos_url.return_value = "http://example.com/repos"
        
        # Mocking the payload returned by get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        
        # Creating an instance of GithubOrgClient
        client = GithubOrgClient("google")
        
        # Calling the method to test
        repos = client.public_repos()
        
        # Assert that the list of repos is what we expect
        self.assertEqual(repos, ["repo1", "repo2"])
        
        # Test that the mocked _public_repos_url and get_json were called exactly once
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

