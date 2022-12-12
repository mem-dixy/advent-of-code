OPTIMAL_LIST_SIZE = 36

monkeys = 4
rounds = 20

monkey_operation = [
    lambda old: old * 19,
    lambda old: old + 6,
    lambda old: old * old,
    lambda old: old + 3,
]

monkey_test = [
    lambda new: 2 if new % 23 else 3,
    lambda new: 2 if new % 19 else 0,
    lambda new: 1 if new % 13 else 3,
    lambda new: 0 if new % 17 else 1,
]

monkey_item = [
    [79, 98] + [None] * (OPTIMAL_LIST_SIZE - 2),
    [54, 65, 75, 74] + [None] * (OPTIMAL_LIST_SIZE - 4),
    [79, 60, 97] + [None] * (OPTIMAL_LIST_SIZE - 3),
    [74] + [None] * (OPTIMAL_LIST_SIZE - 1),
]

monkey_index = [
    0,
    0,
    0,
    0,
]

monkey_inspected = [
    0,
    0,
    0,
    0,
]

for round in range(1, rounds + 1, 1):
    for monkey in range(monkeys):
        index = 0
        item = monkey_item[monkey][index]
        while item:

            monkey_inspected[monkey] += 1

            item = monkey_operation[monkey](item)

            item = item // 3  # relief

            throw_to = monkey_test[monkey](item)
            item = monkey_item[throw_to][monkey_index[throw_to]] = item
            monkey_index[throw_to] += 1

            index += 1
            item = monkey_item[monkey][index]

        for item in range(OPTIMAL_LIST_SIZE):
            monkey_item[monkey][item] = None

        monkey_index[monkey] = 0

    print(F"After round {round},", end="")
    print(" the monkeys are holding items with these worry levels:")


print("hi")
