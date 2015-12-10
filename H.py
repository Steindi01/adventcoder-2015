import sys
import math

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

numbers = [float(my_input[0].split(" ")[0]), float(my_input[0].split(" ")[1])]

size = math.sqrt(2 * (numbers[0] * numbers[0])) + 1.5 * numbers[1]
size = int(math.ceil(size))

print "You need a paper of size " + str(size) + " times " + str(size) + "."
