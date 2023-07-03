# while True:
#     try:
#         n = list(map(int, input().split("/")))[1]
#         n = int(n)
#         count = 0
#
#         for x in range(n + 1, n * 2 + 1):
#             numerator = x - n
#             denominator = x * n
#             if denominator % numerator == 0:
#                 print(f"1/{x} + 1/{denominator // numerator} = 1/{n}")
#                 count += 1
#         print(count)
#
#     except EOFError:
#         break


# a   c   ad   bc       b * d
# - - - = -- - --  ==>  -mod-
# b   d   bd   bd       d - b


# while True:
#     try:
#         n = int(input()[2:])
#         count = 0
#
#         for x in range(n + 1, n * 2 + 1):
#             numerator = x - n
#             denominator = x * n
#             if denominator % numerator == 0:
#                 # print(f"1/{x} + 1/{denominator // numerator} = 1/{n}")
#                 count += 1
#         print(count)
#
#     except EOFError:
#         break


# while True:
#     try:
#         n = int(input()[2:])
#         count = 0
#
#         for x in range(n + 1, n * 2 + 1):
#             if (x * n) % (x - n) == 0:
#                 # print(f"1/{x} + 1/{denominator // numerator} = 1/{n}")
#                 count += 1
#         print(count)
#
#     except EOFError:
#         break


while True:
    try:
        (lambda n: print(sum(not (x * n) % (x - n) for x in range(n + 1, n * 2 + 1))))(int(input()[2:]))
    except EOFError:
        break
