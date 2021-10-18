#!/usr/bin/env python3
"""Python Module"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integersand floats, and returns their sum as a float"""
    return sum(mxd_lst)
