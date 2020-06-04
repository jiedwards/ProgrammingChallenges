import unittest

class mainFunctionTests(unittest.TestCase):

		def test_anagram_validation(self):
			from Anagram import anagram
			self.assertEqual(anagram('go go go','gggooo'),True)
			self.assertEqual(anagram('abc','cba'),True)
			self.assertEqual(anagram('hi man','hi     man'),True)
			self.assertEqual(anagram('aabbcc','aabbc'),False)
			self.assertEqual(anagram('123','1 2'),False)
 
if __name__=='__main__':
	unittest.main()

