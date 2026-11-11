from datetime import datetime

def input_until_valid(input_func):
    while True:
        try:
            return input_func()
        except ValueError as e:
            print(f"Error: {e}\n")


def input_action_number(num_of_options) -> int:
    try:
        action = int(input())
        if not 1 <= action <= num_of_options:
            raise ValueError(f"Invalid choice. Choose an option [0-{num_of_options}]")
        return action
    except ValueError:
        raise ValueError(f"Your choice must be an integer number [0-{num_of_options}]!")


def input_user_name() -> str:
    name = input("Enter player name: ")
    if name.isdigit():
        raise ValueError("Player name must be a string!")
    if not name:
        raise ValueError("Planyer name cannot be empty")
    return name


def input_rounds() -> int:
    try:
        rounds = int(input("How much rounds do you want to play? [1-10]: "))
    except ValueError:
        raise ValueError("Rounds must be an integer number!")
    if not 1 <= rounds <= 10:
        raise ValueError("Rounds must be between 1 to 10!")
    return rounds
