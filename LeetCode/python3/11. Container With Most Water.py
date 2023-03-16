from typing import Dict, List, Optional, Tuple


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left != right:
            if height[left] <= height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
                continue

            max_area = max(max_area, (right - left) * height[right])
            right -= 1

        return max_area


if __name__ == "__main__":
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea([1, 1]))
