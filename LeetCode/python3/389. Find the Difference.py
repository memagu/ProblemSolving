from functools import reduce
from operator import xor


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(xor, map(ord, s + t)))


if __name__ == "__main__":
    print(Solution().findTheDifference("abcd", "abcde"))
    print(Solution().findTheDifference("", "y"))
