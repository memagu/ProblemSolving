import re

_ = input()
print(max(map(int, re.findall(r'\d+', input()))))
