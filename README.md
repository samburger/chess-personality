# Chess Personality Project

A chess stylometry system that analyzes playing styles and matches players to historical chess masters.

## Overview
This project implements the chess stylometry research from the papers in `papers/`. We build a system that:
- Parses PGN files and extracts chess games
- Uses CNN + Transformer architecture to create player embeddings
- Compares uploaded games against historical chess masters
- Provides personality matching results via web interface

Note: We focus on stylometry/player comparisons only (not the Maia-2 engine extensions).

## Environment
- Use `uv` for Python environment management
- Run tests with: `uv run pytest`

## Architecture
- Backend: FastAPI with SQLite database
- ML Pipeline: CNN feature extraction � Transformer aggregation � Player embeddings
- Frontend: Vanilla HTML/CSS/JS
- Processing: Async job queue for analysis tasks


## TODO:

- Implement vectorization for moves
  - 2 FEN go in (before/after), 1 vector comes out
  - 8x8x17
    - First 12 channels: one 8x8 for each piece color/type
      - zeroes(), 1 for each position holding that piece
    - Next 4 channels: all ones() if player can castle
      - White kingside, white queenside, black kingside, black queenside
    - Last channel: all ones() if player to move is white
  - One "move" is a tuple of two position vectors (before/after)
- Create PGN cleanser to remove games with <10 turns, insufficient metadata, etc.

