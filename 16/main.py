import io
import enum
import typing
import types

FILE = "input.txt"
FILE = "sample.txt"

LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)

class Node():
    def __init__(self, line):
        split = line.split(SPACE)
        self.valve = split[1]
        self.rate = int(split[4].strip("rate=;"))
        self.tunnel = split[9:]

    def __repr__(self):
        return F"Valve {self.valve} has flow rate={self.rate} tunnels lead to valves {self.tunnel}"

class Valve():
    def __init__(self, data):
        self.valve = data[1]
        self.rate = int(split[4].strip("rate=;"))
        self.tunnel = split[9:]

    def __repr__(self):
        return F"Valve {self.valve} has flow rate={self.rate} tunnels lead to valves {self.tunnel}"

def tunnel_key(one, two):
    return F"{one}-{two}"


def file_read():
    with open(FILE) as file:
        read = file.read()
        strip = read.strip()
        split = strip.split(LINE_FEED)
    return split

def open_file():
    maze_node = set({})
    maze_valve = {}    # maze_valve.get(valve, 0)
    maze_tunnel = {}

    lines = file_read()
    for line in lines:
        split = line.split(SPACE)
        valve = split[1]
        rate = int(split[4].strip("rate=;"))
        tunnels = split[9:]

        maze_node.add(valve)

        for tunnel in tunnels:
            maze_node.add(tunnel)

        if rate > 0:
            maze_valve[valve] = rate

        for item in tunnels:
            tunnel[valve]

    return nodes


nodes = open_file()

print(nodes)
