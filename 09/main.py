import io

grid = []
forest = []
scores = []
# 0 min 9 max
# 1 min 10 max

import enum
import dataclasses
import types
import typing


EMPTY = "."
VISITED = "#"

HEAD = "H"
TAIL = "T"
BOTH = "S"

DOWN = "D"
LEFT = "L"
RIGHT = "R"
UP = "U"

@dataclasses.dataclass
class Direction():
    direction: str
    steps: int


def parse_input(
) -> list[Direction]:
    lines = []
    with open("input.txt") as file:
        readlines = file.readlines()
        for line in readlines:
            row = line.strip().split()
            if row:
                direction = Direction(row[0], int(row[1]))
                lines.append(direction)
    return lines

def find_maze_limit(
    lines: list[Direction]
) -> typing.Dict[str, int]:
    directions = {
        DOWN: 0,
        LEFT: 0,
        RIGHT: 0,
        UP: 0,
    }
    for line in lines:
        directions[line.direction] += line.steps
    return directions

def find_maze_size(
    directions: typing.Dict[str, int]
) -> typing.Tuple[int]:
    width = 1 + directions[LEFT] + directions[RIGHT]
    height = 1 + directions[DOWN] + directions[UP]
    return (width, height, directions[LEFT], directions[UP])


# generate maze
lines = parse_input()
directions = find_maze_limit(lines)
(width, height, position_x, position_y) = find_maze_size(directions)
maze = []
trail = []
for index_y in range(height):
    for index_x in range(width):
        index = index_y * width + index_x
        maze.append(EMPTY)
        trail.append(False)

index = position_y * width + position_x
maze[index] = BOTH
trail[index] = True

left = -1
right = + 1
up = -width
down = + width




def print_visited():
    global trail

    visited = 0
    for cell in trail:
        if cell:
            visited += 1
    print(visited)

def print_maze(draw_maze, draw_trail):
    global maze
    global trail

    string = io.StringIO()
    for index_y in range(height):
        for index_x in range(width):
            index = index_y * width + index_x
            draw_the_maze = str(maze[index])
            draw_the_trail = VISITED if trail[index] else EMPTY

            if draw_maze and draw_trail:
                if maze[index] != EMPTY:
                    draw = draw_the_maze
                else:
                    draw = draw_the_trail
            elif draw_maze:
                draw = draw_the_maze
            elif draw_trail:
                draw = draw_the_trail
            else:
                draw = ""
            string.write(draw)
        string.write("\n")
    print(string.getvalue())

head_index_x = position_x
head_index_y = position_y
tail_index_x = position_x
tail_index_y = position_y
for line in lines:
    direction = line.direction
    steps = line.steps
    for step in range(steps):
        head_index = head_index_y * width + head_index_x
        tail_index = tail_index_y * width + tail_index_x

        head_goto = head_index

        match direction:
            case "D":
                head_goto += down
                head_index_y += 1
            case "L":
                head_goto += left
                head_index_x -= 1
            case "R":
                head_goto += right
                head_index_x += 1
            case "U":
                head_goto += up
                head_index_y -= 1

        maze[head_goto] = BOTH if maze[head_index] == TAIL else HEAD
        maze[head_index] = TAIL if maze[head_index] == BOTH else EMPTY


print_maze(True, True)
print_visited()
# all touching
# ***
# ***
# ***
#  diagonals have priority
