x = int(input())
n = int(input())
mb = [int(input()) for month in range(n)]

Z = x
for p in mb:
    Z += -p + x

print(Z)