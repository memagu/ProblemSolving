from functools import reduce

arr = [1,2,3,4]

result = reduce(lambda a, b: a * b, arr)

print(result)

