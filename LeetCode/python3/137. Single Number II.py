from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one_occurrences, _ = reduce(
            lambda occurrences, num: (
                (occurrences[0] ^ num) & ~occurrences[1],
                (occurrences[1] ^ num) & ~((occurrences[0] ^ num) & ~occurrences[1])
            ),
            nums,
            (0, 0)
        )
        return one_occurrences


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 3, 2]))
    print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
    print(Solution().singleNumber([6, 6, 6, 3]))
    print(Solution().singleNumber([6, 6, 3, 6]))
    print(Solution().singleNumber([6, 3, 6, 6]))
    print(Solution().singleNumber([3, 6, 6, 6]))
