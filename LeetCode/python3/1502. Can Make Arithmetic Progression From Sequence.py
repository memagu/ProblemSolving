from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return True

        next_max, next_min = max(arr), min(arr)

        if (next_max - next_min) % (len(arr) - 1) != 0:
            return False

        diff = (next_max - next_min) / (len(arr) - 1)

        arr = set(arr)

        while next_max > next_min:
            next_max -= diff
            next_min += diff

            if not (next_max in arr and next_min in arr):
                return False

        return True



if __name__ == "__main__":
    print(Solution().canMakeArithmeticProgression([3, 5, 1]))
    print(Solution().canMakeArithmeticProgression([1, 2, 4]))
