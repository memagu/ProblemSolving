from typing import List


class Solution:
    def rob_recursive(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            a, b = b, max(b, nums[i] + a)

        return b


if __name__ == "__main__":
    print(Solution().rob([1]))
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))
