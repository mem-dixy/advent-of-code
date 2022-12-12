import io
import enum


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
        self.size = axis_x.size * axis_y.size


class Cell():
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


    def goto(self, point_x, point_y):
        self.grid.axis_x.point = point_x
        self.grid.axis_y.point = point_y

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


class Maze():

    def __init__(self, width, height):
        size = width * height

        axis_x = Axis(0, width)
        axis_y = Axis(0, height)
        grid = Grid(axis_x, axis_y)

        self.grid = grid
        self.heightmap = [] * size
        self.draw = ["."] * size
        self.extra = [] * size
        self.distance = [] * size

    def __str__(self):
        cell = Cell.from_index(self.grid, 0)
        string = io.StringIO()
        for index_y in range(self.grid.axis_y.size):
            for index_x in range(self.grid.axis_x.size):
                cell.goto(index_x, index_y)
                index = cell.grid.index()
                draw = self.draw[index]
                string.write(draw)
            string.write("\n")
        return string.getvalue()




class Grid():
    @classmethod
    def clone(cls, grid):
        return cls(
            Axis.clone(grid.axis_x),
            Axis.clone(grid.axis_y),
        )

    def index(self):
        return self.axis_y.point * self.axis_x.size + self.axis_x.point


    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.size = axis_x.size * axis_y.size
