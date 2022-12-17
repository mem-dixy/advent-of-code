from setup import load
import io


FILE = "input.txt"
FILE = "sample.txt"

LIMIT = 2022
WIDTH = 7
HEIGHT = LIMIT * 2
SPAWN_X = +2
SPAWN_Y = +3
AIR = "."
ROCK = "#"

####

#  .#.
# ###
#  .#.

# ..#
# ..#
# ###

#
#
#
#

##
##


class Rock1(Rock):
    def __init__(self):
        super().__init__(
            4,
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
            ],
        )
class Rock2(Rock):
    def __init__(self):
        super().__init__(
            3,
            [
                (1, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (1, 2),
            ],
        )

class Rock3(Rock):
    def __init__(self):
        super().__init__(
            3,
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (2, 1),
                (2, 2),
            ],
        )
class Rock4(Rock):
    def __init__(self):
        super().__init__(
            1,
            [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
            ],
        )
class Rock5(Rock):
    def __init__(self):
        super().__init__(
            2,
            [
                (0, 0),
                (1, 0),
                (0, 1),
                (1, 1),
            ],
        )

# TOD he five roct tymaoes snotehu in the order belowe
class Rock():
    def __init__(self, wind):
        self.wind = wind
        self.fall = self.leaf()

    def leaf(self):
        while True:
            yield from self.wind

    def blow(self):
        match next(self.fall):
            case "<":
                return -1
            case ">":
                return +1
        raise AttributeError

class Wind():
    def __init__(self, wind):
        self.wind = wind
        self.fall = self.leaf()

    def leaf(self):
        while True:
            yield from self.wind

    def blow(self):
        match next(self.fall):
            case "<":
                return -1
            case ">":
                return +1
        raise AttributeError


class Chamber():
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.column = [None] * self.width
        for index in range(self.width):
            self.column[index] = [AIR] * self.height

    def tallness(self):
        best = 0
        for index_x in range(self.width):
            index = 0
            for index_y in range(self.height):
                if self.column[index_x][index_y] == ROCK:
                    index = index_y
            best = max(best, index)
        return best




chamber = Chamber()
wind = Wind(load(FILE))
# print(wind.blow())
print(chamber.tallness())

