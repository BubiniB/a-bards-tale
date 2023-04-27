"""
Used to clear terminal for Windows
Mac and Linux.
Code found at https://www.tutorialspoint.com/how-to-clear-python-shell.
"""
from os import system, name

# Used for delaying clear terminal
from time import sleep


def clear_terminal():
    """
    Clears the terminal for devices running on Windows,
    Mac or Linux, after 3 seconds. Used in game_over().
    """
    sleep(3)
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For Mac and Linux
    else:
        _ = system('clear')
