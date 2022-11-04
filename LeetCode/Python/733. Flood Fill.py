from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        sample = image[sr][sc]
        visited = set()
        queue = [(sr, sc)]

        while queue:
            row, col = queue.pop(0)
            image[row][col] = color

            for new_row, new_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if new_row < 0 or rows - 1 < new_row:
                    continue

                if new_col < 0 or cols - 1 < new_col:
                    continue

                if (new_coord := (new_row, new_col)) in visited or image[new_row][new_col] != sample:
                    continue

                queue.append(new_coord)
                visited.add(new_coord)

        return image


if __name__ == "__main__":
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))  # -> [[2,2,2],[2,2,0],[2,0,1]]
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0]], 0, 0, 0))  # -> [[0,0,0],[0,0,0]]
    # Solution().floodFill([[0, 0], [0, 0]], 0, 0, 0)
