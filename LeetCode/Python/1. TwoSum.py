indices = {}
for i, num in enumerate(nums):
    indices[num] = i

for i, element in enumerate(nums):
    difference = target - element
    try:
        j = indices[difference]
        if j == i:
            continue
        return [i, j]
    except KeyError:
        continue
