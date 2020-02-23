import unittest

class mainFunctionTests(unittest.TestCase):

		def test_add1_array_validation(self):
			from addArray import up_array
			self.assertEqual(up_array([2,3,9]), [2,4,0])
			self.assertEqual(up_array([4,3,2,5]), [4,3,2,6])
			self.assertEqual(up_array([1,-9]), None)

 
if __name__=='__main__':
	unittest.main()

