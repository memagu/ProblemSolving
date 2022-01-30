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

def myPow(x, n):
    return x ** n