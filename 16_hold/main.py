from setup import load
import io

FILE = "input.txt"
FILE = "sample.txt"

START = "AA"
DISTANCE = 30

(maze_node, maze_valve, maze_tunnel, start_state) = load(FILE)

class Elephant():
    def __init__(self, clock, destination, distance):
        self.location = destination
        self.clock = clock - (distance + 1)

    def travel(self, world, clock):
        if clock > self.clock:
            return

        for (destination, distance) in world.tunnel[self.location].items():
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




    def runner(self, location, timer, wait):
        # do setup
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

        # do teardown



    def start_running(self, start, distance, human, elephant):
        time = distance
        pig = Elephant(time, *human)
        dog = Elephant(time, *elephant)
        world = {}

        while time > 0:
            time -= 1
            pig.travel(world, time)
            dog.travel(world, time)


    def start_plan(self, start, distance, start_state):
        tunnel = [(key, value) for (key, value) in start_state.items()]
        length = len(tunnel)
        for index_a in range(0 + 0, length - 1):
            for index_b in range(index_a + 1, length - 0):
                human = tunnel[index_a]
                elephant = tunnel[index_b]
                self.start_running(start, distance, human, elephant)
                self.start_running(start, distance, elephant, human)
        print(self.best)


run = Runner(maze_node, maze_valve, maze_tunnel)
run.start_plan(START, DISTANCE, start_state)

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

