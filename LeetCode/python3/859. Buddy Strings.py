class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        first_misplaced = second_misplaced = -1
        seen = 0

        for i, char in enumerate(s):
            seen |= (1 << ord(char) - 97)
            if char != goal[i]:
                if second_misplaced == -1:
                    if first_misplaced == -1:
                        first_misplaced = i
                        continue

                    second_misplaced = i
                    continue

                return False

        if second_misplaced == -1:
            if first_misplaced == -1:
                return seen.bit_count() < len(s)

            return False

        return s[first_misplaced] == goal[second_misplaced] and s[second_misplaced] == goal[first_misplaced]


if __name__ == "__main__":
    print(Solution().buddyStrings("ab", "ba"))
    print(Solution().buddyStrings("ab", "ab"))
    print(Solution().buddyStrings("aa", "aa"))
    print(Solution().buddyStrings("abcd", "badc"))
    print(Solution().buddyStrings("abcaa", "abcbb"))
