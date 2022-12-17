from setup import load
from setup import timekey
import io


FILE = "input.txt"
FILE = "sample.txt"

START = "AA"
DISTANCE = 30


# (maze_node, maze_valve, maze_tunnel) = load(FILE, START, DISTANCE)
print("*************************")
# print(maze_node)
print("*************************")
# print(maze_valve)
print("*************************")
# print(maze_tunnel)
print("*************************")


maze_node = {'JJ', 'EE', 'BB', 'CC', 'HH', 'DD'}
maze_valve = {'BB': 13, 'CC': 2, 'DD': 20, 'EE': 3, 'HH': 22, 'JJ': 21}
maze_tunnel = {
 'JJ-27': {'BB-23', 'CC-22', 'HH-19', 'DD-23', 'EE-22'},
 'JJ-24': {'DD-20', 'HH-16', 'CC-19', 'BB-20', 'EE-19'},
 'JJ-22': {'DD-18', 'HH-14', 'EE-17', 'BB-18', 'CC-17'},
 'JJ-21': {'EE-16', 'HH-13', 'DD-17', 'CC-16', 'BB-17'},
 'JJ-20': {'DD-16', 'EE-15', 'BB-16', 'CC-15', 'HH-12'},
 'JJ-19': {'EE-14', 'BB-15', 'HH-11', 'DD-15', 'CC-14'},
 'JJ-18': {'EE-13', 'BB-14', 'DD-14', 'CC-13', 'HH-10'},
 'JJ-17': {'BB-13', 'HH-09', 'CC-12', 'EE-12', 'DD-13'},
 'JJ-16': {'EE-11', 'BB-12', 'HH-08', 'CC-11', 'DD-12'},
 'JJ-15': {'HH-07', 'EE-10', 'DD-11', 'BB-11', 'CC-10'},
 'JJ-14': {'BB-10', 'DD-10', 'HH-06', 'EE-09', 'CC-09'},
 'JJ-13': {'CC-08', 'BB-09', 'EE-08', 'DD-09', 'HH-05'},
 'JJ-12': {'HH-04', 'EE-07', 'BB-08', 'CC-07', 'DD-08'},
 'JJ-11': {'CC-06', 'HH-03', 'BB-07', 'DD-07', 'EE-06'},
 'JJ-10': {'BB-06', 'EE-05', 'HH-02', 'CC-05', 'DD-06'},
 'JJ-09': {'EE-04', 'DD-05', 'BB-05', 'HH-01', 'CC-04'},
 'JJ-08': {'BB-04', 'DD-04', 'CC-03', 'HH-00', 'EE-03'},
 'JJ-07': {'DD-03', 'BB-03', 'EE-02', 'CC-02'},
 'JJ-06': {'CC-01', 'BB-02', 'EE-01', 'DD-02'},
 'JJ-05': {'CC-00', 'EE-00', 'BB-01', 'DD-01'},
 'JJ-04': {'DD-00', 'BB-00'},
 'EE-27': {'BB-23', 'DD-25', 'CC-24', 'JJ-22', 'HH-23'},
 'EE-26': {'CC-23', 'DD-24', 'JJ-21', 'HH-22', 'BB-22'},
 'EE-24': {'JJ-19', 'CC-21', 'DD-22', 'BB-20', 'HH-20'},
 'EE-23': {'CC-20', 'HH-19', 'JJ-18', 'DD-21', 'BB-19'},
 'EE-22': {'JJ-17', 'BB-18', 'DD-20', 'HH-18', 'CC-19'},
 'EE-21': {'CC-18', 'DD-19', 'JJ-16', 'BB-17', 'HH-17'},
 'EE-20': {'BB-16', 'DD-18', 'HH-16', 'CC-17', 'JJ-15'},
 'EE-19': {'HH-15', 'BB-15', 'DD-17', 'CC-16', 'JJ-14'},
 'EE-18': {'DD-16', 'CC-15', 'HH-14', 'BB-14', 'JJ-13'},
 'EE-17': {'BB-13', 'JJ-12', 'HH-13', 'DD-15', 'CC-14'},
 'EE-16': {'JJ-11', 'DD-14', 'HH-12', 'BB-12', 'CC-13'},
 'EE-15': {'HH-11', 'BB-11', 'JJ-10', 'CC-12', 'DD-13'},
 'EE-14': {'BB-10', 'CC-11', 'DD-12', 'HH-10', 'JJ-09'},
 'EE-13': {'JJ-08', 'DD-11', 'HH-09', 'BB-09', 'CC-10'},
 'EE-12': {'BB-08', 'DD-10', 'JJ-07', 'HH-08', 'CC-09'},
 'EE-11': {'BB-07', 'CC-08', 'HH-07', 'DD-09', 'JJ-06'},
 'EE-10': {'BB-06', 'JJ-05', 'HH-06', 'CC-07', 'DD-08'},
 'EE-09': {'CC-06', 'BB-05', 'JJ-04', 'DD-07', 'HH-05'},
 'EE-08': {'HH-04', 'BB-04', 'CC-05', 'DD-06', 'JJ-03'},
 'EE-07': {'BB-03', 'HH-03', 'DD-05', 'JJ-02', 'CC-04'},
 'EE-06': {'JJ-01', 'DD-04', 'HH-02', 'CC-03', 'BB-02'},
 'EE-05': {'JJ-00', 'CC-02', 'BB-01', 'DD-03', 'HH-01'},
 'EE-04': {'CC-01', 'BB-00', 'DD-02', 'HH-00'},
 'EE-03': {'CC-00', 'DD-01'},
 'EE-02': {'DD-00'},
 'BB-28': {'DD-25', 'CC-26', 'HH-21', 'EE-24', 'JJ-24'},
 'BB-25': {'EE-21', 'CC-23', 'JJ-21', 'HH-18', 'DD-22'},
 'BB-24': {'CC-22', 'JJ-20', 'DD-21', 'EE-20', 'HH-17'},
 'BB-23': {'JJ-19', 'CC-21', 'DD-20', 'HH-16', 'EE-19'},
 'BB-22': {'CC-20', 'HH-15', 'JJ-18', 'DD-19', 'EE-18'},
 'BB-21': {'JJ-17', 'DD-18', 'HH-14', 'EE-17', 'CC-19'},
 'BB-20': {'EE-16', 'HH-13', 'DD-17', 'CC-18', 'JJ-16'},
 'BB-19': {'DD-16', 'EE-15', 'HH-12', 'CC-17', 'JJ-15'},
 'BB-18': {'EE-14', 'HH-11', 'CC-16', 'DD-15', 'JJ-14'},
 'BB-17': {'EE-13', 'CC-15', 'DD-14', 'JJ-13', 'HH-10'},
 'BB-16': {'CC-14', 'JJ-12', 'HH-09', 'EE-12', 'DD-13'},
 'BB-15': {'EE-11', 'JJ-11', 'HH-08', 'CC-13', 'DD-12'},
 'BB-14': {'HH-07', 'EE-10', 'DD-11', 'JJ-10', 'CC-12'},
 'BB-13': {'DD-10', 'HH-06', 'EE-09', 'CC-11', 'JJ-09'},
 'BB-12': {'JJ-08', 'EE-08', 'DD-09', 'HH-05', 'CC-10'},
 'BB-11': {'HH-04', 'JJ-07', 'EE-07', 'CC-09', 'DD-08'},
 'BB-10': {'HH-03', 'CC-08', 'EE-06', 'DD-07', 'JJ-06'},
 'BB-09': {'EE-05', 'HH-02', 'JJ-05', 'DD-06', 'CC-07'},
 'BB-08': {'EE-04', 'CC-06', 'DD-05', 'JJ-04', 'HH-01'},
 'BB-07': {'DD-04', 'CC-05', 'HH-00', 'EE-03', 'JJ-03'},
 'BB-06': {'DD-03', 'JJ-02', 'EE-02', 'CC-04'},
 'BB-05': {'JJ-01', 'CC-03', 'EE-01', 'DD-02'},
 'BB-04': {'DD-01', 'JJ-00', 'CC-02', 'EE-00'},
 'BB-03': {'CC-01', 'DD-00'},
 'BB-02': {'CC-00'},
 'CC-27': {'DD-25', 'HH-21', 'BB-25', 'EE-24', 'JJ-22'},
 'CC-26': {'DD-24', 'JJ-21', 'BB-24', 'HH-20', 'EE-23'},
 'CC-24': {'EE-21', 'JJ-19', 'HH-18', 'DD-22', 'BB-22'},
 'CC-23': {'HH-17', 'JJ-18', 'DD-21', 'EE-20', 'BB-21'},
 'CC-22': {'JJ-17', 'DD-20', 'HH-16', 'BB-20', 'EE-19'},
 'CC-21': {'HH-15', 'DD-19', 'JJ-16', 'EE-18', 'BB-19'},
 'CC-20': {'DD-18', 'HH-14', 'EE-17', 'BB-18', 'JJ-15'},
 'CC-19': {'EE-16', 'HH-13', 'DD-17', 'JJ-14', 'BB-17'},
 'CC-18': {'DD-16', 'EE-15', 'BB-16', 'HH-12', 'JJ-13'},
 'CC-17': {'EE-14', 'BB-15', 'HH-11', 'JJ-12', 'DD-15'},
 'CC-16': {'EE-13', 'JJ-11', 'BB-14', 'DD-14', 'HH-10'},
 'CC-15': {'BB-13', 'HH-09', 'JJ-10', 'EE-12', 'DD-13'},
 'CC-14': {'EE-11', 'BB-12', 'HH-08', 'DD-12', 'JJ-09'},
 'CC-13': {'JJ-08', 'HH-07', 'EE-10', 'DD-11', 'BB-11'},
 'CC-12': {'BB-10', 'DD-10', 'JJ-07', 'HH-06', 'EE-09'},
 'CC-11': {'BB-09', 'EE-08', 'DD-09', 'HH-05', 'JJ-06'},
 'CC-10': {'HH-04', 'EE-07', 'JJ-05', 'BB-08', 'DD-08'},
 'CC-09': {'HH-03', 'BB-07', 'JJ-04', 'DD-07', 'EE-06'},
 'CC-08': {'BB-06', 'EE-05', 'HH-02', 'DD-06', 'JJ-03'},
 'CC-07': {'EE-04', 'DD-05', 'JJ-02', 'BB-05', 'HH-01'},
 'CC-06': {'JJ-01', 'BB-04', 'DD-04', 'HH-00', 'EE-03'},
 'CC-05': {'DD-03', 'JJ-00', 'BB-03', 'EE-02'},
 'CC-04': {'BB-02', 'EE-01', 'DD-02'},
 'CC-03': {'DD-01', 'EE-00', 'BB-01'},
 'CC-02': {'DD-00', 'BB-00'},
 'HH-24': {'CC-18', 'DD-19', 'JJ-16', 'EE-20', 'BB-17'},
 'HH-23': {'BB-16', 'DD-18', 'CC-17', 'JJ-15', 'EE-19'},
 'HH-22': {'BB-15', 'DD-17', 'CC-16', 'JJ-14', 'EE-18'},
 'HH-21': {'DD-16', 'CC-15', 'BB-14', 'EE-17', 'JJ-13'},
 'HH-20': {'BB-13', 'EE-16', 'JJ-12', 'DD-15', 'CC-14'},
 'HH-19': {'EE-15', 'JJ-11', 'DD-14', 'BB-12', 'CC-13'},
 'HH-18': {'EE-14', 'BB-11', 'JJ-10', 'CC-12', 'DD-13'},
 'HH-17': {'BB-10', 'EE-13', 'CC-11', 'DD-12', 'JJ-09'},
 'HH-16': {'JJ-08', 'DD-11', 'BB-09', 'EE-12', 'CC-10'},
 'HH-15': {'EE-11', 'BB-08', 'DD-10', 'JJ-07', 'CC-09'},
 'HH-14': {'BB-07', 'CC-08', 'EE-10', 'DD-09', 'JJ-06'},
 'HH-13': {'BB-06', 'JJ-05', 'EE-09', 'CC-07', 'DD-08'},
 'HH-12': {'CC-06', 'JJ-04', 'EE-08', 'DD-07', 'BB-05'},
 'HH-11': {'BB-04', 'EE-07', 'CC-05', 'DD-06', 'JJ-03'},
 'HH-10': {'BB-03', 'DD-05', 'JJ-02', 'EE-06', 'CC-04'},
 'HH-09': {'JJ-01', 'EE-05', 'DD-04', 'CC-03', 'BB-02'},
 'HH-08': {'EE-04', 'JJ-00', 'CC-02', 'BB-01', 'DD-03'},
 'HH-07': {'CC-01', 'EE-03', 'BB-00', 'DD-02'},
 'HH-06': {'CC-00', 'EE-02', 'DD-01'},
 'HH-05': {'DD-00', 'EE-01'},
 'HH-04': {'EE-00'},
 'DD-28': {'EE-26', 'CC-26', 'BB-25', 'JJ-24', 'HH-23'},
 'DD-25': {'CC-23', 'JJ-21', 'HH-20', 'BB-22', 'EE-23'},
 'DD-24': {'CC-22', 'JJ-20', 'HH-19', 'EE-22', 'BB-21'},
 'DD-23': {'EE-21', 'JJ-19', 'CC-21', 'HH-18', 'BB-20'},
 'DD-22': {'CC-20', 'JJ-18', 'EE-20', 'HH-17', 'BB-19'},
 'DD-21': {'JJ-17', 'BB-18', 'HH-16', 'CC-19', 'EE-19'},
 'DD-20': {'HH-15', 'CC-18', 'JJ-16', 'EE-18', 'BB-17'},
 'DD-19': {'BB-16', 'HH-14', 'EE-17', 'CC-17', 'JJ-15'},
 'DD-18': {'BB-15', 'EE-16', 'HH-13', 'CC-16', 'JJ-14'},
 'DD-17': {'EE-15', 'CC-15', 'BB-14', 'HH-12', 'JJ-13'},
 'DD-16': {'EE-14', 'BB-13', 'HH-11', 'JJ-12', 'CC-14'},
 'DD-15': {'EE-13', 'JJ-11', 'BB-12', 'CC-13', 'HH-10'},
 'DD-14': {'HH-09', 'BB-11', 'JJ-10', 'CC-12', 'EE-12'},
 'DD-13': {'BB-10', 'EE-11', 'HH-08', 'CC-11', 'JJ-09'},
 'DD-12': {'JJ-08', 'HH-07', 'EE-10', 'BB-09', 'CC-10'},
 'DD-11': {'BB-08', 'JJ-07', 'HH-06', 'EE-09', 'CC-09'},
 'DD-10': {'BB-07', 'CC-08', 'EE-08', 'JJ-06', 'HH-05'},
 'DD-09': {'BB-06', 'HH-04', 'EE-07', 'JJ-05', 'CC-07'},
 'DD-08': {'CC-06', 'HH-03', 'EE-06', 'JJ-04', 'BB-05'},
 'DD-07': {'EE-05', 'BB-04', 'HH-02', 'CC-05', 'JJ-03'},
 'DD-06': {'EE-04', 'BB-03', 'JJ-02', 'HH-01', 'CC-04'},
 'DD-05': {'JJ-01', 'CC-03', 'HH-00', 'EE-03', 'BB-02'},
 'DD-04': {'JJ-00', 'EE-02', 'CC-02', 'BB-01'},
 'DD-03': {'CC-01', 'EE-01', 'BB-00'},
 'DD-02': {'CC-00', 'EE-00'},
 'AA-30': {'EE-27', 'CC-27', 'JJ-27', 'BB-28', 'HH-24', 'DD-28'}
}


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

    def runner(self, location, time):
        for destination in self.tunnel[location].items():

            if self.visited[destination]:
                self.spice_must_flow(time, True)
                self.spice_must_flow(time, False)
                continue


          #  self.spice_must_flow(wait, True)
            self.visited[destination] = True

            self.runner(destination, distance)

            self.visited[destination] = False
           # self.spice_must_flow(wait, False)

    def start_running(self, start, distance):
        starting = timekey(start, distance)
        self.visited[start] = True
        self.runner(starting, distance)
        print(self.best)


run = Runner(maze_node, maze_valve, maze_tunnel)
run.start_running(START, DISTANCE)


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

