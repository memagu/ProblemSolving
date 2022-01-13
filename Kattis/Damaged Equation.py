a, b, c, d = map(int, input().split())


def calc(x, y):
    mul = ["*", x * y]
    add = ["+", x + y]
    sub = ["-", x - y]

    try:
        div = ["/", x // y]
    except ZeroDivisionError:
        div = ["/", None]

    return mul, add, sub, div


hits = []

for i in range(4):
    vl = calc(a, b)[i]
    for j in range(4):
        hl = calc(c, d)[j]
        if vl[1] == hl[1] and not ((vl[0] == "/" and b == 0) or (hl[0] == "/" and c == 0)):
            hits.append(f"{a} {vl[0]} {b} = {c} {hl[0]} {d}")

if len(hits) == 0:
    print("problems ahead")
else:
    for i in range(len(hits)):
        print(hits[i])