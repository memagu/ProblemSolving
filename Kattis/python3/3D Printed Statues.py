"""
required_statues = int(input())
printers = 1
days = 0

while printers < required_statues:
    printers *= 2
    days += 1

print(days + 1)
"""


from math import ceil, log2

print(ceil(log2(int(input()))) + 1)
