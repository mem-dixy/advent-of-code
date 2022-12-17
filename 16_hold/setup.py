LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)

START = "AA"

def tunnel_key(one, two):
    return F"{one}-{two}"


def tunnel_map(maze_node):
    tunnel = {}
    for node in maze_node:
        tunnel[node] = None
    return tunnel


def tunnel_master(maze_node):
    maze_tunnel = tunnel_map(maze_node)
    for node in maze_node:
        maze_tunnel[node] = tunnel_map(maze_node)
    return maze_tunnel


def tunnel_path(tunnel):
    for (key, value) in tunnel.items():
        if value:
            yield (key, value)


def file_read(FILE):
    with open(FILE) as file:
        read = file.read()
        strip = read.strip()
        split = strip.split(LINE_FEED)
    return split


def open_file(file):
    maze_node = set({})
    maze_valve = {}
    maze_tunnel = {}

    lines = file_read(file)

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

    maze_tunnel = tunnel_master(maze_node)

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


def start_explore(maze_tunnel, maze_node):
    for start in maze_node:
        for final in maze_node:
            distance = maze_tunnel[start][final]
            if distance is None:
                continue
            explore(maze_tunnel, start, final, distance)


def trim_maze(maze_node, maze_valve, maze_tunnel):
    start_state = {}
    for (key, value) in maze_tunnel[START].items():
        if value:
            start_state[key] = value

    valves = set({})
    for (valve, rate) in maze_valve.items():
        valves.add(valve)

    tunnel = tunnel_master(maze_node)
    for start in tunnel:
        if start not in valves:
            maze_node.remove(start)
            del maze_tunnel[start]
        else:
            for final in tunnel:
                if final not in valves:
                    del maze_tunnel[start][final]

    return start_state


def make_maze(file):
    (maze_node, maze_valve, maze_tunnel) = open_file(file)
    start_explore(maze_tunnel, maze_node)
    start_state = trim_maze(maze_node, maze_valve, maze_tunnel)
    return (maze_node, maze_valve, maze_tunnel, start_state)


def load(file):
    return make_maze(file)
