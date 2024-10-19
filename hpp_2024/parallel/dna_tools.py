import random


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
        if (i+1) % 1000 == 0:
            print(f'id={job_id} have {len(markers)} markers')

    return list(markers)
