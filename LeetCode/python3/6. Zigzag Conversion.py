class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        result = ""
        step_size = (numRows-1) * 2

        for row in range(numRows):
            for i in range(row, len(s), step_size):
                result += s[i]
                if 0 < row < numRows -1 and i + step_size - 2 * row < len(s):
                    result += s[i + step_size - 2 * row]

        return result


if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("ABC", 1))