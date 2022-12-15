from maze import Direction
from maze import Cell
from maze import Maze
NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

ARROW = NONE.join([SPACE, HYPHEN_MINUS, GREATER_THAN_SIGN, SPACE])
FILE = "input.txt"
# FILE = "sample.txt"

JUNK = " ,:=Sabceilnorstxy"

INFINITY = 9876543210

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
    width = max(wide, tall + tall + 1)
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

