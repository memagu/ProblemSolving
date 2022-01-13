
set = set()

for i in range(int(input())):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        set.add(j)

print(len(set))
