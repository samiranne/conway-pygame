from collections import defaultdict


class Conway(object):

    def __init__(self, size, live_cells=None):
        """
        Constructs a game board for Conway's Game Of Life.

        Args:
            size (int): The width and length of the square game board
                        to be generated.
            live_cells (list): An optional list of tuples indicating the
                               coordinates of all cells that are "alive"
                               at the start of the game. If None, assumes
                               that no cells are alive at the start of the
                               game.
        """
        self.size = size
        self.board = defaultdict(lambda: 0)
        live_cells = live_cells if live_cells is not None else []
        for (row, col) in live_cells:
            self.board[(row, col)] = 1
        self.generation = 0

    def __getitem__(self, coordinate):
        return self.board[coordinate]

    def __setitem__(self, coordinate, value):
        if value != 0 and value != 1:
            raise ValueError("{0} is not a valid value for a cell." +
                             "Valid values are 0 or 1".format(value))
        (row, column) = coordinate
        if row < 0 or row >= self.size:
            raise IndexError("{0} is not a valid row for a game of size {1}"
                             .format(row, self.size))
        if column < 0 or column >= self.size:
            raise IndexError("{0} is not a valid column for a game of size {1}"
                             .format(column, self.size))
        self.board[(row, column)] = value

    def __str__(self):
        result = ""
        for row in range(self.size):
            for col in range(self.size):
                if self.board[(row, col)] == 1:
                    result += "x "
                else:
                    result += ". "
            result += "\n"
        return result

    def step(self):
        self.generation += 1
        cells_to_update = {}
        for row in range(self.size):
            for col in range(self.size):
                neighbor_sum = self.sum_neighbors(row, col)
                if self.board[(row, col)] == 0:
                    if neighbor_sum == 3:
                        cells_to_update[(row, col)] = 1
                else:
                    if neighbor_sum > 3 or neighbor_sum < 2:
                        cells_to_update[(row, col)] = 0
        self.board.update(cells_to_update)

    def sum_neighbors(self, row, col):
        neighbors = [self.board[(i, j)] for i in [row - 1, row, row + 1]
                     for j in [col - 1, col, col + 1]]
        return sum(neighbors, (self.board[(row, col)] * -1))

    def clear(self):
        self.board = defaultdict(lambda: 0)
        self.generation = 0


# conway = Conway(10, [(1, 1), (1, 2), (1, 3)])
# for i in range(5):
#     print(conway)
#     conway.step()
