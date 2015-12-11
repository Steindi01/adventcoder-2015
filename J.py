import sys
import re

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

result = map(list, zip(*my_input))
final_result = []
for i in range(len(result)):
	temp_res = result[i]
	temp_res = ''.join(temp_res)
	temp_res = ' '.join(temp_res.split())
	final_result.append(temp_res)

try:
	final_result.remove([""])
except:
	pass
for i in final_result:
	print i
