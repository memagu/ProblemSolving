from typing import List

from collections import Counter


class Solution:
    def validate_list(self, l: List[str]):
        l = [char for char in l if char != "."]
        return len(l) == len(set(l))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            col = [board[row][i] for row in range(9)]
            if not (self.validate_list(row) and self.validate_list(col)):
                return False

        for row in range(1, 8, 3):
            for col in range(1, 8, 3):
                box = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        box.append(board[row - i][col - j])
                if not self.validate_list(box):
                    return False

        return True


if __name__ == "__main__":
    print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    print(Solution().isValidSudoku([[".", ".", "4", ".", ".", ".", "6", "3", "."],
                                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                                    ["5", ".", ".", ".", ".", ".", ".", "9", "."],
                                    [".", ".", ".", "5", "6", ".", ".", ".", "."],
                                    ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
                                    [".", ".", ".", "7", ".", ".", ".", ".", "."],
                                    [".", ".", ".", "5", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", ".", "."],
                                    [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
