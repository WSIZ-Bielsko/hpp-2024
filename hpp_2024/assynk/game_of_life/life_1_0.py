from datetime import datetime

import numpy as np


def ts():
    return datetime.now().timestamp()


class Life:
    def __init__(self, n_cols, n_rows):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.board: np.ndarray = np.zeros((n_rows, n_cols), dtype=np.int16)

    def get_new_board(self):
        """
        Evolves the "board" by one year:
        - computes new board by applying the rules of the game
        - substitutes self.board by the new board
        :return:
        """

        # now loop over rows and cols in self.board
        # compute n_neigbors; decide if new cell is alive or not

        new_board = [self.get_new_row(r) for r in range(self.n_rows)]
        new_board = np.array(new_board)

        self.board = new_board

    def get_new_row(self, row) -> list[int]:
        # for each column in `row` -- compute if it should be born, survive, or die
        return [
            self.get_new_state(self.board[row][col], self.get_n_neigbors(row, col))
            for col in range(self.n_cols)
        ]

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

    def print_board_console(self):
        # wydrukować ją na konsoli, zamieniając 0 na ., a 1 na *
        for row in self.board:
            print(''.join(['○' if x == 0 else '●' for x in row]))

