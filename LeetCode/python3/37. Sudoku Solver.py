from typing import List


class Solution:
    def is_valid(self, board: list[list[str]], num: str, row: int, col: int) -> bool:
        for i in range(9):
            #  check each value in the row
            if num == board[row][i] and i != col:
                return False

            #  check each value in the column
            if num == board[i][col] and i != row:
                return False

        #  calculate which box
        box_row = row // 3
        box_col = col // 3

        # check each value in the box
        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if i == row and j == col:
                    continue

                if board[i][j] == num:
                    return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        possible = tuple(
            ((row, col), tuple(num for num in map(str, range(1, 10)) if self.is_valid(board, num, row, col)))
            for row in range(9) for col in range(9) if board[row][col] == '.'
        )

        stack = [[0, 0]]

        while stack:
            index, num_index = stack[-1]
            if index == len(possible):
                break

            (row, col), nums = possible[index]

            if num_index >= len(nums):
                board[row][col] = '.'
                stack.pop()
                continue

            stack[-1][1] += 1

            if self.is_valid(board, nums[num_index], row, col):
                board[row][col] = nums[num_index]
                stack.append([index + 1, 0])

        print(board)


if __name__ == "__main__":
    print(Solution().solveSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]))
