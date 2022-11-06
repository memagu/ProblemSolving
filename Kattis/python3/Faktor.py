# x = articles
# y = impact
# impact = total citations / total articles
# y = total citations / total articles
# y = total citations / x
# total citations = x * y

# 875 / 38 = 23.01 = 24
# 38 * 23 = 874
# 38 * 24 = 912

# citations / articles = impact
# citations = articles * impact

"""a, b = input().split()

x = int(a)

y = int(b)

min = y
cites = 0

first = True

for i in range(x * (y - 1), x * y):
    if first:
        first = False
        continue

    if i / x < min:
        cites = i
        min = i / x

print(cites)"""

a, b = input().split()

x = int(a)

y = int(b)

cites = x * (y - 1) + 1

print(cites)






