from typing import List

"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(nums[i] + result[-1])

        return result
"""


# In place
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        return nums


if __name__ == "__main__":
    print(Solution().runningSum([1, 2, 3, 4]))
    print(Solution().runningSum([1, 1, 1, 1, 1]))
    print(Solution().runningSum([3, 1, 2, 10, 1]))
