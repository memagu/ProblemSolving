n = int(input())

for test_case in range(1, n + 1):
    number, source_language, target_language = input().split()

    # Convert the alien number to decimal
    source_base = len(source_language)
    source = {symbol: value for value, symbol in enumerate(source_language)}
    decimal_value = 0
    for digit in number:
        decimal_value = decimal_value * source_base + source[digit]

    # Convert the decimal number to the target alien numeral system
    target_base = len(target_language)
    target = {value: symbol for value, symbol in enumerate(target_language)}
    if decimal_value == 0:
        num = target[0]
        continue

    num = ""
    while decimal_value > 0:
        decimal_value, remainder = divmod(decimal_value, target_base)
        num = target[remainder] + num

    print(f"Case #{test_case}: {num}")
