def get_raw_data():
    with open("05/input.txt") as file:
        line = file.readlines()
        string = "".join(line)
        (top, bottom) = string.split("\n\n")
        return (top, bottom)


def get_stack_data(top):
    top_lines = top.split("\n")
    length_top_lines = len(top_lines) - 1
    index = top_lines[length_top_lines]

    STACK_COUNT = ((len(index)) // 4) + 1
    LINE_LENGTH = ((STACK_COUNT - 1) * 4) + 3

    top_lines = top_lines[0:length_top_lines]
    new_top_lines = []
    for lines in top_lines:
        pad = lines.ljust(LINE_LENGTH)
        if pad.startswith(" "):
            pad = pad.replace("    ", "[_] ", 1)
        pad = pad.replace("    ", " [_]")
        new_top_lines.append(pad)

    # bottom up processing
    stacks = []
    new_top_lines.reverse()
    for item in range(STACK_COUNT):
        stacks.append([])

    for lines in new_top_lines:
        splitt = lines.split(" ")
        for item in range(STACK_COUNT):
            hold = splitt[item]
            hold = hold[1]
            if hold != "_":
                stacks[item].append(hold)

    return stacks

def get_crane_data(bottom):
    crane = []
    lines = bottom.split("\n")
    for line in lines:
        if line:
            sub = line.split(" ")
            move = int(sub[1])
            frm = int(sub[3])
            too = int(sub[5])
            crane.append((move, frm, too))
    return crane

(top, bottom) = get_raw_data()
stack_data = get_stack_data(top)
crane_data = get_crane_data(bottom)

for data in crane_data:
    (move, frm, too) = data
    frm -= 1
    too -= 1
    hold = []
    for times in range(move):
        pickup = stack_data[frm].pop(-1)
        hold.append(pickup)
    hold.reverse()
    stack_data[too].extend(hold)

result = ""
for data in stack_data:
    result += data[-1]

print(stack_data)
print(crane_data)
print(result)
