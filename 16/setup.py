from maze import Direction
from maze import Cell
from maze import Maze
NONE = str()
LINE_FEED = chr(0x000A)
SPACE = chr(0x0020)
COMMA = chr(0x002C)
HYPHEN_MINUS = chr(0x002D)
GREATER_THAN_SIGN = chr(0x003E)

ARROW = NONE.join([SPACE, HYPHEN_MINUS, GREATER_THAN_SIGN, SPACE])
FILE = "input.txt"
FILE = "sample.txt"

ROOM = "."
ROCK = "#"
DROP = "+"
SAND = "o"
FLOW = "~"


value = "Valve HM has flow rate=0; tunnels lead to valves LS, YS"
split = value.split(SPACE)
valve = split[1]
rate = split[4].strip("rate=;")
tunnel = split[9:]
print("cow")
