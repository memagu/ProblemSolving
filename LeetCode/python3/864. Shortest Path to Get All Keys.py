from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        rows, cols = len(grid), len(grid[0])

        start_row = 0
        start_col = 0
        master_key_mask = 0
        reachable = []
        for row, row_string in enumerate(grid):
            reachable_row = []
            for col, char in enumerate(row_string):
                reachable_row.append(
                    [(child_row, child_col) for delta_row, delta_col in directions if
                     0 <= (child_row := row + delta_row) < rows and 0 <= (child_col := col + delta_col) < cols and
                     grid[child_row][child_col] != '#'])

                if char == '@':
                    start_row, start_col = row, col
                    continue

                if 0 <= (key_pos := ord(char) - ord('a')) < 26:
                    master_key_mask |= 1 << key_pos
                    continue

            reachable.append(reachable_row)

        queue = deque(((start_row, start_col, 0, 0),))  # [(row, col, key_mask, start_distance), ...]
        visited = defaultdict[int, set](set)
        visited[0].add((start_row, start_col))

        while queue:
            for _ in range(len(queue)):
                row, col, key_mask, distance = queue.popleft()

                for child_row, child_col in reachable[row][col]:
                    if (child_row, child_col) in visited[key_mask] \
                            or (0 <= (key_bitmask_offset := ord(grid[child_row][child_col]) - ord('A')) < 26
                                and not key_mask & 1 << key_bitmask_offset):
                        continue

                    visited[key_mask].add((child_row, child_col))

                    if 0 <= (key_bitmask_offset := ord(grid[child_row][child_col]) - ord('a')) < 26:
                        new_key_mask = key_mask | 1 << key_bitmask_offset
                        if new_key_mask == master_key_mask:
                            return distance + 1

                        if (child_row, child_col) not in visited[new_key_mask]:
                            queue.append((child_row, child_col, new_key_mask, distance + 1))
                            continue

                    queue.append((child_row, child_col, key_mask, distance + 1))

        return -1


if __name__ == "__main__":
    print(Solution().shortestPathAllKeys(
        [
            "@.a..",
            "###.#",
            "b.A.B"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "@..aA",
            "..B#.",
            "....b"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "@Aa"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "@abcdeABCDEFf"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "@Ab",
            "a##"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "..#....##.",
            "....d.#.D#",
            "#...#.c...",
            "..##.#..a.",
            "...#....##",
            "#....b....",
            ".#..#.....",
            "..........",
            ".#..##..A.",
            ".B..C.#..@"
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "@Aa.",
            "...."
        ]
    ))
    print(Solution().shortestPathAllKeys(
        [
            "Dd#b@",
            ".fE.e",
            "##.B.",
            "#.cA.",
            "aF.#C"
        ]
    ))
