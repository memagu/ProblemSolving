"""
It has at least 6 characters and at most 20 characters.

It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.

It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong,
assuming other conditions are met).
"""
import string
from collections import defaultdict


# class Solution:
#     def strongPasswordChecker(self, password: str) -> int:
#         edits_required = 0
#         lower = True
#         upper = True
#
#         i = 0
#         while i < len(password) - 2:
#             if password[i] == password[i + 1] == password[i + 2]:
#                 edits_required += 1
#                 i += 3
#                 continue
#             i += 1
#
#         removal_edits = max(len(password) - 20, 0)
#         if len(password) > 20:
#             edits_required = max(removal_edits - edits_required, edits_required)
#
#         elif len(password) < 6:
#             edits_required += 6 - len(password) - edits_required
#
#         if not any(item in string.ascii_lowercase for item in password):
#             lower = False
#             if not edits_required - removal_edits:
#                 edits_required += 1
#
#         if not any(item in string.ascii_uppercase for item in password):
#             upper = False
#             if not edits_required - (not lower) - removal_edits:
#                 edits_required += 1
#
#         if not any(item in string.digits for item in password):
#             if not edits_required - (not lower) - (not upper) - removal_edits:
#                 edits_required += 1
#
#         return edits_required


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        upper = 1
        lower = 1
        digit = 1
        to_add = 0
        to_delete = 0
        triplets = 0
        used = 0

        groups = [0]
        group_index = 0

        last_char = password[0]
        for char in password:
            if char == last_char:
                groups[group_index] += 1
            else:
                groups.append(1)
                group_index += 1
            if char.islower():
                lower = 0
            elif char.isupper():
                upper = 0
            elif char in "0123456789":
                digit = 0
            last_char = char

        uld = upper + lower + digit

        for group in groups:
            triplets += group // 3

        if len(password) > 20:
            to_delete = len(password) - 20

        elif len(password) < 6:
            to_add = 6 - len(password)

        if to_add:
            if to_add > uld:
                used += uld
                to_add, uld = to_add - uld, 0
            else:
                used += to_add
                uld, to_add = uld - to_add, 0

            if to_add > triplets:
                used += triplets
                to_add, triplets = to_add - triplets, 0
            else:
                used += to_add
                triplets, to_add = triplets - to_add, 0

        if to_delete:
            if to_delete > triplets:
                used += triplets
                to_delete, triplets = to_delete - triplets, 0
            else:
                used += to_delete
                triplets, to_delete = triplets - to_delete, 0

        if triplets:
            if triplets > uld:
                used += uld
                triplets, uld = triplets - uld, 0
            else:
                used += triplets
                uld, triplets = uld - triplets, 0


        print(uld, to_add, to_delete, triplets)

        return used + uld + to_add + to_delete + triplets


if __name__ == "__main__":
    print(Solution().strongPasswordChecker("a"))  # 5
    print(Solution().strongPasswordChecker("aA1"))  # 3
    print(Solution().strongPasswordChecker("1337C0d3"))  # 0
    print(Solution().strongPasswordChecker("aaa111"))  # 2
    print(Solution().strongPasswordChecker("aaaB1"))  # 1
    print(Solution().strongPasswordChecker("ABABABABABABABABABAB1"))  # 2
    print(Solution().strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))  # 8
