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

        start = self.player.grid.index()

        self.distance = [INFINITY] * size
        self.distance[start] = 0

        self.visited = [None] * size
        self.visited[start] = False

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
    neigh = boar.index()

    maze.distance[neigh] = distance + 1
    maze.visited[neigh] = False

    array.append(boar)

    distance = INFINITY
    for boar in neighboar:
        distance = min(distance, maze.distance[boar.index()])
    return distance


array = []
array.append(Cell.clone(maze.player))
while array:
    cell = array.pop(0)
    index = cell.index()

    distance = maze.distance[index]
    maze.visited[index] = True



    for boar in cell.neighbor():
        neigh = boar.index()

        if maze.visited[neigh] is not None:
            continue

        maze.distance[neigh] = distance + 1
        maze.visited[neigh] = False

        array.append(boar)



print(maze)
