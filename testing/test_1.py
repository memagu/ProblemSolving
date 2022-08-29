def func(x):
    res = 0
    for i in range(x):
        res += i
    return res


def func2(x):
    return sum(i for i in range(x))

print(func2(4))