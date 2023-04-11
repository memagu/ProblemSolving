from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        stone_counts = Counter(stones)
        for jewel in jewels:
            result += stone_counts[jewel]

        return result


if __name__ == "__main__":
    print(Solution().numJewelsInStones("aA", "aAAbbbb"))
    print(Solution().numJewelsInStones("z", "ZZ"))
