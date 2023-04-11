from collections import Counter
from collections import defaultdict


class Solution:
    # Two passes
    # def numIdenticalPairs(self, nums: list[int]) -> int:
    #     return sum(count * (count - 1) / 2 for count in Counter(nums).values())

    # One pass
    def numIdenticalPairs(self, nums: list[int]) -> int:
        result = 0
        counts = defaultdict(int)
        for num in nums:
            result += counts[num]
            counts[num] += 1

        return result


if __name__ == "__main__":
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))
    print(Solution().numIdenticalPairs([1, 2, 3]))
