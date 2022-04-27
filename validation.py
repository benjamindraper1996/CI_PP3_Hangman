"""
Checks the username and email of the player from the spreadsheet database.
"""
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from run import game

# Scope vars as defined in code institute Love_Sandwiches walk-through.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# My database values.
SHEET = GSPREAD_CLIENT.open('CI_PP3_Hangman')
WORKSHEET = SHEET.worksheet("Users")


def login():
    """
    Logs existing players in and creates new accoutns.
    """

    global player_score
    global player_row

    try:
        while True:
            email = get_email()
            existing_user = check_registered(email)

            if existing_user:
                player_row = WORKSHEET.find(email).row
                player_name = WORKSHEET.row_values(player_row)[1]
                player_score = int(WORKSHEET.row_values(player_row)[2])
                print(f'Hello again {player_name}.\n')
                print(f'Your score is {player_score}.\n')
                game()
            else:
                new_player_name = input('Please enter your name: \n')
                player = [email, new_player_name, 0]
                WORKSHEET.append_row(player)
                game()
    except TypeError:
        return None


def get_email():
    """
    Gets the users email address.
    """
    while True:
        email = input('Please enter your email address to continue: \n')
        if valid_email(email):
            break
    return email


def valid_email(email):
    """
    Validates the email given to the format name@emample.com.
    """
    print('Validating email address...')
    try:
        validate_email(email)
        return True
    except EmailNotValidError as err:
        print(str(err), 'Email address not valid please try again!\n')


def check_registered(email):
    """
    Checks if the player is already registered.
    """
    print('Checking registration status...')
    col_email = WORKSHEET.col_values(1)

    if email in col_email:
        return True
    else:
        return False
