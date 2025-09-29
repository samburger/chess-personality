import chess.pgn
import re
from pathlib import Path

def sanitize_for_filename(s: str, maxlen: int = 180) -> str:
    """Remove file-name-unsafe characters; replace spaces with underscores"""

    if not s:
        return "unknown"
    s = s.strip().replace(" ", "_")

    # remove any characters that are not word/dash/dot/underscore
    s = re.sub(r"[^\w\-\._]", "", s)
    return s[:maxlen]

def parse_pgn(pgn_file: str | Path) -> None:
    """Takes multi-game PGN files and iteratively makes one-game-per-file PGNs in a new directory"""
    pgn_path = Path(pgn_file)
    out_dir = Path("parsed_master_games") # note: this will output to current directory!
    out_dir.mkdir(exist_ok=True)

    all_games = open(pgn_path)

    num_games = 1 # used to give unique names to different games with repeated metadata

    while True:
        game = chess.pgn.read_game(all_games)
        if game is None: # game is None when end of file is reached
            break

        headers = game.headers

        # create unqiue file names with white player then black player; soft cap on 9999 games
        file_name = sanitize_for_filename(f"{headers.get('White')}_vs_{headers.get('Black')}_{headers.get('Date')}_{num_games:04d}.pgn")

        # save each game in PGN format to the parsed_master_games directory
        with open(out_dir / file_name, "w", encoding="utf-8") as out:
            exporter = chess.pgn.FileExporter(out)
            game.accept(exporter)
        
        num_games += 1 # increment to make unique file names

def parse_all_pgn(dir: str | Path) -> None:
    """Uses parse_pgn function on all .pgn files in a given directory"""
    dir = Path(dir)

    for pgn_path in dir.glob('*.pgn'):
        parse_pgn(pgn_path)

# example usage below; caution, it takes ~0.5 Ash Twin Project cycles
# and I can smell my processor...
# parse_all_pgn('./concat_master_games')