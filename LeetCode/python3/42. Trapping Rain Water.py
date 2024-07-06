from operator import itemgetter
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        current = result = 0
        while current < len(height):
            water_batch = 0
            second_tallest = (current + 1, 0, 0)
            for lookahead in range(current + 1, len(height)):
                if height[lookahead] >= height[current]:
                    current = lookahead
                    break

                water_batch += height[current] - height[lookahead]
                second_tallest = max(second_tallest, (lookahead, height[lookahead], water_batch - (lookahead - current) * (height[current] - height[lookahead])), key=itemgetter(1))
            else:
                result += second_tallest[2]
                current = second_tallest[0]
                continue
            result += water_batch

        return result


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
    print(Solution().trap([4, 2, 3]))
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 1, 1, 2, 1]))
    print(Solution().trap([6, 8, 5, 0, 0, 6, 5]))
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
