
import math

for test_cases in range(int(input())):
    x = 0
    y = 0
    rotation = 0
    for instructions in range(int(input())):
        rotation_input, distance = list(map(float, input().split()))
        rotation += rotation_input * math.pi / 180
        x += math.sin(rotation) * distance * -1
        y += math.cos(rotation) * distance
    print(str(x) + " " + str(y))
