#
# def modulo(number, mod_by):
#     while number >= mod_by:
#         number -= mod_by
#     return number
#
#
# number_set = set()
#
# for i in range(10):
#     number_set.add(modulo(int(input()), 42))
#
#
# print(len(number_set))

print(len(set(int(input()) % 42 for i in range(10))))