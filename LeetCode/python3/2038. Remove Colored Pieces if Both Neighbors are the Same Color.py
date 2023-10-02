class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_triplets = 0
        b_triplets = 0

        for i in range(1, len(colors) - 1):
            if not (colors[i-1] == colors[i] == colors[i+1]):
                continue

            if colors[i] == 'A':
                a_triplets += 1
                continue

            b_triplets += 1

        return a_triplets > b_triplets



if __name__ == "__main__":
    print(Solution().winnerOfGame("AAABABB"))
    print(Solution().winnerOfGame("AA"))
    print(Solution().winnerOfGame("ABBBBBBBAAA"))
