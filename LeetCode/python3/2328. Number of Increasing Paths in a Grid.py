from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cache = [[0] * cols for _ in range(rows)]
        mod = 10 ** 9 + 7
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col) -> int:
            if cache[row][col]:
                return cache[row][col]

            result = (1 + sum(dfs(new_row, new_col) for d_row, d_col in directions if 0 <= (new_row := row + d_row) < rows and 0 <= (new_col := col + d_col) < cols and grid[new_row][new_col] > grid[row][col])) % mod

            cache[row][col] = result

            return result

        return sum(dfs(row, col) for col in range(cols) for row in range(rows)) % mod


if __name__ == "__main__":
    print(Solution().countPaths([[1, 1], [3, 4]]))
    print(Solution().countPaths([[1], [2]]))
