import unittest

class mainFunctionTests(unittest.TestCase):

		def test_sum_of_multiples_validation(self):
			from SumOfMultiples import find
			self.assertEqual(find(5), 8)
			self.assertEqual(find(10), 33)
			self.assertEqual(find(94), 2028)
 
if __name__=='__main__':
	unittest.main()

