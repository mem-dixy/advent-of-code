import io
import enum
import typing
import types


from setup import load
from setup import Point


sand = Point(500, 0)
cave = load(sand)



count = 0
while False:
    cell = cave.sand.clone()
    falling = True
    while falling:
        falling = cave.fall(cell)
    if falling is False:
        break
    count += 1
    if cell == cave.sand:
        break

print(cave)

print(count)
