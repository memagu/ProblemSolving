from functools import cache


class Solution:

    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True

            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True

        return False


if __name__ == "__main__":
    print(Solution().isScramble("great", "rgeat"))
    print(Solution().isScramble("abcde", "caebd"))
    print(Solution().isScramble("a", "a"))
    print(Solution().isScramble("abc", "cba"))
    print(Solution().isScramble("abcd", "badc"))
    print(Solution().isScramble("abcdefghijklmn", "efghijklmncadb"))
