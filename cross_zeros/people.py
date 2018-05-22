# File: people.py
# Representing module with classes for all persons in the game

from cross_zeros.btree import BuildTree


def get_input(message):
    """
    the function gets move from user for the tic toc toe
    :param message: str
    :return: tuple of int
    """
    while True:
        try:
            move = input(message).split()
            assert len(move) >= 2, "Invalid len"

            permit = True if len(move) == 3 and move[2] == "FICHA!" else False
            move = tuple(map(int, move[:2]))
            assert move[0] in [1, 2, 3] and move[1] in [1, 2, 3], "Invalid num"

            return move[0]-1, move[1]-1, permit
        except (ValueError, AssertionError):
            continue


class AbstractPlayer:
    """
    Representing some common info about players
    """
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Player(AbstractPlayer):
    def make_move(self, board):
        """
        the player makes move by getting parameters from user
        :param board: board on which the move will be made
        :return: board with made move
        """
        row, col, permission = get_input(f"{self.name} Enter move "
                                         f"(two nums, row and col, "
                                         f"divided by space): ")

        return board.add_move(self.symbol, (row, col), permission=permission)


class Bot(AbstractPlayer):
    def make_move(self, board):
        """
        the bots makes move by building all possible moves for this board and
        choosing one with the biggest chance to win
        :param board: board on which the move will be made
        :return: board with made move
        """
        new_board = BuildTree(board).best_choice(self.symbol)
        return new_board
