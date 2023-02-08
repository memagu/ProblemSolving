class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]

        sign = 1
        if s[-1] == '-':
            sign = -1
            s = s[:-1]

        result = sign * int(s)

        return result * (-2 ** 31 - 1 < result < 2 ** 31)


if __name__ == "__main__":
    print(Solution().reverse(10))
    print(Solution().reverse(-10))
    print(Solution().reverse(-451))
    print(Solution().reverse(-451000000000000000001))
