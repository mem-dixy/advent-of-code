NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

ARROW = NONE.join([SPACE, HYPHEN_MINUS, GREATER_THAN_SIGN, SPACE])
FILE = "input.txt"
# FILE = "sample.txt"

from maze import Maze
from maze import Cell

class Point():
    def __init__(self, index_x, index_y):
        self.index_x = int(index_x)
        self.index_y = int(index_y)

    def __repr__(self):
        return F"({self.index_x}, {self.index_y})"

    def __str__(self):
        return F"({self.index_x}, {self.index_y})"




class Cave(Maze):
    def __init__(self, bounds, sand):

        (size, min_x, max_x, min_y, max_y) = bounds

        width = max_x
        height = max_y
        size = width * height

        super().__init__(width, height)

        self.sand = Cell(self.grid)
        self.sand.goto(sand.index_x, sand.index_y)

        self.visited = [None] * size

        self.draw = ["X"] * size


    def __str__(
        self,
    ) -> str:
        """"""

        return super().__str__()


def map_scan():
    rock = []
    with open(FILE) as file:
        read = file.read().strip()
        data = read.split(LINE_FEED)
        for line in data:
            replace = line.replace(ARROW, SPACE)
            split = replace.split(SPACE)
            row = []
            for item in split:
                value = item.split(COMMA)
                point = Point(*value)
                row.append(point)
            rock.append(row)
    return rock

def map_bounds(rock, sand):
    min_x = sand.index_x
    min_y = sand.index_y
    max_x = sand.index_x
    max_y = sand.index_y
    for dirt in rock:
        for item in dirt:
            index_x = item.index_x
            index_y = item.index_y
            min_x = min(min_x, index_x)
            min_y = min(min_y, index_y)
            max_x = max(max_x, index_x)
            max_y = max(max_y, index_y)
    size_x = max_x - min_x
    size_y = max_y - min_y
    size = max(size_x, size_y) + 2
    return (size, min_x, max_x, min_y, max_y)

def point_invert(point, bounds):
    (size, min_x, max_x, min_y, max_y) = bounds
    point.index_x -= min_x
    point.index_y = max_y - point.index_y - min_y
    return point

def map_invert(rock, bounds):
    (size, min_x, max_x, min_y, max_y) = bounds
    for dirt in rock:
        for item in dirt:
            point_invert(item, bounds)
    return rock

def load(sand):
    rock = map_scan()
    bounds = map_bounds(rock, sand)
    rock = map_invert(rock, bounds)
    sand = point_invert(sand, bounds)
    cave = Cave(bounds, sand)
    return cave
