#!/usr/bin/env python3
"""Python Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns a function that multiplies"""
    def toCall(num: float) -> float:
        """function that return the multiplies"""
        return num*multiplier
    return toCall
