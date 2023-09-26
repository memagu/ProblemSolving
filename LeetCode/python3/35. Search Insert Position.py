from bisect import bisect_left
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
