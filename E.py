import sys
from itertools import product

def checkGame(height, starting_height, diamond_height, ground, ceil, length_dungeon, path):
    steps = 1
    current_position = starting_height
    for i in range(len(path)):
        current_position += path[i]
        if current_position > (height - ceil[i+1]):
            return (steps, False)
        if current_position <= ground[i+1]:
            return (steps, False)
        steps += 1

    if current_position == diamond_height:
        return (steps, True)
    else:
        return (steps, False)

def binToList(bin_string, length):
    path = []
    for i in bin_string:
        if i == "0":
            path.append(-1)
        if i == "1":
            path.append(1)
    while len(path) < length:
        path.append(-1)
    return path

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

height = int(my_input[0])
starting_height = int(height/2)
diamond_height = 0
ground = []
ceil = []
length_dungeon = 0

for i in my_input[1:]:
    try:
        diamond_height = int(i)
        break
    except Exception, e:
        i = i.split(",")
        ground.append(int(i[0]))
        ceil.append(int(i[1]))

length_dungeon = len(ceil)

max_dungeon = 1
diamond = False

i = 0
while i < (2**(length_dungeon - 1) - 1):
    p_binary = "{0:b}".format(i)
    p = binToList(p_binary, length_dungeon-1)
    (d, dia) = checkGame(height, starting_height, diamond_height, ground, ceil, length_dungeon, p)
    if dia:
        diamond = True
    if d > max_dungeon:
        max_dungeon = d
    if dia and max_dungeon == length_dungeon:
        break
    p_binary1 = p_binary
    p_binary2 = "{0:b}".format(i + 1)
    while len(p_binary1) < (length_dungeon - 1):
        p_binary1 = p_binary1 + "0"
    while len(p_binary2) < (length_dungeon - 1):
        p_binary2 = p_binary2 + "0"
    i += int(p_binary2, 2) - int(p_binary1, 2)
    #print i

if diamond:
    print "The bat reaches step", max_dungeon, "and gets the diamond"
else:
    print "The bat reaches step", max_dungeon

