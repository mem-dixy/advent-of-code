line = True
count = 0

def myrange(input):
    (left, right) = input.split("-")
    left = int(left)
    right = int(right)
    span = range(left, right + 1, 1)
    span = set(span)
    return span

with open("04/input.txt") as file:
    while line:
        line = file.readline().strip()
        if not line:
            break
        (left, right) = tuple(line.split(","))
        left = myrange(left)
        right = myrange(right)
        if left <= right or right <= left:
            count += 1

print(count)
