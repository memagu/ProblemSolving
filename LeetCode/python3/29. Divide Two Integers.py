from typing import Dict, List, Optional, Tuple


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return max(-2 ** 31, min(2 ** 31 - 1, int(dividend / divisor)))


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
