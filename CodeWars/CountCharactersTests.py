import unittest

class mainFunctionTests(unittest.TestCase):

		def test_count_validation(self):
			from CountCharacters import count
			self.assertEqual(count('aba'), {'a': 2, 'b': 1})
			self.assertEqual(count(''), {})
 
if __name__=='__main__':
	unittest.main()
