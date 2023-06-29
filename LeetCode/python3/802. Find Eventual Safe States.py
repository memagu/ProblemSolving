from typing import List, Optional


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        cache: list[Optional[bool]] = [None] * n

        def dfs(node) -> bool:
            if cache[node] is not None:
                return cache[node]

            cache[node] = False

            if all(dfs(child) for child in graph[node]):
                cache[node] = True
                return True

            return False

        return [node for node in range(n) if dfs(node)]


if __name__ == "__main__":
    print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(Solution().eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
