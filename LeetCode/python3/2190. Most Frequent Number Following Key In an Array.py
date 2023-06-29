from collections import Counter
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        return Counter(nums[i + 1] for i in range(len(nums) - 1) if nums[i] == key).most_common(1)[0][0]


if __name__ == "__main__":
    print(Solution().mostFrequent([1, 100, 200, 1, 100], 1))
    print(Solution().mostFrequent([2, 2, 2, 2, 3], 2))
