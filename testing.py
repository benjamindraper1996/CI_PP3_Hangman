"""
Automated Testing Module
"""
import unittest
from unittest.mock import Mock, patch
import gspread
from google.oauth2.service_account import Credentials
import validation as val

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


# def get_input(text):
#     """Fake player input"""
#     return input(text)


class TestEmail(unittest.TestCase):
    """
    Validates the email given by the player.
    """

    def test_valid_email(self):
        """Tests for a Valid Email"""
        print('Testing For Valid Email')
        self.assertTrue(val.valid_email('test@gmail.com'), True)
        print('Test Complete')

    def test_invalid_email(self):
        """Tests for a Invalid Email"""
        print('Testing For Invalid Email')
        self.assertFalse(val.valid_email('1234'), None)
        print('Test Complete')


# class TestLogin(unittest.TestCase):
#     """
#     Validates the Player Login function.
#     """

#     def test_login(self):
#         """Tests the login function"""
#         print('Testing player login')
#         response = 'test@gmail.com'
#         test_input = Mock(side_effect=response)
#         with patch('builtins.input', test_input):
#             val.login()
#         print('Test Complete')


# class TestNewLogin(unittest.TestCase):
#     """
#     Validates the New Player Login function.
#     """

#     def test_new_login(self):
#         """Tests the login function to create a new player"""
#         print('Testing new player login')

#         self.assertFalse(val.login(), True)
#         print('Test Complete')


if __name__ == "__main__":
    unittest.main()
