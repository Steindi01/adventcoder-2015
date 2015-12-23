import sys
import math

my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

a = float(my_input[0].split(",")[0])
r = float(my_input[0].split(",")[1])


area = 0.0
diag = math.sqrt((a / 2) * (a / 2) + (a / 2) * (a / 2))

if r <= (a / 2):
    area = r**2 * math.pi
elif r >= diag:
    area = a * a
else:
    side_part = math.sqrt(r**2 - (a / 2)**2)
    area += 4 * (side_part * (a / 2))
    angle = math.radians(360)
    angle -= 8 * (math.acos((a / 2) / r))
    angle = math.degrees(angle)
    part_circle = (r**2) * math.pi
    part_circle *= (angle / 360)
    area += part_circle

print round(area, 2)
