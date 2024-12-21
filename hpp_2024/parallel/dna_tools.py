import random
from collections import Counter
from time import sleep


def generate_random_dna(n_elems: int) -> str:
    tokens = ['A', 'C', 'G', 'T']
    dna = ''.join(random.choices(tokens, k=n_elems))
    return dna


def gen_random_markers(dna: str, n_markers: int, marker_len: int, job_id: int) -> list[str]:
    print(f'starting job {job_id}')
    markers = set()
    i = 0
    while len(markers) < n_markers:
        marker = generate_random_dna(marker_len)
        if marker not in dna:
            markers.add(marker)
        i += 1
        if (i + 1) % 1000 == 0:
            print(f'id={job_id} have {len(markers)} markers')
    sleep(1.5)
    return list(markers)


def get_sequence_frequency(seq: str | list, n_items: int) -> dict[str, int]:
    counts = Counter(seq)
    frequent = counts.most_common()[:n_items]
    return dict(frequent)


def get_most_frequent_subsequences(seq: str, seq_len: int, n_items: int) -> dict[str, int]:
    short_seqs = [seq[s:s + seq_len] for s in range(len(seq) - seq_len + 1)]
    return get_sequence_frequency(short_seqs, n_items)
