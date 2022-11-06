class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n-1):
            one, two = one + two, one

        return one

if __name__ == "__main__":
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
    print(Solution().climbStairs(5))
