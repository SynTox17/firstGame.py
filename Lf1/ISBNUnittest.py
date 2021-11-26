import unittest
from ISBN_function import generate_check_digit


class EintrittTest(unittest.TestCase):

    def testCheckDigitGeneration(self):

        self.assertEqual(9, generate_check_digit(213456789))
        self.assertEqual(9, generate_check_digit(123456798))
        self.assertEqual(0, generate_check_digit(987654321))
        self.assertEqual(8, generate_check_digit(123123123))
        self.assertEqual(4, generate_check_digit(481516234))


if __name__ == "__main__":
    unittest.main()