from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
    print(Solution().singleNumber([1]))
