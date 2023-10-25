from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        result = 1
        while result in unique_nums:
            result += 1

        return result


if __name__ == "__main__":
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
