class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum // n + n // 2

        while left <= right:
            mid = (left + right) // 2

            left_arithmetic_length = max(0, min(mid - 2, index))
            left_arithmetic_sum = left_arithmetic_length * (mid - 1 + mid - left_arithmetic_length) / 2
            left_ones = index - left_arithmetic_length
            left_sum = left_arithmetic_sum + left_ones

            right_arithmetic_length = max(0, min(mid - 2, n - (index + 1)))
            right_arithmetic_sum = right_arithmetic_length * (mid - 1 + mid - right_arithmetic_length) / 2
            right_ones = n - (index + 1 + right_arithmetic_length)
            right_sum = right_arithmetic_sum + right_ones

            total_sum = left_sum + right_sum + mid

            if total_sum > maxSum:
                right = mid - 1
                continue

            left = mid + 1

        return (left + right) // 2


if __name__ == "__main__":
    print(Solution().maxValue(4, 2, 6))
    print(Solution().maxValue(6, 1, 10))
    print(Solution().maxValue(3, 2, 18))
    print(Solution().maxValue(5, 2, 15))
    print(Solution().maxValue(2, 1, 21))
