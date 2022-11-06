"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        indices = []

        for i, char in enumerate(s):
            if char.lower() in vowels:
                indices.append(i)

        s = list(s)

        for index, reversed_index in zip(indices[:len(indices) // 2], reversed(indices)):
            print(index, reversed_index)
            s[index], s[reversed_index] = s[reversed_index], s[index]

        return "".join(s)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'u', 'U', 'o', 'O', 'i', 'I', 'e', 'E'}
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels:
                while s[right] not in vowels:
                    right -= 1

                s[left], s[right] = s[right], s[left]
                right -= 1
            left += 1

        return "".join(s)




if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))

