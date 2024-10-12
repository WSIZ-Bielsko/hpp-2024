import concurrent
import random
from concurrent.futures import ProcessPoolExecutor, wait


def generate_random_dna(n_elems: int) -> str:
    tokens = ['A', 'C', 'G', 'T']
    dna = ''.join(random.choice(tokens) for _ in range(n_elems))
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

if __name__ == '__main__':
    dna = generate_random_dna(2 * 10**6)

    executor = ProcessPoolExecutor(max_workers=20)
    futures = []
    for i in range(20):
        # markers = gen_random_markers(dna, n_markers=10, marker_len=9)
        futures.append(executor.submit(gen_random_markers, dna, n_markers=10, marker_len=9, job_id=i))

    wait(futures)
    for f in futures:
        markers = f.result()
        print(markers)