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
FILE = "sample.txt"

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


def map_bounds(points):
    min_x = + INFINITY
    min_y = + INFINITY
    max_x = - INFINITY
    max_y = - INFINITY
    for point in points:
        min_x = min(min_x, point.index_x)
        min_y = min(min_y, point.index_y)
        max_x = max(max_x, point.index_x)
        max_y = max(max_y, point.index_y)
    width = 1 + max_x - min_x
    height = 1 + max_y - min_y
    push = -min_x
    lift = -min_y
    return (width, height, push, lift)


def point_resize(point, bounds):
    (width, height, push, lift) = bounds
    point.index_x += push
    point.index_y += lift


def map_resize(points, bounds):
    for point in points:
        point_resize(point, bounds)


def load():
    (sensors, beacons) = map_scan()
    points = sensors + beacons
    bounds = map_bounds(points)
    map_resize(points, bounds)

#    cave = Cave(bounds, sand)
#    return cave

load()
