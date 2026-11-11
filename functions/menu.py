from .utils import clear_screen
from .user_inputs import input_until_valid, input_action_number

def display_menu():
    clear_screen()
    print("""
================================
          ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit

Choose an option:
    """)

def get_action(num_of_options):
    action = input_until_valid(lambda: input_action_number(num_of_options))
    clear_screen()
    return action
