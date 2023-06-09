from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
                continue

            left = mid + 1

        return letters[left * (left != len(letters))]


if __name__ == "__main__":
    print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))
    print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))
    print(Solution().nextGreatestLetter(["x", "x", "y", "y"], "z"))
