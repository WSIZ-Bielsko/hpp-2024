from datetime import datetime
from random import gauss

import numpy as np


def ts() -> float:
    return datetime.now().timestamp()


def calc_normal(x, y):
    c = 0
    for (a, b) in zip(x, y):
        c += a * b
    return c


def calc_np(x, y):
    return np.matmul(x, y)


if __name__ == '__main__':
    x = [gauss(mu=0, sigma=1) for _ in range(10 ** 5)]
    y = [gauss(mu=0.5, sigma=1) for _ in range(10 ** 5)]

    st = ts()
    u = 0
    for _ in range(1000):
        u += calc_normal(x, y)
    print(u, f'elapsed; {ts() - st:.3f}s')

    x = np.array(x)
    y = np.array(y)

    st = ts()
    u = 0
    for _ in range(1000):
        u += calc_np(x, y)
    print(u, f'elapsed; {ts() - st:.3f}s')

    # simulation
    print(x, y)

    dt = 0.01
    x = x + y * dt
    y = y + (-0.1) * dt

    print(x, y)

    # print(type(x))  # "dense" array
    # print(x.shape)

    # d = np.sin(x)
    # print(d[:10])
