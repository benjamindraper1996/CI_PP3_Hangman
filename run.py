"""
Hangman game file.
"""
import os
import random
import string
import validation as val

# List of words for use inside the game.
LIBRARY = ["computer", "approach", "daughter", "positive", "dedicate",
           "solution", "evaluate", "minimize", "delicate", "producer",
           "definite", "hardware", "terminal", "finished", "absolute",
           "scenario", "argument", "category", "variable", "function"]

gallows_dict = {
    0: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |        /|\\
        |         |
        |        / \\
        |___________
    """,
    1: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |         |\\
        |         |
        |        / \\
        |___________
    """,
    2: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |         |
        |         |
        |        / \\
        |___________
    """,
    3: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |         |
        |         |
        |        /
        |___________
    """,
    4: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |         |
        |         |
        |
        |___________
    """,
    5: """
        ___________
        |  /      |
        | /       |
        |/       ( )
        |
        |
        |
        |___________
    """,
    6: """
        ___________
        |  /      |
        | /       |
        |/
        |
        |
        |
        |___________
    """,
    7: """
        ___________
        |  /
        | /
        |/
        |
        |
        |
        |___________
    """,
    8: """
        ___________
        |
        |
        |
        |
        |
        |
        |___________
    """,
    9: """

        |
        |
        |
        |
        |
        |
        |___________
    """,
    10: """







        ____________
    """}


def pick_word(lib):
    """
    Chooses a random word from the library.
    """
    word = random.choice(lib).lower()

    return word


def clear_log(lines=80):
    """
    Clears the console screen.
    lines variable used as the fallback option when the OS is unknown.
    """
    if os.name == 'posix':
        # Linux/MacOS/etc
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for unknown OS
        print('\n' * lines)


def restart_game():
    """
    Reloads the game when it has been won or lost.
    """
    while True:
        end_game = input('Would you like to play again? y/n\n').lower()
        if end_game == 'y':
            clear_log()
            game()
        elif end_game == 'n':
            clear_log()
            print('Thanks for playing! To restart, press the button above.')
            exit()
        else:
            clear_log()
            print('Invalid character, Please try again!\n')


def game():
    """
    Gather user input and check against the 'game_word' variable.
    """
    game_word = pick_word(LIBRARY)
    letters = set(game_word)
    alphabet = set(string.ascii_lowercase)
    attempts = set()
    lives_left = 10

    title()

    while len(letters) > 0 and lives_left > 0:
        print(f'Lives remaining: {lives_left}')
        print('These are the letters you have used: ', ' '.join(attempts))
        guess = [letter if letter in attempts else '_' for letter in game_word]
        print(gallows_dict[lives_left])
        print(' '.join(guess))
        user_choice = input('Try and guess a letter:\n').lower()
        if user_choice in alphabet - attempts:
            attempts.add(user_choice)
            if user_choice in letters:
                letters.remove(user_choice)
                clear_log()
                title()
                print(f'{user_choice} is a correct letter!\n')
            else:
                lives_left -= 1
                clear_log()
                title()
                print(f'{user_choice} is not part of the word.\n')
        elif user_choice in attempts:
            clear_log()
            title()
            print(f'{user_choice} has been used, Please try again!\n')
        else:
            clear_log()
            title()
            print('Invalid character, Please try again!\n')

    if lives_left == 0:
        clear_log()
        title()
        print(gallows_dict[lives_left])
        print(f'You have runout of lives! The word was {game_word}.')
        restart_game()
    else:
        clear_log()
        title()
        val.player_score += 1
        val.WORKSHEET.update_cell(val.player_row, 3, val.player_score)
        print(f'Well done you managed to guess the word {game_word}!')
        restart_game()


def title():
    """
    Creates a Header for the game.
    """
    print("""
    #     #       #       #     #    ###      #       #       #       #     #
    #     #      # #      ##    #  ##   ##    ##     ##      # #      ##    #
    #     #     #   #     # #   # #           # #   # #     #   #     # #   #
    #######    #######    #  #  # #     ##### #  # #  #    #######    #  #  #
    #     #   #       #   #   # # #       #   #   #   #   #       #   #   # #
    #     #  #         #  #    ##  ##   ##    #       #  #         #  #    ##
    #     # #           # #     #    ###      #       # #           # #     #
    """)


def welcome_message():
    """
    Prints a title and a message explaining how to play the game.
    """
    title()
    print(
        'To play the game enter a letter to guess,\n'
        'If it is in the word the letter will reveal itself.\n'
        'If it is not in the word you will lose a life!\n')
    val.login()


def main():
    """
    Run all game functions.
    """
    pick_word(LIBRARY)
    welcome_message()
    game()
    restart_game()


if __name__ == "__main__":
    main()
