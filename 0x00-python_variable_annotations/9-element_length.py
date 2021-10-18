#!/usr/bin/env python3
"""Python Module"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function"""
    return [(i, len(i)) for i in lst]
