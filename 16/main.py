import io
import enum
import typing
import types

FILE = "input.txt"
#  FILE = "sample.txt"

LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)

NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

INFINITY = 9876543210


def tunnel_key(one, two):
    return F"{one}-{two}"


def tunnel_map(maze_node):
    tunnel = {}
    for node in maze_node:
        tunnel[node] = None
    return tunnel


def tunnel_path(tunnel):
    for (key, value) in tunnel.items():
        if value:
            yield (key, value)


def file_read():
    with open(FILE) as file:
        read = file.read()
        strip = read.strip()
        split = strip.split(LINE_FEED)
    return split


def open_file():
    maze_node = set({})
    maze_valve = {}    # maze_valve.get(valve, 0)
    maze_tunnel = {}     # maze_valve.get(valve, INFINITY)

    lines = file_read()

    for line in lines:
        split = line.split(SPACE)
        valve = split[1]
        rate = int(split[4].strip("rate=;"))
        tunnels = split[9:]

        maze_node.add(valve)
        for tunnel in tunnels:
            maze_node.add(tunnel.strip(COMMA))
        if rate > 0:
            maze_valve[valve] = rate

    maze_tunnel = tunnel_map(maze_node)
    for node in maze_node:
        maze_tunnel[node] = tunnel_map(maze_node)

    for line in lines:
        split = line.split(SPACE)
        valve = split[1]
        tunnels = split[9:]

        for tunnel in tunnels:
            maze_tunnel[valve][tunnel.strip(COMMA)] = 1
            maze_tunnel[tunnel.strip(COMMA)][valve] = 1

    return (maze_node, maze_valve, maze_tunnel)


def explore(maze_tunnel, origin, location, depth):
    for (destination, distance) in maze_tunnel[location].items():
        if distance is None:
            continue

        if destination == origin:
            continue

        distance += depth
        length = maze_tunnel[origin][destination]

        if length and length <= distance:
            continue

        maze_tunnel[origin][destination] = distance
        explore(maze_tunnel, origin, destination, distance)


def start(maze_tunnel, maze_node):
    for start in maze_node:
        for final in maze_node:
            distance = maze_tunnel[start][final]
            if distance is None:
                continue
            explore(maze_tunnel, start, final, distance)


def make_maze():
    (maze_node, maze_valve, maze_tunnel) = open_file()
    start(maze_tunnel, maze_node)
    print("HI")

    return (maze_node, maze_valve, maze_tunnel)


def load():
    return make_maze()


(maze_node, maze_valve, maze_tunnel) = load()



string = io.StringIO()
for maze in maze_tunnel:
    string.write(F"{maze}:\n")
    for (destination, distance) in maze_tunnel[maze].items():
        if distance is None:
            continue
        string.write(F"    {destination} = {distance}\n")

print(string.getvalue())
