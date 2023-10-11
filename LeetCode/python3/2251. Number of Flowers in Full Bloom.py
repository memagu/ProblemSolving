from bisect import bisect_left, bisect_right
from operator import itemgetter
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(map(itemgetter(0), flowers))
        ends = sorted(map(itemgetter(1), flowers))

        return [bisect_right(starts, time) - bisect_left(ends, time) for time in people]


if __name__ == "__main__":
    print(Solution().fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
    print(Solution().fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]))
