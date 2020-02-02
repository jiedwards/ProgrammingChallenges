import unittest

class mainFunctionTests(unittest.TestCase):

		def test_largest_one_digit_validation_invalid(self):
			from largestOneDigitInt import largestOneDigit
			self.assertTrue(largestOneDigit([0,0,0,0]) == "Invalid input supplied")

		def test_largest_one_digit_validation_valid(self):
			from largestOneDigitInt import largestOneDigit
			self.assertTrue(largestOneDigit([3,0,9,0]) == 9)
 
if __name__=='__main__':
	unittest.main()