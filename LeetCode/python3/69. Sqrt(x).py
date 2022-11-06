class Solution:
    def mySqrt(self, x: int) -> int:
        return int(self.sqrt(x))

    def sqrt(self, num, *, upper: float = 0, lower: float = 0, depth: int = 62):
        if not upper:
            upper = num * 2

        mid = (upper + lower) / 2

        if not depth:
            return mid

        mid_sq = mid ** 2

        if mid_sq == num:
            return mid

        if mid_sq > num:
            return self.sqrt(num, upper=mid, lower=lower, depth=depth-1)

        # if mid_sq < num:
        return self.sqrt(num, upper=upper, lower=mid, depth=depth-1)