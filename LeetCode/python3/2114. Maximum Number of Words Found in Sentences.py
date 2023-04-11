class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(sentence.count(' ') for sentence in sentences) + 1


if __name__ == "__main__":
    print(Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
    print(Solution().mostWordsFound(["please wait", "continue to fight", "continue to win"]))