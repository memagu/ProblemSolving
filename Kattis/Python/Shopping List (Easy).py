# number_of_lists, number_of_items = list(map(int, input().split()))
#
# start_list = input().split()
# remaining_list = []
#
# for items in range(number_of_lists -1):
#     remaining_list += input().split()
#
# all_includes = []
#
# for item in start_list:
#     all_includes_temporary = []
#     for i in range(number_of_lists - 1):
#         if item in remaining_list[i * number_of_items:i * number_of_items + number_of_items]:
#             all_includes_temporary.append(item)
#             if len(all_includes_temporary) == number_of_lists - 1:
#                 all_includes.append(all_includes_temporary[0])
#                 break
#
# print(len(all_includes))
# for items in all_includes:
#     print(items)

# number_of_lists, _ = list(map(int, input().split()))
#
# checklist = input().split()
# checklist = set(checklist)
# to_remove = set()
#
# for i in range(number_of_lists - 1):
#     current_list = input().split()
#     for item in checklist:
#         if item not in current_list:
#             to_remove.add(item)
#
# for item in to_remove:
#     checklist.remove(item)
#
# checklist = list(checklist)
# checklist.sort()
#
# print(len(checklist))
# for item in checklist:
#     print(item)


# from functools import reduce
#
# number_of_lists, _ = list(map(int, input().split()))
# lists = []
#
# for i in range(number_of_lists):
#     lists.append(set(input().split()))
#
# result = reduce(lambda a, b: a.intersection(b), lists)
#
# result = list(result)
# result.sort()
#
# print(len(result))
# for item in result:
#     print(item)

n = int(input().split()[0])

for i in range(n):
    temp = []
    current = list(set(input().split()))
    if i == 0:
        previous = [*current]

    for item in previous:
        if item in current:
            temp.append(item)

    previous = [*temp]

print(len(previous))
for item in sorted(previous):
    print(item)
