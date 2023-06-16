from math import gcd

# F = 9 / 5 * C + 32
# C = (F - 32) * 5 / 9

divisor, dividend = map(int, input().split('/'))
divisor = (divisor - 32 * dividend) * 5
if divisor == 0:
    print("0/1")
    exit()

dividend *= 9
common_factor = gcd(dividend, divisor)

print('/'.join(map(lambda x: str(x // common_factor), (divisor, dividend))))
