import io
import enum
import typing
import types


from setup import load
from setup import Point
fish = set()
dog = "Sensor at x=, y=: closest beacon is at x=, y="
for name in dog:
    fish.add(name)


crash = [0] * 4000000
turtle = list(fish)
turtle.sort()

frog = "".join(turtle)

print(F"[{frog}]")

(sensors, beacons, bounds) = load(Point(0, 10))
# (sensors, beacons, bounds) = load(Point(0, 2000000))

(width, height, push, lift) = bounds
search = [False] * width


friends = zip(sensors, beacons)
for (sensor, beacon) in friends:
    distance_x = sensor.index_x - beacon.index_x
    distance_y = sensor.index_y - beacon.index_y
    length = abs(distance_x) + abs(distance_y)
    span = length - abs(sensor.index_y)
    if span > 0:
        start = max(sensor.index_x - span, 0)
        haltt = max(sensor.index_x + span, width)
        for index in range(start, haltt):
            search[index] = True



string = io.StringIO()
for item in search:
    string.write("#" if item else ".")

print(string.getvalue())
print("EXAMPLE INPUT")
