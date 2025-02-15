import numpy as np
from scipy.signal import convolve2d

class LifeNumpy:
    def __init__(self, n_cols, n_rows):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.board: np.ndarray = np.zeros((n_rows, n_cols), dtype=np.int16)

    def get_new_board(self):
        """
        Evolves the "board" by one generation using convolution to compute neighbors.
        """
        # Define a kernel to count neighbors (3x3 matrix with 1s, excluding the center)
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]])

        # Compute the number of alive neighbors for each cell using convolution
        # n_alive_neighbors = convolve2d(self.board, kernel, mode='same', boundary='wrap')
        n_alive_neighbors = convolve2d(self.board, kernel, mode='same', boundary='fill', fillvalue=0)

        # Apply the rules of the Game of Life to update the board
        new_board = np.where(
            (self.board == 1) & ((n_alive_neighbors == 2) | (n_alive_neighbors == 3)),  # Survival rule
            1,
            np.where((self.board == 0) & (n_alive_neighbors == 3),  # Birth rule
                     1,
                     0)  # All other cells die or stay dead
        )

        self.board = new_board

    def get_new_state(self, current: int, n_alive_neighbors: int) -> int:
        """
        This method is no longer necessary when using convolutions,
        as the rules are applied directly in `get_new_board`.
        """
        raise NotImplementedError("This method is replaced by convolution-based rules.")

    def print_board_console(self):
        # wydrukować ją na konsoli, zamieniając 0 na ., a 1 na *
        for row in self.board:
            print(''.join(['○' if x == 0 else '●' for x in row]))


if __name__ == '__main__':
    pass