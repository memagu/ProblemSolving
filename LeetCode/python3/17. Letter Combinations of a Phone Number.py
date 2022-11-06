class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {"2": ["a", "b", "c"],
                            "3": ["d", "e", "f"],
                            "4": ["g", "h", "i"],
                            "5": ["j", "k", "l"],
                            "6": ["m", "n", "o"],
                            "7": ["p", "q", "r", "s"],
                            "8": ["t", "u", "v"],
                            "9": ["w", "x", "y", "z"]}


        def combinations(digits: str) -> [str]:
            if not digits:
                return [""]

            result = []
            for letter in digit_to_letters[digits[0]]:
                for combination in combinations(digits[1:]):
                    result.append(letter + combination)

            return result


        return combinations(digits)