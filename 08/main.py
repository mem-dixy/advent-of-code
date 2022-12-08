import io

grid = []

# 0 min 9 max
# 1 min 10 max
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        for item in line.strip():
            number = int(item)
            grid.append(number + 1)

width = len(lines[0]) - 1
size = len(grid)
height = size // width
visible = height + height + width + width - 4

left = -1
right = + 1
up = +width
down = -width


def forest(tree):
    pass

for index in range(size):

    row = index // width
    col = index % width
    print(grid[index], row, col)


def show_forest():
    visible = 0
    string = io.StringIO()
    for index_y in range(height):
        for index_x in range(width):
            index = index_y * width + index_x
            if grid[index] < 5:
                string.write("_")
                visible += 1
            else:
                string.write("*")
        string.write("\n")
    print(string.getvalue())
    print(visible)

show_forest()
