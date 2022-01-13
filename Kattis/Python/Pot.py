acc = 0
for _ in range(int(input())):
    s = input()
    n = int(s[:-1])
    p = int(s[-1])
    acc += n ** p

print(acc)
