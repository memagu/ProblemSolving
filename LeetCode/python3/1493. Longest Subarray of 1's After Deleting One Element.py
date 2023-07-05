from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        prev_sum = curr_sum = result = 0
        contains_zeros = False

        for i, num in enumerate(nums):
            if num == 1:
                curr_sum += 1
                continue

            contains_zeros = True
            result = max(result, prev_sum + curr_sum)
            prev_sum, curr_sum = curr_sum, 0

        return max(result, prev_sum + curr_sum) - (not contains_zeros)


if __name__ == "__main__":
    print(Solution().longestSubarray([1, 1, 0, 1]))
    print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
    print(Solution().longestSubarray([1, 1, 1]))
