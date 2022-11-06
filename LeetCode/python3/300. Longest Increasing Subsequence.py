from typing import List


"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1 for _ in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            max_len = 0
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i] and max_len < counts[j]:
                    max_len = counts[j]

            counts[i] += max_len

        return max(counts)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]

        for i in range(1, len(nums)):
            index_of_smallest_greater = self.binary_search(lis, nums[i])
            if index_of_smallest_greater == -1:
                lis.append(nums[i])
                continue

            lis[index_of_smallest_greater] = nums[i]

        return len(lis)

    def binary_search(self, arr: List[float], target: float) -> int:
        left = 0
        right = len(arr) - 1
        result = float("inf")
        while left <= right:
            center = int((left + right) / 2)
            if arr[center] >= target:
                result = min(result, center)
                right = center - 1
                continue

            left = center + 1

        return result if result != float("inf") else -1




# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         max_len = 0
#         for i, num in enumerate(nums):
#             if max_len == len(nums) - i:
#                 break
#
#             local_max_len = 0
#             current_num = num
#             for j, next_num in enumerate(nums[i + 1:]):
#                 if next_num <= current_num:
#                     break
#
#                 local_max_len += 1
#                 current_num = next_num
#
#             max_len = max(max_len, local_max_len)
#
#         return max_len + 1


if __name__ == "__main__":
    # print(Solution().lengthOfLIS([11, 2, 4, 12]))
    # print(Solution().lengthOfLIS([7, 7, 7, 7]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
    # print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
