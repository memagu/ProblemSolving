"""
1 Read in and ignore any leading whitespace.

2 Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is
  either. This determines if the final result is negative or positive respectively. Assume the result is positive if
  neither is present.

3 Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the
  string is ignored.

4 Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
  Change the sign as necessary (from step 2).

5 If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in
  the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should
  be clamped to 231 - 1.

6 Return the integer as the final result.
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        nums = "0123456789"
        read_number = False
        sign = 1
        for char in s:
            if read_number:
                if char in nums:
                    result += char
                    continue
                break

            if char in nums + "+-":
                if char in nums:
                    result += char
                elif char == "-":
                    sign = -1
                read_number = True
                continue

            if char == " ":
                continue

            break

        result += "0" * (not result)
        return min(max(int(result) * sign, -2147483648), 2147483647)




if __name__ == "__main__":
    print(Solution().myAtoi("42"))              #          42
    print(Solution().myAtoi("   -42"))          #         -42
    print(Solution().myAtoi("4193 with words")) #        4193
    print(Solution().myAtoi("words and 987"))   #           0
    print(Solution().myAtoi("-91283472332"))    # -2147483648




