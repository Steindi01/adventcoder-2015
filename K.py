import sys
import operator

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

output = ""
for i in range(0, len(my_input[0]) - 1, 2):
    cipher = my_input[0][i:i + 2]
    cipher_index = ord(cipher[0])
    cleartext_index = cipher_index - 3
    output += chr(cleartext_index)

print output