from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for interval in intervals:
            start, end = interval
            if result[-1][1] < start:
                result.append([start, end])
                continue

            if end > result[-1][1]:
                result[-1][1] = end

        return result


if __name__ == "__main__":
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge([[1, 4], [4, 5]]))
    print(Solution().merge([[1, 5], [1, 2], [1, 3]]))
    print(Solution().merge([[1, 4], [0, 4], [1, 3]]))
    print(Solution().merge([[1, 4], [2, 3]]))
    print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
