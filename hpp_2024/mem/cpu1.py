import math
from datetime import datetime


def ts() -> float:
    return datetime.now().timestamp()

def run_it(n_epochs):
    x = 0.0

    for e in range(n_epochs):
        for _ in range(10**5):
            x += math.sin(_ * 0.01)
    return x



if __name__ == '__main__':
    st = ts()
    res = run_it(500)
    en = ts()
    print(f'{res=}')
    print(f'elapsed {en-st:.3f}s')