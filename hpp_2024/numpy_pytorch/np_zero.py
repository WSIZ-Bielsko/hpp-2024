import numpy as np

if __name__ == '__main__':
    w = [1, 2, 3, 4]
    wa = np.array(w)
    print(wa)
    print(type(wa))
    print(wa.shape)

    t = np.array([[1, 2, 3], [4, 5, 6]])
    print(t)
    print(t.shape)

    sumz = np.sum(t, axis=0)
    print(sumz)
    # sumz[0] = sum_i t[i,0]

    three_d_list = [
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],
        [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]],
        [[9, 0, 1],
         [2, 3, 4],
         [5, 6, 7]]
    ]
    three_d_list[0][2][1]

    print('--------')
    array_3d = np.array(three_d_list)
    print(array_3d)
    print('===')
    sumz = array_3d.sum(axis=0)
    print(sumz)


    # teraz tablica "images" --> 4 wymiary....
    # images[nr_obrazka, kanał, x, y] -> liczba 0...255 -- intensywność tego koloru w tym miejscu tego obrazka

    max_value = np.max(array_3d)
    max_index = np.unravel_index(np.argmax(array_3d), array_3d.shape)  # finds its position

    print(f"Maximum value: {max_value}")
    print(f"Position (depth, row, column): {max_index}")
