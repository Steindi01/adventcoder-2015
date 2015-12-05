import sys
import math


class slope(object):

    length = 0
    width = 0
    inclination = 0

    def getValues(self):
        values = self.arg.split(",")
        self.length = float(values[0])
        self.width = float(values[1])
        self.inclination = float(values[2])

    def calc(self):
        total_length = self.length
        angle = math.radians(self.inclination)
        gk = self.width
        hyp = gk / math.sin(angle)
        ak = hyp * math.cos(angle)
        full_slopes = 0
        while total_length > ak:
            full_slopes += 1
            total_length -= ak
        return round(full_slopes * hyp + (total_length/ak) * hyp)

    """docstring for slope"""

    def __init__(self, arg):
        super(slope, self).__init__()
        self.arg = arg
        self.getValues()


my_input = []

for line in sys.stdin:
    my_input.append(line.replace("\n", ""))

sum = 0
for i in my_input[1:]:
    current_slope = slope(i)
    sum += current_slope.calc()

print int(sum)
