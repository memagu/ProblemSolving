# https://pokval22.kattis.com/submissions/9436050

def rgb_to_int(color: str) -> int:
    if color == 'R':
        return 4

    if color == 'G':
        return 2

    if color == 'B':
        return 1

# Inputs
rows_cols = tuple(map(int, input().split()))
directions = [tuple(map(rgb_to_int, input())) for _ in range(4)]

# Ta reda på vilken sida som är kortast. En optimering som gör att man utför minimalt antal operationer.
rows_larger_than_cols = rows_cols[0] >= rows_cols[1]

# Sätt "alpha" och "beta" axel utifrån den tidigare testen
alpha, beta = rows_cols[not rows_larger_than_cols], rows_cols[rows_larger_than_cols]
alpha_directions = directions[rows_larger_than_cols], directions[2 + rows_larger_than_cols]
beta_directions = directions[not rows_larger_than_cols], directions[2 + (not rows_larger_than_cols)]

# Räkna ihop hur många av varje färgkombination som finns längsmed alphaaxeln
counter = [0 for _ in range(8)]
for i in range(alpha):
    counter[(alpha_directions[0][i] | alpha_directions[1][i])] += 1

result = 0

# Räkna ihop hur många av dessa kombinationer som bildar vitt ljus med betaaxeln
for i in range(beta):
    combined = beta_directions[0][i] | beta_directions[1][i]
    for mask in range(1, 8):
        final = combined | mask
        if final == 7:
            result += counter[mask]

print(result)