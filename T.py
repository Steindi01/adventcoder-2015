import sys

game = {}
game["left"] = False
game["middle"] = False
game["right"] = False


def swap(a, b):
    temp = game[b]
    game[b] = game[a]
    game[a] = temp


def move(a, b):
    if a == b:
        return
    if b == "left":
        if a == "middle":
            swap("left", "middle")
            return
        if a == "right":
            swap("middle", "right")
            swap("left", "middle")
            return
    if b == "middle":
        if a == "left":
            swap("left", "middle")
            return
        if a == "right":
            swap("middle", "right")
            return
    if b == "right":
        if a == "left":
            swap("left", "middle")
            swap("middle", "right")
            return
        if a == "middle":
            swap("middle", "right")
            return

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)


game[my_input[0]] = True

i = 0
while True:
    if my_input[i].startswith("Where is it?"):
        break
    try:
        line = my_input[i].split(" ")
    except:
        line = [""]
    if line[0] == "swap":
        swap(line[1], line[3])
    if line[0] == "move":
        move(line[1], line[4])
    i += 1


for k in game:
    if game[k] == True:
        print k
