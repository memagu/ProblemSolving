n = int(input())

while int(n) > 0:
    n -= 1
    num = int(input())

    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

#   print(f"{num} is {'even' if num % 2 == 0 else 'odd'}")
#for i in n: