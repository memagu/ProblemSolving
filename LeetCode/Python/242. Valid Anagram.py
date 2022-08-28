from functools import reduce

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum_ord_s = sum([ord(char) ** 4 for char in s])
        sum_ord_t = sum([ord(char) ** 4 for char in t])
        print(f"{sum_ord_s=}, {sum_ord_t}")
        return sum_ord_s == sum_ord_t
    

if __name__ == "__main__":
    print(Solution().isAnagram("vbnxkji", "wqdtegp"))
    # print(Solution().isAnagram("➔", "➔"))