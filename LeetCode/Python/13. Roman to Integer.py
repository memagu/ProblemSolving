def romanToInt(s: str) -> int:
    translate = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

    prev = "I"
    result = 0

    for char in s[::-1]:
        t_char = translate[char]
        t_prev = translate[prev]

        if t_prev > t_char:
            result -= t_char


        else:
            result += t_char

        prev = char

    return result


year = romanToInt("MCMLXX")
month = romanToInt("V")
day = romanToInt("XXVII")

print(f"{day}/{month}-{year}")