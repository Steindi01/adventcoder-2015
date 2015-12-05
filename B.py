import sys

my_input = []

for line in sys.stdin:
	my_input.append(line)

s1 = my_input[0]
s1 = s1.replace(" ", "")
s2 = my_input[1]
s2 = s2.replace(" ", "")

s1_count = {}
s2_count = {}

for i in s1:
	try:
		s1_count[i] += 1
	except Exception, e:
		s1_count[i] = 1

for i in s2:
	try:
		s2_count[i] += 1
	except Exception, e:
		s2_count[i] = 1

if s1_count == s2_count:
	print "Anagram"
else:
	print "No anagram"