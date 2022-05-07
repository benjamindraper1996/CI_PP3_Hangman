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

PLAYER_SCORE = int()
EMAIL = str()
PLAYER_ROW = int()
PLAYER_NAME = str()


def login():
    """
    Logs existing players in and creates new accounts.
    """
    global PLAYER_SCORE
    global EMAIL
    global PLAYER_ROW
    global PLAYER_NAME

    try:
        while True:
            EMAIL = get_email()
            existing_user = check_registered(EMAIL)

            if existing_user:
                PLAYER_ROW = WORKSHEET.find(EMAIL).row
                PLAYER_NAME = WORKSHEET.row_values(PLAYER_ROW)[1]
                PLAYER_SCORE = int(WORKSHEET.row_values(PLAYER_ROW)[2])
                game()
            else:
                new_name = input('Your a new player, enter your name: \n')
                player = [EMAIL, new_name, 0]
                WORKSHEET.append_row(player)
                game()
    except TypeError:
        return None


def get_email():
    """
    Gets the users email address.
    """
    while True:
        EMAIL = input('Please enter your email address to continue: \n')
        if valid_email(EMAIL):
            break
    return EMAIL


def valid_email(EMAIL):
    """
    Validates the email given to the format name@example.com.
    """
    print('Validating email address...')
    try:
        validate_email(EMAIL)
        return True
    except EmailNotValidError as err:
        print(str(err))
        print('Email address not valid please try again!')


def check_registered(EMAIL):
    """
    Checks if the player is already registered.
    """
    print('Checking registration status...')
    col_email = WORKSHEET.col_values(1)

    if EMAIL in col_email:
        return True
    else:
        return False
