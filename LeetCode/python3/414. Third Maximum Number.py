class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = set(nums)

        if len(set_nums) < 3:
            return max(nums)

        max1 = - 2 ** 31
        max2 = - 2 ** 31
        max3 = - 2 ** 31

        for num in set_nums:
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num

            elif num >= max2:
                max3 = max2
                max2 = num

            elif num >= max3:
                max3 = num

        return max3