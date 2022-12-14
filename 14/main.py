import io
import enum
import typing
import types


from setup import load
from setup import Point


sand = Point(500, 0)
cave = load(sand)

print(cave)
