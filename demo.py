
calories = 0
elfs = []
line = True

ROCK = 1
PAPER = 2
SCISSORS = 3

LOST = 0
DRAW = 3
WON = 6

with open("input.txt") as file:
    while line:
        line = file.readline()
        (opponent, you) = tuple(line.split())
        match opponent:
            case "A":
                opponent = ROCK
            case "B":
                opponent = PAPER
            case "C":
                opponent = SCISSORS

        match you:
            case "X":
                opponent = ROCK
            case "Y":
                opponent = PAPER
            case "Z":
                opponent = SCISSORS



ROCK > SCISSORS
SCISSORS > PAPER
PAPER > ROCK

print(max(elfs))

one = max(elfs)
elfs.remove(one)
two = max(elfs)
elfs.remove(two)
three = max(elfs)
elfs.remove(three)

total = one + two + three
print(total)


a = "a"  # Rock
b = "b"  # Paper
c = "c"  # Scissors
