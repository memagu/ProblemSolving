n = int(input())

total_length = 0
for _ in range(n):
    total_length += int(input())

print(total_length - n + 1)