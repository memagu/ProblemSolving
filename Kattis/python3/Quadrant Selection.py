x, y = map(int, (input(), input()))

# if int(x) > 0 and int(y) > 0:
#     print(1)
# elif int(x) > 0 and int(y) < 0:
#     print(4)
# elif int(x) < 0 and int(y) < 0:
#     print(3)
# else:
#     print(2)


if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
