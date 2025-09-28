import chess
import numpy as np

from typing import Union

COLORS = [chess.WHITE, chess.BLACK]
PIECETYPES = [
    chess.PAWN,
    chess.KNIGHT,
    chess.BISHOP,
    chess.ROOK,
    chess.QUEEN,
    chess.KING,
]


def bitboard_to_array(bitboard: chess.Bitboard) -> np.ndarray:
    return np.array([int(b) for b in bin(bitboard)[2:]]).reshape((8, 8))


def squareset_to_array(squareset: chess.SquareSet) -> np.ndarray:
    return np.array([int(b) for b in reversed(squareset)]).reshape((8, 8))


def position_to_vector(position: chess.Board) -> np.ndarray:
    """Given a board position, return a 8x8x17 vector representing:
    12 channels of 8x8 piece positions (PNBRQKpnbrqk)
        1 if the represented piece is present in the given position
        0 otherwise
    4 channels of 8x8 castling status (white kingside/queenside, black kingside/queenside)
        all 1 if the castling direction is possible
        all 0 otherwise
    1 channel of 8x8 move status
        all 1 if it is white to move
        all 0 if it is black to move
    """
    # Get board vector for each piece
    piece_arrays = []
    for color in COLORS:
        for piece in PIECETYPES:
            piece_array = position.pieces(piece, color)
            piece_array = squareset_to_array(piece_array)
            piece_arrays.append(piece_array)
    # Get board vector for each castling status
    castling_arrays = []
    for color in COLORS:
        castling_array = [
            np.ones((8, 8)) * int(position.has_kingside_castling_rights(color)),
            np.ones((8, 8)) * int(position.has_queenside_castling_rights(color)),
        ]
        castling_arrays.extend(castling_array)
    # Get board vector for move status
    tomove_array = 1 if position.turn == chess.WHITE else 0
    tomove_array = np.ones((8, 8)) * tomove_array
    # Stack vectors along new dimension
    all_arrays = piece_arrays + castling_arrays + [tomove_array]
    position_vector = np.stack(all_arrays, axis=-1)
    return position_vector
