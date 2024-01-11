#!/usr/bin/env python3
""" Module for the function to_kv """

from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    type-annotated function to_kv that takes a string k and an
    int OR float v as arguments and returns a tuple.
    """
    return (k, v ** 2)
