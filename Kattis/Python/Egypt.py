# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#
#     print("right") if a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a else print("wrong")
#

# while True:
#     a, b, c = map(int, input().split())
#     if a == b == c == 0:
#         break
#     hypotenuse = max(a, b, c)
#
#     print("right") if (max(a, b, c) ** 2 - min(a, b, c) ** 2)**0.5 in [a, b, c] else print("wrong")
#

# while True:
#     sides = list(map(int, input().split()))
#     if sum(sides) == 0:
#         break
#     sides.sort()
#
#     print("right") if sides[0]**2 + sides[1]**2 == sides[2]**2 else print("wrong")
#
