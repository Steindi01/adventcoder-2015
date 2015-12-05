import sys
import math

def calc_price(n, i, p):
    if n <= 4:
        index = 0
    elif n <= 9:
        index = 1
    elif n <= 99:
        index = 2
    else:
        index = 3
     
    value = 10
    return int(value)

prices_str = """Teddy Bear	5 Euro	5 Euro	4 Euro	4 Euro
LBGT Barbie	55 Euro	49 Euro	39 Euro	35 Euro
Train	25 Euro	25 Euro	22 Euro	19 Euro
OGLE (TM)	125 Euro	99 Euro	79 Euro	69 Euro
Star Trek Lightsaber	75 Euro	73 Euro	69 Euro	68 Euro"""
prices = {}
for line in prices_str.split("\n"):
    line = line.split("\t")
    prices[line[0]] = []
    for element in line[1:]:
        prices[line[0]].append(int(element.replace(" Euro", "")))

my_input = []

for line in sys.stdin:
    my_input.append(line.replace("\n", ""))

sum_price = 0
for i in my_input[1:]:
    index = i.index(" ")
    number = int(i[0:index])
    item = i[index+1:]
    if item.endswith("s"):
        item = item[:-1]
    sum_price += calc_price(number, item, prices)

print sum_price, "Euro"
