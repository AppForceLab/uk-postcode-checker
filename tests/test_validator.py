import unittest
from ukpostcode.validator import UKPostcodeValidator

class TestUKPostcodeValidator(unittest.TestCase):

    def test_valid_postcodes(self):
        self.assertTrue(UKPostcodeValidator.is_valid("SW1A 1AA"))
        self.assertTrue(UKPostcodeValidator.is_valid("EC1A1BB"))

    def test_invalid_postcodes(self):
        self.assertFalse(UKPostcodeValidator.is_valid("1234"))
        self.assertFalse(UKPostcodeValidator.is_valid("XYZ"))

    def test_formatting(self):
        self.assertEqual(UKPostcodeValidator.format("sw1a1aa"), "SW1A 1AA")
        self.assertEqual(UKPostcodeValidator.format("EC1A1BB"), "EC1A 1BB")

    def test_invalid_format_raises(self):
        with self.assertRaises(ValueError):
            UKPostcodeValidator.format("invalid")
