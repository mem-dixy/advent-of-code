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
                you = Outcome.LOST
            case "Y":
                you = Outcome.DRAW
            case "Z":
                you = Outcome.WON

        match opponent:
            case Shape.ROCK:
                match you:
                    case Outcome.LOST:
                        outcome = Shape.SCISSORS
                    case Outcome.DRAW:
                        outcome = Shape.ROCK
                    case Outcome.WON:
                        outcome = Shape.PAPER
            case Shape.PAPER:
                match you:
                    case Outcome.LOST:
                        outcome = Shape.ROCK
                    case Outcome.DRAW:
                        outcome = Shape.PAPER
                    case Outcome.WON:
                        outcome = Shape.SCISSORS
            case Shape.SCISSORS:
                match you:
                    case Outcome.LOST:
                        outcome = Shape.PAPER
                    case Outcome.DRAW:
                        outcome = Shape.SCISSORS
                    case Outcome.WON:
                        outcome = Shape.ROCK


        score = you.value + outcome.value
        total_score += score

print(total_score)
