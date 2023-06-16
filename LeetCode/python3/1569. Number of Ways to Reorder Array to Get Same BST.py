from math import comb
from typing import List


class Solution:
    def __init__(self):
        self.mod = 10 ** 9 + 7

    def dfs(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 1

        root = nums[0]

        left_nodes = [node for node in nums if node < root]
        right_nodes = [node for node in nums if node > root]

        return self.dfs(left_nodes) * self.dfs(right_nodes) * comb(len(nums) - 1, len(left_nodes)) % self.mod

    def numOfWays(self, nums: List[int]) -> int:
        return (self.dfs(nums) - 1) % self.mod


if __name__ == "__main__":
    print(Solution().numOfWays([2, 1, 3]))
    print(Solution().numOfWays([3, 4, 5, 1, 2]))
    print(Solution().numOfWays([1, 2, 3]))
