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



class Tile():
    def __init__(self, width, height, position_x, position_y):
        self.width = width
        self.height = height
        self.index_x = position_x
        self.index_y = position_y

    def index(self):
        return self.index_y * self.width + self.index_x

    def draw(self, grid, shape):
        grid[self.index()] = shape

    def down(self):
        self.index_y += 1

    def left(self):
        self.index_x -= 1

    def right(self):
        self.index_x += 1

    def up(self):
        self.index_y -= 1



class Head(Tile):
    def move(self, direction):
        match direction:
            case "D":
                self.down()
            case "L":
                self.left()
            case "R":
                self.right()
            case "U":
                self.up()

class Tail(Tile):
    def move(self, goto):
        distance_x = abs(goto.index_x - self.index_x)
        distance_y = abs(goto.index_y - self.index_y)
        distance = distance_x + distance_y

        if distance == 2 and distance_x != distance_y:
            if goto.index_x > self.index_x:
                self.right()
            if goto.index_x < self.index_x:
                self.left()
            if goto.index_y > self.index_y:
                self.down()
            if goto.index_y < self.index_y:
                self.up()

        if distance == 3 and goto.index_y > self.index_y:
            if goto.index_x > self.index_x:
                self.down()
                self.right()
            if goto.index_x < self.index_x:
                self.down()
                self.left()

        if distance == 3 and goto.index_y < self.index_y:
            if goto.index_x > self.index_x:
                self.up()
                self.right()
            if goto.index_x < self.index_x:
                self.up()
                self.left()



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


def find_maze_size(
    directions: typing.Dict[str, int]
) -> typing.Tuple[int]:
    index_x = 0
    index_y = 0
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for line in lines:
        steps = line.steps
        match line.direction:
            case "D":
                index_y += steps
            case "L":
                index_x -= steps
            case "R":
                index_x += steps
            case "U":
                index_y -= steps

        min_x = min(min_x, index_x)
        max_x = max(max_x, index_x)
        min_y = min(min_y, index_y)
        max_y = max(max_y, index_y)

    width = 1 + abs(min_x) + max_x
    height = 1 + abs(min_y) + max_y
    return (width, height, abs(min_x), abs(min_y))


# generate maze
lines = parse_input()
directions = find_maze_size(lines)
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



head = Head(width, height, position_x, position_y)
tail_1 = Tail(width, height, position_x, position_y)
tail_2 = Tail(width, height, position_x, position_y)
tail_3 = Tail(width, height, position_x, position_y)
tail_4 = Tail(width, height, position_x, position_y)
tail_5 = Tail(width, height, position_x, position_y)
tail_6 = Tail(width, height, position_x, position_y)
tail_7 = Tail(width, height, position_x, position_y)
tail_8 = Tail(width, height, position_x, position_y)
tail_9 = Tail(width, height, position_x, position_y)

for line in lines:
    direction = line.direction
    steps = line.steps
    for step in range(steps):

        tail_9.draw(maze, EMPTY)
        tail_8.draw(maze, EMPTY)
        tail_7.draw(maze, EMPTY)
        tail_6.draw(maze, EMPTY)
        tail_5.draw(maze, EMPTY)
        tail_4.draw(maze, EMPTY)
        tail_3.draw(maze, EMPTY)
        tail_2.draw(maze, EMPTY)
        tail_1.draw(maze, EMPTY)
        head.draw(maze, EMPTY)

        head.move(direction)
        tail_1.move(head)
        tail_2.move(tail_1)
        tail_3.move(tail_2)
        tail_4.move(tail_3)
        tail_5.move(tail_4)
        tail_6.move(tail_5)
        tail_7.move(tail_6)
        tail_8.move(tail_7)
        tail_9.move(tail_8)

        tail_9.draw(maze, "9")
        tail_8.draw(maze, "8")
        tail_7.draw(maze, "7")
        tail_6.draw(maze, "6")
        tail_5.draw(maze, "5")
        tail_4.draw(maze, "4")
        tail_3.draw(maze, "3")
        tail_2.draw(maze, "2")
        tail_1.draw(maze, "1")
        head.draw(maze, HEAD)

        trail[tail_9.index()] = True

        print_maze(True, False)


print_maze(False, True)
print_visited()
# all touching
# ***
# ***
# ***
#  diagonals have priority
