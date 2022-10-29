# target, _, lengths = int(input()), input(), tuple(map(int, input().split()))
#
# combinations = [[(length, i)] for i, length in enumerate(lengths)]
#
# for i, num in enumerate(lengths):
#     sub_target = target / num
#
#     for j, num_2 in enumerate(lengths):
#         if i == j:
#             continue
#
#         if num_2 >= sub_target:
#             combinations[i].append((num_2, j))
#
# combinations.sort(key=len)
#
# count = 0
# used = set()
#
# for combination in combinations:
#     if len(combination) == 1:
#         continue
#
#     for i, num in enumerate(combination):
#         if num in used and not i:
#             break
#
#         if num in used or not i:
#             continue
#
#         count += 1
#         used.update((combination[0], num))
#         break
#
# print(count)

# target, n, lengths = int(input()), int(input()), sorted(tuple(map(int, input().split())))
#
# count = 0
# left, right = 0, n - 1
#
# while left < right:
#     if lengths[left] * lengths[right] < target:
#         left += 1
#         continue
#
#     left += 1
#     right -= 1
#
#     count += 1
#
# print(count)



