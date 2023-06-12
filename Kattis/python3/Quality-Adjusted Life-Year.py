# https://open.kattis.com/problems/qaly
from math import prod

print(sum(prod(map(float, input().split())) for _ in range(int(input()))))
