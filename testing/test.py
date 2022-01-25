import random
random.seed(1)

def generate_grid():

    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '.']
    chars = random.sample(chars, 16)
    result = []
    for i in range(4):
        result.append(chars[i * 4: i * 4 + 4])

    return result
