from heapq import heappush, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap_queue = []
        for i, row in enumerate(mat):
            heappush(heap_queue, (row.count(1), i))

        return [heappop(heap_queue)[1] for _ in range(k)]


if __name__ == "__main__":
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
                                  3))
    print(Solution().kWeakestRows([[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2))
