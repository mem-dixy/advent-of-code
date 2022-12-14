

import io
import enum
import typing
import types

NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

ARROW = NONE.join([SPACE, HYPHEN_MINUS, GREATER_THAN_SIGN, SPACE])
FILE = "input.txt"
# FILE = "sample.txt"
INFINITY = 9876543210


class Point():
    def __init__(self, index_x, index_y):
        self.index_x = int(index_x)
        self.index_y = int(index_y)

    def __repr__(self):
        return F"({self.index_x}, {self.index_y})"

    def __str__(self):
        return F"({self.index_x}, {self.index_y})"


sand = Point(500, 0)

def scan_cave():
    done = []
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
            done.append(row)
    return done

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

rock = scan_cave()
print(rock)


bounds = map_bounds(rock, sand)
size = bounds
def map_display(rocks):
    string = io.StringIO()
    for index_y in range(size):
        for index_x in range(size):
            string.write("x")
        string.write(LINE_FEED)
    print(string.getvalue())
