import sys
import copy


def print_game(g):
    for i in g:
        print i
    print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def get_fire(g):
    for i in g:
        for j in i:
            if j == "f":
                return True
    return False


def next_step(g, robot):
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

print_game(game)

prev_robot = "."
while get_fire(game):
    game = next_step(game, ("N", prev_robot))
    print_game(game)
