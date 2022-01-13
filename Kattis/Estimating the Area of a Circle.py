import math

while True:
    r, m, c = map(float, input().split())
    if set((r, m, c)) == {0}:
        break

    print(r ** 2 * math.pi, (c / m) * 4 * r ** 2)

