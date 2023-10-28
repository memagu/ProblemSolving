class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        ones = num.bit_count()
        zeros = num.bit_length() - ones

        return (ones << 1) - 1 + zeros


if __name__ == "__main__":
    print(Solution().numberOfSteps(14))
    print(Solution().numberOfSteps(8))
    print(Solution().numberOfSteps(123))
    print(Solution().numberOfSteps(0))
    print(Solution().numberOfSteps(15))
