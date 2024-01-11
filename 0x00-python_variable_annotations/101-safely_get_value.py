#!/usr/bin/env python3
""" Module for the function safely_get_value """

from typing import Mapping, Any, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """ type-annotated function safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
