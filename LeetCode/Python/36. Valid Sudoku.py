from typing import List

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_counter = defaultdict(int)
            for num in row:
                if num == ".":
                    continue
                if row_counter[num]:
                    return False
                row_counter[num] += 1

            for column in row:


if __name__ == "__main__":
    print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                       , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                       , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                       , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                       , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                       , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                       , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                       , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                       , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
