abc = list(map(int, input().split()))

if abc[1] - abc[0] > abc[2] - abc[1]:
    print(abc[1] - abc[0] - 1)
else:
    print(abc[2] - abc[1] - 1)
