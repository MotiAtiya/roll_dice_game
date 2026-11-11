import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "DATA/game_history.json"

def load_game_history() -> list:
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def dump_games(games):
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(games, file, indent=2, ensure_ascii=False)

def save_game(game):
    games = load_game_history()
    games.append(game)
    dump_games(games)
    return True
