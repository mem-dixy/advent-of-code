import io

VISIBLE = "."
HIDDEN = "_"

TREE_HOUSE = "$"
PRETTY_TREES = "%"

grid = []
forest = []
scores = []
# 0 min 9 max
# 1 min 10 max
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        for item in line.strip():
            number = int(item)
            grid.append(number)
            forest.append(HIDDEN)
            scores.append(0)

width = len(lines[0]) - 1
size = len(grid)
height = size // width

left = -1
right = + 1
up = -width
down = + width


def this_is_edge(index):
    row = index // width
    col = index % width

    north = row - 1 < 0
    south = row + 1 >= height
    east = col + 1 >= width
    west = col - 1 < 0
    return north or south or east or west



# show edges
for index in range(size):
    if this_is_edge(index):
        forest[index] = VISIBLE

# from the top
for index_x in range(1, width - 1):
    tallest = grid[index_x]
    for index_y in range(1, height - 1):
        index = index_y * width + index_x
        if grid[index] > tallest:
            tallest = grid[index]
            forest[index] = VISIBLE


# from the bottom
for index_x in range(1, width - 1):
    tallest = grid[size - width + index_x]
    for index_y in range(height - 2, 0, -1):
        index = index_y * width + index_x
        if grid[index] > tallest:
            tallest = grid[index]
            forest[index] = VISIBLE


# from the left
for index_y in range(1, height - 1):
    tallest = grid[index_y * width]
    for index_x in range(0 + 1, width - 1, +1):
        index = index_y * width + index_x
        if grid[index] > tallest:
            tallest = grid[index]
            forest[index] = VISIBLE

# from the right
for index_y in range(1, height - 1):
    tallest = grid[index_y * width + width - 1]
    for index_x in range(width - 2, 0, -1):
        index = index_y * width + index_x
        if grid[index] > tallest:
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



def travel_left(row, col, tallness, magic):
    seen = 0
    index_y = row
    for index_x in range(col - 1, 0 - 1, -1):
        index = index_y * width + index_x
        seen += 1
        if magic:
            forest[index] = PRETTY_TREES
        if grid[index] >= tallness:
            return seen
    return seen

def travel_right(row, col, tallness, magic):
    seen = 0
    index_y = row
    for index_x in range(col + 1, width):
        index = index_y * width + index_x
        seen += 1
        if magic:
            forest[index] = PRETTY_TREES
        if grid[index] >= tallness:
            return seen
    return seen

def travel_up(row, col, tallness, magic):
    seen = 0
    index_x = col
    for index_y in range(row - 1, 0 - 1, -1):
        index = index_y * width + index_x
        seen += 1
        if magic:
            forest[index] = PRETTY_TREES
        if grid[index] >= tallness:
            return seen
    return seen

def travel_down(row, col, tallness, magic):
    seen = 0
    index_x = col
    for index_y in range(row + 1, height):
        index = index_y * width + index_x
        seen += 1
        if magic:
            forest[index] = PRETTY_TREES
        if grid[index] >= tallness:
            return seen
    return seen


# find treehouse
index = 0
for index in range(size):
    if this_is_edge(index):
        continue

    tallness = grid[index]
    row = index // width
    col = index % width

    magic = index == 741
    if magic:
        forest[index] = TREE_HOUSE
    score = 1
    score *= travel_left(row, col, tallness, magic)
    score *= travel_right(row, col, tallness, magic)
    score *= travel_up(row, col, tallness, magic)
    score *= travel_down(row, col, tallness, magic)
    scores[index] = score
    if score == 252000:
        print(index)

show_forest()  # again
print(max(scores))
# count trees: my height < next height = +1 tree seen
# if edge: trees += 0 break
# if next >= us: trees += 1 break
# if next < us: trees += 1 continue
# up * down *right * left
