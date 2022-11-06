_ = input()
temps = list(map(int, input().split()))

count = 0
for temp in temps:
    if temp < 0:
        count += 1

print(count)
