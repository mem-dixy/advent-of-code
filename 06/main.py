string = ""

SIZE = 14

class Buffer():
    def __init__(self):
        self.hold = []
        for ignore in range(SIZE):
            self.hold.append(None)
        self.count = 0
        self.index = 0

    def add(self, item):
        self.hold[self.index] = item
        self.count += 1
        self.index += 1
        self.index %= SIZE

    def found(self):
        test = set()
        for index in range(SIZE):
            test.add(self.hold[index])

        if None in test:
            return False

        return len(test) == SIZE


with open("input.txt") as file:
    string = file.readline().strip()

    buffer = Buffer()

    for character in string:
        buffer.add(character)
        if buffer.found():
            print(buffer.count)
            break
