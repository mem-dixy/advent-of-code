with open("input.txt") as file:
    line = file.readline().strip()
    match line.split():
        case ["cd", ".."]:
            move_up = 0
        case ["cd", "/"]:
            go_root = 0
        case ["cd", x]:
            go = x
        case ["ls"]:
            go = x
        case ["dir", directory]:
            pass
        case [size, file]:
            go = file

    line = file.readlines()
    string = "".join(line)
    (top, bottom) = string.split("\n\n")
    return (top, bottom)






print(crane_data)
print(result)
