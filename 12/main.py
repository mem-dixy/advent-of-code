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

