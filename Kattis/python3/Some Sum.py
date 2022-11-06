
even = ["0", "2", "4", "6", "8"]
odd = ["1", "3", "5", "7", "9"]

n = int(input())

sum_one = 0
sum_two = 0

for integer in range(1, n + 1):
    sum_one += integer
for integer in range(2, n + 2):
    sum_two += integer

last_sum_one = []
last_sum_two = []

for integer in str(sum_one):
    last_sum_one.append(integer)
last_sum_one = last_sum_one[-1]

for integer in str(sum_two):
    last_sum_two.append(integer)
last_sum_two = last_sum_two[-1]

if last_sum_one in even and last_sum_two in odd:
    print("Either")
elif last_sum_two in even and last_sum_one in odd:
    print("Either")
elif last_sum_one in even:
    print("Even")
else:
    print("Odd")