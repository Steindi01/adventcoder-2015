import sys
import math

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

santa = int(my_input[0].split(",")[0])
santa_inc = int(my_input[0].split(",")[1])
supplier = int(my_input[0].split(",")[2])
supplier_dec = int(my_input[0].split(",")[3])

i = 0
while True:
    if i % 2 == 1:
        supplier -= supplier_dec
        if supplier <= santa:
            print santa
            break
    else:
        santa += santa_inc
        if santa >= supplier:
            print supplier
            break

    i += 1
