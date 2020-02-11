import unittest

class mainFunctionTests(unittest.TestCase):

		def test_is_pangram_validation(self):
			from DetectPanagram import is_pangram
			pangram = "The quick, brown fox jumps over the lazy dog!"
			self.assertEqual(is_pangram(pangram), True)

 
if __name__=='__main__':
	unittest.main()

