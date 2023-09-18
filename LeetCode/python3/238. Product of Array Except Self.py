from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        for i in range(1, len(nums)):
            products[i] = nums[i - 1] * products[i - 1]

        right_product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]

        return products


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
    print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
