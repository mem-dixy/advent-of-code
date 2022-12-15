import io

SENSOR = "S"
BEACON = "B"
NETHER = "."
SCANED = "#"

NONE = str()
LINE_FEED = chr(0x000A)

FILE = "input.txt"
# FILE = "sample.txt"

JUNK = " ,:=Sabceilnorstxy"

INFINITY = 9876543210123456789

SENSOR = "S"
BEACON = "B"
NETHER = "."
SCANED = "#"


class Point():
    def __init__(self, index_x, index_y):
        self.index_x = int(index_x)
        self.index_y = int(index_y)

    def __repr__(self):
        return F"({self.index_x}, {self.index_y})"

    def __str__(self):
        return F"({self.index_x}, {self.index_y})"


def map_scan():
    sensors = []
    beacons = []
    with open(FILE) as file:
        read = file.read().strip()
        data = read.split(LINE_FEED)
        for line in data:
            points = line.replace(":", ",").split(",")
            info = [point.strip(JUNK) for point in points]
            sensor = Point(info[0], info[1])
            beacon = Point(info[2], info[3])
            sensors.append(sensor)
            beacons.append(beacon)
    return (sensors, beacons)


def map_bounds(points, move):
    min_x = + INFINITY
    min_y = + INFINITY
    max_x = - INFINITY
    max_y = - INFINITY
    for point in points:
        min_x = min(min_x, point.index_x)
        min_y = min(min_y, point.index_y)
        max_x = max(max_x, point.index_x)
        max_y = max(max_y, point.index_y)
    wide = 1 + abs(min_x) + abs(max_x)
    tall = 1 + abs(min_y) + abs(max_y)
    width = max(wide, tall + tall + tall + tall + 1)
    height = tall
    push = wide - max_x
    lift = -move.index_y
    return (width, height, push, lift)


def point_resize(point, bounds):
    (width, height, push, lift) = bounds
    point.index_x += push
    point.index_y += lift


def map_resize(points, bounds):
    for point in points:
        point_resize(point, bounds)


def load(point):
    (sensors, beacons) = map_scan()
    points = sensors + beacons
    bounds = map_bounds(points, point)
    map_resize(sensors, bounds)
    map_resize(beacons, bounds)
    point_resize(point, bounds)
    return (sensors, beacons, bounds)


(sensors, beacons, bounds) = load(Point(0, 2000000))
# (sensors, beacons, bounds) = load(Point(0, 11))

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

done = [item for item in search if item == SENSOR or item == SCANED]

SENSOR = "S"
BEACON = "B"
NETHER = "."
SCANED = "#"
print(len([item for item in search if item == SENSOR]))
print(len([item for item in search if item == BEACON]))
print(len([item for item in search if item == NETHER]))
print(len([item for item in search if item == SCANED]))
count = len(done)
print(count)

# string = io.StringIO()
# for item in search:
#    string.write(item)
# print(string.getvalue())
# print("EXAMPLE INPUT")

# 5108328

# 5441371
# - 2
