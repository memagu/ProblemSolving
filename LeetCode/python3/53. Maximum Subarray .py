from typing import Dict, List, Tuple


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current_sum = 0

        for num in nums:
            current_sum *= current_sum > 0
            current_sum += num
            result = max(result, current_sum)

        return result


if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray([1]))
    print(Solution().maxSubArray([5, 4, -1, 7, 8]))
