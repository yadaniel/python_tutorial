#!/cygdrive/c/Python37/python

import functools as ft
import platform as p
from typing import List

n: int = 0
s: str = "test"

def incr(n: int) -> int:
    return n+1

def makesum(xs: List[int]) -> int:
    return ft.reduce(lambda x,y: x+y, xs)

def main():
    print("in main")
    print(p.version())
    print(makesum([1,2,3,4]))


if __name__ == "__main__":
    print(__file__,  __name__)
    main()

