import sys
import math

def calc_price(n, i, p):
    minimum_number = [1, 5, 10, 100]
    if n <= 4:
        index = 0
    elif n <= 9:
        index = 1
    elif n <= 99:
        index = 2
    else:
        index = 3
    if index == 3:
        return int(n * p[i][index])
    else:
        real_amount = int(n * p[i][index])
        virtual_amount = int(minimum_number[index+1] * p[i][index+1])
        if real_amount < virtual_amount:
            return real_amount
        else:
            return virtual_amount

prices = {}
prices["Teddy Bear"] = [5, 5, 4, 4]
prices["LBGT Barbie"] = [55, 49, 39, 35]
prices["Train"] = [25, 25, 22, 19]
prices["OGLE (TM)"] = [125, 99, 79, 69]
prices["Star Trek Lightsaber"] = [75, 73, 69, 68]

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

sum_price = 0
num_products = int(my_input[0])
for i in my_input[1:num_products+1]:
    index = i.index(" ")
    number = int(i[0:index])
    item = i[index+1:]
    if item.endswith("s"):
        item = item[:-1]
    sum_price += calc_price(number, item, prices)

print sum_price, "Euro"
