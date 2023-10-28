class Solution:
    def numberOfSteps(self, num: int) -> int:
        return 0 if num == 0 else num.bit_count() - 1 + num.bit_length()


if __name__ == "__main__":
    print(Solution().numberOfSteps(14))
    print(Solution().numberOfSteps(8))
    print(Solution().numberOfSteps(123))
    print(Solution().numberOfSteps(0))
    print(Solution().numberOfSteps(15))
