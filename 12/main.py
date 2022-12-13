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

        self.slope = heightmap


        self.distance = [INFINITY] * size

        self.visited = [None] * size

        self.draw = data_lookup


    def __str__(
        self,
    ) -> str:
        """"""

        self.draw = self.distance
        return super().__str__()



def climbable(here, goto):
    return here + CLIMB_LIMIT <= goto


data = None
with open("input.txt") as file:
    data = file.read()



def find_distance_from_cell(data, start):
    maze = Hill(data)

    starting = start.index()
    maze.distance[starting] = 0
    maze.visited[starting] = False

    array = []
    array.append(start)
    while array:
        cell = array.pop(0)
        index = cell.index()

        slope = maze.slope[index]
        distance = maze.distance[index]

        maze.visited[index] = True

        for boar in cell.neighbor():
            neigh = boar.index()

            if maze.visited[neigh] is not None:
                continue

            if slope + CLIMB_LIMIT < maze.slope[neigh]:
                continue

            maze.distance[neigh] = distance + 1
            maze.visited[neigh] = False

            array.append(boar)


    return maze.distance[maze.finish.index()]


master = Hill(data)

start_zone = []
for index_y in range(master.grid.axis_y.size):
    for index_x in range(master.grid.axis_x.size):
        cell = Cell.clone(master.player)
        cell.goto(index_x, index_y)

        draw = master.draw[cell.index()]
        if draw == "S" or draw == "a":
            start_zone.append(cell)

distance = INFINITY
for zone in start_zone:
    result = find_distance_from_cell(data, zone)
    # print(result)
    distance = min(distance, find_distance_from_cell(data, zone))


print(distance)

