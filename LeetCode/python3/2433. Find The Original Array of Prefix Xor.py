from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i - 1] for i in range(1, len(pref))]


if __name__ == "__main__":
    print(Solution().findArray([5, 2, 0, 3, 1]))
    print(Solution().findArray([13]))
