from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == '__main__':
    print(Solution().buildArray([0, 2, 1, 5, 3, 4]))  # -> [0, 1, 2, 4, 5, 3]
    print(Solution().buildArray([5, 0, 1, 2, 3, 4]))  # -> [4, 5, 0, 1, 2, 3]
