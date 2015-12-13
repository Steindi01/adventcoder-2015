import sys

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

input_str = my_input[0]
input_str = ''.join([i for i in input_str if i.isalpha()])
input_str = input_str.upper()

str_1 = ""
str_2 = ""
str_3 = ""
str_4 = ""

for i in range(len(input_str)):
    if (i % 6) == 0:
        str_1 += input_str[i]
    if (i % 6) == 1:
        str_2 += input_str[i]
    if (i % 6) == 2:
        str_3 += input_str[i]
    if (i % 6) == 3:
        str_4 += input_str[i]
    if (i % 6) == 4:
        str_3 += input_str[i]
    if (i % 6) == 5:
        str_2 += input_str[i]


output_str = str_1 + str_2 + str_3 + str_4
print output_str
