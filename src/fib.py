#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import lru_cache

@lru_cache
def fib(a):
    if a == 0 or a == 1:
        return 0
    return fib(a-1) + fib(a-2)
