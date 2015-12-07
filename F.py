import sys

def print_game(g):
    for i in g:
        print i

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

dim = int(my_input[0])
position = my_input[1].split(",")
pos = [int(position[1]), int(position[0])]

if not (0 in pos or (dim -1) in pos):
    game = [[0 for x in range(dim)] for x in range(dim)]

    for i in range(dim):
        for j in range(dim):
            game[i][j] = my_input[i + 2][j]

    direction = ""
    if game[pos[0] + 1][pos[1]] == " ":
        direction = "S"
    if game[pos[0] - 1][pos[1]] == " ":
        direction = "N"
    if game[pos[0]][pos[1] + 1] == " ":
        direction = "E"
    if game[pos[0]][pos[1] - 1] == " ":
        direction = "W"

    while True:
        if 0 in pos:
            break
        if (dim - 1) in pos:
            break
        
        if direction == "N":
            if game[pos[0] - 1][pos[1]] == " ":
                print "straight"
                direction = "N"
                pos = [pos[0] - 1, pos[1]]
            
            elif game[pos[0]][pos[1] + 1] == " ":
                print "right"
                direction = "E"
                pos = [pos[0], pos[1] + 1]
            
            elif game[pos[0]][pos[1] - 1] == " ":
                print "left"
                direction = "W"
                pos = [pos[0], pos[1] - 1]
        
        elif direction == "E":
            if game[pos[0]][pos[1] + 1] == " ":
                print "straight"
                direction = "E"
                pos = [pos[0], pos[1] + 1]
            
            elif game[pos[0] + 1][pos[1]] == " ":
                print "right"
                direction = "S"
                pos = [pos[0] + 1, pos[1]]
            
            elif game[pos[0] - 1][pos[1]] == " ":
                print "left"
                direction = "N"
                pos = [pos[0] - 1, pos[1]]
        
        elif direction == "S":
            if game[pos[0] + 1][pos[1]] == " ":
                print "straight"
                direction = "S"
                pos = [pos[0] + 1, pos[1]]
            
            elif game[pos[0]][pos[1] - 1] == " ":
                print "right"
                direction = "W"
                pos = [pos[0], pos[1] - 1]
            
            elif game[pos[0]][pos[1] + 1] == " ":
                print "left"
                direction = "E"
                pos = [pos[0], pos[1] + 1]
        
        elif direction == "W":
            if game[pos[0]][pos[1] - 1] == " ":
                print "straight"
                direction = "W"
                pos = [pos[0], pos[1] - 1]
            
            elif game[pos[0] - 1][pos[1]] == " ":
                print "right"
                direction = "N"
                pos = [pos[0] - 1, pos[1]]
            
            elif game[pos[0] + 1][pos[1]] == " ":
                print "left"
                direction = "S"
                pos = [pos[0] + 1, pos[1]]
