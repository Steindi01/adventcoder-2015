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

def next_step(g, dim, robot):
    new_game = copy.deepcopy(g)
    for i in range(dim[0]):
        for j in range(dim[1]):
            if g[i][j] == "f":
                new_game[i][j] = "."
                if (i + 1) in range(dim[0]):
                    if g[i+1][j] == "X":
                        new_game[i+1][j] = "f"
                if (i - 1) in range(dim[0]):
                    if g[i-1][j] == "X":
                        new_game[i-1][j] = "f"
                if (j + 1) in range(dim[1]):
                    if g[i][j+1] == "X":
                        new_game[i][j+1] = "f"
                if (j - 1) in range(dim[1]):
                    if g[i][j-1] == "X":
                        new_game[i][j-1] = "f"
                        


    return new_game


my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

dim = [int(my_input[0].split(",")[0]), int(my_input[0].split(",")[1])]
game = [[0 for x in range(dim[1])] for x in range(dim[0])]

for i in range(dim[0]):
    for j in range(dim[1]):
        game[i][j] = my_input[i + 1][j]

print_game(game)

while get_fire(game):
    game = next_step(game, dim, "N")
    print_game(game)