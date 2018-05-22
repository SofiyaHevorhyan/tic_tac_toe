# File: btree.py
# A simple module representing the tree of different choices to make

from anytree import RenderTree, Node
from cross_zeros.board import Board


class BuildTree:
    """
    Built a tree using module anytree
    """
    def __init__(self, brd):
        """
        Initialize new tree with given board as a Node for root of the tree
        :param brd: Board(), the root of the tree
        """
        board = Node(brd)
        self.tree = RenderTree(board)

    def best_choice(self, symbol):
        """
        Built all choices for given board and symbol and pick up the best
        (the one that has max num of (winning - losing) )
        :param symbol: the symbol for which best choice should be found
        :return: board, the best choice
        """
        self._fill_tree(symbol)
        board = max(self.tree.node.children, key=lambda x: x.chance)
        return board.name

    def _fill_tree(self, symbol):
        """
        built a tree with all moves for given symbol
        :param symbol: str
        """

        def fill_tree_node(node, sym):
            """
            Recursive function for building a tree using Node from anytree
            :param node: the node for which all choices must be found
            :param sym: the symbol for which choices must be found
            """
            current_board = node.name
            children = current_board.possible_moves(sym)

            for brd in children:
                child = Node(brd, parent=node, chance=None)

                # if winning is for current symbol, return 1 as win
                # losing count as -1, dead heat as 0
                if brd.state:
                    if (brd.state == 1 and symbol == brd.CROSS) or \
                            (brd.state == -1 and symbol == brd.ZERO):
                        chance = 1
                    else:
                        chance = -1
                elif brd.state == 0:
                    chance = 0

                # if the state on the board is uncertain, change symbol for
                # which possible moves will be found and start recursion
                else:
                    sym = brd.CROSS if brd.last_move[0] == brd.ZERO \
                        else brd.ZERO
                    fill_tree_node(child, sym)
                    chance = sum([elem.chance for elem in child.children])

                child.chance = chance

        fill_tree_node(self.tree.node, symbol)


if __name__ == "__main__":

    board1 = Board()
    board1 = board1.add_move("x", (0, 0))
    board1 = board1.add_move("o", (0, 1))
    board1 = board1.add_move("x", (0, 2))

    board1 = board1.add_move("x", (1, 0))
    board1 = board1.add_move("o", (1, 1))
    board1 = board1.add_move("o", (1, 2))

    print("Searching the tree of moves for:\n", board1)
    tree = BuildTree(board1)
    best_board = tree.best_choice("x")
    print(best_board)
    print(tree.tree.by_attr())
