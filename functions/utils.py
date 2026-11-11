import os

def clear_screen():
    # Clear the terminal screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')
