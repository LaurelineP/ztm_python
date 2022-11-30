import re

print('''
-----------------------------------------------------------------------------------
				REGEXP - REGULAR EXPRESSION
-----------------------------------------------------------------------------------
	🔸 Are made to match patterns to identify its existence in a string
		- package to import: import re

		- re.compile(<STRING-PATTERN>):
			create a regular expression instance 

		- <PATTERN>.match(<STRING>, [<START>, [<END>]]):
			tries to find a match at the beginning of the string if <START> and 
			<END> were not specified

		- <PATTERN>.search(<STRING>):
			searches for the very first occurrence in the string / return
			match instance object with attributes `span` and `match`

		- <PATTERN>.find(...):
			finds the first occurrence matching pattern / returns value found

-----------------------------------------------------------------------------------
''')

phrase = 'Hellowwww and welcome amongst us! This is 2022.'
pattern_year = re.compile('Hello')
print('Pattern stored in `pattern_year`:', pattern_year)

result = pattern_year.match(phrase)
print(result)
