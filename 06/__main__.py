with open("06/input.txt") as file:
    line = file.readlines()
    string = "".join(line)
    (top, bottom) = string.split("\n\n")
    return (top, bottom)


import enum

line = True
score = 0
total_score = 0


with open("03/input.txt") as file:
    while line:
        one = file.readline().strip()

print(total_score)

