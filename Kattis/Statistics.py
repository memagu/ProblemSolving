# with open("sample.in", "r") as f:
#     for i, line in enumerate(f.readlines()):
#         numbers = list(map(int, line.split()))
#         numbers.sort()
#         print("Case ", str(i + 1) + ":", numbers[0], numbers[-1], numbers[-1] - numbers[0])

# import sys
#
# for i, line in enumerate(sys.stdin.readlines()):
#     numbers = list(map(int, line.split()))
#     numbers.sort()
#     print("Case ", str(i + 1) + ":", numbers[0], numbers[-1], numbers[-1] - numbers[0])


for i in range(10):
    try:
        numbers = list(map(int, input().split()))[1:]
        numbers.sort(key=int)
        print("Case ", str(i + 1) + ":", numbers[0], numbers[-1], numbers[-1] - numbers[0])
    except:
        break