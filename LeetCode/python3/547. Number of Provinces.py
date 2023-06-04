from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        groups = 0

        for i in range(len(isConnected)):
            if isConnected[i][i] < 0:
                continue

            isConnected[i][i] = -1
            groups += 1
            queue = [i]

            while queue:
                node = queue.pop()
                for child, status in enumerate(isConnected[node]):
                    if status == 1 and isConnected[child][child] == 1:
                        queue.append(child)
                        isConnected[child][child] = -1

        return groups


if __name__ == "__main__":
    print(Solution().findCircleNum(
        [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1]
        ]
    ))
    print(Solution().findCircleNum(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
    ))
    print(Solution().findCircleNum(
        [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ]
    ))
