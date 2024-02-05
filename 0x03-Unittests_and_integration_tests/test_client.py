#!/usr/bin/env python3
"""test cases for the client module"""

from unittest import TestCase
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json):
        """Test the public_repos method of GithubOrgClient."""
        test_payload = [
                {'name': 'name1'},
                {'name': 'name2'}
                ]
        mocked_get_json.return_value = test_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_property:
            mocked_property.return_value = 'za url'
            name_list = GithubOrgClient('random name').public_repos()
        self.assertEqual(['name1', 'name2'], name_list)
        mocked_get_json.assert_called_once_with('za url')

    @parameterized.expand([
        ({"name": "repo1", "license": {"key": "my_license"}},
         "my_license", True),
        ({"name": "repo2", "license": {"key": "other_license"}},
         "my_license", False)
        ])
    def test_has_license(self, repo, licence, expected):
        """Test the has_license static method of GithubOrgClient."""
        self.assertEqual(GithubOrgClient.has_license(repo, licence), expected)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the class for integration testing."""
        def side(url):
            """Side effect function for requests.get mock."""
            repo = []
            mock_response = Mock()
            for payload in TEST_PAYLOAD:
                if url == payload[0]["repos_url"]:
                    repo = payload[1]
                    break
            mock_response.json.return_value = repo
            return mock_response
        cls.get_patcher = patch('requests.get', side_effect=side)
        cls.org_patcher = patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock,
                return_value=cls.org_payload)
        cls.get_patcher.start()
        cls.org_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after integration testing."""
        cls.get_patcher.stop()
        cls.org_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method without specifying a license."""
        inst = GithubOrgClient('google/repos')
        self.assertEqual(inst.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with a specified license."""
        inst = GithubOrgClient('google/repos')
        self.assertEqual(inst.public_repos(license="apache-2.0"),
                         self.apache2_repos)
