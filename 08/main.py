
with open("input.txt") as file:
    line = True
    while line:
        line = file.readline().strip()
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



