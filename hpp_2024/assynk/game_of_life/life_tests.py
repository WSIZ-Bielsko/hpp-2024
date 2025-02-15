import numpy as np

from hpp_2024.assynk.game_of_life.life_1_0 import Life, ts
from hpp_2024.assynk.game_of_life.life_numpy import LifeNumpy

if __name__ == '__main__':
    N = 3000
    YEARS = 100
    plain_model = Life(n_cols=N, n_rows=N)
    numpy_model = LifeNumpy(n_cols=N, n_rows=N)

    np.random.seed(42)
    b = np.random.randint(2, size=(N, N))
    # model = plain_model
    model = numpy_model

    # b = np.array([
    #     [0, 0, 1, 0, 0],
    #     [0, 1, 1, 1, 0],
    #     [1, 1, 1, 0, 0],
    #     [0, 1, 1, 0, 0],
    #     [0, 1, 0, 0, 0]
    # ])
    # model.board = b.copy()
    model.board = b.copy()

    print('initial board:')
    # ll.print_board_console()


    st = ts()
    for year in range(YEARS):
        # ll.print_board_console()
        model.get_new_board()
        # xx.get_new_board()
        # print(f'\n---- year {year} ----')
    en = ts()
    print(f'computation of {YEARS} years took {en - st:.3f}s')
    # model.print_board_console()
