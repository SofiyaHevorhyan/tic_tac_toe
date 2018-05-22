# File: play.py
# A simple module for playing tic tac toy game
# By Sofiya Hevorhyan

from cross_zeros.board import Board
from cross_zeros.people import Player, Bot


def choose_players():
    """
    functions set the type of the toe - with two bots, two users or user vs.bot
    :return: tuple of players
    """
    message = "Choose players:\n0 for 2 bots,\n1 for player&bot,\n" \
              "2 for 2 players: "
    res = get_response(message, ["0", "1", "2"])

    if res == "0":
        print("Please, be patient. Computation will take a second")
        return Bot("Bot1", Board.CROSS), Bot("Bot2", Board.ZERO)
    elif res == "1":
        variant = get_response("U want to be Player 1 or 2? ", ["1", "2"])
        print("Please, be patient. Computation will take a second")
        return (Player("Player 1", Board.CROSS), Bot("Bot1", Board.ZERO)) \
            if variant == "1" else \
            (Bot("Bot1", Board.CROSS), Player("Player 2", Board.ZERO))
    else:
        return Player("Player 1", Board.CROSS), Player("Player 2", Board.ZERO)


def get_response(message, valid):
    """
    the function gets
    :param message:
    :param valid:
    :return:
    """
    response = input(message)
    while response not in valid:
        response = input(message)
    return response


if __name__ == "__main__":
    brd = Board()
    plr, bot = choose_players()

    while brd.state is None:
        brd = plr.make_move(brd)
        print(brd)

        if brd.state is None:
            brd = bot.make_move(brd)
            print(brd)

    if brd.state == 0:
        print("Dead Heat")
    elif brd.state == 1:
        print(f"Oooops {plr.name} wins! Congratulations!")
    else:
        print(f"Oooops {bot.name} wins! Congratulations!")
