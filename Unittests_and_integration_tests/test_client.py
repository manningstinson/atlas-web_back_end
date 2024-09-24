#!/usr/bin/env python3
"""Test cases for client.py"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), {"name": org_name})
        mock_get_json.assert_called_once_with
        (f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url returns correct URL"""
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns correct list"""
        mock_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license works as expected"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": TEST_PAYLOAD[0][0],
     "repos_payload": TEST_PAYLOAD[0][1],
     "expected_repos": TEST_PAYLOAD[0][2],
     "apache2_repos": TEST_PAYLOAD[0][3]},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class with patched requests.get"""
        cls.get_patcher = patch('requests.get', autospec=True)
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if "orgs" in url:
                return Mock(json=lambda: cls.org_payload)
            elif "repos" in url:
                return Mock(json=lambda: cls.repos_payload)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patched requests.get"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method in an integration test"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
