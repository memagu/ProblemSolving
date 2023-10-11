from bisect import bisect_left
from collections import defaultdict
from operator import itemgetter
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flower_delta = defaultdict(int)

        for start, end in flowers:
            flower_delta[start] += 1
            flower_delta[end + 1] -= 1

        last_value = 0
        prefix_sum = [(key, last_value := last_value + delta) for key, delta in sorted(flower_delta.items())]

        return [prefix_sum[bisect_left(prefix_sum, time + 1, key=itemgetter(0)) - 1][1] for time in people]


if __name__ == "__main__":
    print(Solution().fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
    print(Solution().fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]))
