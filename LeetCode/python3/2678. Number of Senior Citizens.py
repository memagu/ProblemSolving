from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(detail[11:13] > "60" for detail in details)


if __name__ == "__main__":
    print(Solution().countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))
    print(Solution().countSeniors(["1313579440F2036", "2921522980M5644"]))
