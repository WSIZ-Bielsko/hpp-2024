import numpy as np


class Life:
    def __init__(self, n_cols, n_rows):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.board = np.zeros((n_rows, n_cols), dtype=np.int16).tolist()

    def get_new_board(self):
        new_board = np.zeros((self.n_rows, self.n_cols), dtype=np.int16).tolist()

        # now loop over rows and cols in self.board
        # compute n_neigbors; decide if new cell is alive or not

        self.board = new_board

    def get_n_neigbors(self, row, col) -> int:
        # compute number of get_n_neigbors
        pass

if __name__ == '__main__':
    ll = Life(n_cols=2, n_rows=2)
    print(ll.board)
