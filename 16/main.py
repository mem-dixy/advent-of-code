from setup import load
import io
import enum
import typing
import types

FILE = "input.txt"
FILE = "sample.txt"



(maze_node, maze_valve, maze_tunnel) = load(FILE)


# maze_valve.get(valve, 0)
# maze_valve.get(valve, INFINITY)



class Runner():
    def __init__(self, maze_node, maze_valve, maze_tunnel):
        self.node = maze_node
        self.valve = maze_valve
        self.tunnel = maze_tunnel
        self.visited = {}
        self.scores = {}
        self.best = 0

        for node in self.node:
            self.visited[node] = False
            self.scores[node] = 0

    def runner(self, location, time):
        for (destination, distance) in self.tunnel[location].items():
            if distance is None:
                continue

            if self.visited[destination]:
                continue


            wait = distance + 1
            distance = time - wait
            if distance < 0:
                continue

            # update flow
            for node in self.node:
                if self.visited[node]:
                    self.scores[node] += self.valve[node] * wait

            # see how we doing
            total = 0
            for (item, score) in self.scores.items():
                total += score
            self.best = max(self.best, total)

            #  travel to next node
            self.visited[destination] = True

            self.runner(destination, distance)

            # begin undo backtrack
            self.visited[destination] = False

            # undo update flow
            for node in self.node:
                if self.visited[node]:
                    self.scores[node] -= self.valve[node] * wait


    def start_running(self):
        start = "AA"
        distance = 30
        self.visited[start] = True
        self.runner(start, distance)
        print(self.best)

run = Runner(maze_node, maze_valve, maze_tunnel)
run.start_running()

def draw():
    string = io.StringIO(FILE)
    for maze in maze_tunnel:
        string.write(F"{maze}:\n")
        for (destination, distance) in maze_tunnel[maze].items():
            if distance is None:
                continue
            string.write(F"    {destination} = {distance}\n")

    print(string.getvalue())

# draw()

