from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            for sub_word in word.split(separator):
                if sub_word:
                    result.append(sub_word)

        return result


if __name__ == "__main__":
    print(Solution().splitWordsBySeparator(["one.two.three", "four.five", "six"], "."))
    print(Solution().splitWordsBySeparator(["$easy$", "$problem$"], "$"))
    print(Solution().splitWordsBySeparator(["|||"], "|"))
