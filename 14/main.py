import io
import enum
import typing
import types


from setup import load
from setup import Point


sand = Point(500, 0)
cave = load(sand)

cell = cave.sand.clone()
cell.goto(2, 6)
cave.draw[cell.index()] = "%"
collision = cave.collision(cell)
print(collision)


event = 4
for turn in range(event):
    cell = cave.sand.clone()
    falling = True
    while falling:
        falling = cave.fall(cell)

print(cave)
