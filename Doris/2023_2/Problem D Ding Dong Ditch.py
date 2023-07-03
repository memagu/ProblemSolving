# import heapq
#
# _ = input()
#
# houses = list(map(int, input().split()))
# heapq.heapify(houses)
#
# for ambition in input().split():
#     to_readd = []
#     result = 0
#     for _ in range(int(ambition)):
#         to_readd.append(heapq.heappop(houses))
#         result += to_readd[-1]
#     for house in to_readd:
#         heapq.heappush(houses, house)
#     print(result)

from itertools import accumulate

_ = input()
anger_values = tuple(accumulate(sorted(map(int, input().split()))))

for friend in map(int, input().split()):
    print(anger_values[friend - 1])