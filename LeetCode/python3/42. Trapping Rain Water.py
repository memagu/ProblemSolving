from operator import itemgetter
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        summit = max(enumerate(height), key=itemgetter(1))[0]
        result = 0

        current = 0
        lookahead = current + 1
        while lookahead < summit:
            if height[lookahead] >= height[current]:
                current = lookahead
            result += height[current] - height[lookahead]
            lookahead += 1

        current = len(height) - 1
        lookahead = current - 1
        while lookahead > summit:
            if height[lookahead] >= height[current]:
                current = lookahead
            result += height[current] - height[lookahead]
            lookahead -= 1

        return result


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
    print(Solution().trap([4, 2, 3]))
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 1, 1, 2, 1]))
    print(Solution().trap([6, 8, 5, 0, 0, 6, 5]))
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([5, 0, 4, 0, 3, 0, 2, 0, 1, 0]))
