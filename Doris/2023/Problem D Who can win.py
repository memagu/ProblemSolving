from functools import reduce

WIN_CONDITIONS = (
    0b111000000, 0b000111000, 0b000000111,  # rows
    0b100100100, 0b010010010, 0b001001001,  # columns
    0b100010001, 0b001010100                # diagonals
)


def bit_count(n) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


bitmask, free_positions = reduce(lambda acc, curr: (
(acc[0] | 1 << curr[0]) if curr[1] == 'X' else acc[0], (acc[1] + [curr[0]]) if curr[1] == '_' else acc[1]),
                                 enumerate((char for _ in range(3) for char in input() if char != ' ')), (0, []))

johan_can_win = False
abdullah_can_win = False

for place_bitmask in range(2 ** len(free_positions)):
    if abdullah_can_win and johan_can_win:
        break

    temp_bitmask = bitmask
    for i, grid_index in enumerate(free_positions):
        if place_bitmask & 1 << i:
            temp_bitmask |= 1 << grid_index
            continue

        temp_bitmask &= ~(1 << grid_index)

    if bit_count(temp_bitmask) != 5:
        continue

    for win_condition in WIN_CONDITIONS:
        if abdullah_can_win and johan_can_win:
            break

        johan_can_win = johan_can_win or win_condition & temp_bitmask == win_condition
        abdullah_can_win = abdullah_can_win or win_condition & ~temp_bitmask == win_condition

if not (johan_can_win or abdullah_can_win):
    print("ingen kan vinna")
elif johan_can_win:
    if abdullah_can_win:
        print("Abdullah och Johan kan vinna")
    else:
        print("Johan kan vinna")
else:
    print("Abdullah kan vinna")