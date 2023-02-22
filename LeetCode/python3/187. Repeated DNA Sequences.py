from typing import Dict, List, Optional, Tuple


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeated = set()
        seen = set()

        for i in range(len(s) - 9):
            subsequence = s[i:i + 10]
            if subsequence in seen:
                repeated.add(subsequence)
                continue

            seen.add(subsequence)

        return list(repeated)


if __name__ == "__main__":
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))
