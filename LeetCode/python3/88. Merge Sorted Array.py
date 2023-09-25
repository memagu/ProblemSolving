from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        fill_pointer = i + n

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[fill_pointer] = nums1[i]
                i -= 1
            else:
                nums1[fill_pointer] = nums2[j]
                j -= 1
            fill_pointer -= 1


if __name__ == "__main__":
    print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    print(Solution().merge([1], 1, [], 0))
    print(Solution().merge([0], 0, [1], 1))
    print(Solution().merge([2, 0], 1, [1], 1))
    print(Solution().merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5))
    print(Solution().merge([4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5))
