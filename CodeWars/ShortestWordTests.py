import unittest

class mainFunctionTests(unittest.TestCase):

		def test_shortest_word_validation(self):
			from ShortestWord import find_short
			self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
			self.assertEqual(find_short("turns out random test cases are easier than writing out basic ones"), 3)
			self.assertEqual(find_short("lets talk about javascript the best language"), 3)
			self.assertEqual(find_short("i want to travel the world writing code one day"), 1)
			self.assertEqual(find_short("Lets all go on holiday somewhere very cold"), 2)
 
if __name__=='__main__':
	unittest.main()

