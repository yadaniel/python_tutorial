#!/cygdrive/c/Python37/python

import functools as ft
import platform as p
from typing import Set, List, Dict, Tuple, Optional, Sequence, NewType, Any, Iterable, Union, Callable

# mypy=OK => reports error
# mypy=NOK => mypy does not report error

Meter = NewType("Meter", float)
Filename = NewType("Filename", str)

n: int = 0
s: str = "test"
# sx: str = 1   # mypy=OK, pyright=OK

xs: Sequence[int] = [1,2,3,4]
ys: Sequence[str] = "1,2,3,4"
zs: Dict[str,int] = {}      # empty dict
ps: Set[Any] = {()}         # empty set
qs: Set[int] = {1,2,3,4}    # set

xs_: Iterable[int] = [1,2,3,4]
xs__: Iterable[float] = [1,2,3,4,5.0]
# xs__: Iterable[int|float] = [1.0,2,3,4]  # requires python 3.10
ys_: Iterable[str] = "1,2,3,4"
zs_: Iterable[str] = {"1":1, "2":2, "3":3, "4":4}
qs_: Iterable[int] = {1,2,3,4}

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

NoneType = type(None)
def tryOpen(f: Filename, b: bool) -> Union[str, NoneType]:
    if b:
        return "data"
    else:
        return None

def zipWithFunc(xs: List[int], ys: List[int], f: Callable[[int,int],int]) -> List[Tuple[int,int,int]]:
    z = []
    for x,y in zip(xs,ys):
        z.append((x,y,f(x,y)))
    return z

def main():
    print("in main")
    print(p.version())
    print(makesum([1,2,3,4]))
    print(lookup({"one":1}, "one"))
    print(lookup({"one":1}, "two"))
    # tryOpen("./readme", True)   # mypy:0 issues, pyright: cannot assign Literal to Filename
    tryOpen(Filename("./readme"), True)
    print(zipWithFunc([1,2,3],[4,5,6,7], lambda x,y: x+y))
    print(zipWithFunc([1,2,3],[4,5,6,7], lambda x,y: x*y))

if __name__ == "__main__":
    print(__file__,  __name__)
    main()

