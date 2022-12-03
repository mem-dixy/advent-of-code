import enum

line = True
score = 0
total_score = 0


def priority(letter):
    cord = ord(letter)
    if cord < 97:
        return cord - 64 + 26

    return cord - 96


with open("03/input.txt") as file:
    while line:
        line = file.readline().strip()
        if not line:
            break
        full = len(line)
        half = full // 2
        one = line[0:half]
        two = line[half:full]
        left = set({})
        right = set({})
        for item in one:
            left.add(item)
        for item in two:
            right.add(item)

        both = left & right
        for item in both:
            letter = item

        score = priority(letter)
        total_score += score




print(total_score)
