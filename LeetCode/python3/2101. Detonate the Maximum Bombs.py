# https://leetcode.com/problems/detonate-the-maximum-bombs/

from collections import defaultdict
from typing import List

"""
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_graph = defaultdict(list)

        for i in range(len(bombs) - 1):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]

                distance_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

                if distance_sq <= r1 ** 2:
                    bomb_graph[i].append(j)

                if distance_sq <= r2 ** 2:
                    bomb_graph[j].append(i)

        detonated = defaultdict(set)

        queue = []
        for i in range(len(bombs)):
            queue.append(i)
            detonated[i].add(i)

            while queue:
                for child in bomb_graph[queue.pop()]:
                    if child in detonated[i]:
                        continue

                    if detonated[child]:
                        detonated[i].update(detonated[child])
                        continue

                    queue.append(child)
                    detonated[i].add(child)

            if len(detonated[i]) == len(bombs):
                return len(bombs)

            if len(detonated[i]) == 1:
                detonated.pop(i)

        if not detonated:
            return 1

        return max(map(len, detonated.values()))
"""


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        bomb_graph = defaultdict(list)

        for i in range(len(bombs) - 1):
            x1, y1, r1 = bombs[i]
            for j in range(i + 1, len(bombs)):
                x2, y2, r2 = bombs[j]

                distance_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

                if distance_sq <= r1 ** 2:
                    bomb_graph[i].append(j)

                if distance_sq <= r2 ** 2:
                    bomb_graph[j].append(i)

        max_detonation_count = 0

        visited = set()
        queue = []
        for i in range(len(bombs)):
            queue.append(i)
            visited.add(i)

            while queue:
                for child in bomb_graph[queue.pop()]:
                    if child in visited:
                        continue

                    queue.append(child)
                    visited.add(child)

            if len(visited) == len(bombs):
                return len(bombs)

            max_detonation_count = max(max_detonation_count, len(visited))
            visited.clear()

        return max_detonation_count


if __name__ == "__main__":
    print(Solution().maximumDetonation(
        [
            [2, 1, 3],
            [6, 1, 4]
        ]
    ))
    print(Solution().maximumDetonation(
        [
            [1, 1, 5],
            [10, 10, 5]
        ]
    ))
    print(Solution().maximumDetonation(
        [
            [1, 2, 3],
            [2, 3, 1],
            [3, 4, 2],
            [4, 5, 3],
            [5, 6, 4]
        ]
    ))
    print(Solution().maximumDetonation(
        [
            [7, 26, 7],
            [7, 18, 4],
            [3, 10, 7],
            [17, 50, 1],
            [3, 25, 10],
            [85, 23, 8],
            [80, 50, 1],
            [58, 74, 1],
            [38, 39, 7],
            [50, 51, 8],
            [31, 99, 3],
            [53, 6, 5],
            [59, 27, 10],
            [87, 78, 9],
            [68, 58, 3]
        ]
    ))
