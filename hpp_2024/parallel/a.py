import random


def generate_random_dna(n_elems: int) -> str:
    tokens = ['A', 'C', 'G', 'T']
    dna = ''.join(random.choice(tokens) for _ in range(n_elems))
    return dna


if __name__ == '__main__':
    print(generate_random_dna(10 ** 5))
