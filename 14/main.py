

import io
import enum
import typing
import types

NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

ARROW = NONE.join([SPACE, HYPHEN_MINUS, GREATER_THAN_SIGN, SPACE])
FILE = "input.txt"
# FILE = "sample.txt"
INFINITY = 9876543210



from setup import load
from setup import Point


sand = Point(500, 0)
cave = load(sand)

print(cave)
