import sys
from itertools import product

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

height = int(my_input[0])
starting_height = int(height / 2)
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

rows = []
for i in range(len(ceil)):
    r = {}
    r["g"] = ground[i]
    r["c"] = height - ceil[i]
    r["values"] = []
    rows.append(r)

rows[0]["values"] = [starting_height]

for i in range(1, len(rows)):
    for v in rows[i - 1]["values"]:
        if (v + 1) <= rows[i]["c"] and (v + 1) > rows[i]["g"] and (v + 1) not in rows[i]["values"]:
            rows[i]["values"].append(v + 1)
        if (v - 1) <= rows[i]["c"] and (v - 1) > rows[i]["g"] and (v - 1) not in rows[i]["values"]:
            rows[i]["values"].append(v - 1)

if diamond_height in rows[-1]["values"]:
    print "The bat reaches step", len(rows), "and gets the diamond"
else:
    max_step = 0
    for r in rows:
        if r["values"] != []:
            max_step += 1
    print "The bat reaches step", max_step

# if diamond:
#     print "The bat reaches step", max_dungeon, "and gets the diamond"
# else:
#     print "The bat reaches step", max_dungeon
