import io
import enum
import typing
import types


from maze import Cell
from maze import Maze


CLIMB_LIMIT = 1
INFINITY = 1234567890

def elevation(letter):
    if letter == "S":
        letter = "a"
    if letter == "E":
        letter = "z"
    return ord(letter) - ord("a")



class Hill(Maze):
    def __init__(self, data):

        data_split = data.split()
        width = len(data_split[0])
        height = len(data_split)

        super().__init__(width, height)

        data_lookup = [item for item in data if item.isalpha()]

        self.player = Cell.from_index(self.grid, data_lookup.index("S"))
        self.finish = Cell.from_index(self.grid, data_lookup.index("E"))

        heightmap = [elevation(item) for item in data_lookup]
        size = len(heightmap)

        self.distance = [INFINITY] * size
        self.distance[self.player.grid.index()] = 0

        self.draw = data_lookup
        self.draw = self.distance


    def __str__(
        self,
    ) -> str:
        """"""

        self.draw = self.distance
        return super().__str__()



def climbable(here, goto):
    return here + CLIMB_LIMIT <= goto

maze = None
with open("input.txt") as file:
    data = file.read()
    maze = Hill(data)


def happy_neighboar(neighboar):
    distance = INFINITY
    for boar in neighboar:
        distance = min(distance, maze.distance[boar.index()])
    return distance

for index_y in range(5):
    for index_x in range(8):
        cell = Cell.clone(maze.player)
        cell.goto(index_x, index_y)
        if cell == maze.player:
            continue

        neighbor = cell.neighbor()
        distance = happy_neighboar(neighbor)

        chek = cell.index()
        maze.distance[cell.index()] = distance + 1

print(maze)


size = 1
for round in range(size):
    player = Cell.clone(maze.player)
    neighbor = player.neighbor()
    for dog in neighbor:
        print(dog)

print(maze)
