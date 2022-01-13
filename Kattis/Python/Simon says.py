def starts_with(start, string):
    ms = len(start.split())
    if string.split(maxsplit=ms)[:ms] == start.split():
        return True
    else:
        return False


start = "Simon says"

for i in range(int(input())):

    
    s = input()
    if starts_with(start, s):
        print(s[len(start):])