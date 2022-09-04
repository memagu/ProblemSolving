"""
It has at least 6 characters and at most 20 characters.

It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.

It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong,
assuming other conditions are met).
"""
import string


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        edits_required = 0
        lower = True
        upper = True

        i = 0
        while i < len(password) - 2:
            if password[i] == password[i + 1] == password[i + 2]:
                edits_required += 1
                i += 3
                continue
            i += 1

        removal_edits = max(len(password) - 20, 0)
        if len(password) > 20:
            edits_required = max(removal_edits - edits_required, edits_required)

        elif len(password) < 6:
            edits_required += 6 - len(password) - edits_required

        if not any(item in string.ascii_lowercase for item in password):
            lower = False
            if not edits_required - removal_edits:
                edits_required += 1

        if not any(item in string.ascii_uppercase for item in password):
            upper = False
            if not edits_required - (not lower) - removal_edits:
                edits_required += 1

        if not any(item in string.digits for item in password):
            if not edits_required - (not lower) - (not upper) - removal_edits:
                edits_required += 1

        return edits_required


if __name__ == "__main__":
    print(Solution().strongPasswordChecker("a"))
    print(Solution().strongPasswordChecker("aA1"))
    print(Solution().strongPasswordChecker("1337C0d3"))
    print(Solution().strongPasswordChecker("aaa111"))
    print(Solution().strongPasswordChecker("aaaB1"))
    print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))
    print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
    "bb faa faa faa faa faa fcc ccc"
    "bb  aa faa 8aa 8aa faa  cc  Fc"
    "bbaaaaaaaaaaaaaaacccccc"
    print(len("bbaaaaaaaaaaaaaaacccccc")) #7-3
