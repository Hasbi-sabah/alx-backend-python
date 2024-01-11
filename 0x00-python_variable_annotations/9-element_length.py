#!/usr/bin/env python3
""" Module for the function element_length """

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    type-annotated function element_length that takes an iterable
    of sequences as argument and returns a list of tuples,
    first element is iterable and second element is int
    """
    return [(i, len(i)) for i in lst]
