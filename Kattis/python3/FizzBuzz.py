a, b, c = input().split()

x = int(a)

y = int(b)

z = int(c)

for i in range(1, z + 1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % y == 0:
        print("Buzz")
    elif i % x == 0:
        print("Fizz")
    else:
        print(i)