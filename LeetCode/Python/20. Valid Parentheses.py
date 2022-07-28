class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        open_to_closed = {"(": ")",
                          "{": "}",
                          "[": "]"}
        expected = []

        for char in s:
            if char in open_to_closed:
                expected.append(open_to_closed[char])
                continue

            if expected and char == expected.pop():
                continue

            return False

        return not expected


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
    print(Solution().isValid("){"))
    print(Solution().isValid("{}("))
