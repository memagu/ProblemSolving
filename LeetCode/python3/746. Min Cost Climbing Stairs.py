from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return min(cost[-1], cost[-2])

    def minCostClimbingStairs_w_vars(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, cost[i] + min(a, b)

        return min(a, b)


if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(Solution().minCostClimbingStairs([0, 1, 1, 0]))
    print(Solution().minCostClimbingStairs([0, 1, 0]))
    print(Solution().minCostClimbingStairs([0, 0, 0, 1]))
