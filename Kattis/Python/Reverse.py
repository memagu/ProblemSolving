
integers = []

for i in range(int(input())):
    integers.append(input())

for i in range(len(integers)):
    print(integers[(i + 1) * -1])

