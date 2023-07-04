# a, b, c, d = map(int, input().split())
#
#
# def calc(x, y):
#     mul = ["*", x * y]
#     add = ["+", x + y]
#     sub = ["-", x - y]
#
#     try:
#         div = ["/", x // y]
#     except ZeroDivisionError:
#         div = ["/", None]
#
#     return mul, add, sub, div
#
#
# hits = []
#
# for i in range(4):
#     vl = calc(a, b)[i]
#     for j in range(4):
#         hl = calc(c, d)[j]
#         if vl[1] == hl[1] and not ((vl[0] == "/" and b == 0) or (hl[0] == "/" and c == 0)):
#             hits.append(f"{a} {vl[0]} {b} = {c} {hl[0]} {d}")
#
# if len(hits) == 0:
#     print("problems ahead")
# else:
#     for i in range(len(hits)):
#         print(hits[i])


from operator import add, floordiv, mul, sub

operators = (
    (mul, '*'),
    (add, '+'),
    (sub, '-'),
    (floordiv, '/')
)

a, b, c, d = map(int, input().split())

solution_found = False
for op_left, symbol_left in operators:
    if not b and op_left is floordiv:
        continue

    for op_right, symbol_right in operators:
        if not d and op_right is floordiv:
            continue

        if op_left(a, b) != op_right(c, d):
            continue

        solution_found = True
        print(f"{a} {symbol_left} {b} = {c} {symbol_right} {d}")

if not solution_found:
    print("problems ahead")
