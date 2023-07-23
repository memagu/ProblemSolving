class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2)).removeprefix("0b")

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         result = ""
#
#         carry = False
#         bin_long, bin_short = (a, b) if len(a) >= len(b) else (b, a)
#         for i in range(-1, -len(bin_long) - 1, -1):
#             long_val = bin_long[i]
#             short_val = bin_short[i] if i >= -len(bin_short) else '0'
#
#             if carry:
#                 if long_val == short_val == '0':
#                     carry = False
#
#                 if long_val == short_val:
#                     result += '1'
#                 else:
#                     result += '0'
#             else:
#                 if long_val != short_val:
#                     result += '1'
#                 else:
#                     if long_val == '1':
#                         carry = True
#
#                     result += '0'
#
#         return (result + ('1' if carry else ''))[::-1]

# def parse_binary(binary_string: str) -> int:
#     result = 0
#     for char in binary_string:
#         result <<= 1
#         result += char == '1'
#
#     return result
#
#
# def get_binary_representation(integer: int) -> str:
#     result = ''
#     while integer > 0:
#         result += '1' if integer & 1 else '0'
#         integer >>= 1
#
#     return result[::-1]
#
#
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return get_binary_representation(parse_binary(a) + parse_binary(b))


if __name__ == "__main__":
    print(Solution().addBinary("11", "1"))
    print(Solution().addBinary("1010", "1011"))
