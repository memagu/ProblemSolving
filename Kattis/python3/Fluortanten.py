_ = input()

mul = 2
acc = 0
acc_diff = 0
max_diff = 0
for num in map(int, input().split()):
    if num == 0:
        continue

    acc += num * mul
    mul += 1

    acc_diff += -num
    max_diff = max(max_diff, acc_diff)

print(acc + max_diff)
