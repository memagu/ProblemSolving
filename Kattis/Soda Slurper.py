
e, f, c = map(int, input().split())

total = 0

empty_bottles = e + f
while empty_bottles >= c:

    empty_bottles -= c
    total += 1
    empty_bottles += 1

print(total)
