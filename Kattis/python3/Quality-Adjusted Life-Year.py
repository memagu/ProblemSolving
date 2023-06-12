# https://open.kattis.com/problems/qaly
import math

print(sum(math.prod(map(float, input().split())) for _ in range(int(input()))))
