from functions.menu import display_menu, get_action
from functions.game_manager import start_game
from functions.printer import display_game_results, display_game_history, display_statistics
from functions.data_manager import load_game_history, save_game

def main() -> None:

    while True:
        try:
            display_menu()
            action = get_action(4)

            match action:
                case 1:
                    game = start_game()
                    display_game_results(game)
                    if save_game(game):
                        print("Game saved successfully!")
                case 2:
                    games = load_game_history()
                    display_game_history(games)
                case 3:
                    games = load_game_history()
                    display_statistics(games)
                case 4:
                    print("Bye!")
                    exit(0)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()