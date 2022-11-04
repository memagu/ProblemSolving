class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        a, b = 1, 0
        for _ in range(n-1):
            a, b = a + b, a

        return a