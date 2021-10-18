#!/usr/bin/env python3
"""Python Module"""
from typing import Union, Tuple


def to_kv(k: str, v:Union[int, float]) -> Tuple[str, float]:
    """Takes a string and integer or float and returns a tuple"""
    return(k, v*v)
