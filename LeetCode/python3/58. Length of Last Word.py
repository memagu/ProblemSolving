class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        return len(s) - 1 - s.rfind(' ')


if __name__ == "__main__":
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
    print(Solution().lengthOfLastWord("luffy is still joyboy"))
