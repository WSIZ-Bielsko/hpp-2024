import numpy as np
import torch
import torch.nn.functional as F

from hpp_2024.assynk.game_of_life.life_1_0 import ts

"""
Aby użyć tego kodu, trzeba zainstalować bibliotekę torch, czyli:

poetry add torch

(albo pip install torch)
"""


class LifeCuda:
    def __init__(self, n_cols, n_rows, use_cuda=True):
        self.n_cols = n_cols
        self.n_rows = n_rows
        self.device = torch.device("cuda" if use_cuda and torch.cuda.is_available() else "cpu")
        self.board = torch.zeros((n_rows, n_cols), dtype=torch.int32, device=self.device)

    def get_new_board(self):
        """
        Evolves the "board" by one generation using 2D convolution to compute neighbors.
        """
        # Define a kernel to count neighbors (3x3 matrix with 1s, excluding the center)
        kernel = torch.tensor([[1, 1, 1],
                               [1, 0, 1],
                               [1, 1, 1]], dtype=torch.float32, device=self.device).unsqueeze(0).unsqueeze(0)

        # Add batch and channel dimensions to the board for convolution
        board = self.board.unsqueeze(0).unsqueeze(0).float()

        # Compute the number of alive neighbors for each cell using convolution
        n_alive_neighbors = F.conv2d(board, kernel, padding=1).squeeze(0).squeeze(0)

        # Apply the rules of the Game of Life to update the board
        new_board = torch.where(
            (self.board == 1) & ((n_alive_neighbors == 2) | (n_alive_neighbors == 3)),  # Survival rule
            torch.tensor(1, device=self.device),
            torch.where((self.board == 0) & (n_alive_neighbors == 3),  # Birth rule
                        torch.tensor(1, device=self.device),
                        torch.tensor(0, device=self.device))  # All other cells die or stay dead
        )

        self.board = new_board.int()

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

    if __name__ == '__main__':
        N = 3000
        YEARS = 100
        cuda_model = LifeCuda(n_cols=N, n_rows=N)

        np.random.seed(42)
        b = torch.tensor(np.random.randint(2, size=(N, N)))
        model = cuda_model
        model.board = b.to(model.device)

        print('initial board:')
        # ll.print_board_console()

        st = ts()
        for year in range(YEARS):
            model.get_new_board()
        en = ts()
        print(f'computation of {YEARS} years took {en - st:.3f}s')
