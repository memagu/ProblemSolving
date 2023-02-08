# class Solution:
#     def intToRoman(self, num: int) -> str:
#         num = str(num)
#
#         integer_to_roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
#         index_to_builders = ((1, 5), (10, 50), (100, 500), (1000, 1000))
#
#         result = ""
#         for i, part in enumerate(num):
#             i = (len(num) - 1 - i)
#             part = int(part) * 10 ** i
#
#             if part in integer_to_roman:
#                 result += integer_to_roman[part]
#                 continue
#
#             if i > 2:
#                 result += integer_to_roman[1000] * (part // 1000)
#                 continue
#
#             if part > index_to_builders[i][1]:
#                 if part == index_to_builders[i+1][0] - index_to_builders[i][0]:
#                     result += integer_to_roman[index_to_builders[i][0]] + integer_to_roman[index_to_builders[i+1][0]]
#                     continue
#                 result += integer_to_roman[index_to_builders[i][1]] + integer_to_roman[index_to_builders[i][0]] * ((part - index_to_builders[i][1]) // index_to_builders[i][0])
#                 continue
#
#             if part == index_to_builders[i][1] - index_to_builders[i][0]:
#                 result += integer_to_roman[index_to_builders[i][0]] + integer_to_roman[index_to_builders[i][1]]
#                 continue
#
#             result += integer_to_roman[index_to_builders[i][0]] * (part // index_to_builders[i][0])
#
#         return result

"""
class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = ((1000, 'M'),
                  (900, 'CM'),
                  (500, 'D'),
                  (400, 'CD'),
                  (100, 'C'),
                  (90, 'XC'),
                  (50, 'L'),
                  (40, 'XL'),
                  (10, 'X'),
                  (9, 'IX'),
                  (5, 'V'),
                  (4, 'IV'),
                  (1, 'I'))

        result = ""

        i = 0
        while num:
            decimal, roman = conversion[i]
            if num >= decimal:
                num -= decimal
                result += roman
            else:
                i += 1

        return result
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        integers = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        romans = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")

        result = ""
        for integer, roman in zip(integers, romans):
            result += roman * (num // integer)
            num %= integer

        return result


if __name__ == "__main__":
    print(Solution().intToRoman(58))
    print(Solution().intToRoman(1994))
    print(Solution().intToRoman(20))
    print(Solution().intToRoman(60))
