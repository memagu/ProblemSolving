"""
# O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        start = 0
        end = 0
        for i in range(len(s)):
            for j in range(len(s)-i):
                sub_str = s[i:j+i+1]
                if sub_str == sub_str[::-1] and len(sub_str) > max_len:
                    max_len = len(sub_str)
                    start = i
                    end = i+j+1

        return s[start:end]
"""


#

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if is_palindrome(s):
            return s

        max_len = 0
        start = 0
        end = 0

        for i, char in enumerate(s):
            sub_str = char
            left_exp = 0
            right_exp = 0
            candidates_pointers = [(0, 1)]
            while is_palindrome(sub_str) and len(sub_str) < len(s):
                for _ in range(2):
                    if len(sub_str) % 2 and i + right_exp + 1 < len(s):
                        right_exp += 1
                        sub_str += s[i + right_exp]

                    elif i - left_exp - 1 >= 0:
                        left_exp += 1
                        sub_str = s[i - left_exp] + sub_str

                    if is_palindrome(sub_str):
                        candidates_pointers.append((i - left_exp, i + right_exp + 1))
                        break

                if len(candidates_pointers) > 1 and candidates_pointers[-2] == candidates_pointers[-1]:
                    break

            if not candidates_pointers:
                continue

            longest_candidate = candidates_pointers[-1]
            longest_candidate_len = longest_candidate[1] - longest_candidate[0]
            if longest_candidate_len > max_len:
                max_len = longest_candidate_len
                start, end = longest_candidate

        return s[start:end]


def is_palindrome(s):
        return s == s[::-1]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("cbbbbbd"))
    print(Solution().longestPalindrome("aa"))
    print(Solution().longestPalindrome("ab"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("ccc"))
    print(Solution().longestPalindrome("ccd"))
    print(Solution().longestPalindrome("dcc"))
