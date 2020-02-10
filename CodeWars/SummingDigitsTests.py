import unittest

class mainFunctionTests(unittest.TestCase):

		def test_sum_digits_validation(self):
			from SummingDigits import sum_digits
			self.assertEqual(sum_digits(10), 1)
			self.assertEqual(sum_digits(99), 18)
			self.assertEqual(sum_digits(-32), 5)
 
if __name__=='__main__':
	unittest.main()

