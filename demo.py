line = True
with open("elf.txt") as file:
    while line:
        line = file.readline()
        match line:
            case "":
                print("EOL")
            case "\n":
                print("break")
            case _:
                number = int(line.strip())
                print(number)
