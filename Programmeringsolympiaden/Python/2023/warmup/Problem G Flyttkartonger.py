
"""
piles_amount, piles = int(input()), list(map(int, input().split()))

extra_boxes = 260

while True:
    temp = piles.copy()
    temp[0] += extra_boxes

    for i in range(piles_amount - 1):
        if temp[i] < temp[i + 1]:
            extra_boxes += 1
            break

        if temp[i] - temp[i + 1] > 1:
            temp[i] = temp[i] + temp[i + 1] - (temp_at_next_i := (temp[i] + temp[i + 1]) // 2)
            temp[i + 1] = temp_at_next_i

    else:
        print(temp)
        break

print(extra_boxes)

"""

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
