from concurrent.futures import ProcessPoolExecutor, wait

from hpp_2024.parallel.dna_tools import generate_random_dna, gen_random_markers

if __name__ == '__main__':
    dna = generate_random_dna(2 * 10**5)

    executor = ProcessPoolExecutor(max_workers=20)
    futures = []
    for i in range(20):
        # markers = gen_random_markers(dna, n_markers=10, marker_len=9)
        futures.append(executor.submit(gen_random_markers, dna, n_markers=10, marker_len=10, job_id=i))

    wait(futures)
    for f in futures:
        markers = f.result()
        print(markers)