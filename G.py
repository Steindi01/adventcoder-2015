import sys


def print_game(g):
    for i in g:
        print i
weather = ["sun", "sun", "clouds", "overcast", "rain", "snow", "snow", "overcast", "overcast", "fog", "clouds", "sun", "clouds", "clouds",
           "sun", "sun", "sun", "sun", "clouds", "snow", "snow", "snow", "overcast", "clouds", "sun", "clouds", "sun", "fog", "clouds", "sun", "clouds"]
order = ["sun", "clouds", "overcast", "fog", "rain", "snow"]
my_input = []

for line in sys.stdin:
    line = line.replace("\r", "")
    line = line.replace("\n", "")
    my_input.append(line)

forecast = {}
for i in range(len(weather)):
    weather_array = ["", "", ""]
    weather_forecast = ""
    day0 = i - 2
    day1 = i - 1
    day2 = i
    day_forecast = i + 1
    if day0 >= 0:
        weather_array[0] = weather[day0]
    if day1 >= 0:
        weather_array[1] = weather[day1]
    if day2 >= 0:
        weather_array[2] = weather[day2]
    if day_forecast < len(weather):
        weather_forecast = weather[day_forecast]

    if tuple(weather_array) in forecast.keys():
        try:
            forecast[tuple(weather_array)][weather_forecast] += 1
        except Exception, e:
            forecast[tuple(weather_array)][weather_forecast] = 1
    else:
        forecast[tuple(weather_array)] = {}
        forecast[tuple(weather_array)][weather_forecast] = 1

question = []
for element in my_input[0].split(","):
    question.append(element)

if tuple(question) in forecast.keys():
    answer = forecast[tuple(question)]
    answer_string = []
    for element in order:
        if element in answer:
            answer_string.append(element)
    print ",".join(answer_string)
else:
    print ",".join(order)
