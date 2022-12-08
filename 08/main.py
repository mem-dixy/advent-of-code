import io

VISIBLE = "_"
HIDDEN = "#"
MYSTERY = "$"

grid = []
forest = []

# 0 min 9 max
# 1 min 10 max
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        for item in line.strip():
            number = int(item)
            grid.append(number)
            forest.append(MYSTERY)

width = len(lines[0]) - 1
size = len(grid)
height = size // width

left = -1
right = + 1
up = -width
down = + width


# show edges
for index in range(size):
    row = index // width
    col = index % width

    north = row - 1 < 0
    south = row + 1 >= height
    east = col + 1 >= width
    west = col - 1 < 0
    if north or south or east or west:
        forest[index] = VISIBLE

# from the top
for index_x in range(1, width - 1):
    tallest = grid[index_x]
    for index_y in range(1, height - 1):
        index = index_y * width + index_x
        if grid[index] <= tallest:
            break
        tallest = grid[index]
        forest[index] = VISIBLE


# from the bottom
for index_x in range(1, width - 1):
    tallest = grid[size - width + index_x]
    for index_y in range(height - 2, 0, -1):
        index = index_y * width + index_x
        if grid[index] <= tallest:
            break
        tallest = grid[index]
        #forest[index] = VISIBLE



# from the left TODO
for index_y in range(1, height - 1):
    tallest = grid[index_y * width]
    for index_x in range(0 + 1, width - 1, +1):
        index = index_y * width + index_x
        if grid[index] <= tallest:
            break
        tallest = grid[index]
        forest[index] = VISIBLE

# from the right TODO
for index_y in range(1, height - 1):
    tallest = grid[index_y * width + width - 1]
    for index_x in range(width - 2, 0, -1):
        index = index_y * width + index_x
        if grid[index] <= tallest:
            break
        tallest = grid[index]
        forest[index] = VISIBLE

def show_forest():
    visible = 0
    string = io.StringIO()
    for index_y in range(height):
        for index_x in range(width):
            index = index_y * width + index_x
            tree = forest[index]
            if tree == VISIBLE:
                visible += 1
            string.write(tree)
        string.write("\n")
    print(string.getvalue())
    print(visible)

show_forest()
