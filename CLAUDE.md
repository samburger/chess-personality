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
- Start development server: `uv run python -m app.main`

## Architecture
- Backend: FastAPI with SQLite database
- ML Pipeline: CNN feature extraction ’ Transformer aggregation ’ Player embeddings
- Frontend: Vanilla HTML/CSS/JS
- Processing: Async job queue for analysis tasks