from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        starts = [(x, 0) for x in range(len(mat[0]))] + [(0, y) for y in range(1, len(mat))]

        for sx, sy in starts:
            nums = []
            x, y = sx, sy
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                nums.append(mat[y][x])
                x += 1
                y += 1

            nums.sort()

            i = 0
            x, y = sx, sy
            while 0 <= x < len(mat[0]) and 0 <= y < len(mat):
                mat[y][x] = nums[i]
                i += 1
                x += 1
                y += 1

        return mat


if __name__ == "__main__":
    print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
    print(Solution().diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))
