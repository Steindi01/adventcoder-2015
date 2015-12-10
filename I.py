import sys
import copy
import math


def print_game(g):
    print get_robo_pos(g)
    for i in g:
        print i
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def get_fire(g):
    for i in g:
        for j in i:
            if j == "f":
                return True
    return False


def get_robo_pos(g):
    index_i = 0
    for i in g:
        index_j = 0
        for j in i:
            if j == "R":
                return [index_i, index_j]
            index_j += 1
        index_i += 1


def next_step(g):
    new_game = copy.deepcopy(g)
    for i in range(len(g)):
        for j in range(len(g[i])):
            dim_0 = len(g)
            dim_1 = len(g[i])
            if g[i][j] == "f":
                new_game[i][j] = "."
                try:
                    if g[i + 1][j] == "X" and (i + 1) >= 0:
                        new_game[i + 1][j] = "f"
                except:
                    pass
                try:
                    if g[i - 1][j] == "X" and (i - 1) >= 0:
                        new_game[i - 1][j] = "f"
                except:
                    pass
                try:
                    if g[i][j + 1] == "X" and (j + 1) >= 0:
                        new_game[i][j + 1] = "f"
                except:
                    pass
                try:
                    if g[i][j - 1] == "X" and (j - 1) >= 0:
                        new_game[i][j - 1] = "f"
                except:
                    pass

    return new_game


def robot_do_step(g, direction, p_robot):
    r_pos = get_robo_pos(g)

    if p_robot == "f":
        g[r_pos[0]][r_pos[1]] = "X"
    else:
        g[r_pos[0]][r_pos[1]] = p_robot

    temp_r_pos = r_pos
    if "N" in direction:
        temp_r_pos[0] -= 1
    if "S" in direction:
        temp_r_pos[0] += 1
    if "E" in direction:
        temp_r_pos[1] += 1
    if "W" in direction:
        temp_r_pos[1] -= 1
    p_robot = g[temp_r_pos[0]][temp_r_pos[1]]
    g[temp_r_pos[0]][temp_r_pos[1]] = "R"

    return (g, p_robot)


def robot_get_direction(g):
    r_pos = get_robo_pos(g)
    min_dist = 100
    temp_r_pos = [0, 0]
    index_i = 0
    for i in g:
        index_j = 0
        for j in i:
            if j == "f":
                delta_x = r_pos[0] - index_i
                delta_y = r_pos[1] - index_j
                if math.sqrt(delta_x**2 + delta_y ** 2) < min_dist:
                    min_dist = math.sqrt(delta_x**2 + delta_y ** 2)
                    temp_r_pos[0] = index_i
                    temp_r_pos[1] = index_j
            index_j += 1
        index_i += 1

    direction = ""
    if temp_r_pos[0] < r_pos[0]:
        direction += "N"
    if temp_r_pos[0] > r_pos[0]:
        direction += "S"
    if temp_r_pos[1] < r_pos[1]:
        direction += "W"
    if temp_r_pos[1] > r_pos[1]:
        direction += "E"
    
    return direction


def get_number_buildings(g):
    number = 0
    for i in g:
        for j in i:
            if j == "X":
                number += 1
    return number

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

dim = [int(my_input[0].split(",")[0]), int(my_input[0].split(",")[1])]
game = []

for i in range(dim[0]):
    game.append([])
    for j in range(len(my_input[i + 1])):
        game[i].append(my_input[i + 1][j])

#print_game(game)

prev_robot = "."
while get_fire(game):
    d = robot_get_direction(game)
    (game, prev_robot) = robot_do_step(game, d, prev_robot)
    game = next_step(game)
    # print_game(game)

n = get_number_buildings(game)
if prev_robot == "X" or prev_robot == "f":
    n += 1
print n, "buildings remaining"
