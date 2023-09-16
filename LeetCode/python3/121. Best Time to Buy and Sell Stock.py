from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # O(n)
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            if price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


"""


from itertools import islice
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:  # O(n^2)
        max_profit = 0
        for i, buy_price in enumerate(prices):
            for sell_price in islice(prices, i + 1, len(prices)):
                max_profit = max(max_profit, sell_price - buy_price)
        return max_profit
"""

if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
    print(Solution().maxProfit([1, 2]))
    print(Solution().maxProfit([2, 1, 4]))
    print(Solution().maxProfit([6, 1, 3, 2, 4, 7]))
    print(Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]))
    print(Solution().maxProfit([1, 2, 0, 1, 2]))
    print(Solution().maxProfit([2, 7, 1, 4, 11]))
    print(Solution().maxProfit([7, 4, 1, 2]))
    print(Solution().maxProfit([2, 11, 1, 4, 7]))
    print(Solution().maxProfit([9, 5, 7, 4, 2, 4, 1, 6, 4]))
