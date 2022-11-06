n, w, h = map(int, input().split())
d = (w ** 2 + h ** 2) ** 0.5

for i in range(n):
    inp = int(input())
    if inp <= w or inp <= h or inp <= d:
        print("DA")
    else:
        print("NE")
