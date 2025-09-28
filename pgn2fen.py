from pathlib import Path

import chess as ch


def pgn_to_fen(pgn: str | Path) -> list:
    """Given a chess game PGN file, returns a list of FEN position strings one for each move in the game."""

    raise NotImplementedError

    pgn = open(pgn)game = ch.pgn.read_game(pgn)

    print(game.board(pgn))

pgn_to_fen('./test.pgn')
