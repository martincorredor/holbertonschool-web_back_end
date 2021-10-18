#!/usr/bin/env python3
"""Python Module"""


def sum_list(input_list: list[float]) -> float:
    """takes a list of floats and return their sums as a float"""
    suma: float = 0
    for i in input_list:
        suma = suma + i
    return suma
