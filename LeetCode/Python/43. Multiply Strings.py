class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convtoint(num1) * self.convtoint(num2))

    def convtoint(self, string):
        num = 0
        for i, c in enumerate(string[::-1]):
            num += (ord(c) - 48) * 10 ** i
        return num


# class Solution1:
#     def multiply(self, num1: str, num2: str) -> str:
#         num1 = num1[::-1]
#         num2 = num2[::-1]
#

