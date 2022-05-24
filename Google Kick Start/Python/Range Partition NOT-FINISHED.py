def how_sum(target, arr, memo=None):
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for num in arr:
        temp = arr.copy()
        temp.remove(num)
        result = how_sum(target - num, temp)

        if result != None:
            memo[target] = [*result, num]
            return memo[target]

    return None


for testcase in range(1, int(input())+1):
    n, x, y = map(int, input().split())
    s = ((n**2 + n) / 2)

    rx = 1
    ry = y / x

    rs = s / (x+y)

    if not rs.is_integer():
        print(f"Case #{testcase}: IMPOSSIBLE")
        continue

    print(f"Case #{testcase}: POSSIBLE")
    nums = how_sum(rs, list(range(1, n+1)))
    print(len(nums))
    print(" ".join(list(map(str, nums))[::-1]))
