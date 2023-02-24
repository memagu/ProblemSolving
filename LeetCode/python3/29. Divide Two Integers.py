from typing import Dict, List, Optional, Tuple


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        return max(min(len(range(0, abs(dividend) - abs(divisor) + 1, abs(divisor))) * (-1 if dividend >= 0 > divisor or dividend < 0 <= divisor else 1), 2 ** 31 - 1), -2 ** 31)


if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))
    print(Solution().divide(1, 1))
    print(Solution().divide(2147483647, 1))
