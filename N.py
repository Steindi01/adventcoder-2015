import sys

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

input_str = my_input[0]
input_str = input_str.replace("?", ".")
input_str = input_str.replace("!", ".")
errors = 0
sentences = input_str.split(". ")

if sentences[-1][-1] != ".":
    errors += 1
else:
    sentences[-1] = sentences[-1][:-1]

for s in sentences:
    if len(s) == 0:
        errors += 1
    else:
        if s[0] != s[0].upper():
            errors += 1
        for word in s.split(" "):
            if len(word) == 0:
                errors += 1
            else:
                for i in range(len(word)):
                    if (i >= 1) and (word[i] == word[i].upper()):
                        errors += 1
                    if word[i] == ".":
                        errors += 1

print errors
