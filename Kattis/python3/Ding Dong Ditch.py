from itertools import accumulate

_ = input()
anger_values = tuple(accumulate(sorted(map(int, input().split()))))

for friend in map(int, input().split()):
    print(anger_values[friend - 1])