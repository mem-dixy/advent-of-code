from setup import load
import io
import enum
import typing
import types

FILE = "input.txt"
#  FILE = "sample.txt"


(maze_node, maze_valve, maze_tunnel) = load(FILE)


# maze_valve.get(valve, 0)
# maze_valve.get(valve, INFINITY)


string = io.StringIO(FILE)
for maze in maze_tunnel:
    string.write(F"{maze}:\n")
    for (destination, distance) in maze_tunnel[maze].items():
        if distance is None:
            continue
        string.write(F"    {destination} = {distance}\n")

print(string.getvalue())
