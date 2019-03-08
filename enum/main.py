#!/cygdrive/c/Python37/python

import sys
from enum import Enum, auto 

print("using interperter = %s" % sys.executable)

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    rgb = (0,0,0)
    RGB = 100

print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)

r = Color.RED
g = Color.GREEN
b = Color.BLUE
print(r,g,b)

# color = Color[input()]    # accepts case-sensitive RED, YELLOW, BLUE
# color = Color(100)        # accepts numerical value and sets RGB

inp = input()
try:
    print("try enum values")
    color = Color(int(inp)) # (...) operator
except:
    try:
        print("try enum labels")
        color = Color[inp]  # [...] operator
    except:
        print("nothing")
        sys.exit()

if color == Color.RED:
    print("red")
elif color  == Color.GREEN:
    print("green")
elif color == Color.BLUE:
    print("blue")
elif color == Color.RGB:
    print("RGB")
else:
    print("unknown")


