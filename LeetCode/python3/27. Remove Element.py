from typing import List

"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
                continue

            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]

            left += 1

        return left
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num == val:
                continue

            nums[i] = num
            i += 1

        return i


if __name__ == "__main__":
    print(Solution().removeElement([3, 2, 2, 3], 3))
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(Solution().removeElement([2], 3))
    print(Solution().removeElement([1, 1, 1, 1, 1, 1, 1, 1], 1))
    print(Solution().removeElement([1], 1))
