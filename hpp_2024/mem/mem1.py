import sys
from datetime import datetime
from random import randint


def ts() -> float:
    return datetime.now().timestamp()

if __name__ == '__main__':
    print('ok')
    st = ts()
    w = [randint(0,10**7) for _ in range(100 * 10**6)]
    # w = [0 for _ in range(100 * 10**6)]
    en = ts()
    # print(sys.getsizeof(w) // (1024)**2)
    print(f'suma={sum(w)}')
    input('1> ')
    w[0] = 12
    input('2> ')

    print(f'elapsed: {en-st:.3f}s')
    input('3> ')