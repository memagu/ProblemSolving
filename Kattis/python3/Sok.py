a, b, c = map(int, input().split())
i, j, k = map(int, input().split())


def sok(a, b, c, i, j, k):
    f_a = a / i
    f_b = b / j
    f_c = c / k

    fractions = [f_a, f_b, f_c]

    max_juice = 0
    max_fraction = 0

    for fraction in fractions:
        amt_a = round(fraction * i, 10)
        amt_b = round(fraction * j, 10)
        amt_c = round(fraction * k, 10)

        if amt_a > a or amt_b > b or amt_c > c:
            continue

        juice = amt_a + amt_b + amt_c

        if juice > max_juice:
            max_juice = juice
            max_fraction = fraction

    return a - i * max_fraction, b - j * max_fraction, c - k * max_fraction


def sok_cpp(a, b, c, i, j, k):
    f_a = a / i
    f_b = b / j
    f_c = c / k

    f = f_a if f_a < f_b and f_a < f_c else f_b if f_b < f_c else f_c

    return a - i * f, b - j * f, c - k * f


print(*sok(a, b, c, i, j, k))
