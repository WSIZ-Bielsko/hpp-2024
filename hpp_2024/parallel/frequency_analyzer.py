import os
from collections import Counter

from hpp_2024.parallel.dna_tools import get_most_frequent_subsequences
from hpp_2024.parallel.utils import ts


def get_sequence_frequency(seq: str) -> dict[str, int]:
    counts = Counter(seq)
    frequent = counts.most_common()[:5]
    return dict(frequent)



def get_dna_from_file(file_name: str) -> str:
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]
        return ''.join(lines[1:])


if __name__ == '__main__':
    # dna = 'AACCTTGGGAACCGGTTTTTTTTTTTTTTTTTTTAAAAAAA'

    dna = get_dna_from_file('dna_data/chrom_400M.txt')

    st = ts()
    x = get_most_frequent_subsequences(dna, seq_len=6, n_items=30)
    # print(x)
    en = ts()
    print(f'elapsed: {en-st:.3f}s')
    for k, v in x.items():
        print(k, v)


