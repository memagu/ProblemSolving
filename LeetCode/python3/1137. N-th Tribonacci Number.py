class Solution:
    def tribonacci(self, n: int) -> int:
        t_1 = 1
        t_2 = 1
        t_3 = 2

        if n < 3:
            return int(bool(n))

        for i in range(n-3):
            t_3, t_2, t_1 = t_1 + t_2 + t_3, t_3, t_2

        return t_3


if __name__ == "__main__":
    print(Solution().tribonacci(0))
    print(Solution().tribonacci(1))
    print(Solution().tribonacci(2))
    print(Solution().tribonacci(3))
    print(Solution().tribonacci(4))
    print(Solution().tribonacci(25))