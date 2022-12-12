import io
import enum
import typing
import types


from maze import Cell
from maze import Maze



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

        self.start = Cell.from_index(self.grid, data_lookup.index("S"))
        self.finish = Cell.from_index(self.grid, data_lookup.index("E"))

        heightmap = [elevation(item) for item in data_lookup]
        size = len(heightmap)
        distance = [None] * size
        distance[self.start.grid.index()] = 0

        self.draw = data_lookup


CLIMB_LIMIT = 1

def climbable(here, goto):
    return here + CLIMB_LIMIT <= goto

maze = None
with open("input.txt") as file:
    data = file.read()
    maze = Hill(data)



print(maze)

size = 1
for round in range(size):
    pass

