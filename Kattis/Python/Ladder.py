import math
h, v = input().split()
result = int(h) / math.sin(math.radians(int(v)))

print(int(result) + 1 if result > int(result) else int(result))
