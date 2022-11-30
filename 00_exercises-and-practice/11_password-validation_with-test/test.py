import unittest

from password_checker import is_valid_password, request_password

# Solution: https://repl.it/@aneagoie/Guessing-Game-2-1

class TestIsPasswordValid(unittest.TestCase):

	def test_string_of_8_digits(self):
		""" \n1️⃣	Test Case: string of length 8 with digits"""
		value_length_8_digits_as_string = '12345678'
		result = is_valid_password(value_length_8_digits_as_string)
		self.assertTrue(result,"Should return True")

	def test_number_of_8_digits(self):
		""" \n2️⃣	Test Case: number with 8 with digits: 12345678"""
		value_length_8_digits_as_number = 12345678
		result = is_valid_password(value_length_8_digits_as_number)
		self.assertFalse(result, "Should return False")

	def test_number_of_8_letters(self):
		""" \n3️⃣	Test Case: string of length 16 with digits: 'abcdabcd'"""
		value_length_8_letters = 'abcdabcd'
		result = is_valid_password(value_length_8_letters)
		self.assertFalse(result,"Should return False")

	def test_number_of_16_digits(self):
		""" \n4️⃣	Test Case: string of length 16 with digits: 1234567891010101"""
		value_length_16_digits = 1234567891010101
		result = is_valid_password(value_length_16_digits)
		self.assertFalse(result,"Should return False")


	def test_string_of_16_digits(self):
		""" \n5️⃣	Test Case: string of length 16 with digits: '1234567891010101'"""
		value_length_16_digits = '1234567891010101'
		result = is_valid_password(value_length_16_digits)
		self.assertTrue(result,"Should return True")


	def test_mixt_8_characters_without_ending_number(self):
		""" \n6️⃣	Test Case: string with mixt characters and not ending with digit: 'dkehd<i98&{\|/e 9889y7 '"""
		value_mixt_not_digit_ending = 'dkehd<i98&{\|/e 9889y7 '
		result = is_valid_password(value_mixt_not_digit_ending)
		self.assertFalse(result,"Should return False")

	def test_mixt_8_characters_without_ending_number(self):
		""" \n7️⃣	Test Case: string with mixt characters and ending with digit: 'dkehd<i98&{\|/e 9889y7'"""
		value_mixt_digit_ending = 'dkehd<i98&{\|/e 9889y7'
		result = is_valid_password(value_mixt_digit_ending)
		self.assertTrue(result,"Should return True")



	



if __name__ == '__main__':
	unittest.main()