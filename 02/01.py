import enum

class Shape(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(enum.Enum):
    LOST = 0
    DRAW = 3
    WON = 6


line = True
score = 0
total_score = 0

with open("02/input.txt") as file:
    while line:
        line = file.readline()
        if not line:
            break
        (opponent, you) = tuple(line.split())
        score = 0
        match opponent:
            case "A":
                opponent = Shape.ROCK
            case "B":
                opponent = Shape.PAPER
            case "C":
                opponent = Shape.SCISSORS

        match you:
            case "X":
                you = Shape.ROCK
            case "Y":
                you = Shape.PAPER
            case "Z":
                you = Shape.SCISSORS

        match you:
            case Shape.ROCK:
                match opponent:
                    case Shape.ROCK:
                        outcome = Outcome.DRAW
                    case Shape.PAPER:
                        outcome = Outcome.LOST
                    case Shape.SCISSORS:
                        outcome = Outcome.WON
            case Shape.PAPER:
                match opponent:
                    case Shape.ROCK:
                        outcome = Outcome.WON
                    case Shape.PAPER:
                        outcome = Outcome.DRAW
                    case Shape.SCISSORS:
                        outcome = Outcome.LOST
            case Shape.SCISSORS:
                match opponent:
                    case Shape.ROCK:
                        outcome = Outcome.LOST
                    case Shape.PAPER:
                        outcome = outcome.WON
                    case Shape.SCISSORS:
                        outcome = Outcome.DRAW

        score = you.value + outcome.value
        total_score += score

print(total_score)
