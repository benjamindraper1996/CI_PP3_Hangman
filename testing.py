"""
Automated Testing Module
"""

import unittest
import validation as val


class TestValidEmail(unittest.TestCase):
    """
    Validates the player email input.
    """
    def test_valid_email(self):
        """Tests for a Valid Email"""
        self.assertTrue(val.valid_email('test@gmail.com'), True)

    def test_invalid_email(self):
        """Tests for invalid email"""
        self.assertTrue(val.valid_email('1234'), None)
