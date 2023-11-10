from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(num * -((i + 1) * (len(arr) - i) // -2) for i, num in enumerate(arr))


if __name__ == "__main__":
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(Solution().sumOddLengthSubarrays([1, 2]))
    print(Solution().sumOddLengthSubarrays([10, 11, 12]))
