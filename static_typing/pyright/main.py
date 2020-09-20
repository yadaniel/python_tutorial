#!/cygdrive/c/Python37/python

import functools as ft
import platform as p
from typing import Set, List, Dict, Tuple, Optional, Sequence, NewType, Any

# mypy=OK => reports error
# mypy=NOK => mypy does not report error

n: int = 0
s: str = "test"
# sx: str = 1   # mypy=OK, pyright=OK

xs: Sequence[int] = [1,2,3,4]
ys: Sequence[str] = "1,2,3,4"
# zs: Sequence[str] = {}      # empty dict
ps: Set[Any] = {()}         # empty set
qs: Set[int] = {1,2,3,4}    # set

def incr(n: int) -> int:
    return n+1

def makesum(xs: List[int]) -> int:
    return ft.reduce(lambda x,y: x+y, xs)

def first(x: Tuple[int,int]) -> int:
    return x[0]

def second(x: Tuple[int,int]) -> int:
    return x[1]
    # return x[2]     # mypy=OK, pyright=NOK

def lookup(d: Dict[str,int], key: str) -> Optional[int]:
    if key in d.keys():
        return d[key]
    return None

def main():
    print("in main")
    print(p.version())
    print(makesum([1,2,3,4]))
    print(lookup({"one":1}, "one"))
    print(lookup({"one":1}, "two"))


if __name__ == "__main__":
    print(__file__,  __name__)
    main()

