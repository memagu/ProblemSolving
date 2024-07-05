import decimal

a, b, c = map(decimal.Decimal, input().split())
print(a * b / c)
