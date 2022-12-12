import io
import enum
import typing
import types



class Agent():
    def __init__(self, index, width):
        self.width = width
        self.index_x = index % width
        self.index_y = index // width

    def index(self):
        return self.index_y * self.width + self.index_x

    def down(self):
        self.index_y += 1

    def left(self):
        self.index_x -= 1

    def right(self):
        self.index_x += 1

    def up(self):
        self.index_y -= 1

class Dimension():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = width * height
        ##


class Direction(enum.Enum):
    east = enum.auto()
    north = enum.auto()
    south = enum.auto()
    west = enum.auto()


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
    @classmethod
    def from_index(cls, grid, index):
        width = grid.axis_x.size
        height = grid.axis_y.size
        index_x = index % width
        index_y = index // width
        return cls(
            Grid(
                Axis(index_x, width),
                Axis(index_y, height),
            )
        )

    @classmethod
    def clone(cls, grid):
        return cls(
            Axis.clone(grid.axis_x),
            Axis.clone(grid.axis_y),
        )

    def __init__(self, grid):
        self.grid = grid

    def move(self, direction):
        self.grid.move(direction)

    def step(self, direction):
        grid = Grid.clone(self.grid)
        grid.move(direction)
        return grid if grid.valid() else None

    def neighbor(self, test):
        grid = []
        grid.append(self.step(Direction.east))
        grid.append(self.step(Direction.north))
        grid.append(self.step(Direction.south))
        grid.append(self.step(Direction.west))
        return filter(None, grid)



def elevation(letter):
    if letter == "S":
        letter = "a"
    if letter == "E":
        letter = "z"
    return ord(letter) - ord("a")

class Maze(Agent):

    def __init__(self, data):

        data_split = data.split()
        width = len(data_split[0])
        height = len(data_split)
        axis_x = Axis(0, width)
        axis_y = Axis(0, height)
        grid = Grid(axis_x, axis_y)

        self.grid = grid
        self.heightmap = []
        self.draw = []
        self.extra = []
        self.distance = []

        data_lookup = [item for item in data if item.isalpha()]

        self.start = Agent(data_lookup.index("S"), width)
        self.finish = Agent(data_lookup.index("E"), width)

        heightmap = [elevation(item) for item in data_lookup]
        size = len(heightmap)
        distance = [None] * size
        distance[self.start.index()] = 0





CLIMB_LIMIT = 1

maze = None
with open("input.txt") as file:
    data = file.read()
    maze = Maze(data)









def climbable(here, goto):
    return here + CLIMB_LIMIT <= goto



size = 1
for round in range(size):
    pass

