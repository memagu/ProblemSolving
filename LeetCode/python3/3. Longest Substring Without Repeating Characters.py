from typing import Dict, List, Optional, Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        result = 0
        left = right = 0
        while right < len(s):
            cur_num = s[right]
            if cur_num in seen:
                left = max(left, seen[cur_num] + 1)
                del seen[cur_num]

            seen[cur_num] = right
            right += 1

            result = max(result, right - left)

        return result

    def lengthOfLongestSubstring_slow_on2(self, s: str) -> int:
        seen = set()
        result = 0
        left = right = 0
        while right < len(s):
            cur_num = s[right]
            while cur_num in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            right += 1

            result = max(result, right - left)

        return result


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))
    print(Solution().lengthOfLongestSubstring("1"))
    print(Solution().lengthOfLongestSubstring("abba"))
