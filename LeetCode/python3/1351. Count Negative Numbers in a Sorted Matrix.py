from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        left = 0

        for row in range(len(grid) - 1, -1, -1):
            if grid[row][-1] >= 0:
                return count

            right = len(grid[0]) - 1

            while left <= right:
                mid = (left + right) // 2

                if grid[row][mid] < 0:
                    right = mid - 1
                    continue

                left = mid + 1

            count += len(grid[0]) - left

        return count


if __name__ == "__main__":
    print(Solution().countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(Solution().countNegatives([[3, 2], [1, 0]]))
