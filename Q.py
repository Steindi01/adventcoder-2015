import sys

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

number_bunnies = int(my_input[0].split(" ")[0])
number_foxes = int(my_input[0].split(" ")[1])
number_days = int(my_input[0].split(" ")[2])

bunnie_babies = []
dying_foxes = 0
dying_bunnies = 0

for i in range(1, number_days + 1):
    number_foxes -= dying_foxes
    dying_foxes = 0
    # number_bunnies -= dying_bunnies
    # dying_bunnies = 0
    for j in reversed(range(len(bunnie_babies))):
        bunnie_babies[j] -= 1
        if bunnie_babies[j] == 0:
            bunnie_babies.pop(j)
            number_bunnies += 1
    if i % 15 == 0 and i > 0:
        for j in range(number_bunnies):
            bunnie_babies.append(31)
    if i % 20 == 0 and i > 0:
        number_foxes = number_foxes * 2
    if i % 10 == 0 and i > 0:
        half_bunnies = int(number_bunnies / 2)
        if number_foxes > half_bunnies:
            dying_bunnies = half_bunnies
        else:
            dying_bunnies = number_foxes

        if dying_bunnies < number_foxes:
            dying_foxes = (number_foxes - dying_bunnies)

        number_bunnies -= dying_bunnies
    print number_bunnies, number_foxes, bunnie_babies, i
