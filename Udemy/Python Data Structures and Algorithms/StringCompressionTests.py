import unittest

class mainFunctionTests(unittest.TestCase):

		def test_compression_validation(self):
			from StringCompression import compress
			self.assertEqual(compress(''), 'Invalid input length.')
			self.assertEqual(compress('AABBCC'), 'A2B2C2')
			self.assertEqual(compress('AAABCCDDDDD'), 'A3B1C2D5')
			self.assertEqual(compress('AABBbbbCCxxxx'), 'A2B2b3C2x4')
 
if __name__=='__main__':
	unittest.main()