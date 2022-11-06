n, k = map(int, input().split())

result = set()

for i in range(2, n + 1):
    result.add(i)
    if len(result) == k:
        print(i)
        quit()

    for j in range(i+i, n+1, i):
        result.add(j)
        if len(result) == k:
            print(j)
            quit()
