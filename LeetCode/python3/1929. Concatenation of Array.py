from typing import List


class Solution:
    def getConcatenation_slow(self, nums: List[int]) -> List[int]:
        ans = [*nums]
        for elem in nums:
            ans.append(elem)

        return ans

    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2