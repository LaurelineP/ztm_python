import unittest
import main

print("""
	🔸 0 - Define a class to hold all the tests and has as param: `unittest.TestCase`
		🔹 1 - Assert the result of the test: `self.assertEqual(result, 25)`
""")


class TestMain(unittest.TestCase):

	def setUp(self):
		print('[ SETUP ] FUNCTION ')

	def test_multiply_OK(self):
		test_x = 5
		test_y = 5

		result = main.multiply(test_x, test_y)
		# asserts expected value
		self.assertEqual(result, 25)

	def test_multiply_NOK(self):
		test_x = 5
		test_y = ''

		result = main.multiply(test_x, test_y)

		# asserts expected error value
		self.assertTrue( ValueError )

	def tearDown(self):
		print('----[ TEARDOWN ] FUNCTION\n')
		


print("\t🔸  Run the unit test by executing `unittest.main()`")

# Runs it only for this file and on running time
if __name__ == 'main':
	unittest.main()
