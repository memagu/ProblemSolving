c = float(input())
l = int(input())
z = 0
for _ in range(l):
    w, h = map(float, input().split())
    z += w * h * c

print(z)
