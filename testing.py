"""
Automated Testing Module
"""
import unittest
from unittest import mock
import validation as val
import run as run


class TestEmail(unittest.TestCase):
    """
    Validates the email given by the player.
    """

    def test_valid_email(self):
        """Tests for a Valid Email"""
        print('Testing For Valid Email')
        self.assertTrue(val.valid_email('test@gmail.com'), True)

    def test_invalid_email(self):
        """Tests for a Invalid Email"""
        print('Testing For Invalid Email')
        self.assertFalse(val.valid_email('1234'), None)


class TestLogin(unittest.TestCase):
    """
    Validates the Player Login function.
    """

    def test_login(self):
        """Tests the login function"""
        print('Testing player login')
        with mock.patch(
         'builtins.input', side_effect=iter(['test@gmail.com', ])):
            assert val.login() is run.title()


class TestNewLogin(unittest.TestCase):
    """
    Validates the New Player Login function.
    """

    def test_new_login(self):
        """Tests the login function to create a new player"""
        print('Testing new player login')
        with mock.patch(
          'builtins.input', side_effect=iter(['1234@gmail.com', 'test', ])):
            assert val.login() is run.title()

    def test_temp_login(self):
        """deletes the email to be reused on the next run"""
        test_email = '1234@gmail.com'
        test_player = val.WORKSHEET.find(test_email).row
        val.WORKSHEET.delete_rows(test_player)


class TestDisplays(unittest.TestCase):
    """
    Tests the title, clear_log and welcome_message functions
    """

    def test_title(self):
        """Tests the title function"""
        print('Testing title print')
        self.assertFalse(run.title(), True)

    def test_clear_log(self):
        """Tests clear_log function"""
        print('Testing clear_log')
        with mock.patch(
          'os.system', side_effect=iter(['posix', 'dos', 'err'])):
            self.assertIsNone(run.clear_log(), True)

    # def test_welcome_message(self):
    #     """Tests welcome_message function"""
    #     print('Testing welcome_message')


class TestRestartGame(unittest.TestCase):
    """
    Tests the restart_game function
    """

    def test_restart_game(self):
        """Tests restart_game function"""
        print('Testing restart_game')
        text = ['x', 'y', 'n']
        with mock.patch('builtins.input', side_effect=iter(text)):
            assert run.restart_game() is run.title()


if __name__ == "__main__":
    unittest.main()
