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

ROOM = "."
ROCK = "#"
DROP = "+"
SAND = "o"
FLOW = "~"


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

        (min_x, max_x, min_y, max_y) = bounds

        width = 3 + max_x - min_x
        height = 3 + max_y - min_y
        size = width * height

        super().__init__(width, height)

        self.sand = Cell(self.grid)
        self.sand.goto(sand.index_x, sand.index_y)

        self.data = [None] * size

        self.draw = [ROOM] * size
        self.draw[self.sand.index()] = DROP

        self.valid = [True] * size
        self.valid[self.sand.index()] = None
        for index in range(size):
            cell = Cell.from_index(self.grid, index)

            g = cell.grid.axis_y.point == cell.grid.axis_y.size - 2

            a = cell.grid.axis_x.point <= 0
            b = cell.grid.axis_x.point >= cell.grid.axis_x.size - 1
            d = cell.grid.axis_y.point <= 0
            e = cell.grid.axis_y.point >= cell.grid.axis_y.size - 1
            if a or b or d or e:
                self.valid[cell.index()] = False
            if g and not a and not b:
                self.data[cell.index()] = True
                self.draw[cell.index()] = ROCK

    def paint(self, rock):
        for dirt in rock:
            start = None
            finish = None
            first = True
            for item in dirt:
                if first:
                    first = False
                    start = self.sand.clone()
                    start.goto(item.index_x, item.index_y)
                    self.data[start.index()] = True
                    self.draw[start.index()] = ROCK
                else:
                    finish = self.sand.clone()
                    finish.goto(item.index_x, item.index_y)
                    self.data[finish.index()] = True
                    self.draw[finish.index()] = ROCK

                    direction = start.face(finish)
                    while direction:
                        start.move(direction)
                        direction = start.face(finish)
                        self.data[start.index()] = True
                        self.draw[start.index()] = ROCK

    def collision(
        self,
        point: Cell
    ) -> list[bool]:
        """"""

        collisions = []
        directions = [
            Direction.NORTH,
            Direction.NORTHEAST,
            Direction.EAST,
            Direction.SOUTHEAST,
            Direction.SOUTH,
            Direction.SOUTHWEST,
            Direction.WEST,
            Direction.NORTHWEST,
        ]
        for direction in directions:
            cell = point.clone()
            cell.move(direction)
            collisions.append(self.data[cell.index()])

        return collisions

    def fall(
        self,
        cell: Cell
    ) -> Direction:
        """"""

        collisions = self.collision(cell)
        # north = collisions[0]
        # northeast = collisions[1]
        # east = collisions[2]
        southeast = collisions[3]
        south = collisions[4]
        southwest = collisions[5]
        # west = collisions[6]
        # northwest = collisions[7]

        if south is None:
            cell.move(Direction.SOUTH)
        elif southwest is None:
            cell.move(Direction.SOUTHWEST)
        elif southeast is None:
            cell.move(Direction.SOUTHEAST)
        else:
            self.data[cell.index()] = False
            self.draw[cell.index()] = SAND
            return None

        return self.valid[cell.index()]

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

    min_y += 0
    max_y += 2

    tall = max_y - min_y

    min_x = min(min_x, sand.index_x - tall)
    max_x = max(max_x, sand.index_x + tall)

    return (min_x, max_x, min_y, max_y)


def point_resize(point, bounds):
    (min_x, max_x, min_y, max_y) = bounds
    point.index_x = 1 + point.index_x - min_x
    point.index_y = 1 + point.index_y - min_y
    return point


def map_resize(rock, bounds):
    for dirt in rock:
        for item in dirt:
            point_resize(item, bounds)
    return rock


def load(sand):
    rock = map_scan()
    bounds = map_bounds(rock, sand)
    rock = map_resize(rock, bounds)
    sand = point_resize(sand, bounds)
    cave = Cave(bounds, sand)
    cave.paint(rock)
    return cave
