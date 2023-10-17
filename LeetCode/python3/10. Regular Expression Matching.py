from functools import cache


class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        match = s and p[0] in (s[0], '.')

        if len(p) >= 2 and p[1] == '*':
            return match and self.isMatch(s[1:], p) or self.isMatch(s, p[2:])

        return match and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))  # -> False
    print(Solution().isMatch("aa", "a*"))  # -> True
    print(Solution().isMatch("ab", ".*"))  # -> True
    print(Solution().isMatch("aaaabbc", "a*.*c"))  # -> True
    print(Solution().isMatch("aaaabbc", "a*.*d"))  # -> False
    print(Solution().isMatch("aab", "c*a*b"))  # -> True
    print(Solution().isMatch("ccc", "c*a*b"))  # -> False
    print(Solution().isMatch("ccc", "ca*b"))  # -> False
    print(Solution().isMatch("cb", "ca*b"))  # -> True
    print(Solution().isMatch("caaaaaaaaaaaaaab", "ca*b"))  # -> True
    print(Solution().isMatch("bbb", "c*a*b"))  # -> False
    print(Solution().isMatch("b", "c*a*b"))  # -> True
    print(Solution().isMatch("mississippi", "mis*is*p*."))  # -> False
