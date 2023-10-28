from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_indices = {"type": 0, "color": 1, "name": 2}
        rule_index = rule_indices[ruleKey]

        return sum(item[rule_index] == ruleValue for item in items)


if __name__ == '__main__':
    print(Solution().countMatches(
        [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver"))
    print(Solution().countMatches(
        [["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))
