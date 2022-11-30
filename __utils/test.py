import unittest
import index


class TestIndex(unittest.TestCase):
	def test_print_non_dunder_empty_arg(self):
		self.assertRaises( index.print_non_dunder())


# Runs it only for this file and on running time
if __name__ == 'main':
	unittest.main()
