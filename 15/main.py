import io
import enum
import typing
import types


from setup import load

fish = set()
dog = "Sensor at x=, y=: closest beacon is at x=, y="
for name in dog:
    fish.add(name)

turtle = list(fish)
turtle.sort()

frog = "".join(turtle)

print(F"[{frog}]")

load()
