import unittest

class mainFunctionTests(unittest.TestCase):

		def test_break_camel_case_validation(self):
			from BreakCamelCase import break_camel_case
			self.assertEqual(break_camel_case("helloWorld"), "hello World")
			self.assertEqual(break_camel_case("camelCase"), "camel Case")
			self.assertEqual(break_camel_case("breakCamelCase"), "break Camel Case")
 
if __name__=='__main__':
	unittest.main()
