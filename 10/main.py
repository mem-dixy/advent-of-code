import io

grid = []
forest = []
scores = []
# 0 min 9 max
# 1 min 10 max

import enum
import dataclasses
import types
import typing


EMPTY = "."
VISITED = "#"

HEAD = "H"
TAIL = "T"
BOTH = "S"

DOWN = "D"
LEFT = "L"
RIGHT = "R"
UP = "U"

def parse_input(
) -> list[str]:
    lines = []
    with open("input.txt") as file:
        readlines = file.readlines()
        for line in readlines:
            row = line.strip().split()
            if row:
                lines.append(row)
    return lines



class Instruction():
    def __init__(self, time, run):
        self.time = time
        self.run = run

    def tick(self):
        self.time -= 1
        if self.time <= 0:
            self.run()
            return False
        return True

class Add(Instruction):
    def __init__(self, value):
        super().__init__(2, self.add)
        self.value = int(value)

    def add(self):
        global register_x
        register_x += self.value


class Nothing(Instruction):
    def __init__(self):
        super().__init__(1, self.nothing)

    def nothing(self):
        pass



instruction = None
clock = 1
register_x = 1
strength = 0

lines = parse_input()
for line in lines:
    if clock > 217:
        pass

    # start of idle state
    match line:
        case ["addx", value]:
            instruction = Add(value)
        case ["noop"]:
            instruction = Nothing()

    wait = True
    while wait:
        # start of busy cycle

        if clock % 40 == 20:
            signal = clock * register_x
            strength += signal
            print(signal)

        # end of cycle
        wait = instruction.tick()
        clock += 1
    # goto idle state


print("final")
print(strength)
