import random
import string

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

    return word


def game():
    """
    Gather user input and check against the 'word' variable.
    """
    game_word = pick_word(LIBRARY)
    letters = set(game_word)
    alphabet = set(string.ascii_lowercase)
    attempts = set()
    lives_left = 11

    while len(letters) > 0:
        print(f'Lives remaining: {lives_left}')
        print(f'These are the letters you have used:', ' '.join(attempts))
        guess = [letter if letter in attempts else '_' for letter in game_word]
        print(' '.join(guess))
        user_choice = input('Try and guess a letter:\n').lower()
        if user_choice in alphabet - attempts:
            attempts.add(user_choice)
            if user_choice in letters:
                letters.remove(user_choice)
            else:
                lives_left -= 1
                print('Letter is not in the word.\n')
        elif user_choice in attempts:
            print('This letter has been used, Please try again!\n')
        else:
            print('Invalid character, Please try again!\n')

    if lives_left == 0:
        print(f'You have runout of lives! The word was {game_word}.')
    else:
        print(f'Well done you managed to guess the word {game_word}!')


def main():
    """
    Run all game functions.
    """
    pick_word(LIBRARY)
    game()


main()
