with open("test.txt", "w") as f:
    _ = input().strip()
    ltr = input().strip()
    rtl = input().strip()
    shift = int(input().strip())

    f.write(f"{_} {ltr} {rtl} {shift}")