from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        return all((coordinates[i][1] - y1) * dx == dy * (coordinates[i][0] - x1) for i in range(2, len(coordinates)))


if __name__ == "__main__":
    print(Solution().checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(Solution().checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
    print(Solution().checkStraightLine([[0, 0], [0, 1], [0, -1]]))
