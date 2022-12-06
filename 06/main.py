string = ""

class Buffer():
    def __init__(self):
        self.hold = ["", "", "", ""]
        self.count = 0
        self.index = 0

    def add(self, item):
        self.hold[self.index] = item
        self.count += 1
        self.index += 1
        self.index %= 4

    def found(self):
        test = set()
        test.add(self.hold[0])
        test.add(self.hold[1])
        test.add(self.hold[2])
        test.add(self.hold[3])
        if "" in test:
            return False
        return len(test) == 4


with open("input.txt") as file:
    string = file.readline().strip()

    buffer = Buffer()

    for character in string:
        buffer.add(character)
        if buffer.found():
            print(buffer.count)
            break
