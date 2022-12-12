import io
import enum
import typing
import types


class Cell():
    def __init__(self, index, width):
        self.width = width
        self.index_x = index % width
        self.index_y = index // width

    def index(self):
        return self.index_y * self.width + self.index_x


class Agent(Cell):
    def down(self):
        self.index_y += 1

    def left(self):
        self.index_x -= 1

    def right(self):
        self.index_x += 1

    def up(self):
        self.index_y -= 1


class Direction(enum.Enum):
    east = enum.auto()
    north = enum.auto()
    south = enum.auto()
    west = enum.auto()


class Dimension():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = width * height


class Axis():
    @classmethod
    def clone(cls, axis):
        return cls(axis.point, axis.size)

    def index(self):
        return self.point

    def move(self, point):
        self.point += point

    def valid(self):
        return 0 <= self.point < self.size

    def __init__(self, point, size):
        self.point = point
        self.size = size


class Grid():
    @classmethod
    def clone(cls, grid):
        return cls(
            Axis.clone(grid.axis_x),
            Axis.clone(grid.axis_y),
        )

    def index(self):
        return self.axis_y.point * self.axis_x.size + self.axis_x.point

    def move(self, direction):
        match direction:
            case Direction.east:
                self.axis_x.move(+1)
            case Direction.north:
                self.axis_x.move(-self.axis_x.size)
            case Direction.east:
                self.axis_x.move(+self.axis_x.size)
            case Direction.west:
                self.axis_x.move(-1)

    def valid(self):
        return self.axis_x.valid() and self.axis_y.valid()

    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y

class Cell(Agent):
    def __init__(self, grid):

        self.grid = grid

    def move(self, direction):

        match direction:
            case Direction.east:

                self.index_x += 1
            case Direction.north:
                self.index_y -= 1
            case Direction.east:
                self.index_y += 1
            case Direction.west:
                self.index_x -= 1

    def move(self, direction):
        self.grid.move(direction)

    def neighbor(
        self,
        test: typing.Callable
    ) -> list[Direction]:

        item = Grid.clone(self.grid)
        path = []
        if
        Coordinate

        match direction:
            case Direction.east:
                self.index_x += 1
            case Direction.north:
                self.index_y -= 1
            case Direction.east:
                self.index_y += 1
            case Direction.west:
                self.index_x -= 1

class Cell(Agent):
    def __init__(self, grid):

        self.grid = grid

    def move(
        self,
        direction: Direction
    ) -> None:

        match direction:
            case Direction.east:
                self.index_x += 1
            case Direction.north:
                self.index_y -= 1
            case Direction.east:
                self.index_y += 1
            case Direction.west:
                self.index_x -= 1

    def move(
        self,
        direction: Direction
    ) -> None:

        match direction:
            case Direction.east:
                self.index_x += 1
            case Direction.north:
                self.index_y -= 1
            case Direction.east:
                self.index_y += 1
            case Direction.west:
                self.index_x -= 1

    def neighbor(
        self,
        test: typing.Callable
    ) -> list[Direction]:

        item = Grid.clone(self.grid)
        path = []
        if
        Coordinate

        match direction:
            case Direction.east:
                self.index_x += 1
            case Direction.north:
                self.index_y -= 1
            case Direction.east:
                self.index_y += 1
            case Direction.west:
                self.index_x -= 1


CLIMB_LIMIT = 1


data = None
with open("input.txt") as file:
    data = file.read()


def make_maze(data):
    data_split = data.split()
    width = len(data_split[0])
    height = len(data_split)
    axis_x = Axis(0, width)
    axis_y = Axis(0, height)
    maze = Grid(axis_x, axis_y)
    return maze


maze = make_maze(data)

data_lookup = [item for item in data if item.isalpha()]

player = Agent(data_lookup.index("S"), dimension.width)
goal = Cell(data_lookup.index("E"), dimension.width)


def elevation(letter):
    if letter == "S":
        letter = "a"
    if letter == "E":
        letter = "z"
    return ord(letter) - ord("a")


def climbable(here, goto):
    return here + CLIMB_LIMIT <= goto


heightmap = [elevation(item) for item in data_lookup]
distance = [None] * size
distance[player.index()] = 0


for round in range(size):

