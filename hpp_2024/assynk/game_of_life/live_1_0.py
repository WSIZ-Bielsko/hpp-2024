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

    def get_new_row(self, row) -> list[int]:
        # for each column in `row` -- compute if it should be born, survive, or die
        pass

    def get_new_state(self, current: int, n_alive_neighbors: int) -> int:
        """
        True rules of the game of life...
        :param current:
        :param n_alive_neighbors:
        :return:
        """
        if current == 1:  # Cell is currently alive
            if n_alive_neighbors in [2, 3]:
                return 1  # Survives
            else:
                return 0  # Dies (underpopulation or overpopulation)
        else:  # Cell is currently dead
            if n_alive_neighbors == 3:
                return 1  # Becomes alive (reproduction)
            else:
                return 0  # Stays dead

    def get_n_neigbors(self, row, col) -> int:
        # compute number of get_n_neigbors
        return sum(
            self.board[row + dr][col + dc]
            for dr in (-1, 0, 1)
            for dc in (-1, 0, 1)
            if (dr, dc) != (0, 0)
            and 0 <= row + dr < self.n_rows
            and 0 <= col + dc < self.n_cols
        )


if __name__ == '__main__':
    ll = Life(n_cols=3, n_rows=3)
    ll.board[0][0] = 1
    ll.board[1][1] = 1
    ll.board[1][2] = 1
    print(ll.get_n_neigbors(1, 1))
