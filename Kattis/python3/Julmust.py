r_min, r_max = 1, int(input()) * 2

for day in range(1, 86):
    mid = (r_min + r_max) // 2

    print(mid * day, flush=True)

    response = input()

    if response == "less":
        r_max = mid
        continue

    if response == "more":
        r_min = mid
        continue

    if response == "exact":
        break
