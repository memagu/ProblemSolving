from collections import deque, namedtuple

House = namedtuple("House", ("label", "x", "y"))


def distance(a: House, b: House) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)


t, n = input(), int(input())

houses = []
for house_num in range(1, n + 1):
    x, y = map(int, input().split())

    houses.append(House(str(house_num), x, y))

houses.sort(key=lambda house: house.x + house.y)

median = len(houses) >> 1
left = median - 1
right = median + 1

result = deque((houses[median],))
for _ in range(median - 1):
    left_dist = right_dist = float("inf")

    if left >= 0:
        left_dist = distance(result[0], houses[left])

    if right < len(houses):
        right_dist = distance(result[-1], houses[right])

    if left_dist <= right_dist:
        result.appendleft(houses[left])
        left -= 1
        continue

    result.append(houses[right])
    right += 1

print(" ".join(house.label for house in result))
