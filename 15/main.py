import io
import enum
import typing
import types


from setup import load
from setup import Point

SENSOR = "S"
BEACON = "B"
NETHER = "."
SCANED = "#"


(sensors, beacons, bounds) = load(Point(0, 9))
# (sensors, beacons, bounds) = load(Point(0, 2000000))

(width, height, push, lift) = bounds
search = [NETHER] * width

count = 0
line = 0
friends = zip(sensors, beacons)
for (sensor, beacon) in friends:
    line += 1
    distance_x = sensor.index_x - beacon.index_x
    distance_y = sensor.index_y - beacon.index_y
    length = abs(distance_x) + abs(distance_y)
    span = length - abs(sensor.index_y)
    if span >= 0:
        count = 0
        start = max(sensor.index_x - span, 0)
        haltt = min(sensor.index_x + span, width)
        for index in range(start, haltt + 1):
            search[index] = SCANED
            count += 1
    if sensor.index_y == 0:
        search[sensor.index_x] = SENSOR
    if beacon.index_y == 0:
        search[beacon.index_x] = BEACON

done = [item for item in search if item in [SENSOR, SCANED]]
count = len(done)
print(count)

# string = io.StringIO()
# for item in search:
#    string.write(item)
# print(string.getvalue())
# print("EXAMPLE INPUT")
