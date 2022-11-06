from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indices = {}
#         for i, num in enumerate(nums):
#             indices[num] = i
#
#         for i, element in enumerate(nums):
#             difference = target - element
#             try:
#                 j = indices[difference]
#                 if j == i:
#                     continue
#                 return [i, j]
#             except KeyError:
#                 continue

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            num2 = target - num
            if num2 not in hash_map:
                continue

            j = hash_map[num2]

            if i != j:
                return [i, j]
