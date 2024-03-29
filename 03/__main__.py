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
        one = file.readline().strip()
        two = file.readline().strip()
        three = file.readline().strip()
        if not one:
            break
        left = set({})
        middle = set({})
        right = set({})
        for item in one:
            left.add(item)
        for item in two:
            middle.add(item)
        for item in three:
            right.add(item)

        both = left & middle & right
        for item in both:
            letter = item

        score = priority(letter)
        total_score += score




print(total_score)
