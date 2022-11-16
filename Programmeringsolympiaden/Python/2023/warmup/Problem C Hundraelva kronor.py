"""
result = 0

price = int(input())
for bill in (int('1' * i) for i in range(len(str(price)), 0, -1)):
    result += (bill_amount := price // bill)
    price -= bill * bill_amount

print(result)

"""
result = 0

price = int(input())
while price:
    if (bill := int('1' * len(str(price)))) > price:
        bill //= 10

    result += (amount_of_bills := price // bill)
    price -= amount_of_bills * bill

print(result)