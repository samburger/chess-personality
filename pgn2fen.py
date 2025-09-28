import numpy as np
from pathlib import Path

import chess.pgn


def pgn_to_fen(pgn_file: str | Path) -> np.array:
    """Given a chess game PGN file, returns a NumPy array of FEN position strings for each move in the game."""

    # open provided .pgn file using chess.pgn
    pgn_game = open(pgn_file)
    game = chess.pgn.read_game(pgn_game)

    # initialize board position and fen array
    board = game.board()
    fen_array = []

    # for each position, append to array and progress one move
    for move in game.mainline_moves():
        fen_array.append(board.fen())
        board.push(move)
    fen_array.append(board.fen()) # append final position outside of loop
    
    return np.array(fen_array)