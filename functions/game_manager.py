import random
from .user_inputs import input_until_valid, input_user_name, input_rounds
from .printer import print_title


def roll_dice() -> int:
    return random.randint(1, 6)


def play_round() -> dict:
    return {
        "player_dice": roll_dice(),
        "computer_dice": roll_dice()
    }


def calculate_round_winner(round, player_name):
    if round["player_dice"] > round["computer_dice"]:
        return player_name
    if round["player_dice"] < round["computer_dice"]:
        return "Computer"
    return "None"


def calculate_scores(round_results):
    player = computer = 0
    for round in round_results:
        if round["player_dice"] > round["computer_dice"]:
            player += 1
        elif round["player_dice"] < round["computer_dice"]:
            computer += 1
    return player, computer


def calculate_winner(player_score, computer_score, player_name):
    if player_score > computer_score:
        return player_name
    if player_score < computer_score:
        return "Computer"
    return "None"


def start_game() -> dict:
    print_title("New Game")
    player_name = input_until_valid(input_user_name)
    num_of_rounds = input_until_valid(input_rounds)
    round_results = []

    for i in range(num_of_rounds):
        round = play_round()
        round["round"] = i + 1
        round["winner"] = calculate_round_winner(round, player_name)
        round_results.append(round)


    player_score, computer_score = calculate_scores(round_results)
    winner = calculate_winner(player_score, computer_score, player_name)

    game_data = {
        "player_name": player_name,
        "rounds": num_of_rounds,
        "player_score": player_score,
        "computer_score": computer_score,
        "winner": winner,
        "results": round_results
    }
    return game_data
