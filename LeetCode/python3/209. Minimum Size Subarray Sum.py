from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = window_sum = 0
        min_window_width = float("inf")

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_window_width = min(min_window_width, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_window_width if min_window_width != float("inf") else 0


if __name__ == "__main__":
    print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
    print(Solution().minSubArrayLen(4, [1, 4, 4]))
    print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
