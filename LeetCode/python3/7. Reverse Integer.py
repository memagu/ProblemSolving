def reverse(self, x: int) -> int:
    s = str(x)
    sign = 1

    if s[0] == '-':
        sign = -1
        s = s[1:]

    result = sign * int(s[::-1])
    if -2 ** 31 - 1 < result < 2 ** 31:
        return result
    return 0
