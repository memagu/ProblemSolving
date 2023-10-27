class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = balance = 0
        for char in s:
            balance += 2 * (char == 'L') - 1
            result += balance == 0

        return result


if __name__ == "__main__":
    print(Solution().balancedStringSplit("RLRRLLRLRL"))  # 4
    print(Solution().balancedStringSplit("RLRRRLLRLL"))  # 2
    print(Solution().balancedStringSplit("LLLLRRRR"))  # 1
