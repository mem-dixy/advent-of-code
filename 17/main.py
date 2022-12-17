from setup import load
import io


FILE = "input.txt"
FILE = "sample.txt"

LIMIT = 2022

WIDTH_INSIDE = 7
HEIGHT_INSIDE = 15
SIZE_INSIDE = WIDTH_INSIDE * HEIGHT_INSIDE

WIDTH_OUTSIDE = WIDTH_INSIDE + 2
HEIGHT_OUTSIDE = HEIGHT_INSIDE + 1
SIZE_OUTSIDE = WIDTH_OUTSIDE * HEIGHT_OUTSIDE

SPAWN_X = +2
SPAWN_Y = +3
AIR = "."
ROCK = "#"

LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)

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

class Rock():
    def __init__(self, width, shape):
        self.width = width
        self.shape = shape
        self.left = SPAWN_X
        self.right = SPAWN_X + width - 1

    def move(self, air):
        pass





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


class Rocky():
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
        self.column = [AIR] * SIZE_OUTSIDE
        for index in range(SIZE_OUTSIDE):
            left = index % WIDTH_OUTSIDE == 0
            right = index % WIDTH_OUTSIDE == WIDTH_OUTSIDE - 1
            down = index // WIDTH_OUTSIDE >= HEIGHT_INSIDE
            test = left or right or down
            draw = ROCK if test else AIR
            self.column[index] = draw

    def tallness(self):
        best = 0
        for index_x in range(WIDTH):
            index = 0
            for index_y in range(HEIGHT):
                if self.column[index_x][index_y] == ROCK:
                    index = index_y
            best = max(best, index)
        return best


chamber = Chamber()
wind = Wind(load(FILE))
# print(wind.blow())

string = io.StringIO()

for index_y in range(HEIGHT_OUTSIDE):
    print(index_y)
    for index_x in range(WIDTH_OUTSIDE):
        index = index_y * WIDTH_OUTSIDE + index_x
        string.write(chamber.column[index])
    string.write(LINE_FEED)

print(string.getvalue())

# print(chamber.tallness())

