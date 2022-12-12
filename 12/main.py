import io
import enum

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

class Maze(Agent):
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


CLIMB_LIMIT = 1


data = None
with open("input.txt") as file:
    data = file.read()

data_split = data.split()
width = len(data_split[0])
height = len(data_split)
size = width * height

data_lookup = [item for item in data if item.isalpha()]

player = Agent(data_lookup.index("S"), width)
goal = Cell(data_lookup.index("E"), width)

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

