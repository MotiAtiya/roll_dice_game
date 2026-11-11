def print_title(title) -> None:
    print("* * * *  " + title + "  * * * *\n")

def display_round_results(round, plyaer_name):
    print(f"\n---------- ROUND {round["round"]} ----------\n")
    print(f"{f"{plyaer_name}:".ljust(15)}🎲 {round["player_dice"]}")
    print(f"{"Computer:".ljust(15)}🎲 {round["computer_dice"]}")
    print()
    
    if round["winner"]:
        print(f"{round["winner"]} wins this round!")
    else:
        print(f"The round ended in a draw")

def display_game_results(game) -> None:
    for round in game["results"]:
        display_round_results(round, game["player_name"])

    print("""
================================
          GAME OVER
================================
    """)
    print(f"{f"{game["player_name"]}:".ljust(15)}{game["player_score"]}")
    print(f"{"Computer:".ljust(15)}{game["computer_score"]}")
    print()
    if game["winner"]:
        print(f"WINNER: {game["winner"]}!")
    else:
        print("The game ended in a draw")
    

def display_game_history(history) -> None:
    if history == []:
        print("There are no saved games yet")
        return
    
    for game in history:
        print(f"{game["player_name"]} vs Computer")
        print(f"{game["rounds"]} rounds")
        print(f"{f"{game["player_name"]}:".ljust(15)}{game["player_score"]}")
        print(f"{"Computer:".ljust(15)}{game["computer_score"]}")
        if game["winner"] != "None":
            print(f"WINNER: {game["winner"]}!")
        else:
            print("The game ended in a draw")
        print()


def display_statistics(history) -> None:
    if history == []:
        print("There are no saved games yet")
        return

    players = computer = draws = 0
    for game in history:
        if game["winner"] == "Computer":
            computer += 1
        elif game["winner"] == "None":
            draws += 1
        else:
            players += 1

    print(f"{len(history)} games in total")
    print("WINNINGS:")
    print("players:", players)
    print("computer:", computer)
    print("draws:", draws)
    print()
    print(f"Players' win percentage:, {round(players / len(history) * 100)}%")
