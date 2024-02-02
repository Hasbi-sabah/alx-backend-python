#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock


class TestGithubOrgClient(TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name: str, mocked_get_json: MagicMock):
        """Test the org method of GithubOrgClient."""
        GithubOrgClient(org_name).org
        mocked_get_json.assert_called_once_with(
            "https://api.github.com/orgs/" + org_name
        )
