"""
Checks the username and email of the player from the spreadsheet database.
"""
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError

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

    global PLAYER_EMAIL
    global PLAYER_NAME
    global PLAYER_SCORE

    try:
        while True:
            email = valid_email(input('Enter your email address: \n'))
            existing_user = check_registered(email)

            if existing_user:
                PLAYER_EMAIL = WORKSHEET.find(PLAYER_EMAIL).row
                PLAYER_NAME = \
                    WORKSHEET.find(PLAYER_NAME)[1]
                PLAYER_SCORE = \
                    WORKSHEET.find(PLAYER_SCORE)[2]
            else:
                print('Email not found please enter email again: \n')
                new_player_email = input('Please enter your email: \n')
                new_player_name = input('Please enter your name: \n')
                player_data = [new_player_email, new_player_name, 0]
                WORKSHEET.append_row(player_data)
                break
    except TypeError:
        return None


def valid_email(email_address):
    """
    Validates the email given to the form name@emample.com.
    """
    try:
        validate_email(email_address)
        return True
    except EmailNotValidError as err:
        print(str(err) + 'Email address not valid please try again!\n')


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
