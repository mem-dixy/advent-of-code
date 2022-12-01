elfs = []
number = 0
line = True

with open("elf.txt") as file:
    while line:
        line = file.readline()
        match line:
            case "":
                line = False
            case "\n":
                elfs.append(number)
                number = 0
            case _:
                number += int(line.strip())

print(elfs)
print(max(elfs))

one = max(elfs)
elfs.remove(one)
two = max(elfs)
elfs.remove(two)
three = max(elfs)
elfs.remove(three)

total = one + two + three
print(total)
