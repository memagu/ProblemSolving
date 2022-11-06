from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self._rob(nums[1:]), self._rob(nums[:-1]))

    def _rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            a, b = b, max(b, nums[i] + a)

        return b


if __name__ == "__main__":
    print(Solution().rob([0]))
    print(Solution().rob([1]))
    print(Solution().rob([1, 1]))
    print(Solution().rob([1, 2, 1]))
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))
