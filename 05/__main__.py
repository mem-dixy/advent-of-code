line = True
count = 0

with open("05/input.txt") as file:
    line = file.readlines()
    string = "".join(line)

    (top, bottom) = string.split("\n\n")
    top_lines = top.split("\n")
    length_top_lines = len(top_lines) - 1
    index = top_lines[length_top_lines]

    STACKS = ((len(index)) // 4) + 1
    LINE_LENGTH = ((STACKS - 1) * 4) + 3

    top_lines = top_lines[0:length_top_lines]
    new_top_lines = []
    for lines in top_lines:
        pad = lines.ljust(LINE_LENGTH)
        if pad.startswith(" "):
            pad = pad.replace("    ", "[_] ", 1)
        pad = pad.replace("    ", " [_]")
        new_top_lines.append(pad)

    print(new_top_lines)


    cat = "\n".join(new_top_lines)

    print(cat)
    print("------------")
    print(bottom)
