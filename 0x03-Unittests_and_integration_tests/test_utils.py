#!/usr/bin/env python3
"""test cases for the utils module"""

from typing import Mapping, Sequence, Dict, Any
from utils import access_nested_map, get_json, memoize
from unittest import TestCase
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            n_map: Mapping,
            path: Sequence,
            expected: Any):
        """Test successful access_nested_map."""
        self.assertEqual(access_nested_map(n_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self,
            n_map: Mapping,
            path: Sequence):
        """Test expected exceptions during access_nested_map."""
        with self.assertRaises(KeyError):
            access_nested_map(n_map, path)


class TestGetJson(TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(
            self,
            url: str,
            test_payload: Dict):
        """Test the get_json function by mocking the requests.get method."""
        mocked_response = Mock()
        mocked_response.json.return_value = test_payload
        with patch('requests.get', return_value=mocked_response) as mocked_get:
            output = get_json(url)
        mocked_get.assert_called_once_with(url)
        self.assertEqual(output, test_payload)


class TestMemoize(TestCase):
    """Test cases for the memoize decorator."""
    def test_memoize(self):
        """Test the memoize decorator on a property by mocking a_method."""
        class TestClass:
            """Dummy class for testing."""
            def a_method(self) -> int:
                """Mocked method for testing purposes."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Property under test using the memoize decorator."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked_method:
            mocked_method.return_value = 42
            dummy = TestClass()
            res1 = dummy.a_property
            res2 = dummy.a_property

        dummy = TestClass()
        res1 = dummy.a_property
        res2 = dummy.a_property

        mocked_method.assert_called_once()
        self.assertEqual(res1, 42)
        self.assertEqual(res2, 42)
