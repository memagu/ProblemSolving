blocks = int(input())
levels = [1]

itt = 1
while blocks >= sum(levels):
    levels.append((itt + 2) ** 2)
    itt += 2

print(len(levels) - 1)
