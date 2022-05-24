n = 3
x = 1
y = 1

for i in range(1, n+1):
    s = sum(range(1, i+1))
    print(i, s, ((i+1)/2 * i), round(s/(x+y), 2))

