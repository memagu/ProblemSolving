def part1():
    with open("data.in", 'r') as f:
        first_line = f.readline()
        amount_of_piles = (len(first_line.removesuffix('\n')) + 1) // 4

        piles = [[pile] if pile != ' ' else [] for i, pile in enumerate(first_line) if i % 4 == 1]

        read_piles = True

        for line in f.readlines():
            if not line.strip():
                for i, _ in enumerate(piles):
                    piles[i].pop()
                    piles[i].reverse()

                read_piles = False
                continue

            if read_piles:
                for i in range(amount_of_piles):
                    if line[i * 4 + 1] != ' ':
                        piles[i].append(line[i * 4 + 1])

                continue

            _, amount, _, source, _, destination = line.strip().split()
            source, destination = map(lambda s: int(s) - 1, (source, destination))

            for _ in range(int(amount)):
                piles[destination].append(piles[source].pop())

        return ''.join(pile.pop() for pile in piles)


def part2():
    with open("data.in", 'r') as f:
        first_line = f.readlines(1)[0]
        amount_of_piles = (len(first_line.removesuffix('\n')) + 1) // 4

        piles = [[pile] if pile != ' ' else [] for i, pile in enumerate(first_line) if i % 4 == 1]

        read_piles = True

        for line in f.readlines():
            if not line.strip():
                for i, _ in enumerate(piles):
                    piles[i].pop()
                    piles[i].reverse()

                read_piles = False
                continue

            if read_piles:
                for i in range(amount_of_piles):
                    if line[i * 4 + 1] != ' ':
                        piles[i].append(line[i * 4 + 1])

                continue

            _, amount, _, source, _, destination = line.strip().split()
            amount = int(amount)
            source, destination = map(lambda s: int(s) - 1, (source, destination))

            piles[destination] += list(piles[source])[-amount:]
            piles[source] = list(piles[source])[:-amount]

        return ''.join(pile.pop() for pile in piles)


if __name__ == "__main__":
    print(part1())
    print(part2())
