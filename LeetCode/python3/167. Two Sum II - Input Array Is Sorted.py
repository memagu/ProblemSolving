from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left != right:
            diff = target - numbers[left] - numbers[right]

            if not diff:
                return [left + 1, right + 1]

            if diff < 0:
                right -= 1
            else:
                left += 1


if __name__ == "__main__":
    print(Solution().twoSum([2,7,11,15], 9))
    print(Solution().twoSum([2,3,4], 6))
    print(Solution().twoSum([-1,0], -1))
