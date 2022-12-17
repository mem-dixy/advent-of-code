from setup import load
import io


FILE = "input.txt"
FILE = "sample.txt"

LIMIT = 2022

WIDTH_INSIDE = 7
HEIGHT_INSIDE = 3100
SIZE_INSIDE = WIDTH_INSIDE * HEIGHT_INSIDE

WIDTH_OUTSIDE = WIDTH_INSIDE + 2
HEIGHT_OUTSIDE = HEIGHT_INSIDE + 1
SIZE_OUTSIDE = WIDTH_OUTSIDE * HEIGHT_OUTSIDE

SPAWN_X = +2
SPAWN_Y = +3
AIR = "."
ROCK = "#"
FLOOR = "-"
WALL = "|"
CORNER = "+"

LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)


class Rock():
    def __init__(self, index, width, shape):
        self.index = index
        self.width = width
        self.shape = shape
        self.left = SPAWN_X
        self.right = SPAWN_X + width - 1

    def plan(self, air):
        shape = []
        for index in range(len(self.shape)):
            (index_x, index_y) = self.shape[index]
            if air:
                index_x += air
            else:
                index_y += 1
            shape.append((index_x, index_y))
        self.shape = shape


    def move(self, canyon, air):
        before = self.shape
        self.plan(air)

        blocked = False
        for offset in self.spawn():
            blocked |= canyon.column[offset] != AIR

        if blocked:
            self.shape = before

        return blocked

    def spawn(self):
        array = []
        for item in self.shape:
            (offset_x, offset_y) = item
            offset = offset_y * WIDTH_OUTSIDE + offset_x
            array.append(self.index + offset)
        return array

class Rock1(Rock):
    def __init__(self, index):
        super().__init__(
            index,
            4,
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (3, 0),
            ],
        )


class Rock2(Rock):
    def __init__(self, index):
        super().__init__(
            index,
            3,
            [
                (1, 0),
                (0, -1),
                (1, -1),
                (2, -1),
                (1, -2),
            ],
        )


class Rock3(Rock):
    def __init__(self, index):
        super().__init__(
            index,
            3,
            [
                (0, 0),
                (1, 0),
                (2, 0),
                (2, -1),
                (2, -2),
            ],
        )


class Rock4(Rock):
    def __init__(self, index):
        super().__init__(
            index,
            1,
            [
                (0, 0),
                (0, -1),
                (0, -2),
                (0, -3),
            ],
        )


class Rock5(Rock):
    def __init__(self, index):
        super().__init__(
            index,
            2,
            [
                (0, 0),
                (1, 0),
                (0, -1),
                (1, -1),
            ],
        )


class Rocky():
    def __init__(self):
        self.rocky = [1, 2, 3, 4, 5]
        self.tree = self.leaf()

    def leaf(self):
        while True:
            yield from self.rocky

    def fall_off(self, index):
        match next(self.tree):
            case 1:
                return Rock1(index)
            case 2:
                return Rock2(index)
            case 3:
                return Rock3(index)
            case 4:
                return Rock4(index)
            case 5:
                return Rock5(index)
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


class Canyon():
    def __init__(self):
        self.wind = Wind(load(FILE))
        self.rocky = Rocky()
        self.column = [AIR] * SIZE_OUTSIDE
        for index in range(SIZE_OUTSIDE):
            draw = AIR
            if self._left(index):
                draw = WALL
            if self._right(index):
                draw = WALL
            if self._down(index):
                if draw == WALL:
                    draw = CORNER
                else:
                    draw = FLOOR
            self.column[index] = draw

    def _left(self, index):
        return index % WIDTH_OUTSIDE == 0

    def _right(self, index):
        return index % WIDTH_OUTSIDE == WIDTH_OUTSIDE - 1

    def _down(self, index):
        return index // WIDTH_OUTSIDE >= HEIGHT_INSIDE

    def _border(self, index):
        left = self._left(index)
        right = self._right(index)
        down = self._down(index)
        return left or right or down

    def tallness(self):
        for index_y in range(HEIGHT_OUTSIDE):
            for index_x in range(WIDTH_OUTSIDE):
                index = index_y * WIDTH_OUTSIDE + index_x
                if self._border(index):
                    continue
                if self.column[index] == ROCK:
                    return HEIGHT_INSIDE - index_y
        return 0

    def safe(self, plan):
        index_x = 1 + SPAWN_X
        index_y = HEIGHT_INSIDE - (1 + self.tallness() + SPAWN_Y)
        index = index_y * WIDTH_OUTSIDE + index_x

        for offset in plan:
            self.column[index + offset] = ROCK

    def spawn(self):
        index_x = 1 + SPAWN_X
        index_y = HEIGHT_INSIDE - (1 + self.tallness() + SPAWN_Y)
        index = index_y * WIDTH_OUTSIDE + index_x

        rock = self.rocky.fall_off(index)

        floating = True
        while floating:
            rock.move(self, self.wind.blow())
            floating = not rock.move(self, 0)


        for offset in rock.spawn():
            self.column[offset] = ROCK




    def display(self):
        string = io.StringIO()
        for index_y in range(HEIGHT_OUTSIDE):
            for index_x in range(WIDTH_OUTSIDE):
                index = index_y * WIDTH_OUTSIDE + index_x
                string.write(self.column[index])
            string.write(LINE_FEED)
        return string.getvalue()



canyon = Canyon()

for index in range(LIMIT):
    canyon.spawn()

print(canyon.display())
print(canyon.tallness())
