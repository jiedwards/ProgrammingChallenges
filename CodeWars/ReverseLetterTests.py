import unittest

class mainFunctionTests(unittest.TestCase):

		def test_reverse_letter_validation(self):
			from ReverseLetter import reverse_letter
			self.assertEqual(reverse_letter("krishan"),"nahsirk")
			self.assertEqual(reverse_letter("ultr53o?n"),"nortlu")
			self.assertEqual(reverse_letter("ab23c"),"cba")
			self.assertEqual(reverse_letter("krish21an"),"nahsirk")
 
if __name__=='__main__':
	unittest.main()

