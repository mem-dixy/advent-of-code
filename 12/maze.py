""""""

import io
import enum
import typing


class Direction(enum.Enum):
    """"""

    EAST = enum.auto()
    NORTH = enum.auto()
    SOUTH = enum.auto()
    WEST = enum.auto()


class Axis():
    """"""

    point: int
    size: int

    def clone(
        self,
    ) -> typing.Self:
        """"""

        return Axis(self.point, self.size)

    @classmethod
    def copy(
        cls,
        axis: typing.Self,
    ) -> typing.Self:
        """"""

        return cls(axis.point, axis.size)

    def index(
        self,
    ) -> int:
        """"""

        return self.point

    def move(
        self,
        point: int,
    ) -> None:
        """"""

        self.point += point

    def valid(
        self,
    ) -> bool:
        """"""

        return 0 <= self.point < self.size

    def __eq__(
        self,
        other: typing.Self,
    ) -> bool:
        """"""

        point = self.point == other.point
        size = self.size == other.size
        return point and size

    def __init__(
        self,
        point: int,
        size: int,
    ) -> None:
        """"""

        self.point = point
        self.size = size


class Grid():
    """"""

    axis_x: Axis
    axis_y: Axis
    size: int

    def clone(
        self,
    ) -> typing.Self:
        """"""

        return Grid(self.axis_x.clone(), self.axis_y.clone())

    @classmethod
    def copy(
        cls,
        grid: typing.Self,
    ) -> typing.Self:
        """"""

        return cls(Axis.copy(grid.axis_x), Axis.copy(grid.axis_y))

    def index(
        self,
    ) -> int:
        """"""

        return self.axis_y.point * self.axis_x.size + self.axis_x.point

    def move(
        self,
        direction: Direction,
    ) -> None:
        """"""

        match direction:
            case Direction.EAST:
                self.axis_x.move(+1)
            case Direction.NORTH:
                self.axis_y.move(-1)
            case Direction.SOUTH:
                self.axis_y.move(+1)
            case Direction.WEST:
                self.axis_x.move(-1)

    def valid(
        self,
    ) -> bool:
        """"""

        return self.axis_x.valid() and self.axis_y.valid()

    def __eq__(
        self,
        other: typing.Self,
    ) -> bool:
        """"""

        axis_x = self.axis_x == other.axis_x
        axis_y = self.axis_y == other.axis_y
        return axis_x and axis_y

    def __init__(
        self,
        axis_x: Axis,
        axis_y: Axis,
    ) -> None:
        """"""

        self.axis_x = axis_x
        self.axis_y = axis_y
        self.size = axis_x.size * axis_y.size


class Cell():
    """"""

    def clone(
        self,
    ) -> typing.Self:
        """"""

        return Cell(self.grid.clone())

    @classmethod
    def copy(
        cls,
        cell: typing.Self,
    ) -> typing.Self:
        """"""

        return cls(Grid.copy(cell.grid))

    def index(
        self,
    ) -> int:
        """"""

        return self.grid.index()

    def move(
        self,
        direction: Direction,
    ) -> None:
        """"""

        self.grid.move(direction)

    def valid(
        self,
    ) -> bool:
        """"""

        return self.grid.valid()

    def __eq__(
        self,
        other: typing.Self,
    ) -> bool:
        """"""

        return self.grid == other.grid

    def __init__(self, grid):
        self.grid = grid

    def __str__(
        self,
    ) -> str:
        """"""

        index_x = self.grid.axis_x.point
        index_y = self.grid.axis_y.point
        return F"({index_x}, {index_y})"


    @classmethod
    def from_index(
        cls,
        grid: Grid,
        index: int,
    ):
        """"""

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

    def goto(
        self,
        point_x: int,
        point_y: int,
    ) -> None:
        """"""

        self.grid.axis_x.point = point_x
        self.grid.axis_y.point = point_y

    def neighbor(
        self,
    ) -> list[typing.Self]:
        """"""

        cell = []
        cell.append(self.step(Direction.EAST))
        cell.append(self.step(Direction.NORTH))
        cell.append(self.step(Direction.SOUTH))
        cell.append(self.step(Direction.WEST))
        return list(filter(None, cell))

    def step(
        self,
        direction: Direction,
    ) -> typing.Self:
        """"""

        cell = self.clone()
        cell.move(direction)
        return cell if cell.grid.valid() else None


class Maze():
    """"""

    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        """"""

        self.size = width * height

        axis_x = Axis(0, width)
        axis_y = Axis(0, height)
        grid = Grid(axis_x, axis_y)

        self.grid = grid
        self.data = [0] * self.size
        self.draw = [""] * self.size

    def __str__(
        self,
    ) -> str:
        """"""

        cell = Cell.from_index(self.grid, 0)
        string = io.StringIO()
        for index_y in range(self.grid.axis_y.size):
            for index_x in range(self.grid.axis_x.size):
                cell.goto(index_x, index_y)
                index = cell.grid.index()
                draw = self.draw[index]
                # string.write(str(draw))
                if draw < 10:
                    string.write(F"[00{draw}]")
                elif draw < 100:
                    string.write(F"[0{draw}]")
                elif draw < 1000:
                    string.write(F"[{draw}]")
            string.write("\n")
        return string.getvalue()
