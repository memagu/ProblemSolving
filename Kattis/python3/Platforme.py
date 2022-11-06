# import operator
#
# number_of_platforms = int(input())
# platformY = []
# platformX = []
#
# for i in range(number_of_platforms):
#     y, x1, x2 = map(int, input().split())
#     platformY.append(y)
#     platformX.append(list(range(x1, x2+1)))
#
# platformYX = zip(platformY, platformX)
# platformX = sorted(platformYX, key=operator.itemgetter(0))
# platformYX = list(zip(*platformX))
#
# pillar_length = platformYX[0][0]
#
# for i in range(1, number_of_platforms - 1):
#     if platformYX[1][i][0] in platformYX[1][i-1] or platformYX[1][i][-1] in platformYX[1][i-1]:
#         print(platformYX[1][i][0])
#
#
# print(platformYX)

from operator import itemgetter
from sys import maxsize

number_of_platforms = int(input())

platforms = [(0, 0, maxsize)]

for i in range(number_of_platforms):
    platforms.append(tuple(map(int, input().split())))


platforms = sorted(platforms, key=itemgetter(0), reverse=True)


def pillars(y, x1, x2, other_platforms):

    left = y - next(filter(lambda t: t[1] < (x1 + 0.5) < t[2], other_platforms))[0]
    right = y - next(filter(lambda t: t[1] < (x2 - 0.5) < t[2], other_platforms))[0]

    return left + right


total = 0

for i in range(number_of_platforms):
    total += pillars(*platforms[i], platforms[i + 1:])


print(total)
