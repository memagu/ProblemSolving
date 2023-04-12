class Solution:
    def minimumSum(self, num: int) -> int:
        return sum(digit * (10 if i < 2 else 1) for i, digit in enumerate(sorted(map(int, str(num)))))


if __name__ == "__main__":
    print(Solution().minimumSum(2932))
    print(Solution().minimumSum(4009))
