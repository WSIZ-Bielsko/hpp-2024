import numpy as np
from scipy.signal import convolve2d

if __name__ == '__main__':

    # b = np.array([
    #     [0, 0, 1, 0, 0],
    #     [0, 1, 0, 1, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 0, 0, 0]
    # ])

    b = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # print(b)
    # print(np.where(b > 1, 100, 0))

    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])

    # kernel = np.array([[0, 0, 0],
    #                    [0, 0, 0],
    #                    [0, 1, 0]])

    convoluted = convolve2d(b, kernel, mode='same', boundary='fill', fillvalue=0)
    print(b)
    print('----')

    print(convoluted)