#4  9   25  81  289 1089
#s  1   2   3   4   5
#2  3   5   9   17  33
#   1   2   4   8   16

points_in_row = 2

for i in range(int(input())):
    points_in_row += points_in_row - 1

print(points_in_row*points_in_row)