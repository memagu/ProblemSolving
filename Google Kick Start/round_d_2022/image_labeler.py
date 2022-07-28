from typing import List


def median(arr: List[int]):
    if not len(arr):
        return

    arr.sort()
    if len(arr) % 2:
        return arr[(len(arr) - 1) // 2]

    return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2


test_cases = int(input())

for test_case in range(1, test_cases + 1):
    _, categories = map(int, input().split())
    region_participants = list(sorted(map(int, input().split())))

    result = 0
    for i in range(categories - 1):
        result += region_participants.pop()
    result += median(region_participants)

    print(f"Case #{test_case}: {result}")

"""
1 2 3 4

12 34 = 1.5 + 3.5 = 5
13 24 = 2 + 3 = 5
14 23 = 2.5 + 2.5 = 5
123 4 = 2 + 4 = 6
124 3 = 2 + 3 = 5
134 2 = 3 + 2 = 5
234 1 = 3 + 1 = 4

12345

12 + 34 + 5 = 1.5 + 3.5 + 5
123 + 4 + 5 = 2 + 4 + 5

list = [0, 2, 1, 3]

list.sort() -> list = [0, 1, 2 ,3]

a = sorted(list) -> list = [0, 2, 1, 3], a = [0, 1, 2 ,3]

[0, 1, 2 ,3]

"1"
"3 2"
"11 24 10" -> ["11", "24", "10"] -> [11, 24, 10] -> [10, 11, 24] -> [24, [10, 11]]
input         split()               int()           sort()          result

"""