from typing import List
from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(0, max(accumulate(gain)))


if __name__ == "__main__":
    print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
    print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
    print(Solution().largestAltitude([]))
