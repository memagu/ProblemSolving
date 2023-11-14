from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for num in nums:
            while num > 0:
                num, ones_digit = divmod(num, 10)
                digit_sum += ones_digit

        return sum(nums) - digit_sum


if __name__ == "__main__":
    print(Solution().differenceOfSum([1, 15, 6, 3]))
    print(Solution().differenceOfSum([1, 2, 3, 4]))
