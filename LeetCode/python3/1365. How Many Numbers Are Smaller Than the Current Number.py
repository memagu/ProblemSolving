from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_map = [-1] * 101
        for i, num in enumerate(sorted(nums)):
            if smaller_map[num] == -1:
                smaller_map[num] = i

        return [smaller_map[num] for num in nums]


if __name__ == "__main__":
    print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
    print(Solution().smallerNumbersThanCurrent([6, 5, 4, 8]))
    print(Solution().smallerNumbersThanCurrent([7, 7, 7, 7]))
