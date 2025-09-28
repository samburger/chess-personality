import numpy as np

import chess
from pgn2fen import pgn_to_fen


def fen_to_board(fen_array: np.array) -> np.array:
    """Given a NumPy array of FEN strings, returns a NumPy array of python-chess Board objects."""

    board_array = []

    for fen in fen_array:
        board_array.append(chess.Board(fen))

    return np.array(board_array)
    
print(fen_to_board(pgn_to_fen('./test.pgn')))