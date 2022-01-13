x, y = input(), input()

if int(x) > 0 and int(y) > 0:
    print(1)
elif int(x) > 0 and int(y) < 0:
    print(4)
elif int(x) < 0 and int(y) < 0:
    print(3)
else:
    print(2)