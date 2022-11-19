"""
# O(nlog2(n))


piles_amount, piles = int(input()), list(map(int, input().split()))

extra_boxes_maximum = 2 ** piles_amount * max(piles) + 1
extra_boxes_minimum = -1

while (extra_boxes := (extra_boxes_maximum + extra_boxes_minimum) // 2) != extra_boxes_minimum:
    temp = piles.copy()
    temp[0] += extra_boxes

    for i in range(piles_amount - 1):
        if temp[i] < temp[i + 1]:
            extra_boxes_minimum = extra_boxes
            break

        if temp[i] - temp[i + 1] > 1:
            temp[i] = temp[i] + temp[i + 1] - (temp_at_next_i := (temp[i] + temp[i + 1]) // 2)
            temp[i + 1] = temp_at_next_i

    else:
        extra_boxes_maximum = extra_boxes

print((extra_boxes + 1) * (extra_boxes != -1))
"""


# O(n)


piles_amount, piles = int(input()), list(map(int, input().split()))
piles.append(piles[-1])

accumulated = 0
for i in range(piles_amount - 1, -1, -1):
    if piles[i] == piles[i + 1]:
        continue

    accumulated = max(2 * accumulated + piles[i + 1] - piles[i], 0)

print(accumulated)


"""
# O(n)


from functools import reduce


_ = input(), print(reduce(
    lambda acc, pile: ((pile, acc) if piles == acc[0] else (pile, max(2 * acc[1] + acc[0] - pile, 0))),
    reversed(piles := tuple(map(int, input().split()))),
    (piles[-1], 0))[1])

"""