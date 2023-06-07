class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        one_flips = (a | b) ^ c
        two_flips = a & b & one_flips

        return one_flips.bit_count() + two_flips.bit_count()


if __name__ == "__main__":
    print(Solution().minFlips(2, 6, 5))
    print(Solution().minFlips(4, 2, 7))
    print(Solution().minFlips(1, 2, 3))
