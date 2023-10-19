from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def build_permutation(available_open: int, available_closed: int = 0, s: str = ''):
            if not (available_open or available_closed):
                return [s]

            permutations = []

            if available_open:
                permutations.extend(build_permutation(available_open - 1, available_closed + 1, s + '('))

            if available_closed:
                permutations.extend(build_permutation(available_open, available_closed - 1, s + ')'))

            return permutations

        return build_permutation(n)


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(4))
