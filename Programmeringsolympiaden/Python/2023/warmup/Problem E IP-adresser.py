def is_valid_part(ipv4_part: str) -> bool:
    return int(ipv4_part) > 255 or len(ipv4_part) > 1 and ipv4_part[0] == '0'


s = input()
result = 0

for i in range(1, 4):
    p1 = s[:i]
    if is_valid_part(p1):
        continue

    for j in range(i + 1, i + 4):
        p2 = s[i:j]
        if is_valid_part(p2):
            continue

        for k in range(j + 1, len(s)):
            p3 = s[j:k]
            if is_valid_part(p3):
                continue

            p4 = s[k:]
            if is_valid_part(p4):
                continue

            result += 1

print(result)
