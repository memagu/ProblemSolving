from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = 20_001
        min_diff_sum = 0
        for i, num in enumerate(nums):
            left = 0
            right = len(nums) - 1
            while i != left < right != i:
                current_sum = nums[left] + num + nums[right]
                if current_sum == target:
                    return current_sum

                diff = abs(current_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    min_diff_sum = current_sum

                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return min_diff_sum


if __name__ == "__main__":
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
    print(Solution().threeSumClosest([0, 0, 0], 1))
