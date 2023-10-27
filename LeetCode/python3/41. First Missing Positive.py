from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i, num in enumerate(nums, 1):
            if num != i:
                return i

        return len(nums) + 1



if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
    print(Solution().firstMissingPositive([3, 4, 5, -1, 1]))
    print(Solution().firstMissingPositive([5,1,1,1,1,1,1,5,4,3,2,1,0]))
