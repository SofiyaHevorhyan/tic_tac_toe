# File: board_people.py
# A simple module representing players
# Note: DEFAULT_ROW and DEFAULT_COL for board is 3

from copy import deepcopy


class Board:
    """
    Representing board for tic tac toe, default size - 3x3
    """
    CROSS = "x"
    ZERO = "o"
    NUM_ROWS = 3
    NUM_COL = 3

    def __init__(self):
        """
        Initialize new board with parameters state, representing the state of
        the board and fill, representing the num of filled cells
        """
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]

        # None for undefined, 0 for dead heat, 1 for player1's win, -1 for other
        self.state = None
        self.fill = 0
        # representing last move as symbol, row and col
        self.last_move = None

    def win(self):
        """
        Inspects if there is the end of the game, changing parameter state in
        self - 1 for winning cross, -1 for winning zero's, 0 for dead heat,
        None for undefined condition
        """
        condition = self._condition()
        if condition == self.CROSS:
            self.state = 1
        elif condition == self.ZERO:
            self.state = -1
        elif condition == 0:
            self.state = condition
        else:
            self.state = None

    def _condition(self):
        """
        Inspects if there is some winning combinations on the board
        :return: 0 for dead heat, symbol for winning, None for undefined
        """
        # check rows and columns
        for i in range(self.NUM_ROWS):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and \
                    self.board[i][0] is not None:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and \
                    self.board[0][i] is not None:
                return self.board[0][i]

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and \
                self.board[0][0] is not None:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and \
                self.board[0][2] is not None:
            return self.board[0][2]

        # check if there is undefined condition
        if self.fill < 9:
            return None
        return 0

    def __str__(self):
        """
        Represents board as a string
        """
        brd = ""
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COL):
                sign = self.board[i][j]
                brd += sign if sign else " "
            brd += "\n"

        return brd

    def possible_moves(self, symbol):
        """
        Forms list of all possible moves for the board
        :param symbol: symbol to put on the board for each possibility
        :return: list of boards
        """
        possibilities = list()
        for i in range(self.NUM_ROWS):
            for j in range(self.NUM_COL):
                if not self.board[i][j]:
                    new_board = self.add_move(symbol, (i, j))
                    possibilities.append(new_board)

        return possibilities

    def add_move(self, item, index, permission=False):
        """
        Add an item to the given position (index) if there is space at this pos
        :param item: symbol to put on a position, str
        :param index: tuple of row and col to put
        :param permission: bool
        :return: board
        """
        assert len(index) == 2, "invalid parameters to add move to the board"
        row = index[0]
        col = index[1]
        assert (int, row) and (0 <= row < self.NUM_ROWS), "invalid row"
        assert (int, col) and (0 <= col < self.NUM_COL), "invalid col"
        new = deepcopy(self)

        # if someone has permission it can set whatever move he wants
        if new.board[row][col] is None or permission:
            new.board[row][col] = item
            new.last_move = (item, row, col)
            if item is not None:
                new.fill += 1
            else:
                new.fill -= 1
            new.win()

        return new
