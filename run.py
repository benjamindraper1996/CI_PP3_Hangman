import random

# List of words for use inside the game.
LIBRARY = ["computer", "approach", "daughter", "positive", "dedicate",
           "solution", "evaluate", "minimize", "delicate", "producer",
           "definite", "hardware", "terminal", "finished", "absolute",
           "scenario", "argument", "category", "variable", "function"]


def pick_word(lib):
    """
    Chooses a random word from the library.
    """
    word = random.choice(lib).lower()

    print(word)


def main():
    """
    Run all game functions.
    """
    pick_word(LIBRARY)


main()
