from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return list(filter(bool, (split_word for word in words for split_word in word.split(separator))))


if __name__ == "__main__":
    print(Solution().splitWordsBySeparator(["one.two.three", "four.five", "six"], "."))
    print(Solution().splitWordsBySeparator(["$easy$", "$problem$"], "$"))
    print(Solution().splitWordsBySeparator(["|||"], "|"))
