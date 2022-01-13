
import math


def string_to_characters(string):
    return [character for character in string]


n = int(input())

for x in range(n):
    decoded = []
    decoded_printable = []
    encoded = string_to_characters(input())
    for sqrt_length in range(int(math.sqrt(len(encoded)))):
        decoded.insert(0, encoded[sqrt_length::int(math.sqrt(len(encoded)))])

    for lists in decoded:
        decoded_printable += lists

    print(*decoded_printable, sep="")

