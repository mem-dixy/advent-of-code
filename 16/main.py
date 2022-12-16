from setup import load
import io
import enum
import typing
import types

FILE = "input.txt"
# FILE = "sample.txt"


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

    def spice_must_flow(self, wait, no_time_travel):
        for node in self.node:
            if self.visited[node]:
                value = self.valve[node] * wait
                if no_time_travel:
                    self.scores[node] += value
                else:
                    self.scores[node] -= value
                    total = 0
        if no_time_travel:
            total = 0
            for (item, score) in self.scores.items():
                total += score
            self.best = max(self.best, total)


    def human(self, clock, wait):
        time = wait
        while time > 0:
            yield
            time -= 1


        for (destination, distance) in self.tunnel[location].items():
            if distance is None:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

        human(clock - wait,


    def countdown(self, clock):
        time = clock - 1

        do_work(1)
        do_work(2)

        self.countdown(time)


    def runner(self, location, timer, wait):
        time = wait
        while time > 0:
            yield
            time -= 1

        for (destination, distance) in self.tunnel[location].items():
            if self.visited[destination]:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

            wait = distance + 1
            distance = time - wait
            if distance < 0:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

            self.spice_must_flow(wait, True)
            self.visited[destination] = True

            self.runner(destination, distance)

            self.visited[destination] = False
            self.spice_must_flow(wait, False)


    def runner(self, location, time):
        for (destination, distance) in self.tunnel[location].items():
            if distance is None:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

            if self.visited[destination]:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

            wait = distance + 1
            distance = time - wait
            if distance < 0:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue

            self.spice_must_flow(wait, True)
            self.visited[destination] = True

            self.runner(destination, distance)

            self.visited[destination] = False
            self.spice_must_flow(wait, False)

    def start_running(self):
        start = "AA"
        distance = 30
        self.visited[start] = True
        self.runner(start, distance)


        self.runner(start, distance, 0)
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

