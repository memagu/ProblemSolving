n = int(input())
preference = 2 if input() == "antal" else 3

candidates = [(-1, -1, -1, -1)]  # [(index, combined, amount, size), ...]

for i in range(1, n + 1):
    amount, size = map(int, input().split())
    combined = amount + size

    if combined > candidates[0][1]:
        candidates = [(i, combined, amount, size)]
        continue

    if combined == candidates[0][1]:
        candidates.append((i, combined, amount, size))

print(max(candidates, key=lambda x: x[preference])[0])
