import io

OPTIMAL_LIST_SIZE = 36

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
    inspected_items: int

    index: int

    def __init__(self, line):
        self.monkey = int(line[0].split()[-1].split(":")[0])

        items = line[1].split()[2:]
        starting_items = [int(item.split(",")[0]) for item in items]
        self.starting_items = [None] * OPTIMAL_LIST_SIZE
        self.index = 0
        for stuff in starting_items:
            self.starting_items[self.index] = stuff
            self.index += 1

        self.operation_type_addition = line[2].split()[-2] == "+"

        value = line[2].split()[-1]
        self.operation_value = None if value == "old" else int(value)

        self.test_divisible_by = int(line[3].split()[-1])
        self.if_true_throw_to_monkey = int(line[4].split()[-1])
        self.if_false_throw_to_monkey = int(line[5].split()[-1])

        self.inspected_items = 0

    def catch(self, item):
        self.starting_items[self.index] = item
        self.index += 1

    def take_turn(self):
        global monkeys

        index = 0
        item = self.starting_items[index]
        while item:

            if item is None:
                return

            self.inspected_items += 1

            if self.operation_value:
                value = self.operation_value
            else:
                value = item

            if self.operation_type_addition:
                item = item + value
            else:
                item = item * value

            item = item // 3  # relief

            if item % self.test_divisible_by == 0:
                monkeys[self.if_true_throw_to_monkey].catch(item)
            else:
                monkeys[self.if_false_throw_to_monkey].catch(item)

            index += 1
            item = self.starting_items[index]


        for index in range(OPTIMAL_LIST_SIZE):
            self.starting_items[index] = None
        self.index = 0

    def __str__(self):
        array = str(self.starting_items)[1:-1]
        return F"Monkey {self.monkey}: {array}"


monkeys = input()



def play_round(round):
    for monkey in monkeys:
        monkey.take_turn()
    if round % 1000 == -1:
        pass
    else:

        for monkey in monkeys:
            print(monkey)
        print(monkey)
        print()



def optimize():
    total = []
    for monkey in monkeys:
        total.extend(monkey.starting_items)

    print(len(total))

# optimize()

rounds = 20
for round in range(1, rounds + 1, 1):
    if round % 1000 == -1:
        pass
    else:
        print(F"After round {round},", end="")
        print(" the monkeys are holding items with these worry levels:")
    play_round(round)


for monkey in monkeys:
    index = monkey.monkey
    times = monkey.inspected_items
    print(F"Monkey {index} inspected items {times} times.")

def monkey_business():
    array = []
    for monkey in monkeys:
        array.append(monkey.inspected_items)
    array.sort()
    array.reverse()
    (one, two) = array[0:2]
    result = one * two
    print()
    print(result)

monkey_business()
