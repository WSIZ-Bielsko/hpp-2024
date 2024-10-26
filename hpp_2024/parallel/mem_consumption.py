import tracemalloc

if __name__ == '__main__':
    tracemalloc.start()
    mem_current, mem_peak = tracemalloc.get_traced_memory()
    print(f'{mem_current=}, {mem_peak=}')
    f = [0.0 for i in range(10 ** 8)]
    mem_current, mem_peak = tracemalloc.get_traced_memory()
    print(f'{mem_current=}, {mem_peak=}')
    s = input('end? ')