from random import sample, choice

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
special = "#@*&"
all_char = upper + lower + nums * 2 + special * 4

for testcase in range(1, int(input())+1):
    pwd_len = int(input())
    pwd = input()

    r2 = False
    r3 = False
    r4 = False
    r5 = False

    for char in pwd:
        if not r2 and char in upper:
            r2 = True
            continue

        if not r3 and char in lower:
            r3 = True
            continue

        if not r4 and char in nums:
            r4 = True
            continue

        if not r5 and char in special:
            r5 = True
            continue

    if not r2:
        pwd += choice(upper)
        pwd_len += 1

    if not r3:
        pwd += choice(lower)
        pwd_len += 1

    if not r4:
        pwd += choice(nums)
        pwd_len += 1

    if not r5:
        pwd += choice(special)
        pwd_len += 1

    if pwd_len <= 7:
        pwd += "".join(sample(all_char, 7-pwd_len))

    print(f"Case #{testcase}: {pwd}")
