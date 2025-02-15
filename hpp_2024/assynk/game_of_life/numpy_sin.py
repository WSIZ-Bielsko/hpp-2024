from datetime import datetime

import numpy as np


def ts():
    return datetime.now().timestamp()


def get_some_sins(array: np.ndarray):
    return np.sin(array)


if __name__ == '__main__':
    vertices = np.random.random(size=(1000, 1000))

    st = ts()
    for rep in range(1000):
        vertices = get_some_sins(vertices)

    en = ts()
    print(f'computation took {en - st:.3f}s')
