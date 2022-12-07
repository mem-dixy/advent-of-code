class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory():
    def __init__(self, name):
        self.name = name
        self.directories = []
        self.files = []

    def add_file(self, file):
        self.files.append(file)

    def add_directory(self, directory):
        self.directories.append(directory)

    def find(self, name):
        for item in self.directories:
            if item.name == name:
                return item
        return None

    def display(self, indent):
        for ignore in range(indent):
            print(" ", end="")
        print(self.name)
        for item in self.directories:
            item.display(indent+1)


class Filesystem(Directory):
    def __init__(self):
        super().__init__("/")
        self.path = []

    def move_in(self, directory):
        self.path.append(directory)


    def nested(self):
        pointer = self
        for name in self.path:
            pointer = pointer.find(name)
        return pointer

    def move_out(self):
        self.path.pop(-1)

    def move_root(self):
        self.path = ["/"]

    def push_directory(self, directory):
        pointer = self.nested()
        pointer.add_directory(directory)

    def push_file(self, file):
        pointer = self.nested()
        pointer.add_file(file)




system = Filesystem()

with open("input.txt") as file:
    line = "dir /"
    while line:
        match line.split():
            case ["$", "cd", ".."]:
                system.move_out()
            case ["$", "cd", "/"]:
                system.move_root()
            case ["$", "cd", directory]:
                system.move_in(directory)
            case ["$", "ls"]:
                pass
            case ["dir", directory]:
                system.push_directory(Directory(directory))
            case [size, name]:
                system.push_file(File(name, size))

        line = file.readline().strip()



system.display(0)
print(system)
