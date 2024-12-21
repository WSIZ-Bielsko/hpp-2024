import numpy as np

if __name__ == '__main__':
    hh = [1., 2., 3., 4., -1, -2]
    hh = np.array(hh)
    print(hh[2:5])
    print(hh[[1, 2, 4]])

    # wybranie indeksów i wartości tablicy, dla których pewien warunek jest spełniony przez wartości
    indices = np.where((hh > 0) & (hh < 3))
    print(indices)

    print(hh[indices])

