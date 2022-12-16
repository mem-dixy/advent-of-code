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

def tunnel_key(one, two):
    return F"{one}-{two}"

def tunnel_map(maze_node, value):
    tunnel = {}
    for node in maze_node:
        tunnel[node] = value
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

    maze_tunnel = tunnel_map(maze_node, None)
    for node in maze_node:
        maze_tunnel[node] = tunnel_map(maze_node, None)

    for line in lines:
        split = line.split(SPACE)
        valve = split[1]
        tunnels = split[9:]

        for tunnel in tunnels:
            maze_tunnel[valve][tunnel.strip(COMMA)] = 1
            maze_tunnel[tunnel.strip(COMMA)][valve] = 1

    print(len(maze_node))

    return (maze_node, maze_valve, maze_tunnel)

def rarct(maze_tunnel, start, final, distance):
    cat = maze_tunnel[start][final]
    if cat is None or cat > distance:

        maze_tunnel[start][final] = distance

def monkoy(maze_tunnel, start, final, distance):
    distance = 0
    tunnels = tunnel_path(maze_tunnel[node])
    for tunnel in tunnels:

    maze_tunnel[start][final] = distance
    tunnels = tunnel_path(maze_tunnel[node])
    for tunnel in tunnels:

def explore(maze_tunnel, visited, node):
    tunnels = tunnel_path(maze_tunnel[node])
    for tunnel in tunnels:



def make_maze():
    (maze_node, maze_valve, maze_tunnel) = open_file()


    for node in maze_node:
        visited = tunnel_map(maze_node, False)
        tunnels = tunnel_path(maze_tunnel[node])
        for tunnel in tunnels:


        tunnels = [(key, value)
                    for (key, value) in maze_tunnel[node].items() if value]

        print("HI")



    return tunnel



def load():
    return make_maze()


load()

