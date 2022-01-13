
numbers = []

for i in range(9):
    numbers.append(int(input()))

sum_minus_100 = -100

for number in numbers:
    sum_minus_100 += number

for number_1 in numbers:
    for number_2 in numbers:
        if number_1 == number_2:
            break
        if number_1 + number_2 == sum_minus_100:
            numbers.remove(number_1)
            numbers.remove(number_2)
            break

for number in numbers:
    print(number)