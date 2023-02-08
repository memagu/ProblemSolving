from typing import Dict, List, Optional, Tuple

"""
# Old solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            for i in range(len(prefix)):
                if not prefix:
                    return prefix
                if i > len(s) - 1:
                    prefix = prefix[:i]
                    break
                if prefix[i] != s[i]:
                    prefix = prefix[:i]
                    break

        return prefix
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) - 1 < i or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
