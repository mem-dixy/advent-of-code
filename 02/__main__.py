calories = 0
elfs = []
line = True

with open("02/input.txt") as file:
    while line:
        line = file.readline()
        match line:
            case "":  # End of file.
                line = False
            case "\n":  # Blank line.
                elfs.append(calories)
                calories = 0
            case _:
                calories += int(line.strip())

print(max(elfs))

one = max(elfs)
elfs.remove(one)
two = max(elfs)
elfs.remove(two)
three = max(elfs)
elfs.remove(three)

total = one + two + three
print(total)
