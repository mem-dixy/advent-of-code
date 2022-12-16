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

offset = 5000000
width = offset * 4

find = 2000000
# find = 9

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


def map_convert():
    arena = []
    (sensors, beacons) = map_scan()
    friends = zip(sensors, beacons)
    for friend in friends:
        (sensor, beacon) = friend
        distance_x = sensor.index_x - beacon.index_x
        distance_y = sensor.index_y - beacon.index_y
        length = abs(distance_x) + abs(distance_y)
        arena.append((sensor.index_x, sensor.index_y, length))
    return arena


arena = map_convert()
print(arena)


# 5108328 too low
# 5441371 too low?
# 5564017
# 6448357 too high
