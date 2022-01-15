n, e = map(int, input().split())

nums = [str(x) for x in range(1, n+1)]
hits = 0

for num in nums:
    if str(2**e) in num:
        hits += 1

print(hits)