from typing import List

from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        values = defaultdict(int)
        for num in nums:
            values[num] += num

        nums = sorted(list(set(nums)))

        a, b = 0, 0
        for i in range(len(nums)):
            current_value = values[nums[i]]

            if not i or nums[i] - nums[i-1] == 1:
                a, b = b, max(current_value + a, b)
                continue

            a, b = b, current_value + b

        return b


if __name__ == "__main__":
    print(Solution().deleteAndEarn([3, 4, 2]))  # 6
    print(Solution().deleteAndEarn([2, 3, 5, 7]))  # 15
    print(Solution().deleteAndEarn([2, 3, 3, 5, 6, 6]))  # 18
    print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))  # 9
    print(Solution().deleteAndEarn([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]))  # 61
