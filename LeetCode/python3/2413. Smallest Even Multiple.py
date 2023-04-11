class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * (1 + n % 2)


if __name__ == "__main__":
    print(Solution().smallestEvenMultiple(5))
    print(Solution().smallestEvenMultiple(6))
