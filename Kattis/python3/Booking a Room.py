r, n = map(int, input().split())
if r == n:
    print("too late")
    quit()

booked_rooms = [int(input()) for room in range(n)]

for i in range(1, r + 1):
    if i not in booked_rooms:
        print(i)
        quit()

