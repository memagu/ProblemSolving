from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return list(map(str, nums))

        ranges = []
        end = 0

        while end < len(nums):
            start = end
            while end + 1 < len(nums) and nums[end + 1] - nums[end] == 1:
                end += 1

            if start == end:
                ranges.append(str(nums[start]))
            else:
                ranges.append(f"{nums[start]}->{nums[end]}")

            end += 1

        return ranges


if __name__ == "__main__":
    print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
    print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
