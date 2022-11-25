n, s = map(int, input().split())

trees = tuple(tuple(map(int, input().split())) for _ in range(n))

right = s
left = -1

while (mid := (left + right) // 2) != left:
    if sum((l + v * min(mid, t)) for l, v, t in trees) >= s:
        right = mid
        continue

    left = mid

print(mid + 1)

