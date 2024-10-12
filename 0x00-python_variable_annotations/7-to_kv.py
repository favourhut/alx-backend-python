#!/usr/bin/env python3
"""Complex types - string and int/float to tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """Return a tuple where the first element is the string k and
    the second element is the square of v (int or float)"""

    return (k, float(v ** 2))
