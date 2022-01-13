def split(order):
    return [character for character in order]


numbers = list(map(int, input().split()))
numbers.sort()

order = split(input())

def pick(letter):
    return numbers[ord(letter) - 65]

ordered = list(map(pick, order))

print(*ordered)
