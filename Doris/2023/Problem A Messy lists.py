_, integers = input(), map(int, input().split())

print(sum(integer != sorted_integer for integer, sorted_integer in zip(integers, sorted(integers))))
