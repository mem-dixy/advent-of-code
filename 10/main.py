import io

def parse_input():
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


screen = []


instruction = None
clock = 1
register_x = 1
strength = 0

lines = parse_input()
for line in lines:
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

        offset = clock - 1
        position = offset % 40
        value = abs(register_x - position)
        test = value <= 1
        screen.append(test)

        # end of cycle
        wait = instruction.tick()
        clock += 1
    # goto idle state

print(strength)


width = 40
height = 6
string = io.StringIO()
for index_y in range(height):
    for index_x in range(width):
        index = index_y * width + index_x
        draw = "#" if screen[index] else "."
        string.write(draw)
    string.write("\n")

print(string.getvalue())
