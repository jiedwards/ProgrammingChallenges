import unittest

class mainFunctionTests(unittest.TestCase):

		def test_count_smileys(self):
			from CountSmileys import count_smileys
			self.assertEqual(count_smileys([]), 0)
			self.assertEqual(count_smileys([':D',':~)',';~D',':)']), 4)
			self.assertEqual(count_smileys([':)',':(',':D',':O',':;']), 2)
			self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
 
if __name__=='__main__':
	unittest.main()