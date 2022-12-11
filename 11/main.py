import io

def input_read():
    string = io.StringIO()
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            string.write(line)
    return string.getvalue().split("\n\n")

def input_parse(lines):
    monkeys = []
    for line in lines:
        monkeys.append(
            Monkey(
                [item.strip() for item in line.split("\n") if item]
            )
        )
    return monkeys


def input():
    string = input_read()
    return input_parse(string)

class Monkey():
    monkey: int
    starting_items: list[int]
    operation_type_addition: bool
    operation_value: bool
    test_divisible_by: int
    if_true_throw_to_monkey: int
    if_false_throw_to_monkey: int

    def __init__(self, line):
        self.monkey = int(line[0].split()[-1].split(":")[0])

        items = line[1].split()[2:]
        self.starting_items = [int(item.split(",")[0]) for item in items]
        self.starting_items.sort()

        self.operation_type_addition = line[2].split()[-2] == "+"

        value = line[2].split()[-1]
        self.operation_value = None if value == "old" else int(value)

        self.test_divisible_by = int(line[3].split()[-1])
        self.if_true_throw_to_monkey = int(line[4].split()[-1])
        self.if_false_throw_to_monkey = int(line[5].split()[-1])

        self.value = 0

    def operation(self):
        if self.operation_value:
            value = self.operation_value
        else:
            value = self.value

        if self.operation_type_addition:
            self.value = self.value + value
        else:
            self.value = self.value * value


monkeys = input()

