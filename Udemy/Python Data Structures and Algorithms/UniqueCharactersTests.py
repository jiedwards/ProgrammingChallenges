import unittest

class mainFunctionTests(unittest.TestCase):

		def test_unique_characters_validation(self):
			from UniqueCharacters import uni_char
			self.assertEqual(uni_char('goo'), False)
			self.assertEqual(uni_char('abcdefg'), True)
			self.assertEqual(uni_char(''), 'Invalid input length')
 
if __name__=='__main__':
	unittest.main()