import unittest

class mainFunctionTests(unittest.TestCase):

		def test_odd_or_even_validation(self):
			from odd_or_even import oddOrEven
			self.assertEqual(oddOrEven([0, 1, 2]), 'odd')
			self.assertEqual(oddOrEven([0, 1, 3]), 'even')
			self.assertEqual(oddOrEven([1023, 1, 2]), 'even')
 
if __name__=='__main__':
	unittest.main()

