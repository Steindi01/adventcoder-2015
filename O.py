import sys


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return []
    shortest = []
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def get_first_direction(p0, p1):
    if p1[0] < p0[0]:
        return "N"
    if p1[0] > p0[0]:
        return "S"
    if p1[1] < p0[1]:
        return "W"
    if p1[1] > p0[1]:
        return "E"

def get_direction_N(p0, p1):
    if p1[0] < p0[0]:
        print "straight"
        return "N"
    if p1[1] < p0[1]:
        print "left"
        return "W"
    if p1[1] > p0[1]:
        print "right"
        return "E"

def get_direction_E(p0, p1):
    if p1[0] < p0[0]:
        print "left"
        return "N"
    if p1[0] > p0[0]:
        print "right"
        return "S"
    if p1[1] > p0[1]:
        print "straight"
        return "E"

def get_direction_S(p0, p1):
    if p1[0] > p0[0]:
        print "straight"
        return "S"
    if p1[1] < p0[1]:
        print "right"
        return "W"
    if p1[1] > p0[1]:
        print "left"
        return "E"

def get_direction_W(p0, p1):
    if p1[0] < p0[0]:
        print "right"
        return "N"
    if p1[1] < p0[1]:
        print "straight"
        return "W"
    if p1[0] > p0[0]:
        print "left"
        return "S"

def print_wordy_path(p):
    direction = get_first_direction(p[0], p[1])
    for i in range(1, len(p)):
        #print p[i], direction
        if direction == "N":
            direction = get_direction_N(p[i - 1], p[i])
            next
        elif direction == "E":
            direction = get_direction_E(p[i - 1], p[i])
            next
        elif direction == "S":
            direction = get_direction_S(p[i - 1], p[i])
            next
        elif direction == "W":
            direction = get_direction_W(p[i - 1], p[i])
            next
my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

dim = int(my_input[0])
position = my_input[1].split(",")
pos = [int(position[1]), int(position[0])]

game = [[0 for x in range(dim)] for x in range(dim)]

for i in range(dim):
    for j in range(dim):
        game[i][j] = my_input[i + 2][j]


endpos = {}
paths = {}

for i in range(dim):
    for j in range(dim):
        if game[i][j] == " ":
            if i == 0 or i == (dim - 1) or j == 0 or j == (dim - 1):
                endpos[(i, j)] = {}
            paths[(i, j)] = []
            if (i - 1) >= 0:
                if game[i - 1][j] == " ":
                    paths[(i, j)].append((i - 1, j))
            if (j - 1) >= 0:
                if game[i][j - 1] == " ":
                    paths[(i, j)].append((i, j - 1))
            if (i + 1) < dim:
                if game[i + 1][j] == " ":
                    paths[(i, j)].append((i + 1, j))
            if (j + 1) < dim:
                if game[i][j + 1] == " ":
                    paths[(i, j)].append((i, j + 1))

for e in endpos:
    s = (pos[0], pos[1])
    endpos[e]["path"] = find_shortest_path(paths, s, e)
    endpos[e]["length"] = len(endpos[e]["path"])

best_route = []
best_length = 100000
for e in endpos:
    if endpos[e]["length"] < best_length:
        best_route = endpos[e]["path"]
        best_length = len(best_route)

if best_length == 2:
    print "straight"
elif best_length > 2:
    print_wordy_path(best_route)
