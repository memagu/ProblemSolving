a, b, c = map(int, input().split())
i, j, k = map(int, input().split())

f_a = a / i
f_b = b / j
f_c = c / k

fractions = [f_a, f_b, f_c]

max_juice = 0
max_fraction = 0

for fraction in fractions:
    amt_a = fraction * i
    amt_b = fraction * j
    amt_c = fraction * k

    if amt_a > a or amt_b > b or amt_c > c:
        continue

    juice = amt_a + amt_b + amt_c

    if juice > max_juice:
        max_juice = juice
        max_fraction = fraction

print(max_fraction)
print(max_juice)

print(a - i * max_fraction, b - j * max_fraction, c - k * max_fraction)





