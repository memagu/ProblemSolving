from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(int(digit) for num in nums for digit in str(num))


if __name__ == "__main__":
    print(Solution().differenceOfSum([1, 15, 6, 3]))
    print(Solution().differenceOfSum([1, 2, 3, 4]))
