import io

VISIBLE = "."
HIDDEN = "_"

TREE_HOUSE = "$"
PRETTY_TREES = "%"

grid = []
forest = []
scores = []
# 0 min 9 max
# 1 min 10 max

import enum

DOWN = "D"
LEFT = "L"
RIGHT = "R"
UP = "U"

class Direction(enum.Enum):
    down = "D"
    left = "L"
    right = "R"
    up = "U"

directions = {
    DOWN: 0,
    LEFT: 0,
    RIGHT: 0,
    UP: 0,
}


def find_maze_size():
    pass

# maze_size
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        for item in line.strip():
            number = int(item)
            grid.append(number)
            forest.append(HIDDEN)
            scores.append(0)

width = len(lines[0]) - 1
size = len(grid)
height = size // width

left = -1
right = + 1
up = -width
down = + width


def this_is_edge(index):
    row = index // width
    col = index % width

    north = row - 1 < 0
    south = row + 1 >= height
    east = col + 1 >= width
    west = col - 1 < 0
    return north or south or east or west





# all touching
# ***
# ***
# ***
#  diagonals have priority
