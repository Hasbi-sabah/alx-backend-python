#!/usr/bin/env python3
""" Module for the function safe_first_element """

from typing import Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Any | None:
    """
    type-annotated function element_length that takes an iterable
    of sequences as argument and returns a list of tuples,
    first element is iterable and second element is int
    """
    if lst:
        return lst[0]
    else:
        return None
