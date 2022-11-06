# def myPow(x, n):
#     if n == 0:
#         return(1)
#     if n > 0:
#         base1 = x
#         while n > 1:
#             base1 *= x
#             n -= 1
#         return(base1)
#
#     return(1 / pow(x, n * -1))

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n