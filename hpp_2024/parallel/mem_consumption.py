import tracemalloc

from hpp_2024.parallel.utils import ts

if __name__ == '__main__':
    st = ts()
    tracemalloc.start()
    mem_current, mem_peak = tracemalloc.get_traced_memory()
    print(f'{mem_current=}, {mem_peak=}')
    f = [0.0 for i in range(10 ** 8)]
    mem_current, mem_peak = tracemalloc.get_traced_memory()
    print(f'{mem_current=}, mem_peak={mem_peak // (1024**2)} MB')
    en = ts()
    print(f'memory allocated in {en-st:.3f}s')
    s = input('end? ')