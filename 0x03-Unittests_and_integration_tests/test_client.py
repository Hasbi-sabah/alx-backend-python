#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org_name: str, mocked_get_json: MagicMock):
        """Test the org method of GithubOrgClient."""
        inst = GithubOrgClient(org_name)
        inst.org
        mocked_get_json.assert_called_once_with(
            inst.ORG_URL.format(org=org_name)
        )

    @patch('client.GithubOrgClient.org', return_value={"repos_url": 'url'})
    def test_public_repos_url(self, mocked_org):
        """Test the _public_repos_url property of GithubOrgClient."""
        inst = GithubOrgClient('random org url')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = mocked_org.return_value["repos_url"]
            repo_url = inst._public_repos_url
        self.assertEqual('url', repo_url)
