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
    match line:
        case _:
            pass
