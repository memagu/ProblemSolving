diffcount = 0
p1, p2 = input(), input()
for i in range(4):
    if p1[i] != p2[i]:
        diffcount += 1
print(2 ** diffcount)