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
splits = [i for i in range(len(input_str)) if input_str.startswith('.', i)]

sentences = []
last_start = 0
for i in splits:
    if i + 1 == len(input_str):
        sentences.append(input_str[last_start:i + 1])
        break

    if input_str[i + 1] == " ":
        sentences.append(input_str[last_start:i + 1])
        last_start = i + 2

if splits[-1] + 1 != len(input_str):
    sentences.append(input_str[last_start:len(input_str)])

for s in sentences:
    if s[-1] != ".":
        errors += 1
    if s[0] != s[0].upper():
        errors += 1

    words = s[:-1].split(" ")
    for w in words:
        for i in range(len(w)):
            if w[i] == ".":
                errors += 1
            if i > 0 and w[i] == w[i].upper():
                errors += 1

        if len(w) == 0:
            errors += 1


print errors
