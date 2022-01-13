# n = int(input())
#
# while int(n) > 0:
#
#     line = []
#
#     above_average = 0
#
#     n -= 1
#
#     line = input().split()
#
#     line = [int(i) for i in line]
#
#     #print(line)
#
#     summa = sum(line[1:])
#
#     personer = sum(line[:1])
#
#     medelvärde = summa / personer
#
#     for i in line[1:]:
#         if medelvärde < i:
#             above_average += 1
#
#     print("{:.3%}".format(above_average / personer))

# 5
# 5 50 50 70 80 100
# 7 100 95 90 80 70 60 50
# 3 70 90 80
# 3 70 90 81
# 9 100 99 98 97 96 95 94 93 91

for _ in range(int(input())):
    case = list(map(int, input().split()))
    n = case[0]
    z = sum(case[1:])
    avrage = z / n
    count = 0
    for score in case[1:]:
        if score > avrage:
            count += 1

    print("{:.3%}".format(count / n))

