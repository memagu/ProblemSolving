import math

while True:
    try:
        r, x, y = map(float, input().split())
        h = (x ** 2 + y ** 2) ** 0.5
        if h > r:
            print("miss")
            continue

        circle_area = r * r * math.pi
        angle = math.acos(h / r)
        triangle_base = math.sin(angle) * r
        triangle_area = triangle_base * h

        small_area = ((2 * angle) / (math.pi * 2)) * circle_area - triangle_area
        big_area = ((math.pi * 2 - 2 * angle) / (math.pi * 2)) * circle_area + triangle_area

        print(big_area, small_area)

    except EOFError:
        break
