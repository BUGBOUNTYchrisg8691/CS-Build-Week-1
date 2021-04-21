"""Logic for Conway's Game of Life(console)."""

import argparse

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

ON = 255
OFF = 0
vals = [ON, OFF]


class Glider:
    """Glider class."""

    def __init__(self):
        self.shape = np.array([[OFF, OFF, ON], [ON, OFF, ON], [OFF, ON, ON]]).reshape(
            3, 3
        )


class GosperGliderGun:
    """GosperGliderGun class."""

    def __init__(self):
        self.shape = np.zeros(11 * 38).reshape(11, 38)
        self.shape[5][1] = self.shape[5][2] = ON
        self.shape[6][1] = self.shape[6][2] = ON

        self.shape[3][13] = self.shape[3][14] = ON
        self.shape[4][12] = self.shape[4][16] = ON
        self.shape[5][11] = self.shape[5][17] = ON
        self.shape[6][11] = self.shape[6][15] = self.shape[6][17] = self.shape[6][
            18
        ] = ON
        self.shape[7][11] = self.shape[7][17] = ON
        self.shape[8][12] = self.shape[8][16] = ON
        self.shape[9][13] = self.shape[9][14] = ON

        self.shape[1][25] = ON
        self.shape[2][23] = self.shape[2][25] = ON
        self.shape[3][21] = self.shape[3][22] = ON
        self.shape[4][21] = self.shape[4][22] = ON
        self.shape[5][21] = self.shape[5][22] = ON
        self.shape[6][23] = self.shape[6][25] = ON
        self.shape[7][23] = ON

        self.shape[3][35] = self.shape[3][36] = ON
        self.shape[4][35] = self.shape[4][36] = ON


class LifeBoard:
    """Conway's Game of Life(console) board class"""

    def __init__(self, N, board=None):
        self.N = N
        self.board = board
        if board is None:
            self.board = self.generate_board()

    def __repr__(self):
        return f"Life(N={self.N}, board={self.board})"

    def print_board(self):
        """
        Display board as a rectangle with
        dimensions `self.N` x `self.N`.
        """
        for i in range(self.N):
            print(self.board[i])

    def generate_board(self):
        """Generate random board pattern if no pattern is supplied."""
        return np.random.choice(vals, self.N * self.N, p=[0.2, 0.8]).reshape(
            self.N, self.N
        )

    def spawn_glider(self, x, y):
        gli = Glider()
        self.board[x : x + 3, y : y + 3] = gli.shape

    def spawn_gosper_glider_gun(self, x, y):
        gun = GosperGliderGun()
        self.board[x : x + 11, y : y + 38] = gun.shape

    def update_board(self, frame, img):
        """Update state of game board."""
        # create copy of current game board
        new_board = self.board.copy()

        for i in range(self.N):
            for j in range(self.N):

                # compute neighbor sum (toroidal boundary conditions)
                # x and y wrap around board
                total = int(
                    (
                        self.board[i, (j - 1) % self.N]
                        + self.board[i, (j + 1) % self.N]
                        + self.board[(i - 1) % self.N, j]
                        + self.board[(i + 1) % self.N, j]
                        + self.board[(i - 1) % self.N, (j - 1) % self.N]
                        + self.board[(i - 1) % self.N, (j + 1) % self.N]
                        + self.board[(i + 1) % self.N, (j - 1) % self.N]
                        + self.board[(i + 1) % self.N, (j + 1) % self.N]
                    )
                    / 255
                )

                # apply Conway's rules
                if self.board[i, j] == ON:
                    if (total < 2) or (total > 3):
                        new_board[i, j] = OFF
                else:
                    if total == 3:
                        new_board[i, j] = ON
        img.set_data(new_board)
        self.board[:] = new_board[:]

        return (img,)


def main():
    # parse command line args
    parser = argparse.ArgumentParser(
        description="Runs Conway's Game of Life simulation."
    )

    # add args
    parser.add_argument("--grid-size", dest="N", required=False)
    parser.add_argument("--mov-file", dest="mov_file", required=False)
    parser.add_argument("--interval", dest="interval", required=False)
    parser.add_argument("--glider", action="store_true", required=False)
    parser.add_argument("--gosper", action="store_true", required=False)
    args = parser.parse_args()

    # set grid size
    N = 50
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    update_interval = 50
    if args.interval:
        update_interval = int(args.interval)

    # declare game board
    board = np.array([])

    # check flags
    if args.glider:
        board = np.zeros(N * N).reshape(N, N)
        game = LifeBoard(N, board)
        game.spawn_glider(1, 1)
    elif args.gosper:
        board = np.zeros(N * N).reshape(N, N)
        game = LifeBoard(N, board)
        game.spawn_gosper_glider_gun(10, 10)
    else:
        # generate random board
        game = LifeBoard(N)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(game.board, interpolation="nearest")
    ani = animation.FuncAnimation(
        fig,
        game.update_board,
        fargs=(
            img,
            game.board,
            N,
        ),
        frames=10,
        interval=update_interval,
        save_count=50,
    )

    # # of frames?
    # set output file
    if args.mov_file:
        ani.save(args.mov_file, fps=30, extra_args=["-vcodec", "libx264"])

    plt.show()


if __name__ == "__main__":
    main()
