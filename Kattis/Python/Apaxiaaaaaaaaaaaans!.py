
def string_to_characters(string):
    return [character for character in string]


def non_repeats(string):
    head, *tail = string
    if len(tail) == 0:
        return string
    if head == tail[0]:
        return non_repeats(tail)

    return [head] + non_repeats(tail)


print(*non_repeats(string_to_characters(input())), sep="")

