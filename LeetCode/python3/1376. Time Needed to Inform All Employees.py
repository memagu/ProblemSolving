from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        cache = [0] * n
        max_time = 0

        queue = []
        for employee in range(n):
            if employee == headID:
                continue

            queue.clear()

            curr_employee = employee
            while cache[curr_employee] == 0 and manager[curr_employee] != -1:
                queue.append(curr_employee)
                curr_employee = manager[curr_employee]

            while queue:
                curr_employee = queue.pop()
                cache[curr_employee] = informTime[manager[curr_employee]] + cache[manager[curr_employee]]

            max_time = max(max_time, cache[employee])

        return max_time


if __name__ == "__main__":
    print(Solution().numOfMinutes(1, 0, [-1], [0]))
    print(Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
    print(Solution().numOfMinutes(5, 0, [-1, 0, 1, 1, 3], [1, 2, 0, 1, 0]))
    print(Solution().numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
