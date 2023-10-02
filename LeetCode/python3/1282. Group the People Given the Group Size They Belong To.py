from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = defaultdict(list)
        for i, size in enumerate(groupSizes):
            group = groups[size]
            group.append(i)
            if not len(group) % size:
                result.append(group[-size:])

        return result


if __name__ == "__main__":
    print(Solution().groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    print(Solution().groupThePeople([2, 1, 3, 3, 3, 2]))
