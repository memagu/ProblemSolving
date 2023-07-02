from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        max_achievable_requests = 0

        for bitmask in range(2 ** len(requests)):
            bit_count = bitmask.bit_count()
            if bit_count < max_achievable_requests:
                continue

            changes = [0] * n
            for i, (origin, destination) in enumerate(requests):
                if bitmask & 1 << i:
                    changes[origin] -= 1
                    changes[destination] += 1
            if any(changes):
                continue

            max_achievable_requests = max(max_achievable_requests, bit_count)

        return max_achievable_requests


if __name__ == "__main__":
    print(Solution().maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))
    print(Solution().maximumRequests(3, [[0, 0], [1, 2], [2, 1]]))
    print(Solution().maximumRequests(4, [[0, 3], [3, 1], [1, 2], [2, 0]]))
    print(Solution().maximumRequests(3, [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]))
