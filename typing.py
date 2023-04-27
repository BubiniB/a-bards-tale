# Code found at https://www.101computing.net/python-typing-text-effect/

# Used for creating a typing text effect
import time
import sys


def typing_print(text):
    # Let's the text appear as if it was typed.
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
