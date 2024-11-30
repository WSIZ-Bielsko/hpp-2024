from datetime import datetime
from random import random, seed

import numpy as np


def ts() -> float:
    return datetime.now().timestamp()


def multiply_classic_way(x, y) -> float:
    z = sum(a * b for a, b in zip(x, y))
    return z


def multiply_np_way(x, y) -> float:
    return np.dot(x, y)


if __name__ == '__main__':
    seed(111)
    st = ts()
    x = [random() for _ in range(5 * 10 ** 7)]
    y = [random() for _ in range(5 * 10 ** 7)]
    en = ts()

    # chcemy wyliczyć x[0] * y[0] + x[1] * y[1] ....
    print(f'randoms created; elapsed {en - st:.3f}s')

    st = ts()
    for _ in range(1):
        r = multiply_classic_way(x, y)
    en = ts()
    print(f"multiply result: {r}; elapsed {en - st:.3f}s")
    xx = np.array(x)
    yy = np.array(y)

    st = ts()
    for _ in range(200):
        r = multiply_np_way(xx, yy)
    en = ts()
    print(f"multiply result: {r}; elapsed {en - st:.3f}s")
