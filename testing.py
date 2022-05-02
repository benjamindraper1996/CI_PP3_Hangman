"""
Automated Testing Module
"""
import unittest
import validation as val


class TestEmail(unittest.TestCase):
    """
    Validates the email given by the player.
    """
    def test_valid_email(self):
        """Tests for a Valid Email"""
        self.assertTrue(val.valid_email('test@gmail.com'), True)

    def test_invalid_email(self):
        """Tests for a Invalid Email"""
        self.assertFalse(val.valid_email('1234'), None)


class TestLogin(unittest.TestCase):
    """
    Validates the Player Login function.
    """

    def test_login(self):
        """Tests the login Function"""
        self.assertTrue(val.login(), True)  # Requires User interaction
