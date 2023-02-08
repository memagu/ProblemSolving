from collections import namedtuple
from random import shuffle

House = namedtuple("House", ("label", "x", "y"))


def distance(a: House, b: House) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


t, n = input(), int(input())

houses = []
for house_num in range(1, n + 1):
    x, y = map(int, input().split())

    houses.append(House(str(house_num), x, y))

houses.sort(key=lambda house: house.x + house.y)

house_amount = (len(houses) >> 1) - 1

min_interval = (0, sum(distance(houses[i], houses[i + 1]) for i in range(house_amount)))
interval_distance = min_interval[1]

for i in range(1, len(houses) >> 1):
    interval_distance += distance(houses[i + house_amount], houses[i + house_amount + 1]) - distance(houses[i - 1], houses[i])

    if interval_distance < min_interval[1]:
        min_interval = (i, interval_distance)

houses = houses[min_interval[0]:min_interval[0] + house_amount + 1]
min_houses = houses.copy()
min_houses_distance = min_interval[1]

for _ in range(256):
    shuffle(houses)
    house_distance = sum(distance(houses[i], houses[i + 1]) for i in range(house_amount))

    if house_distance < min_houses_distance:
        min_houses_distance = house_distance
        min_houses = houses.copy()

print(" ".join(house.label for house in min_houses))
