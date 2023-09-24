from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        non_duplicate_index = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            nums[non_duplicate_index] = nums[i + 1]
            non_duplicate_index += 1

        return non_duplicate_index


if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(Solution().removeDuplicates([1, 1, 2]))
