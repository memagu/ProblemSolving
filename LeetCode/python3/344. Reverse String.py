from typing import List


"""
class Solution:
    def reverseString(self, s: List[str]) -> None:    
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        last_index = len(s) - 1
        for i in range(last_index // 2 + 1):
            s[i], s[last_index - i] = s[last_index - i], s[i]

        return s


if __name__ == "__main__":
    print(Solution().reverseString(
        ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"]))
